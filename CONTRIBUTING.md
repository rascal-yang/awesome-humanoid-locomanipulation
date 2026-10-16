# Contributing

Thank you for helping build a focused, readable resource for humanoid loco-manipulation.

## Add a paper or resource

1. Check both READMEs for an existing entry.
2. Use an original paper, author project page, or author-owned repository as the source. Do not infer acceptance or resource availability from an aggregator.
3. First decide scope: add direct humanoid whole-body contributions to a suitable H3 subgroup in both `README.md` and `README.zh-CN.md`; put transferable arm, avatar, and general learning methods in both language sections of `docs/RELATED_READING.md`, with a scope boundary. Sort entries within each homepage subgroup newest first by first public release. Keep original titles and URLs identical across languages.
4. State the input and output, and write one factual sentence about the method. Avoid unsupported performance comparisons and marketing claims.
5. Link only verified official resources. Omit unavailable links rather than guessing a repository URL. A benchmark-only release should be labeled **Benchmark**, not presented as a complete data-generation implementation.
6. Update the homepage core-entry count in both READMEs, including badge URLs and alt text, and add a source note to `docs/SOURCES.md`. Update the curation date if you recheck the list.

```markdown
| [**Method**](PAPER_URL)<br><sub>Original full title</sub> | YYYY-MM<br><sub>Venue or arXiv</sub> | Source → output | One factual sentence. | [Paper](PAPER_URL) · [Project](PROJECT_URL) · [Code](CODE_URL) |
```

Use `YYYY` when only the year is verified. Keep venue and first release separate; later arXiv uploads can postdate a conference publication. Describe those exceptions in the source notes. Reuse the same URLs in both languages.

## Add a topic

The homepage currently uses seven H2 directions: Real2Sim, Real2Sim2Real, Sim2Real & Sim–Real Co-Training, Interaction, Foundations, Harness, and Iterative Improvement. H2 headings represent broad research directions, technical routes, or system paradigms; H3 headings describe concrete methods within them. For example, Real2Sim2Real is an H2 route, and counterfactual video augmentation is one H3 method within it. Harness is an H2 system paradigm, with spatial memory and skill orchestration at H3. Create or rename a subgroup when the existing label misrepresents a verified contribution; a useful subgroup may contain a single paper. Keep the names, order, and heading levels of these seven H2 sections fixed. Add or refine H3 subgroups, paper placement, cross-links, and tags within that structure; change H2 sections only when the maintainer explicitly requests it. Use [the topic template](docs/TOPIC_TEMPLATE.md) to define an H3 subgroup and its boundaries in both languages. Preserve existing explicit anchors when renaming or splitting headings, and link to the new subgroups when an old anchor covers several topics.

Give each work a primary table entry for readability, then use cross-links and concise contribution tags for other relevant directions. These are overlapping contributions, not mutually exclusive classes. Distinguish real-video reconstruction, virtual interaction synthesis, and simulation-demonstration expansion. Real-data co-training or real-robot evaluation alone does not establish a Real2Sim stage. For iterative improvement, state what persists and improves across rounds: data, policies, programs, or tools. Do not equate within-rollout feedback, synthetic data generation, or adaptive curriculum sampling with strict recursive self-improvement.

The initial 17-entry data-engine list is preserved as a dated historical snapshot in [a separate document](docs/DATA_ENGINE_READING_LIST.md). Distinguish simulated-human controllers from robot foundations and papers from project reports.

## Correct an entry

Explain what changed and link the source: title, venue, official code, dataset availability, or the summary. Please distinguish human-avatar research, robot reference data, simulated robot evaluation, and real-robot results.

## Before submitting

- Confirm paper titles, first-release dates, and any recorded venues against primary sources.
- Open each newly added link and check that it points to the intended author material.
- Preview both READMEs on GitHub: five columns, readable sentences, working contents anchors, no oversized badges.
- Keep both languages synchronized. If a translation is missing, explicitly mention that in the pull request.

## 中文说明

新增论文时请同步中英文 README，保持原始英文题名，写清数据来源与产出，并给出一句客观简介。每个 H3 内按首次公开时间倒序排列；会议年份单独标注。优先引用论文、作者项目页与官方仓库，不猜测代码地址，不把人体仿真结果写成真实机器人结果。

首页当前采用 Real2Sim、Real2Sim2Real、Sim2Real & Sim–Real Co-Training、Interaction、Foundations、Harness、Iterative Improvement 七个 H2 方向。H2 表示宏观研究方向、技术路线或系统范式，H3 表示其中的具体方法。例如 Real2Sim2Real 是 H2 路线，反事实视频扩增是其中的 H3 方法；Harness 是 H2 系统范式，空间记忆与技能编排是其中的 H3 方法。保持这七个 H2 的名称、顺序与层级不变；只有维护者明确要求时，才调整 H2。后续分类调整通过新增或细化 H3、调整论文位置、交叉链接与标签完成。H3 标题不能准确描述论文时，可以新建或改名，小节可以只有一篇。新增 H3 时使用主题模板说明范围，并同步两版目录；改名或拆分 H3 时保留已有显式锚点，必要时增加指向新小节的链接。

每项工作设一个主表格条目，交叉贡献通过链接和简短标签呈现，不要求互斥归类。真实视频重建、全虚拟交互合成和仿真示教扩增应分别描述；真实数据混合训练或真机评测本身不代表存在 Real2Sim。迭代改进需写清跨轮次保留并改进的对象，不将单次生成、回合内反馈或自适应采样等同于严格 RSI。机械臂、仿真人体与通用方法放入双语关联阅读并说明边界；项目报告与论文分别标注。
