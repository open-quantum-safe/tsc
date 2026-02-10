#!/usr/bin/env python
"""
tsc-helpers.py

Command-line helpers for TSC workflows.

Currently supported workflows:
- status-agenda: Generate a meeting agenda based on GitHub activity
  since the previous meeting.

The tool is designed to be extensible via subcommands so that additional
workflows can be added over time.

GitHub data is fetched using the GitHub REST API. Authentication is optional
but recommended via the GITHUB_TOKEN environment variable to avoid rate limits.
"""

import argparse
import datetime as dt
import enum
import os
import sys
from zoneinfo import ZoneInfo
from urllib.parse import urlparse
import warnings

import jinja2
import requests

TSCHELPERS_DEBUG = os.getenv("TSCHELPERS_DEBUG", None)

GITHUB_API_BASE = "https://api.github.com"

SUBPROJECTS = [
    ("OQS Technical Steering Committee", "https://github.com/open-quantum-safe/tsc"),
    ("liboqs", "https://github.com/open-quantum-safe/liboqs"),
    ("OQS-OpenSSL 3 provider", "https://github.com/open-quantum-safe/oqs-provider"),
    ("OQS-BoringSSL", "https://github.com/open-quantum-safe/boringssl"),
    ("OQS-OpenSSH", "https://github.com/open-quantum-safe/openssh"),
    ("oqs-demos", "https://github.com/open-quantum-safe/oqs-demos"),
    ("ci-containers", "https://github.com/open-quantum-safe/ci-containers"),
    ("www.openquantumsafe.org", "https://github.com/open-quantum-safe/www"),
    ("liboqs-cpp", "https://github.com/open-quantum-safe/liboqs-cpp"),
    ("liboqs-go", "https://github.com/open-quantum-safe/liboqs-go"),
    ("liboqs-java", "https://github.com/open-quantum-safe/liboqs-java"),
    ("liboqs-python", "https://github.com/open-quantum-safe/liboqs-python"),
    ("liboqs-rust", "https://github.com/open-quantum-safe/liboqs-rust"),
]

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    warnings.warn("GITHUB_TOKEN not found")

# NOTE: most GitHub API can return up to 100 items per page. Setting page size
#   beyond 100 will not increase the number of items returned.
GITHUB_PAGE_SIZE = 100

OQS_STATUS_AGENDA_TEMPLATE = """
# {{ meeting_date.strftime("%Y-%m-%d") }} - OQS status meeting - agenda

**When:**
- US Eastern time:          {{ eastern_time.strftime("%I:%M %p") }}
- US Pacific time:          {{ pacific_time.strftime("%I:%M %p") }}
- Central European time:    {{ eu_time.strftime("%I:%M %p") }}

**Where:** [Zoom](https://pqca.org/calendar)

## Agenda

## OQS subprojects
{% for project in subprojects -%}
- {{ project.name }}
{% endfor %}

## Pre-meeting project reviews
See project dashboard at: https://openquantumsafe.org/dashboard.html

Updates since last meeting on {{ prev_date.strftime("%Y-%m-%d") }}:

{% for project in subprojects %}
1. **{{ project.name }}**
    {%- if not project.merged_prs %}
    - Merged pull requests since {{ prev_date.strftime("%Y-%m-%d") }}: *None*
    {% else %}
    - Merged pull requests since {{ prev_date.strftime("%Y-%m-%d") }}
        {%- for pull in project.merged_prs %}
        - [#{{ pull.number }}]({{ pull.url }}): {{ pull.title }}
        {%- endfor %}
    {% endif -%}
    {%- if not project.open_prs %}
    - Open pull requests: *None*
    {% else %}
    - Open pull requests:
        {%- for pull in project.open_prs %}
        - [#{{ pull.number }}]({{ pull.url }}): {{ pull.title }}
        {%- endfor %}
    {% endif -%}
    {%- if not project.issues %}
    - New or updated issues: *None*
    {% else %}
    - New or updated issues
        {%- for issue in project.issues %}
        - [#{{ issue.number }}]({{ issue.url }}): {{ issue.title }}
        {%- endfor %}
    {% endif -%}
{% endfor %}
"""


def debug(*args, **kwargs):
    if TSCHELPERS_DEBUG:
        print(*args, file=sys.stderr, **kwargs)


class GHState(enum.Enum):
    Open = 1
    Closed = 2

    @staticmethod
    def from_str(s: str):
        match s:
            case "open":
                return GHState.Open
            case "closed":
                return GHState.Closed
        raise ValueError(f"Invalid string {s}")


