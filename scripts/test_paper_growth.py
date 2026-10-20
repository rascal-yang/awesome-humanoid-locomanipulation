import unittest
import re
from pathlib import Path

from paper_growth import parse_entries, cumulative_counts, validate_translation


def row(name, url, date):
    return f'| [**{name}**]({url})<br><sub>Original title</sub> | {date}<br><sub>arXiv</sub> | input → output | Summary. | [Paper]({url}) |'


class PaperGrowthTests(unittest.TestCase):
    def test_real_readmes_match_the_badge_and_each_other(self):
        repo = Path(__file__).resolve().parents[1]
        entries = parse_entries((repo / 'README.md').read_text('utf-8'))
        badge = re.search(r'Core_entries-(\d+)-', (repo / 'README.md').read_text('utf-8'))
        self.assertEqual(len(entries), int(badge.group(1)))
        validate_translation(entries, parse_entries((repo / 'README.zh-CN.md').read_text('utf-8')))

    def test_links_outside_primary_rows_are_not_counted(self):
        text = '## Interaction\n' + row('A', 'https://arxiv.org/abs/2401.00001', '2024-01')
        text += '\nSee [A](https://arxiv.org/abs/2401.00001) again.\n'
        self.assertEqual(len(parse_entries(text)), 1)

    def test_versions_cannot_be_counted_twice(self):
        text = '## Interaction\n' + row('A', 'https://arxiv.org/abs/2401.00001v1', '2024-01')
        text += '\n' + row('A revised', 'https://arxiv.org/abs/2401.00001v2', '2024-01')
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            parse_entries(text)

    def test_monthly_cumulative_counts_keep_empty_months(self):
        text = '## Interaction\n' + row('A', 'https://arxiv.org/abs/2401.00001', '2024-01')
        text += '\n## Foundations\n' + row('B', 'https://arxiv.org/abs/2403.00001', '2024-03')
        months, counts = cumulative_counts(parse_entries(text))
        self.assertEqual(months, ['2024-01', '2024-02', '2024-03'])
        self.assertEqual(counts['Interaction'], [1, 1, 1])
        self.assertEqual(counts['Foundations'], [0, 0, 1])
        self.assertEqual(counts['Real2Sim'], [0, 0, 0])

    def test_year_only_dates_are_explicitly_bucketed_at_year_end(self):
        entry = parse_entries('## Harness\n' + row('A', 'https://example.org/report', '2023'))[0]
        self.assertEqual(entry.month, '2023-12')
        self.assertTrue(entry.year_only)

    def test_bad_dates_or_unknown_sections_fail_instead_of_dropping_entries(self):
        for heading, date in [('Interaction', '2024-13'), ('Unknown', '2024-01'), ('Interaction', 'TBD')]:
            with self.subTest(heading=heading, date=date), self.assertRaises(ValueError):
                parse_entries(f'## {heading}\n' + row('A', 'https://example.org/a', date))

    def test_translation_date_or_category_mismatch_fails(self):
        en = parse_entries('## Interaction\n' + row('A', 'https://example.org/a', '2024-01'))
        for heading, date in [('Foundations｜基座', '2024-01'), ('Interaction｜交互', '2024-02')]:
            with self.assertRaisesRegex(ValueError, 'differ'):
                validate_translation(en, parse_entries(f'## {heading}\n' + row('A', 'https://example.org/a', date)))


if __name__ == '__main__':
    unittest.main()
