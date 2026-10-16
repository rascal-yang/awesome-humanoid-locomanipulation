# H3 topic template / H3 子主题模板

Use this template to add or revise an H3 subgroup under an existing H2 in both READMEs. The seven H2 names, order, and heading levels are fixed: Real2Sim, Real2Sim2Real, Sim2Real & Sim–Real Co-Training, Interaction, Foundations, Harness, and Iterative Improvement. Change H2 sections only when the maintainer explicitly requests it.

Copy the block below into the appropriate existing H2 section in both READMEs. Translate the prose and summaries, replace every placeholder before publishing, and keep paper titles and URLs identical in both versions.

````markdown
### Concrete method within this direction

**Scope.** One or two sentences describing the method and its role within the existing H2 direction.

**Reading guide.** A few starting points and what each contributes.

| Paper | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**Method**](PAPER_URL)<br><sub>Original full title</sub> | YYYY-MM<br><sub>Venue or arXiv</sub> | Source → output | One factual sentence. | [Paper](PAPER_URL) · [Project](PROJECT_URL) |

````

Add an H3 contents link in each README, update the entry count if papers are added or removed, and record primary sources in `docs/SOURCES.md`. A subgroup may contain one verified work. Preserve existing anchors when renaming or splitting H3 subgroups; express overlapping contributions through cross-links and tags.

A heading must not imply a pipeline stage absent from its entries. Distinguish Real2Sim reconstruction, fully virtual synthesis, simulation-demonstration expansion, and sim-and-real co-training.

中文操作：保持现有七个 H2 的名称、顺序与层级不变，只有维护者明确要求时才调整 H2。在合适的现有 H2 下新增或细化 H3，说明具体方法与所属方向的关系，并同步中英文目录、范围与简介，保留相同的论文题名和链接。小节可以只有一项经核实的工作；论文数量变化时同步更新计数与来源说明。

通过调整论文位置、交叉链接和标签呈现重叠贡献，不要求互斥归类。改名或拆分 H3 时保留已有锚点；标题不应暗示论文中不存在的步骤，应区分 Real2Sim 重建、全虚拟合成、仿真示教扩增和虚实混合训练。
