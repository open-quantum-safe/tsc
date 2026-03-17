"""Generate an OQS status meeting agenda markdown file.

This script creates a ready-to-use agenda file (e.g.
"2026-03-10 - OQS status meeting - agenda.md") in the current directory.
The agenda includes:
  - Meeting time in multiple time zones
  - A list of OQS subprojects and language wrappers
  - Non-Done items from the GitHub project board
  - Per-repository summaries of new issues, recently merged PRs, and open PRs

Usage:
    python generate_oqs_agenda.py [date] [time]

Arguments (both optional):
    date    Meeting date in YYYY-MM-DD format.
            If omitted, the next OQS Status Meeting is fetched from the
            PQCA LFX calendar automatically.
    time    Meeting start time in HH:MM Eastern format (e.g. 12:30).
            Only used when 'date' is also provided; defaults to 12:30.

Examples:
    # Auto-detect the next meeting from the LFX calendar:
    python generate_oqs_agenda.py

    # Generate an agenda for a specific date (time defaults to 12:30 ET):
    python generate_oqs_agenda.py 2026-03-10

    # Generate an agenda for a specific date and time:
    python generate_oqs_agenda.py 2026-03-10 13:00

Dependencies:
    Python packages (install with pip):
        pytz
        icalendar          (only needed for calendar auto-detection)
        recurring-ical-events  (only needed for calendar auto-detection)

    External tools:
        gh  (GitHub CLI, https://cli.github.com/)
            Must be authenticated with credentials that have read access to
            the open-quantum-safe GitHub organization and its project boards.
            Run `gh auth login` to set up credentials before using this script.
"""

import argparse
from collections import defaultdict
import json
import subprocess
import urllib.request
from pytz import timezone
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Configuration — edit these values to customise the generated agenda
# ---------------------------------------------------------------------------

# iCalendar feed for the PQCA LFX calendar, used to auto-detect the next
# OQS Status Meeting when no date argument is supplied.
CALENDAR_URL = 'https://webcal.prod.itx.linuxfoundation.org/lfx/a092M00001NWnfNQAT_sub'

# Fixed items included in the "Agenda" section of every meeting.
AGENDA_ITEMS = ['Status updates & items seeking help']

# GitHub project board to pull non-Done items from.
# Set PROJECT_NUMBER to the number from:
#   https://github.com/orgs/open-quantum-safe/projects/<PROJECT_NUMBER>
# Set to None to skip the project board section.
PROJECT_ORG = 'open-quantum-safe'
PROJECT_NUMBER = 11

# Primary OQS repositories. Each entry has a 'gh_name' (GitHub repo name under
# open-quantum-safe) and a 'fmt_name' (display name used in the agenda).
# These appear in the "OQS subprojects" list and receive per-repo PR/issue summaries.
SUBPROJECTS = [
    {'gh_name': 'tsc',            'fmt_name': 'OQS Technical Steering Committee'},
    {'gh_name': 'liboqs',         'fmt_name': 'liboqs'},
    {'gh_name': 'oqs-provider',   'fmt_name': 'OQS-OpenSSL 3 provider'},
    {'gh_name': 'openssh',        'fmt_name': 'OQS-OpenSSH'},
    {'gh_name': 'boringssl',      'fmt_name': 'OQS-BoringSSL'},
    {'gh_name': 'oqs-demos',      'fmt_name': 'oqs-demos'},
    {'gh_name': 'ci-containers',  'fmt_name': 'ci-containers'},
    {'gh_name': 'www',            'fmt_name': 'www.openquantumsafe.org'},
]

# liboqs language wrapper repositories. Same structure as SUBPROJECTS.
# Comment out any entry to exclude it from the agenda.
WRAPPERS = [
    {'gh_name': 'liboqs-cpp',    'fmt_name': 'liboqs-C++'},
    # {'gh_name': 'liboqs-dotnet','fmt_name': 'liboqs-.NET'},
    {'gh_name': 'liboqs-go',     'fmt_name': 'liboqs-Go'},
    {'gh_name': 'liboqs-java',   'fmt_name': 'liboqs-Java'},
    {'gh_name': 'liboqs-js',     'fmt_name': 'liboqs-js'},
    {'gh_name': 'liboqs-python', 'fmt_name': 'liboqs-Python'},
    {'gh_name': 'liboqs-rust',   'fmt_name': 'liboqs-Rust'},
]

# ---------------------------------------------------------------------------
# Internal constants
# ---------------------------------------------------------------------------

