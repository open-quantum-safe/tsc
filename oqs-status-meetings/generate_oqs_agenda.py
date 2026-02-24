import argparse
from collections import defaultdict
import json
import subprocess
from pytz import timezone
from datetime import datetime, timedelta

EST = timezone('US/Eastern')
CEST = timezone('Europe/Berlin')
PST = timezone('US/Pacific')

parser = argparse.ArgumentParser(description='Generate OQS status meeting agenda')
parser.add_argument('date', help='Meeting date (YYYY-MM-DD)')
parser.add_argument('time', nargs='?', default='12:30', help='Meeting time in HH:MM Eastern (default: 12:30)')
args = parser.parse_args()

_date = datetime.strptime(args.date, '%Y-%m-%d')
_hour, _minute = map(int, args.time.split(':'))
MEETING_TIME = EST.localize(datetime(_date.year, _date.month, _date.day, _hour, _minute))

AGENDA_ITEMS = ['Status updates & items seeking help']

# GitHub project board to pull non-Done items from.
# Set PROJECT_NUMBER to the number from:
#   https://github.com/orgs/open-quantum-safe/projects/<PROJECT_NUMBER>
# Set to None to skip the project board section.
PROJECT_ORG = 'open-quantum-safe'
PROJECT_NUMBER = 11

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

WRAPPERS = [
    {'gh_name': 'liboqs-cpp',    'fmt_name': 'liboqs-C++'},
    # {'gh_name': 'liboqs-dotnet','fmt_name': 'liboqs-.NET'},
    {'gh_name': 'liboqs-go',     'fmt_name': 'liboqs-Go'},
    {'gh_name': 'liboqs-java',   'fmt_name': 'liboqs-Java'},
    {'gh_name': 'liboqs-python', 'fmt_name': 'liboqs-Python'},
    {'gh_name': 'liboqs-rust',   'fmt_name': 'liboqs-Rust'},
]


def gh(args):
    """Run a gh CLI command and return the parsed JSON output."""
    return json.loads(subprocess.check_output(['gh'] + args))


def format_item(item, kind):
    """Format a PR or issue dict as a markdown link with an optional label list."""
    labels = ' '.join(f'`{l["name"]}`' for l in item.get('labels', []))
    line = f'[{kind} {item["number"]}]({item["url"]}): {item["title"].replace("_", chr(92) + "_")}'
    if labels:
        line += f'  {labels}'
    return line


def fetch_project_items(org, project_number):
    """Return (project_title, project_url, items_by_status) for non-Done items.

    items_by_status maps status string -> list of formatted markdown strings.
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
        typename = item.get('type', '')

        if url:
            number = content.get('number')
            repo = content.get('repository', '').split('/')[-1]
            kind = 'PR' if typename == 'PULL_REQUEST' else 'Issue'
            label = f'[{kind} {number}]({url}): {title}'
            if repo:
                label += f' ({repo})'
        else:
            label = f'{title} *(draft)*'

        items_by_status[status or '(no status)'].append(label)

    return project_title, project_url, items_by_status


# Might be slightly off due to the timezone, but should work for our purposes
earliest_merged_pr_cutoff = MEETING_TIME.date() - timedelta(days=7)

filename = MEETING_TIME.date().strftime('%Y-%m-%d - OQS status meeting - agenda.md')
with open(filename, 'w') as f:
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

    f.write('## Agenda\n\n')
    for idx, item in enumerate(AGENDA_ITEMS, start=1):
        f.write(f'{idx}. {item}\n\n')

    f.write('## OQS subprojects\n\n')
    for idx, project in enumerate(SUBPROJECTS, start=1):
        f.write(f'{idx}. {project["fmt_name"]}\n')
    wrapper_names = ', '.join(w['fmt_name'] for w in WRAPPERS)
    f.write(f'{len(SUBPROJECTS) + 1}. liboqs language wrappers: {wrapper_names}\n')

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

    f.write('\n\n## Pre-meeting project reviews\n\n')
    f.write('See project dashboard at: https://openquantumsafe.org/dashboard.html')

    for idx, project in enumerate(SUBPROJECTS + WRAPPERS, start=1):
        gh_name = project['gh_name']
        fmt_name = project['fmt_name']
        f.write(f'\n\n{idx}. **[{fmt_name}](https://github.com/open-quantum-safe/{gh_name})**\n\n\n')

        new_issues = gh([
            'search', 'issues',
            '--repo', f'open-quantum-safe/{gh_name}',
            '--created', f'>={earliest_merged_pr_cutoff.strftime("%Y-%m-%d")}',
            '--json', 'number,title,url,labels', '--limit', '100',
        ])
        if not new_issues:
            f.write('\t- New issues in the last 7 days: None.\n')
        else:
            f.write('\t- New issues in the last 7 days:\n')
            for issue in new_issues:
                f.write(f'\t\t - {format_item(issue, 'Issue')}\n')

        recently_merged = gh([
            'search', 'prs',
            '--repo', f'open-quantum-safe/{gh_name}',
            '--merged-at', f'>={earliest_merged_pr_cutoff.strftime("%Y-%m-%d")}',
            '--json', 'number,title,url,labels', '--limit', '100',
        ])
        if not recently_merged:
            f.write('\t- Merges in the last 7 days: None.\n')
        else:
            f.write('\t- Merges in the last 7 days:\n')
            for pr in recently_merged:
                f.write(f'\t\t - {format_item(pr, 'PR')}\n')

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
