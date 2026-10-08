# Contributing

Thank you for helping build a focused, readable resource for humanoid loco-manipulation.

## Add a paper or resource

1. Check both READMEs for an existing entry.
2. Use an original paper, author project page, or author-owned repository as the source. Do not infer acceptance or resource availability from an aggregator.
3. Add the entry to the closest subgroup in `README.md` and `README.zh-CN.md`, newest first by its first public release. Keep the original paper title in both versions.
4. State the input and output, and write one factual sentence about the method. Avoid unsupported performance comparisons and marketing claims.
5. Link only verified official resources. Omit unavailable links rather than guessing a repository URL. A benchmark-only release should be labeled **Benchmark**, not presented as a complete data-generation implementation.
6. Update the entry count in both READMEs, including badge URLs and alt text, and add a source note to `docs/SOURCES.md`. Update the curation date if you recheck the list.

```markdown
| [**Method**](PAPER_URL)<br><sub>Original full title</sub> | YYYY-MM<br><sub>Venue or arXiv</sub> | Source → output | One factual sentence. | [Paper](PAPER_URL) · [Project](PROJECT_URL) · [Code](CODE_URL) |
```

Use `YYYY` when only the year is verified. Keep venue and first release separate; later arXiv uploads can postdate a conference publication. Describe those exceptions in the source notes. Reuse the same URLs in both languages.

## Add a topic

Copy [the topic template](docs/TOPIC_TEMPLATE.md), choose a clear scope, and add an H2 section to each README. Add contents links and optional H3 subgroups as needed. Start with a few verified entries; empty speculative categories should remain proposals rather than public tables.

The initial data-engine topic remains independent. Possible future topics include contact-rich whole-body control, visual loco-manipulation, and planning and evaluation, once contributors supply relevant entries.

## Correct an entry

Explain what changed and link the source: title, venue, official code, dataset availability, or the summary. Please distinguish human-avatar research, robot reference data, simulated robot evaluation, and real-robot results.

## Before submitting

- Confirm paper titles, first-release dates, and any recorded venues against primary sources.
- Open each newly added link and check that it points to the intended author material.
- Preview both READMEs on GitHub: five columns, readable sentences, working contents anchors, no oversized badges.
- Keep both languages synchronized. If a translation is missing, explicitly mention that in the pull request.

## 中文说明

新增论文时请同步中英文 README，保持原始英文题名，写清数据来源与产出，并给出一句客观简介。按首次公开时间倒序排列；会议年份单独标注。优先引用论文、作者项目页与官方仓库，不猜测代码地址，不把人体仿真结果写成真实机器人结果。新增主题直接复制主题模板，增加 H2 标题与目录链接即可。