EST = timezone('US/Eastern')
CEST = timezone('Europe/Berlin')
PST = timezone('US/Pacific')

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def fetch_next_meeting_from_calendar(calendar_url):
    """Fetch the next OQS Status Meeting datetime from an iCalendar feed.

    Args:
        calendar_url: URL of the iCalendar (.ics) feed to fetch.

    Returns:
        A timezone-aware datetime (US/Eastern) for the nearest upcoming event
        whose summary contains 'OQS Status Meeting'.

    Raises:
        ImportError: If the icalendar or recurring-ical-events packages are
            not installed.
        ValueError: If no matching event is found within the next 90 days.
    """
    try:
        import icalendar
        import recurring_ical_events
    except ImportError:
        raise ImportError(
            'Required packages not found. Install with:\n'
            '  pip install icalendar recurring-ical-events'
        )

    with urllib.request.urlopen(calendar_url) as response:
        cal_data = response.read()

    cal = icalendar.Calendar.from_ical(cal_data)
    now = datetime.now(tz=EST)
    end = now + timedelta(days=90)

    events = recurring_ical_events.of(cal).between(now, end)
    oqs_events = [e for e in events if 'OQS Status Meeting' in str(e.get('SUMMARY', ''))]

    if not oqs_events:
        raise ValueError('No upcoming OQS Status Meeting found in the calendar within the next 90 days')

    oqs_events.sort(key=lambda e: e['DTSTART'].dt)
    dt = oqs_events[0]['DTSTART'].dt

    if not hasattr(dt, 'tzinfo') or dt.tzinfo is None:
        dt = EST.localize(dt)
    else:
        dt = dt.astimezone(EST)

    return dt


def gh(args):
    """Run a gh CLI command and return the parsed JSON output.

    Args:
        args: List of arguments passed to gh (not including 'gh' itself).

    Returns:
        The parsed JSON response (dict or list, depending on the subcommand).

    Raises:
        subprocess.CalledProcessError: If gh exits with a non-zero status.
    """
    return json.loads(subprocess.check_output(['gh'] + args))


def format_item(item, kind):
    """Format a PR or issue as a markdown link with an optional label list.

    Args:
        item: Dict with keys 'number', 'url', 'title', and optionally 'labels'
            (a list of dicts with a 'name' key), as returned by gh search or
            gh pr list with --json.
        kind: Display prefix for the link text, e.g. 'PR' or 'Issue'.

    Returns:
        A markdown string of the form '[kind number](url): Title  `label1`'.
    """
    labels = ' '.join(f'`{l["name"]}`' for l in item.get('labels', []))
    line = f'[{kind} {item["number"]}]({item["url"]}): {item["title"].replace("_", chr(92) + "_")}'
    if labels:
        line += f'  {labels}'
    return line


def fetch_project_items(org, project_number):
    """Fetch non-Done items from a GitHub project board.

    Args:
        org: GitHub organization name (e.g. 'open-quantum-safe').
        project_number: Integer project board number as it appears in the
            URL: https://github.com/orgs/<org>/projects/<project_number>.

    Returns:
        A tuple (project_title, project_url, items_by_status) where
        items_by_status is a defaultdict mapping each status string to a list
        of formatted markdown strings for the items in that status column.
        Items with status 'Done' are excluded.
    """
    meta = gh(['project', 'view', str(project_number), '--owner', org, '--format', 'json'])
    project_title = meta['title']
    project_url = meta['url']

    data = gh(['project', 'item-list', str(project_number),
               '--owner', org, '--format', 'json', '--limit', '1000'])

    items_by_status = defaultdict(list)
    for item in data.get('items', []):
        status = item.get('status')
        if status == 'Done':
            continue

        title = item.get('title', '').replace('_', '\\_')
        content = item.get('content') or {}
        url = content.get('url', '')

        if url:
            number = content.get('number')
            repo = content.get('repository', '').split('/')[-1]
            kind = 'PR' if '/pull/' in url else 'Issue'
            label = f'[{kind} {number}]({url}): {title}'
            if repo:
                label += f' ({repo})'
        else:
            label = f'{title} *(draft)*'

        items_by_status[status or '(no status)'].append(label)

    return project_title, project_url, items_by_status

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


# Resolve the meeting time from CLI args or the LFX calendar.
parser = argparse.ArgumentParser(description='Generate OQS status meeting agenda')
parser.add_argument('date', nargs='?', default=None,
                    help='Meeting date (YYYY-MM-DD); if omitted, determined from the LFX calendar')
parser.add_argument('time', nargs='?', default=None,
                    help='Meeting time in HH:MM Eastern (default: from calendar, or 12:30)')
args = parser.parse_args()

if args.date is None:
    MEETING_TIME = fetch_next_meeting_from_calendar(CALENDAR_URL)
    print(f'Using next meeting from calendar: {MEETING_TIME.strftime("%Y-%m-%d %H:%M")} ET')
else:
    _date = datetime.strptime(args.date, '%Y-%m-%d')
    _hour, _minute = map(int, (args.time or '12:30').split(':'))
    MEETING_TIME = EST.localize(datetime(_date.year, _date.month, _date.day, _hour, _minute))

