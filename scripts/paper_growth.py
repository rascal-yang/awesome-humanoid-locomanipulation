"""Build the README growth chart from primary entries, without network requests."""
from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

SECTIONS = (
    'Real2Sim', 'Real2Sim2Real', 'Sim2Real & Sim–Real Co-Training',
    'Interaction', 'Foundations', 'Harness', 'Iterative Improvement',
)
COLORS = ('#264E86', '#527EB5', '#87A6CC', '#168578', '#8056AE', '#CB8A2E', '#BC526B')
STYLES = ('solid', (0, (6, 2)), (0, (1, 2)), 'solid', 'solid', 'solid', 'solid')


@dataclass(frozen=True)
class Entry:
    identity: str
    section: str
    month: str
    year_only: bool = False


def identity(url: str) -> str:
    arxiv = re.search(r'arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})', url)
    if arxiv:
        return 'arxiv:' + arxiv.group(1)
    parsed = urlsplit(url)
    return urlunsplit((parsed.scheme.lower(), parsed.netloc.lower(), parsed.path.rstrip('/'), parsed.query, ''))


def parse_entries(text: str) -> list[Entry]:
    section = None
    entries, seen = [], set()
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith('## '):
            section = line[3:].split('｜', 1)[0].strip()
        if not re.match(r'^\|\s*\[\*\*', line):
            continue
        if section not in SECTIONS:
            raise ValueError(f'Unknown core section at line {number}: {section}')
        cells = line.split('|')[1:-1]
        if len(cells) != 5:
            raise ValueError(f'Expected five columns at line {number}')
        match = re.match(r'\s*\[\*\*.+?\*\*\]\(([^)]+)\)', cells[0])
        release = re.fullmatch(r'\s*(\d{4})(?:-(\d{2}))?\s*(?:<br>.*)?', cells[1])
        if not match or not release:
            raise ValueError(f'Missing primary URL or release date at line {number}')
        year, month = int(release[1]), int(release[2] or 12)
        date(year, month, 1)  # Invalid dates must fail rather than disappear from the chart.
        key = identity(match[1])
        if key in seen:
            raise ValueError(f'Duplicate primary work at line {number}: {key}')
        seen.add(key)
        entries.append(Entry(key, section, f'{year:04d}-{month:02d}', release[2] is None))
    if not entries:
        raise ValueError('No primary entries found')
    return entries


def validate_translation(primary: list[Entry], translated: list[Entry]) -> None:
    if set(primary) != set(translated):
        raise ValueError('English and Chinese identities, H2 sections, or dates differ')


def cumulative_counts(entries: list[Entry]) -> tuple[list[str], dict[str, list[int]]]:
    first, last = min(e.month for e in entries), max(e.month for e in entries)
    year, month = map(int, first.split('-'))
    months = []
    while f'{year:04d}-{month:02d}' <= last:
        months.append(f'{year:04d}-{month:02d}')
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    increments = Counter((e.section, e.month) for e in entries)
    counts = {}
    for section in SECTIONS:
        running, values = 0, []
        for m in months:
            running += increments[section, m]
            values.append(running)
        counts[section] = values
    return months, counts


