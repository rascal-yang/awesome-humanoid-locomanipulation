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
  <img src="https://img.shields.io/badge/Core_entries-17-4263eb?style=flat-square" alt="17 core entries">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

人形移动操作将**移动、平衡与操作**协同起来。本清单按六个研究方向组织 **17 项核心工作**，每项设一个主条目，并用交叉链接呈现重叠贡献；另提供 [13 项关联方法](docs/RELATED_READING.md#中文)，说明机械臂、仿真人体与通用学习方法对本主题的参考价值。

**收录范围：** 优先选择直接研究人形全身操作、接触交互、重定向、训练迁移或执行系统的工作。论文与项目报告明确区分，分类属于编辑判断。

**分类核对：2026-10-16。** 表中为首次公开月份与单独核实的发表信息，不是阅读日期。资源链接不保证完整实现已发布，见 [来源与收录说明](docs/SOURCES.md)。

小节按研究问题或数据生成路径组织，可以只有一项工作；标签呈现交叉贡献，不要求一篇论文只属于一个互斥类别。

**目录**

- [Motion Retargeting｜动作重定向](#retargeting)
  - [接触保持的重定向](#motion-retargeting)
- [Data Generation & Policy Learning｜数据生成与策略学习](#data-generation-policy-learning)
  - [视频扩增与虚实迁移](#video-augmentation-real2sim2real)
  - [基于资产与视频先验的交互合成](#asset-video-interaction-synthesis)
  - [仿真中的示教扩增](#simulation-demonstration-expansion)
- [Interaction｜交互学习与控制](#interaction)
  - [从人类视频学习交互](#interaction-learning-from-human-videos)
  - [灵巧全身交互](#dexterous-whole-body-interaction)
  - [接触与力控制](#contact-force-control)
- [Foundations｜模型与控制基座](#foundations)
  - [全身 VLA 与人类数据预训练](#whole-body-vla-human-pretraining)
  - [世界模型条件化的全身策略](#world-model-conditioned-policies)
  - [通用全身控制](#generalist-whole-body-control)
- [Systems｜系统与技能编排](#systems)
  - [空间记忆与长程技能编排](#spatial-memory-skill-orchestration)
- [Iterative Improvement｜迭代改进](#iterative-improvement)
  - [执行反馈驱动的数据与策略协同改进](#execution-guided-data-policy-co-improvement)

<a id="retargeting"></a>
<a id="real2sim"></a>

## Motion Retargeting｜动作重定向

将人体动作与交互几何适配到机器人形态，为后续学习和控制提供参考轨迹。

<a id="motion-retargeting"></a>
<a id="contact-preserving-motion-retargeting"></a>
<a id="接触保持的动作重定向"></a>

### 接触保持的重定向

在跨形态适配示教动作时，保持机器人、物体与环境之间的接触关系。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**OTRetarget**](https://arxiv.org/abs/2609.36602)<br><sub>OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport</sub> | 2026-09<br><sub>arXiv</sub> | 人体物体示教 → 机器人与物体联合参考轨迹 | 利用最优传输匹配表面交互，联合优化机器人与物体位姿，在形态变化后保留接触关系。<br><sub>标签: Contact preservation · Joint robot–object optimization</sub> | [论文](https://arxiv.org/abs/2609.36602) |
| [**OmniRetarget**](https://arxiv.org/abs/2509.26633)<br><sub>OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction</sub> | 2025-09<br><sub>ICRA 2026</sub> | 人体交互动捕 → 交互保持的参考轨迹 | 利用交互网格保留主体、物体与地形的关系，支持动作重定向与扩增。<br><sub>标签: Contact preservation · Motion augmentation</sub> | [论文](https://arxiv.org/abs/2509.26633) · [项目](https://omniretarget.github.io/) · [代码](https://github.com/amazon-far/holosoma) · [数据](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) |

**跨方向阅读：** [HumanX 与 HDMI](#interaction-learning-from-human-videos) 从视频恢复交互参考；[Weave](#dexterous-whole-body-interaction) 与 [InterMimicGen](#execution-guided-data-policy-co-improvement) 也包含接触感知重定向。

[关联视频重建与资产方法](docs/RELATED_READING.md#real2sim-zh)：EgoInfinity、EgoEngine、USDCraft。

<a id="data-generation-policy-learning"></a>
<a id="harness-real2sim2real"></a>
<a id="harness--real2sim2real"></a>
<a id="simulation-policy-transfer"></a>
<a id="simulation-data-generation--policy-transfer"></a>
<a id="仿真数据生成与策略迁移"></a>

## Data Generation & Policy Learning｜数据生成与策略学习

按数据来源与生成机制区分真实视频重建、全虚拟合成和仿真示教扩增；训练中使用真实数据本身不代表存在 Real2Sim 步骤。

<a id="video-augmentation-real2sim2real"></a>

### 视频扩增与虚实迁移

从真实交互视频扩增数据，重建机器人可用的参考轨迹，再将训练后的策略部署到真机。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**PRISM**](https://arxiv.org/abs/2609.38172)<br><sub>Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | 少量真实视频 → 扩增数据 → 真机策略 | 生成反事实交互视频，重建接触锚定的参考轨迹，并训练可用于真实人形机器人搬运的策略。<br><sub>标签: Video generation · Real2Sim2Real</sub> | [论文](https://arxiv.org/abs/2609.38172) |

<a id="asset-video-interaction-synthesis"></a>

### 基于资产与视频先验的交互合成

从已知虚拟资产和场景出发，利用视频先验合成用于机器人学习的交互数据。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**GRAIL**](https://arxiv.org/abs/2606.05160)<br><sub>GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors</sub> | 2026-06<br><sub>CoRL 2026</sub> | 3D 资产与视频先验 → 人形机器人训练数据 | 在已知虚拟场景中合成交互，恢复具有真实尺度的 4D 轨迹，并训练可迁移至真机的人形策略。<br><sub>标签: 3D assets · Video priors · Sim-to-real</sub> | [论文](https://arxiv.org/abs/2606.05160) · [代码](https://github.com/NVlabs/GRAIL) |

<a id="simulation-demonstration-expansion"></a>

### 仿真中的示教扩增

将少量仿真机器人示教适配、扩增为大规模数据；部署可采用仿真到现实迁移或虚实数据混合训练。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanoidMimicGen**](https://arxiv.org/abs/2605.27724)<br><sub>HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning</sub> | 2026-05<br><sub>arXiv</sub> | 仿真机器人示教 → 扩增仿真数据 → 虚实混合训练 | 通过技能适配与全身规划扩增仿真示教，真机评测时再与真实示教混合训练策略。<br><sub>标签: Simulation data · Whole-body planning · Sim-and-real co-training</sub> | [论文](https://arxiv.org/abs/2605.27724) · [项目](https://humanoidmimicgen.github.io/) · [基准代码](https://github.com/NVlabs/humanoidmimicgen) |
| [**DemoHLM**](https://arxiv.org/abs/2510.11258)<br><sub>DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation</sub> | 2025-10<br><sub>arXiv</sub> | 单条仿真示教 → 合成训练数据 | 从单条仿真示教扩增任务数据，在全身控制器之上学习视觉操作策略并迁移至真机。<br><sub>标签: Simulation data · Demonstration expansion · Sim-to-real</sub> | [论文](https://arxiv.org/abs/2510.11258) · [项目](https://beingbeyond.github.io/DemoHLM/) |

**跨方向阅读：** [HumanX](#interaction-learning-from-human-videos) 也包含交互数据扩增；[InterMimicGen](#execution-guided-data-policy-co-improvement) 则将扩增与多轮执行、跟踪器更新相连。执行系统集成见 [Systems](#systems)。

<a id="interaction"></a>

## Interaction｜交互学习与控制

学习并控制人形机器人与物体、环境的物理交互，覆盖身体与手部协调及接触力调节。

<a id="interaction-learning-from-human-videos"></a>
<a id="human-object-interaction"></a>
<a id="whole-body-interaction-from-demonstrations"></a>
<a id="从示教学习全身交互"></a>

### 从人类视频学习交互

从视频恢复人体与物体的交互参考，学习能够执行相应交互的机器人策略。基于捕获示教的灵巧手与全身协调见 [灵巧全身交互](#dexterous-whole-body-interaction)。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanX**](https://arxiv.org/abs/2602.02473)<br><sub>HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos</sub> | 2026-02<br><sub>CoRL 2026</sub> | 人类视频 → 扩增参考轨迹 → 交互技能 | 结合以锚点为中心的交互合成与交互优先的模仿学习，获得可迁移至 G1 的敏捷技能。<br><sub>标签: Video reconstruction · Data augmentation · Interaction learning</sub> | [论文](https://arxiv.org/abs/2602.02473) · [项目](https://wyhuai.github.io/human-x/) |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | 单目 RGB 视频 → 全身交互策略 | 提取人体与物体轨迹，通过联合跟踪机器人和物体状态学习全身交互技能。<br><sub>标签: Video reconstruction · Interaction imitation · Sim-to-real</sub> | [论文](https://arxiv.org/abs/2509.16757) · [项目](https://hdmi-humanoid.github.io/) · [代码](https://github.com/LeCAR-Lab/HDMI) |

<a id="dexterous-whole-body-interaction"></a>

### 灵巧全身交互

从捕获的示教学习交互，重点协调全身运动与灵巧手接触。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**Weave**](https://arxiv.org/abs/2609.16683)<br><sub>Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions</sub> | 2026-09<br><sub>arXiv</sub> | 人体交互动捕 → 灵巧机器人与物体交互 | 结合接触感知重定向与几何感知策略，协调身体和手指关节以跟踪机器人与物体参考轨迹。<br><sub>标签: HOI motion capture · Dexterous hands · Contact-aware retargeting</sub> | [论文](https://arxiv.org/abs/2609.16683) · [项目](https://xiaohu-art.github.io/Weave/) |

<a id="contact-force-control"></a>

### 接触与力控制

在执行动作轨迹时进一步调节柔顺性与接触力。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**KPI**](https://arxiv.org/abs/2609.36151)<br><sub>KPI: A Promptable Kernel for Physical Interaction on Humanoids</sub> | 2026-09<br><sub>arXiv</sub> | 轨迹与交互约束 → 自适应接触控制 | 在保留底层全身跟踪器的基础上，按跟踪、柔顺及力范围要求调整手臂阻抗与参考量。<br><sub>标签: Impedance adaptation · Force regulation</sub> | [论文](https://arxiv.org/abs/2609.36151) · [项目](https://kpi-robot.github.io/) |

**跨方向阅读：** [PRISM](#video-augmentation-real2sim2real) 与 [GRAIL](#asset-video-interaction-synthesis) 也学习交互策略，主条目侧重其数据生成贡献。[KPI](#contact-force-control) 还包含智能体驱动的轨迹与交互约束生成。

<a id="foundations"></a>

## Foundations｜模型与控制基座

收录直接支撑人形全身技能的可复用模型与控制接口，区分人体数据预训练的 VLA、世界模型条件化策略和通用运动控制器。

<a id="whole-body-vla-human-pretraining"></a>
<a id="whole-body-action-models"></a>
<a id="全身动作模型"></a>

### 全身 VLA 与人类数据预训练

利用人类经验预训练全身视觉语言动作策略，并适配到机器人形态。世界模型条件化的路线见 [MotionWAM](#world-model-conditioned-policies)。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**λ₀**](https://arxiv.org/abs/2610.00438)<br><sub>Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining</sub> | 2026-09<br><sub>arXiv</sub> | 第一视角身体与手部数据 → 全身 VLA | 通过分阶段人体数据预训练与形态适配，学习协调全身和手部动作的策略。<br><sub>标签: VLA · Human-data pretraining · Embodiment adaptation</sub> | [论文](https://arxiv.org/abs/2610.00438) |

<a id="world-model-conditioned-policies"></a>

### 世界模型条件化的全身策略

以学习到的视觉动态特征为条件，预测协调的全身动作。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**MotionWAM**](https://arxiv.org/abs/2606.09215)<br><sub>MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | 第一视角视频 → 统一全身动作 token | 利用视频世界模型特征驱动统一全身策略，实时协调移动、躯干、足部与手部动作。<br><sub>标签: Video world model · Unified whole-body actions</sub> | [论文](https://arxiv.org/abs/2606.09215) |

<a id="generalist-whole-body-control"></a>

### 通用全身控制

面向多种指令接口、遥操作或任务目标提供可复用运动控制；各方法支持的接口有所不同。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**ULTRA**](https://arxiv.org/abs/2603.03279)<br><sub>ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation</sub> | 2026-03<br><sub>IROS 2026</sub> | 动作参考或稀疏目标 → 全身控制 | 将动作跟踪技能蒸馏为多模态控制器，支持从稀疏目标和第一视角感知产生自主行为。<br><sub>标签: Multimodal control · Sparse goals · Motion tracking</sub> | [论文](https://arxiv.org/abs/2603.03279) |
| [**HOVER**](https://arxiv.org/abs/2410.21229)<br><sub>HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</sub> | 2024-10<br><sub>ICRA 2025</sub> | 多种指令空间 → 单一全身控制器 | 以运动学动作模仿为共同基础，将多种控制模式蒸馏到同一策略中。<br><sub>标签: Multi-mode control · Policy distillation</sub> | [论文](https://arxiv.org/abs/2410.21229) · [项目](https://hover-versatile-humanoid.github.io/) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858)<br><sub>OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</sub> | 2024-06<br><sub>CoRL 2024</sub> | 运动学位姿指令 → 全身遥操作与技能学习 | 提供统一位姿接口与可部署的全身控制器，支持遥操作及从示教学得自主技能。<br><sub>标签: Teleoperation · Whole-body control · Imitation learning</sub> | [论文](https://arxiv.org/abs/2406.08858) · [项目](https://omni.human2humanoid.com/) |

**跨方向阅读：** [InterMimicGen](#execution-guided-data-policy-co-improvement) 除迭代数据循环外，也训练通用交互跟踪器。

[关联模型与学习基础](docs/RELATED_READING.md#foundations-zh)：Astranomy、InternW0-Δ、Diffusion Policy、Dreamer、InterMimic。

<a id="systems"></a>

## Systems｜系统与技能编排

将感知、记忆、可复用技能和执行反馈组织为可运行的人形机器人系统。

<a id="spatial-memory-skill-orchestration"></a>
<a id="agentic-skill-orchestration"></a>
<a id="智能体技能编排"></a>

### 空间记忆与长程技能编排

利用空间记忆与技能执行结果，规划并调整长时程任务执行。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HomeBody**](https://tml.stanford.edu/homebody/)<br><sub>HomeBody: A Humanoid That Explores, Remembers, and Acts on Its Own</sub> | 2026-09<br><sub>项目报告</sub> | 空间记忆与技能库 → 长时程任务执行 | 将 VLM 与导航、操作技能相连，用空间记忆和执行结果协调 G1 的长时程任务。<br><sub>标签: Spatial memory · Skill orchestration · Execution feedback</sub> | [项目报告](https://tml.stanford.edu/homebody/) |

**跨方向阅读：** [OmniH2O](#generalist-whole-body-control) 连接遥操作与技能学习；[KPI](#contact-force-control) 连接智能体生成的参考轨迹与接触调节。

[关联执行与训练方法](docs/RELATED_READING.md#harness-zh)：RoboICL、Recova、SGS。

<a id="iterative-improvement"></a>
<a id="rsi"></a>

## Iterative Improvement｜迭代改进

利用跨轮次保留的执行反馈改进后续数据或策略，明确改进对象与机制；迭代数据飞轮不等于不受限的递归自我改进（RSI）。

<a id="execution-guided-data-policy-co-improvement"></a>
<a id="self-evolving-data-engines"></a>
<a id="execution-guided-data--policy-improvement"></a>
<a id="执行反馈驱动的数据与策略改进"></a>

### 执行反馈驱动的数据与策略协同改进

保留成功执行结果，作为后续轮次数据扩增与跟踪策略更新的起点。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimicGen**](https://arxiv.org/abs/2610.06850)<br><sub>InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</sub> | 2026-10<br><sub>arXiv</sub> | 交互参考与执行结果 → 扩增动作及改进后的跟踪器 | 迭代扰动交互参考、微调通用跟踪器，并保留成功执行的变体作为下一轮扩增种子。<br><sub>标签: Contact-aware retargeting · Generalist tracking · Iterative augmentation</sub> | [论文](https://arxiv.org/abs/2610.06850) · [项目](https://sirui-xu.github.io/InterMimicGen/) |

[关联程序与执行框架演进](docs/RELATED_READING.md#rsi-zh)：HarnessPAI、PhysEvo。它们提供可借鉴的机制，评测范围与人形全身控制有所不同。

---

**更多资源：** [关联方法与基础阅读](docs/RELATED_READING.md#中文) · [历史数据引擎清单（2026-10-08）](docs/DATA_ENGINE_READING_LIST.md) · [贡献指南](CONTRIBUTING.md) · [主题模板](docs/TOPIC_TEMPLATE.md)。

**参考仓库：** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation)。

**许可：** 原创整理文字与资产采用 [MIT 许可](LICENSE)；链接中的研究与资源保留各自许可。
