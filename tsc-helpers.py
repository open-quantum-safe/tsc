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
from typing import List, Dict
from urllib.parse import urlparse

import requests

GITHUB_API_BASE = "https://api.github.com"

DEFAULT_SUBPROJECTS = [
    "https://github.com/example/project-a",
    "https://github.com/example/project-b",
]

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def parse_date(date_str: str) -> dt.datetime:
    """
    Parse a human-readable date string into a datetime object.

    :param date_str: Date string in the format "%a %b %d, %Y"
    :return: Parsed datetime
    """
    return dt.datetime.strptime(date_str, "%a %b %d, %Y")


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


def github_headers() -> Dict[str, str]:
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


def github_get(url: str, params: Dict | None = None) -> List[Dict]:
    """
    Perform a GET request against the GitHub API and transparently handle
    pagination.

    :param url: Initial GitHub API endpoint
    :param params: Optional query parameters (only sent on first request)
    :return: Aggregated list of JSON objects from all pages
    """
    results: List[Dict] = []
    while url:
        response = requests.get(url, headers=github_headers(), params=params)
        response.raise_for_status()
        results.extend(response.json())
        url = response.links.get("next", {}).get("url")
        params = None
    return results


def get_pull_requests(repo: str, state: str) -> List[Dict]:
    """
    Retrieve pull requests for a repository.

    :param repo: Repository identifier in the form "owner/repo"
    :param state: PR state ("open", "closed", or "all")
    """
    url = f"{GITHUB_API_BASE}/repos/{repo}/pulls"
    return github_get(url, params={"state": state, "per_page": 100})


def get_issues(repo: str) -> List[Dict]:
    """
    Retrieve issues for a repository.

    Pull requests are included by the GitHub API and should be filtered
    by the caller if necessary.
    """
    url = f"{GITHUB_API_BASE}/repos/{repo}/issues"
    return github_get(url, params={"state": "all", "per_page": 100})


def filter_since(
    items: List[Dict],
    since: dt.datetime,
    field: str,
) -> List[Dict]:
    """
    Filter GitHub API objects based on a timestamp field.

    :param items: List of GitHub API objects
    :param since: Lower bound datetime (inclusive)
    :param field: Timestamp field name (e.g., "updated_at")
    """
    return [
        item
        for item in items
        if dt.datetime.fromisoformat(
            item[field].replace("Z", "+00:00")
        ) >= since
    ]


def collect_project_status(repo_url: str, since: dt.datetime) -> Dict:
    """
    Collect status information for a single GitHub project.

    Includes:
    - Merged pull requests since the given date
    - Open pull requests updated since the given date
    - Issues created or updated since the given date

    :param repo_url: Full GitHub repository URL
    :param since: Lower bound datetime for activity
    :return: Dictionary containing categorized project activity
    """
    repo = extract_repo(repo_url)

    merged_prs = [
        pr
        for pr in get_pull_requests(repo, "closed")
        if pr.get("merged_at")
        and dt.datetime.fromisoformat(
            pr["merged_at"].replace("Z", "+00:00")
        ) >= since
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
            dt.datetime.fromisoformat(
                issue["created_at"].replace("Z", "+00:00")
            ) >= since
            or dt.datetime.fromisoformat(
                issue["updated_at"].replace("Z", "+00:00")
            ) >= since
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

    subprojects = args.subproject or DEFAULT_SUBPROJECTS

    print(f"\n📅 Status Meeting Agenda — {meeting_date.date()}")
    print(f"🕒 Since: {prev_date.date()}\n")

    for project in subprojects:
        print(f"## {project}")
        data = collect_project_status(project, prev_date)

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
        help="Target meeting date",
    )
    status.add_argument(
        "--prevdate",
        help="Previous meeting date (defaults to 7 days prior)",
    )
    status.add_argument(
        "--subproject",
        action="append",
        help="GitHub repo URL (can be repeated)",
    )
    status.set_defaults(func=status_agenda)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
