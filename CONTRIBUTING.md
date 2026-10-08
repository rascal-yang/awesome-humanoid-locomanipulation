# Contributing

Thank you for helping build a focused, readable resource for humanoid loco-manipulation.

## Add a paper or resource

1. Check both READMEs for an existing entry.
2. Use an original paper, author project page, or author-owned repository as the source. Do not infer acceptance or resource availability from an aggregator.
3. Add the entry to the closest H2 direction in `README.md` and `README.zh-CN.md`, newest first by its first public release. Keep the original paper title in both versions.
4. State the input and output, and write one factual sentence about the method. Avoid unsupported performance comparisons and marketing claims.
5. Link only verified official resources. Omit unavailable links rather than guessing a repository URL. A benchmark-only release should be labeled **Benchmark**, not presented as a complete data-generation implementation.
6. Update the homepage example count in both READMEs, including badge URLs and alt text, and add a source note to `docs/SOURCES.md`. Update the curation date if you recheck the list.

```markdown
| [**Method**](PAPER_URL)<br><sub>Original full title</sub> | YYYY-MM<br><sub>Venue or arXiv</sub> | Source → output | One factual sentence. | [Paper](PAPER_URL) · [Project](PROJECT_URL) · [Code](CODE_URL) |
```

Use `YYYY` when only the year is verified. Keep venue and first release separate; later arXiv uploads can postdate a conference publication. Describe those exceptions in the source notes. Reuse the same URLs in both languages.

## Add a topic

The homepage currently uses five H2 directions: Real2Sim, Harness & Real2Sim2Real, Interaction, Foundations (基座), and RSI (Recursive Self-Improvement). Keep this broad structure without H3 subgroups. To propose another H2 direction, use [the topic template](docs/TOPIC_TEMPLATE.md), define its scope, and provide a few verified examples in both languages.

The initial 17-entry data-engine list is preserved in [a separate document](docs/DATA_ENGINE_READING_LIST.md). A paper may fit multiple directions; list it once on the homepage under its primary contribution. Distinguish reusable simulated-human controllers from robot foundation models, and self-evolving data pipelines from broader claims of recursive self-improvement.

## Correct an entry

Explain what changed and link the source: title, venue, official code, dataset availability, or the summary. Please distinguish human-avatar research, robot reference data, simulated robot evaluation, and real-robot results.

## Before submitting

- Confirm paper titles, first-release dates, and any recorded venues against primary sources.
- Open each newly added link and check that it points to the intended author material.
- Preview both READMEs on GitHub: five columns, readable sentences, working contents anchors, no oversized badges.
- Keep both languages synchronized. If a translation is missing, explicitly mention that in the pull request.

## 中文说明

新增论文时请同步中英文 README，保持原始英文题名，写清数据来源与产出，并给出一句客观简介。按首次公开时间倒序排列；会议年份单独标注。优先引用论文、作者项目页与官方仓库，不猜测代码地址，不把人体仿真结果写成真实机器人结果。首页先保持 Real2Sim、Harness & Real2Sim2Real、Interaction、基座、RSI 五个 H2 大方向，不增加 H3。按主要贡献归类，避免重复收录；RSI 指递归自我改进。新增 H2 时使用主题模板，同步目录与中文标题。
