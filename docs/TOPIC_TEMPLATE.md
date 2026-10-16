# Topic template / 新增主题模板

Copy the block below into both READMEs and translate the prose and summaries. Replace every placeholder before publishing. Keep paper titles and URLs identical in both versions.

````markdown
## Broad research direction, technical route, or system paradigm

**Scope.** One or two sentences defining what belongs in this topic.

**Reading guide.** A few starting points and what each contributes.

### Concrete method within this direction

One sentence describing the concrete method and its role within the H2 direction.

| Paper | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**Method**](PAPER_URL)<br><sub>Original full title</sub> | YYYY-MM<br><sub>Venue or arXiv</sub> | Source → output | One factual sentence. | [Paper](PAPER_URL) · [Project](PROJECT_URL) |

````

Add a contents anchor in each README, update the total entry count, and record primary sources in `docs/SOURCES.md`. Prefer a short table over a large number of columns; use H2 for broad research directions, technical routes, or system paradigms, and H3 for concrete methods within them. Real2Sim2Real and Harness belong at H2; video augmentation and skill orchestration are H3 methods. Add both levels to the contents when introducing a new subgroup.

中文操作：复制模板，在两版 README 中新增同级 H2 标题与目录入口；翻译范围、阅读建议、数据来源与简介，保留相同的题名与链接。H2 表示宏观研究方向、技术路线或系统范式，H3 表示其中的具体方法；Real2Sim2Real、Harness 属于 H2，视频扩增、技能编排属于 H3；新增 H3 时同步目录链接；没有实际条目的新主题先通过 issue 提议。

A subgroup may contain one verified work when it defines a useful distinction. Give each work a primary entry and add cross-links and contribution tags for overlapping directions. A heading must not imply a pipeline stage absent from its entries; distinguish Real2Sim reconstruction, fully virtual synthesis, simulation-demonstration expansion, and sim-and-real co-training. Preserve existing explicit anchors when renaming or splitting topics.

小节可以只有一项经核实的工作。每项设一个主条目，其他相关方向通过交叉链接与贡献标签呈现，不要求互斥归类。标题不应暗示条目中不存在的流程步骤；区分 Real2Sim 重建、全虚拟合成、仿真示教扩增和虚实混合训练。改名或拆分时保留已有显式锚点。
