import unittest
import re
import csv
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from paper_growth import SECTIONS, parse_entries, cumulative_counts, validate_translation, render


def row(name, url, date):
    return f'| [**{name}**]({url})<br><sub>Original title</sub> | {date}<br><sub>arXiv</sub> | input → output | Summary. | [Paper]({url}) |'


class PaperGrowthTests(unittest.TestCase):
    def test_render_merges_simulation_routes_each_month_but_keeps_csv_breakdown(self):
        text = '\n'.join([
            '## Real2Sim', row('A', 'https://arxiv.org/abs/2401.00001', '2024-01'),
            '## Real2Sim2Real', row('B', 'https://arxiv.org/abs/2402.00002', '2024-02'),
            '## Sim2Real & Sim–Real Co-Training', row('C', 'https://arxiv.org/abs/2403.00003', '2024-03'),
            '## Interaction', row('D', 'https://arxiv.org/abs/2401.00004', '2024-01'),
            row('E', 'https://arxiv.org/abs/2403.00005', '2024-03'),
            '## Foundations', row('F', 'https://arxiv.org/abs/2402.00006', '2024-02'),
            '## Harness', row('G', 'https://arxiv.org/abs/2401.00007', '2024-01'),
            '## Iterative Improvement', row('H', 'https://arxiv.org/abs/2403.00008', '2024-03'),
        ])
        entries = parse_entries(text)
        cases = [
            ('2024-01', {'Simulation & Transfer': '1', 'Interaction': '1', 'Foundations': '0', 'Harness': '1', 'Iterative Improvement': '0'}, '3'),
            ('2024-02', {'Simulation & Transfer': '2', 'Interaction': '1', 'Foundations': '1', 'Harness': '1', 'Iterative Improvement': '0'}, '5'),
            ('2024-03', {'Simulation & Transfer': '3', 'Interaction': '2', 'Foundations': '1', 'Harness': '1', 'Iterative Improvement': '1'}, '8'),
        ]
        with tempfile.TemporaryDirectory() as temporary:
            output, csv_path = Path(temporary) / 'chart.svg', Path(temporary) / 'counts.csv'
            for month, expected_legend, expected_total in cases:
                with self.subTest(month=month):
                    render([e for e in entries if e.month <= month], output, csv_path)
                    texts = [node.text for node in ET.parse(output).iter('{http://www.w3.org/2000/svg}text')]
                    labels = {*SECTIONS, 'Simulation & Transfer'}
                    legend = {label: texts[i + 1] for i, label in enumerate(texts) if label in labels}
                    self.assertEqual(legend, expected_legend)
                    with csv_path.open(encoding='utf-8', newline='') as data:
                        reader = csv.DictReader(data)
                        self.assertEqual(reader.fieldnames, ['month', *SECTIONS, 'Total'])
                        rows = list(reader)
                    self.assertEqual(rows[-1]['Total'], expected_total)
                    self.assertEqual(rows[-1]['Real2Sim'], '1')
                    self.assertEqual(rows[-1]['Real2Sim2Real'], '0' if month == '2024-01' else '1')
                    self.assertEqual(rows[-1]['Sim2Real & Sim–Real Co-Training'], '1' if month == '2024-03' else '0')

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
