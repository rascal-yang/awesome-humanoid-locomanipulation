# Reading-list growth / 收录增长图

The chart in both READMEs shows **cumulative core works by first public release month**, with one line for each of the seven H2 sections. It counts the current reading list, including papers and explicitly labeled reports; it is not a field-wide publication statistic or a history of when entries were added to GitHub.

图表按**首次公开月份**累计当前核心条目，每个 H2 一条线，包含已明确标注的论文与报告。它反映当前清单的时间分布，不是全领域发文量，也不是仓库历次添加条目的历史。

## Counting / 统计口径

- `README.md` is the data source; only primary paper/project table rows count. Cross-links and related reading do not count again.
- Each work belongs to its main H2. Moving a work changes that category's curve. Removing a work removes it from the current retrospective counts.
- English and Chinese primary URLs, categories, and release dates must agree. Duplicate arXiv versions and invalid dates fail validation instead of being silently counted.
- Months without new works retain the previous cumulative value. A verified year without a month is placed at December of that year, and the chart displays a note when such entries exist; December is a counting convention, not an inferred publication month.
- Blue shades and distinct line styles group Real2Sim, Real2Sim2Real, and Sim2Real & Sim–Real Co-Training. Other H2 sections have distinct colors.
- The legend totals and headline count come from the data, rather than fixed numbers. The time axis ends at the latest listed release month.

统计只读取英文 README 的主表格条目，跨方向引用与关联阅读不重复计数；中文版本用于一致性核验。条目移类或删除后，累计值会按当前清单重算。仅有年份时统一放到当年年末，并在图上注明该约定，不伪造月份。

## Automatic refresh / 自动更新

The [`Update paper growth chart`](../.github/workflows/update-paper-growth.yml) workflow runs after relevant README, chart script, test, dependency, or workflow changes are pushed to `main`. It checks bilingual consistency, regenerates the SVG and [monthly CSV](paper-growth.csv), and commits only those two generated files when their contents change. It can also be run from the Actions tab using **Run workflow**.

The workflow uses the repository's `GITHUB_TOKEN` with `contents: write` for its update job; no personal token or external chart service is required. Chart-only commits are excluded from its path triggers, and unchanged output creates no commit. If repository policy blocks bot commits, the job fails visibly rather than force-pushing or bypassing that policy.

相关 README、绘图脚本或配置更新并推送到 `main` 后，GitHub Actions 自动重算并提交 SVG 与 CSV；数据未变则不产生提交。也可在 Actions 中手动运行。首次推送这套配置后才能在 GitHub 上运行；本地成功生成不代表云端工作流已验证。

## Local generation / 本地生成

Run from the repository root with Python 3.10 or newer:

```sh
python -m pip install -r scripts/requirements-chart.txt
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/paper_growth.py
```

Optional PNG preview (the README uses the SVG):

```sh
python scripts/paper_growth.py --preview paper-growth-preview.png
```

The script makes no network requests and does not modify either README. The Matplotlib version and SVG metadata are fixed to avoid timestamp-only changes. GitHub Actions uses Python 3.12; minor rendering differences across local environments may still change the SVG once.