# Open the output file and write each section of the agenda.
filename = MEETING_TIME.date().strftime('%Y-%m-%d - OQS status meeting - agenda.md')
with open(filename, 'w') as f:
    # Header: title and meeting time in three time zones.
    date_str = MEETING_TIME.date().strftime('%Y-%m-%d')
    f.write(f'# {date_str} - OQS status meeting - agenda\n\n')
    f.write(
        '<span style="color: red;"> {0} at {1} </span>'
        ' US Eastern Time / {2} Central European / {3} US Pacific Time'
        ' on Zoom (https://pqca.org/calendar/)\n\n'.format(
            MEETING_TIME.date().strftime('%A %B %d'),
            MEETING_TIME.time().strftime('%-I:%M %p'),
            MEETING_TIME.astimezone(CEST).time().strftime('%-I:%M %p'),
            MEETING_TIME.astimezone(PST).time().strftime('%-I:%M %p'),
        )
    )

    # Agenda: fixed items from AGENDA_ITEMS.
    f.write('## Agenda\n\n')
    for idx, item in enumerate(AGENDA_ITEMS, start=1):
        f.write(f'{idx}. {item}\n\n')

    # Subprojects list: numbered entries for each repo and wrapper.
    f.write('## OQS subprojects\n\n')
    for idx, project in enumerate(SUBPROJECTS, start=1):
        f.write(f'{idx}. {project["fmt_name"]}\n')
    wrapper_names = ', '.join(w['fmt_name'] for w in WRAPPERS)
    f.write(f'{len(SUBPROJECTS) + 1}. liboqs language wrappers: {wrapper_names}\n')

    # Project board: non-Done items grouped by status column.
    if PROJECT_NUMBER is not None:
        project_title, project_url, items_by_status = fetch_project_items(PROJECT_ORG, PROJECT_NUMBER)
        f.write(f'\n\n## Project board: [{project_title}]({project_url})\n\n')
        if not items_by_status:
            f.write('No non-Done items.\n')
        else:
            for status, items in items_by_status.items():
                f.write(f'**{status}**\n')
                for item in items:
                    f.write(f'- {item}\n')
                f.write('\n')

    # Pre-meeting reviews: per-repo summary of recent activity and open PRs.
    f.write('\n\n## Pre-meeting project reviews\n\n')
    f.write('See project dashboard at: https://openquantumsafe.org/dashboard.html')

    for idx, project in enumerate(SUBPROJECTS + WRAPPERS, start=1):
        gh_name = project['gh_name']
        fmt_name = project['fmt_name']
        f.write(f'\n\n{idx}. **[{fmt_name}](https://github.com/open-quantum-safe/{gh_name})**\n\n\n')

        # Issues with discussion/activity in the last 7 days.
        discussion_cutoff = MEETING_TIME.date() - timedelta(days=7)
        discussed_issues = gh([
            'search', 'issues',
            '--repo', f'open-quantum-safe/{gh_name}',
            '--updated', f'>={discussion_cutoff.strftime("%Y-%m-%d")}',
            '--json', 'number,title,url,labels', '--limit', '100',
        ])
        if not discussed_issues:
            f.write('\t- Issues with activity in the last 7 days: None.\n')
        else:
            f.write('\t- Issues with activity in the last 7 days:\n')
            for issue in discussed_issues:
                f.write(f'\t\t - {format_item(issue, "Issue")}\n')

        # PRs merged in the last 7 days.
        pr_cutoff = MEETING_TIME.date() - timedelta(days=7)
        recently_merged = gh([
            'search', 'prs',
            '--repo', f'open-quantum-safe/{gh_name}',
            '--merged-at', f'>={pr_cutoff.strftime("%Y-%m-%d")}',
            '--json', 'number,title,url,labels', '--limit', '100',
        ])
        if not recently_merged:
            f.write('\t- Merges in the last 7 days: None.\n')
        else:
            f.write('\t- Merges in the last 7 days:\n')
            for pr in recently_merged:
                f.write(f'\t\t - {format_item(pr, 'PR')}\n')

        # Currently open PRs targeting the default base branch.
        base = 'OQS-v10' if gh_name == 'openssh' else 'main'
        open_pulls = gh([
            'pr', 'list',
            '--repo', f'open-quantum-safe/{gh_name}',
            '--state', 'open', '--base', base,
            '--json', 'number,title,url,labels', '--limit', '100',
        ])
        if not open_pulls:
            f.write('\t- Open PRs: None\n')
        else:
            f.write('\t- Open PRs:\n')
            for pr in open_pulls:
                f.write(f'\t\t - {format_item(pr, 'PR')}\n')