class GHIssue:
    def __init__(
        self,
        title: str,
        url: str,
        number: str,
        state: GHState,
        created_at: dt.datetime,
        updated_at: dt.datetime,
    ):
        self.title = title
        self.url = url
        self.number = number
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at
        # NOTE: don't care about merged_at, closed_at, or other fields

    @staticmethod
    def from_dict(data: dict):
        return GHIssue(
            data["title"],
            data["url"],
            data["number"],
            GHState.from_str(data["state"]),
            dt.datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
            dt.datetime.fromisoformat(data["updated_at"].replace("Z", "+00:00")),
        )


class GHPullRequest(GHIssue):
    """On GitHub, pull requests are another type of issues"""

    def __init__(
        self,
        title: str,
        url: str,
        number: str,
        state: GHState,
        created_at: dt.datetime,
        updated_at: dt.datetime,
        merged_at: dt.datetime | None,
    ):
        self.title = title
        self.url = url
        self.number = number
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at
        self.merged_at = merged_at

    @staticmethod
    def from_dict(data: dict):
        return GHPullRequest(
            data["title"],
            data["url"],
            data["number"],
            GHState.from_str(data["state"]),
            dt.datetime.fromisoformat(data["created_at"].replace("Z", "+00:00")),
            dt.datetime.fromisoformat(data["updated_at"].replace("Z", "+00:00")),
            (
                dt.datetime.fromisoformat(data["merged_at"].replace("Z", "+00:00"))
                if data["merged_at"]
                else None
            ),
        )


class ProjectStatus:
    def __init__(
        self,
        name: str,
        merged_prs: list[GHPullRequest],
        open_prs: list[GHPullRequest],
        issues: list[GHIssue],
        since: dt.datetime,
    ):
        self.name = name
        self.merged_prs = merged_prs
        self.open_prs = open_prs
        self.issues = issues
        self.since = since

    @staticmethod
    def from_url(name: str, url: str, filter_since: dt.datetime):
        components = urlparse(url).path.strip("/").split("/")
        if len(components) < 2:
            raise ValueError(f"Invalid GitHub repo URL: {url}")
        owner, repo = components[0], components[1]

        pulls = [
            GHPullRequest.from_dict(pull)
            for pull in github_get(
                f"{GITHUB_API_BASE}/repos/{owner}/{repo}/pulls",
                params={
                    "state": "all",
                    "per_page": GITHUB_PAGE_SIZE,
                    "sort": "updated",
                    "direction": "desc",
                },
            )
        ]
        issues = [
            GHIssue.from_dict(issue)
            for issue in github_get(
                f"{GITHUB_API_BASE}/repos/{owner}/{repo}/issues",
                params={
                    "state": "all",
                    "per_page": GITHUB_PAGE_SIZE,
                    "sort": "updated",
                    "direction": "desc",
                },
            )
            if "pull_request" not in issue
        ]

        # Filter since
        merged_pulls = [
            pull for pull in pulls if pull.merged_at and pull.merged_at >= filter_since
        ]
        open_pulls = [pull for pull in pulls if pull.state == GHState.Open]
        issues = [issue for issue in issues if issue.updated_at >= filter_since]
        return ProjectStatus(name, merged_pulls, open_pulls, issues, filter_since)


def parse_date(date_str: str) -> dt.datetime:
    """
    Parse a human-readable date string into a datetime object.

    :param date_str: Date string in the format "%a %b %d, %Y"
    :return: Parsed datetime
    """
    parsed = dt.datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
    parsed = parsed.astimezone()  # insert system clock's timezone

    return parsed.astimezone(dt.timezone.utc)


def extract_repo(repo_url: str) -> str:
    """
    Extract the GitHub "owner/repo" identifier from a repository URL.

    :param repo_url: Full GitHub repository URL
    :return: Repository identifier in the form "owner/repo"
    :raises ValueError: If the URL does not appear to reference a repository
    """
    parsed = urlparse(repo_url)
    parts = parsed.path.strip("/").split("/")
    if len(parts) < 2:
        raise ValueError(f"Invalid GitHub repo URL: {repo_url}")
    return f"{parts[0]}/{parts[1]}"