def render(entries: list[Entry], output: Path, csv_path: Path, preview: Path | None = None) -> None:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.dates as mdates
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.ticker import MaxNLocator

    months, counts = cumulative_counts(entries)
    dates = [date.fromisoformat(m + '-01') for m in months]
    prior = date(dates[0].year - 1, 12, 1) if dates[0].month == 1 else date(dates[0].year, dates[0].month - 1, 1)
    dates = [prior] + dates
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'svg.fonttype': 'none', 'svg.hashsalt': 'humanoid-paper-growth', 'axes.unicode_minus': False})
    fig = plt.figure(figsize=(14, 8), facecolor='#FFFFFF')
    ax = fig.add_axes((0.075, 0.335, 0.86, 0.445))
    ax.set_facecolor('#FAFBFD')
    for i, section in enumerate(SECTIONS):
        values = [0] + counts[section]
        ax.step(dates, values, where='post', color=COLORS[i], linestyle=STYLES[i], linewidth=2.6, zorder=3)
        ax.plot(dates[-1], values[-1], 'o', color=COLORS[i], markersize=5.5, markeredgecolor='white', markeredgewidth=1, zorder=4)
    ax.set_ylim(0, max(c[-1] for c in counts.values()) * 1.12 + 1)
    end = dates[-1]
    next_month = date(end.year + 1, 1, 1) if end.month == 12 else date(end.year, end.month + 1, 1)
    ax.set_xlim(dates[0], next_month)
    years = range(dates[0].year, dates[-1].year + 1)
    ticks = [date(y, 1, 1) for y in years]
    ticks[0] = dates[0]
    ax.set_xticks(ticks, [str(y) for y in years])
    ax.xaxis.set_minor_locator(mdates.MonthLocator(bymonth=(4, 7, 10)))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True, nbins=6))
    ax.grid(axis='y', color='#E2E7EF', linewidth=0.8, zorder=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis='both', which='both', length=0, pad=10, labelsize=11, labelcolor='#64748B')
    ax.set_ylabel('Cumulative works', fontsize=11, color='#64748B', labelpad=14)
    fig.text(0.075, 0.925, 'A growing map of humanoid loco-manipulation', fontsize=23, weight='bold', color='#172B49')
    fig.text(0.075, 0.874, f'Core reading list  /  cumulative by first public release  /  through {months[-1]}', fontsize=12, color='#64748B')
    fig.text(0.935, 0.925, str(len(entries)), fontsize=27, weight='bold', color='#172B49', ha='right')
    fig.text(0.935, 0.885, 'CORE WORKS', fontsize=9, color='#64748B', ha='right')
    for i, section in enumerate(SECTIONS):
        column, row = divmod(i, 4)
        x, y = 0.08 + column * 0.46, 0.24 - row * 0.047
        fig.add_artist(Line2D((x, x + 0.028), (y, y), transform=fig.transFigure, color=COLORS[i], linestyle=STYLES[i], linewidth=2.6))
        fig.text(x + 0.04, y, section, va='center', fontsize=11, color='#334155')
        fig.text(x + 0.405, y, str(counts[section][-1]), va='center', ha='right', fontsize=11, weight='bold', color=COLORS[i])
    footnote = 'Source: README primary entries. One work, one main category. Includes papers and reports; not a field-wide publication count.'
    if any(e.year_only for e in entries):
        footnote += ' Year-only releases are placed at year-end.'
    fig.text(0.075, 0.025, footnote, fontsize=8.2, color='#718096')
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, format='svg', metadata={'Date': None, 'Creator': 'paper_growth.py', 'Description': footnote})
    if preview:
        preview.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(preview, dpi=140, facecolor=fig.get_facecolor())
    plt.close(fig)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['month', *SECTIONS, 'Total'])
        for i, month in enumerate(months):
            values = [counts[s][i] for s in SECTIONS]
            writer.writerow([month, *values, sum(values)])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--readme', type=Path, default=Path('README.md'))
    parser.add_argument('--translated-readme', type=Path, default=Path('README.zh-CN.md'))
    parser.add_argument('--output', type=Path, default=Path('assets/paper-growth.svg'))
    parser.add_argument('--csv', type=Path, default=Path('docs/paper-growth.csv'))
    parser.add_argument('--preview', type=Path)
    args = parser.parse_args()
    entries = parse_entries(args.readme.read_text('utf-8'))
    validate_translation(entries, parse_entries(args.translated_readme.read_text('utf-8')))
    render(entries, args.output, args.csv, args.preview)
    print(f'Generated {args.output}: {len(entries)} works across {len(SECTIONS)} H2 sections')


if __name__ == '__main__':
    main()
