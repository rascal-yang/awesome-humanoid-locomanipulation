<p align="center">
  <img src="assets/banner.svg" alt="Human demonstrations, whole-body motion, and humanoid interaction" width="100%">
</p>

<h1 align="center">Awesome-Humanoid-Locomanipulation</h1>

<p align="center">
  <strong>专注于人形机器人全身操作与交互的论文资源清单。</strong>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Loco--Manipulation-087f8c?style=flat-square" alt="Focus: Loco-Manipulation">
  <img src="https://img.shields.io/badge/Examples-5-4263eb?style=flat-square" alt="5 illustrative papers">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

人形移动操作将**移动、平衡与操作**协同起来。首页先按五个研究大方向组织，用 **5 篇论文**展示各方向的范围。论文可能跨越多个方向，这里按主要贡献各列一次。

**目录**

- [Real2Sim](#real2sim)
- [Harness & Real2Sim2Real](#harness-real2sim2real)
- [Interaction](#interaction)
- [基座](#foundations)
- [RSI](#rsi)

**表格说明。** 首次公开时间与发表信息分开记录；官方资源链接不代表代码或数据已完整发布。详细情况见 [来源说明](docs/SOURCES.md)。

<a id="real2sim"></a>

## Real2Sim

将真实世界示教重建或重定向为仿真可用的动作与场景表示。

| 论文 | 首次公开 / 发表 | 数据来源 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**OmniRetarget**](https://arxiv.org/abs/2509.26633)<br><sub>Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction</sub> | 2025-09<br><sub>ICRA 2026</sub> | 人体交互动捕 → 交互保持的参考轨迹 | 利用交互网格保留主体、物体与地形的空间和接触关系，支持跨物体、地形及机器人形态的重定向与扩增。 | [论文](https://arxiv.org/abs/2509.26633) · [项目](https://omniretarget.github.io/) · [代码](https://github.com/amazon-far/holosoma) · [数据](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) |

<a id="harness-real2sim2real"></a>

## Harness & Real2Sim2Real

覆盖仿真任务搭建、训练与评测流程，以及从仿真示教到真实机器人的策略迁移。

| 论文 | 首次公开 / 发表 | 数据来源 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**DemoHLM**](https://arxiv.org/abs/2510.11258)<br><sub>From One Demonstration to Generalizable Humanoid Loco-Manipulation</sub> | 2025-10<br><sub>arXiv</sub> | 单条仿真示教 → 合成训练数据 | 从单条仿真示教生成任务数据，在通用全身控制器之上训练视觉操作策略，并迁移到真实人形机器人。 | [论文](https://arxiv.org/abs/2510.11258) · [项目](https://beingbeyond.github.io/DemoHLM/) |

<a id="interaction"></a>

## Interaction

关注人形机器人与物体及环境的全身交互，包括接触表示与控制。

| 论文 | 首次公开 / 发表 | 数据来源 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | 单目 RGB 视频 → 机器人与物体参考轨迹 | 从单目视频提取并重定向人体与物体轨迹，通过联合跟踪机器人和物体状态学习全身交互技能。 | [论文](https://arxiv.org/abs/2509.16757) · [项目](https://hdmi-humanoid.github.io/) · [代码](https://github.com/LeCAR-Lab/HDMI) |

<a id="foundations"></a>

## 基座

支撑下游全身技能的可复用模型与通用策略。下例是仿真人体交互控制器，作为相关策略基座收录。

| 论文 | 首次公开 / 发表 | 数据来源 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimic**](https://arxiv.org/abs/2502.20390)<br><sub>Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions</sub> | 2025-02<br><sub>CVPR 2025</sub> | 不完美的人体交互动捕 → 物理修正后的交互 | 用教师策略修正不完美的交互动捕并蒸馏可扩展的仿真人体控制器，为物理约束下的交互数据提供基础。 | [论文](https://arxiv.org/abs/2502.20390) · [项目](https://sirui-xu.github.io/InterMimic/) · [代码](https://github.com/Sirui-Xu/InterMimic) |

<a id="rsi"></a>

## RSI

**Recursive Self-Improvement（递归自我改进）：** 利用执行反馈持续改进训练数据与策略的闭环。InterMimicGen 作为该方向中自演进动作模仿的示例。

| 论文 | 首次公开 / 发表 | 数据来源 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimicGen**](https://arxiv.org/abs/2610.06850)<br><sub>Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</sub> | 2026-10<br><sub>arXiv</sub> | 人体交互动捕 → 可执行机器人动作 | 将接触保持重定向、通用动作跟踪与执行验证后的数据扩增组成闭环，持续扩展带灵巧手的人形全身交互动作。 | [论文](https://arxiv.org/abs/2610.06850) · [项目](https://sirui-xu.github.io/InterMimicGen/) |

---

**更多资源：** [初版 17 项数据引擎清单](docs/DATA_ENGINE_READING_LIST.md) · [贡献指南](CONTRIBUTING.md) · [主题模板](docs/TOPIC_TEMPLATE.md)。

**参考仓库：** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation)。

**许可：** 原创整理文字与资产采用 [MIT 许可](LICENSE)；链接中的研究与资源保留各自许可。