def github_headers() -> dict[str, str]:
    """
    Build HTTP headers for GitHub API requests.

    Includes authorization headers if GITHUB_TOKEN is set.
    """
    headers = {
        "Accept": "application/vnd.github+json",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def github_get(
    url: str, params: dict | None = None, count: int = GITHUB_PAGE_SIZE
) -> list[dict]:
    """
    Perform a GET request against the GitHub API and transparently handle
    pagination.

    :param url: Initial GitHub API endpoint
    :param params: Optional query parameters (only sent on first request)
    :param count: Fetch up to this many items
    :return: Aggregated list of JSON objects from all pages
    """
    debug(url)
    results: list[dict] = []
    while url and (len(results) < count):
        response = requests.get(url, headers=github_headers(), params=params)
        response.raise_for_status()
        debug(f"fetched {len(response.json())} items")
        results.extend(response.json())
        url = response.links.get("next", {}).get("url")
        params = None
    return results


def get_pull_requests(repo: str, state: str) -> list[dict]:
    """
    Retrieve pull requests for a repository.

    :param repo: Repository identifier in the form "owner/repo"
    :param state: PR state ("open", "closed", or "all")
    """
    url = f"{GITHUB_API_BASE}/repos/{repo}/pulls"
    pulls = github_get(
        url,
        params={
            "state": state,
            "per_page": GITHUB_PAGE_SIZE,
            "sort": "updated",
            "direction": "desc",
        },
    )
    return pulls


def get_issues(repo: str) -> list[dict]:
    """
    Retrieve issues for a repository.

    Pull requests are included by the GitHub API and should be filtered
    by the caller if necessary.
    """
    url = f"{GITHUB_API_BASE}/repos/{repo}/issues"
    issues = github_get(
        url,
        params={
            "state": "all",
            "per_page": GITHUB_PAGE_SIZE,
            "sort": "updated",
            "direction": "desc",
        },
    )
    return issues


def filter_since(
    items: list[dict],
    since: dt.datetime,
    field: str,
) -> list[dict]:
    """
    Filter GitHub API objects based on a timestamp field.

    :param items: List of GitHub API objects
    :param since: Lower bound datetime (inclusive)
    :param field: Timestamp field name (e.g., "updated_at")
    """
    return [
        item
        for item in items
        if dt.datetime.fromisoformat(item[field].replace("Z", "+00:00")) >= since
    ]


def collect_project_status(repo_url: str, since: dt.datetime) -> dict:
    """
    Collect status information for a single GitHub project.

    Includes:
    - Merged pull requests since the given date
    - Open pull requests updated since the given date
    - Issues created or updated since the given date

    :param repo_url: Full GitHub repository URL
    :param since: Lower bound datetime for activity
    :return: dictionary containing categorized project activity
    """
    repo = extract_repo(repo_url)

    merged_prs = [
        pr
        for pr in get_pull_requests(repo, "closed")
        if pr.get("merged_at")
        and dt.datetime.fromisoformat(pr["merged_at"].replace("Z", "+00:00")) >= since
    ]

    open_prs = filter_since(
        get_pull_requests(repo, "open"),
        since,
        "updated_at",
    )

    issues = [
        issue
        for issue in get_issues(repo)
        if "pull_request" not in issue
        and (
            dt.datetime.fromisoformat(issue["created_at"].replace("Z", "+00:00"))
            >= since
            or dt.datetime.fromisoformat(issue["updated_at"].replace("Z", "+00:00"))
            >= since
        )
    ]

    return {
        "repo": repo,
        "merged_prs": merged_prs,
        "open_prs": open_prs,
        "issues": issues,
    }


def status_agenda(args: argparse.Namespace) -> None:
    """
    Generate and print a status meeting agenda based on GitHub activity.

    :param args: Parsed CLI arguments
    """
    meeting_date = parse_date(args.date)
    prev_date = (
        parse_date(args.prevdate)
        if args.prevdate
        else meeting_date - dt.timedelta(days=7)
    )
    projects = [
        ProjectStatus.from_url(name, url, prev_date) for (name, url) in SUBPROJECTS
    ]
    eastern_time = meeting_date.astimezone(ZoneInfo("US/Eastern"))
    pacific_time = meeting_date.astimezone(ZoneInfo("US/Pacific"))
    eu_time = meeting_date.astimezone(ZoneInfo("Europe/Berlin"))

    markdown = jinja2.Template(OQS_STATUS_AGENDA_TEMPLATE).render(
        {
            "meeting_date": meeting_date,
            "prev_date": prev_date,
            "eastern_time": eastern_time,
            "pacific_time": pacific_time,
            "eu_time": eu_time,
            "subprojects": projects,
        }
    )

    if args.out == "-":
        print(markdown)
    else:
        with open(args.out, "w") as f:
            f.write(markdown)


def main() -> None:
    """Entry point for the tsc-helpers CLI."""
    parser = argparse.ArgumentParser(
        prog="tsc-helpers",
        description="TSC helper workflows",
    )

    subparsers = parser.add_subparsers(
        dest="workflow",
        required=True,
    )

    status = subparsers.add_parser(
        "status-agenda",
        help="Generate status meeting agenda",
    )
    status.add_argument(
        "--date",
        required=True,
        help='Target meeting date (example "Tue Feb 10 10:30:00 2026")',
    )
    status.add_argument(
        "--prevdate",
        help="Previous meeting date (defaults to 7 days prior)",
    )
    status.add_argument(
        "-O", "--out", type=str, default="-", help="Output file path (default: stdout)."
    )
    status.set_defaults(func=status_agenda)

    args = parser.parse_args()

    debug("Output to {}".format(args.out if args.out != "-" else "stdout"))
    args.func(args)


if __name__ == "__main__":
    main()
