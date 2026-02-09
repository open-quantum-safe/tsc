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
import os
from urllib.parse import urlparse
import warnings

import requests

GITHUB_API_BASE = "https://api.github.com"

SUBPROJECTS = {
    "OQS Technical Steering Committee": "https://github.com/open-quantum-safe/tsc",
    "liboqs": "https://github.com/open-quantum-safe/liboqs",
    "OQS-OpenSSL 3 provider": "https://github.com/open-quantum-safe/oqs-provider",
    "OQS-BoringSSL": "https://github.com/open-quantum-safe/boringssl",
    "OQS-OpenSSH": "https://github.com/open-quantum-safe/openssh",
    "oqs-demos": "https://github.com/open-quantum-safe/oqs-demos",
    "ci-containers": "https://github.com/open-quantum-safe/ci-containers",
    "www.openquantumsafe.org": "https://github.com/open-quantum-safe/www",
    "liboqs-cpp": "https://github.com/open-quantum-safe/liboqs-cpp",
    "liboqs-go": "https://github.com/open-quantum-safe/liboqs-go",
    "liboqs-java": "https://github.com/open-quantum-safe/liboqs-java",
    "liboqs-python": "https://github.com/open-quantum-safe/liboqs-python",
    "liboqs-rust": "https://github.com/open-quantum-safe/liboqs-rust",
}

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    warnings.warn("GITHUB_TOKEN not found")
# NOTE: most GitHub API can return up to 100 items per page. Setting page size
#   beyond 100 will not increase the number of items returned.
GITHUB_PAGE_SIZE = 100


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


def github_get(url: str, params: dict | None = None, count: int = GITHUB_PAGE_SIZE) -> list[dict]:
    """
    Perform a GET request against the GitHub API and transparently handle
    pagination.

    :param url: Initial GitHub API endpoint
    :param params: Optional query parameters (only sent on first request)
    :return: Aggregated list of JSON objects from all pages
    """
    results: list[dict] = []
    while url and (len(results) < count):
        response = requests.get(url, headers=github_headers(), params=params)
        response.raise_for_status()
        results.extend(response.json())
        url = response.links.get("next", {}).get("url")
        params = None
    return results


def get_pull_requests(
    repo: str, state: str
) -> list[dict]:
    """
    Retrieve pull requests for a repository.

    :param repo: Repository identifier in the form "owner/repo"
    :param state: PR state ("open", "closed", or "all")
    :param count: only fetch a subset of all filtered items to reduce the number
        of calls to GitHub API
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

    print(f"\n📅 Status Meeting Agenda — {meeting_date.date()}")
    print(f"🕒 Since: {prev_date.date()}\n")

    for name, url in SUBPROJECTS.items():
        data = collect_project_status(url, prev_date)
        print(f"## {name}")
        if len(data["merged_prs"]) + len(data["open_prs"]) + len(data["issues"]) == 0:
            print("\nNo recent issues or pull requests\n")
            continue

        print("\n### Merged PRs")
        for pr in data["merged_prs"]:
            print(f"- {pr['title']} ({pr['html_url']})")

        print("\n### Open PRs")
        for pr in data["open_prs"]:
            print(f"- {pr['title']} ({pr['html_url']})")

        print("\n### Issues")
        for issue in data["issues"]:
            print(f"- {issue['title']} ({issue['html_url']})")

        print()


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
    status.set_defaults(func=status_agenda)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
