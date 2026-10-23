<a id="top"></a>

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
  <img src="https://img.shields.io/badge/Core_entries-119-4263eb?style=flat-square" alt="119 core entries">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

人形移动操作将**移动、平衡与操作**协同起来。本清单按七个研究方向组织 **119 项核心工作**，每项设一个主条目，并用交叉链接呈现重叠贡献；另提供 [13 项关联方法](docs/RELATED_READING.md#中文)，说明机械臂、仿真人体与通用学习方法对本主题的参考价值。

**收录范围：** 优先选择直接研究人形全身操作、接触交互、重定向、训练迁移或执行系统的工作。论文与项目报告明确区分，分类属于编辑判断。

**分类核对：2026-10-16。** 表中为首次公开月份与单独核实的发表信息，不是阅读日期。资源链接不保证完整实现已发布，见 [来源与收录说明](docs/SOURCES.md)。

**最新收录：2026-10-23（新增 ExtremControl，见[来源与证据](docs/SOURCES.md#extremcontrol-addition-2026-10-23)）。**

H2 表示宏观研究方向、技术路线或系统范式，H3 表示其中的具体方法，小节可以只有一项工作；交叉链接与标签呈现重叠贡献。

<p align="center">
  <img src="assets/paper-growth.svg?v=20261023-119" alt="按首次公开月份累计的核心条目增长趋势，共五条曲线，前三个仿真相关方向合并展示" width="100%">
</p>

<sub>按首次公开月份累计收录的论文与报告；蓝色 Simulation & Transfer（仿真与迁移）曲线合并 Real2Sim、Real2Sim2Real 和 Sim2Real & Sim–Real Co-Training，正文仍保留七个独立分类。[按 H2 拆分的逐月数据](docs/paper-growth.csv) · [统计口径与自动更新](docs/CHART.md)。</sub>

**固定 H2 结构：** 保持以下七个 H2 的名称、顺序与层级不变：**Real2Sim**、**Real2Sim2Real**、**Sim2Real & Sim–Real Co-Training**、**Interaction**、**Foundations**、**Harness**、**Iterative Improvement**。后续新增或细化 H3、调整论文位置，并用交叉链接与标签呈现重叠贡献；只有维护者明确要求时，才调整 H2。

**目录**

- [Real2Sim｜真实数据到仿真参考](#real2sim)
  - [接触保持的动作重定向](#motion-retargeting)
  - [控制器感知的示教对齐](#controller-aware-demonstration-alignment)
- [Real2Sim2Real｜真实到仿真再到真实](#real2sim2real)
  - [接触一致的执行器建模](#contact-consistent-actuator-modeling)
  - [反事实视频扩增](#counterfactual-video-augmentation)
  - [场景重建与合成示教](#scene-reconstruction-synthetic-demonstrations)
- [Sim2Real & Sim–Real Co-Training｜仿真迁移与虚实混合训练](#sim2real-co-training)
  - [资产与视频先验驱动的交互合成](#asset-video-interaction-synthesis)
  - [仿真中的示教扩增](#simulation-demonstration-expansion)
  - [视觉策略学习与评测](#visual-policy-learning-evaluation)
  - [全身策略迁移](#whole-body-policy-transfer)
- [Interaction｜交互学习与控制](#interaction)
  - [从人类示教学习交互](#interaction-learning-from-human-videos)
  - [灵巧全身交互](#dexterous-whole-body-interaction)
  - [接触与力控制](#contact-force-control)
  - [触觉引导的全身操作](#tactile-guided-manipulation)
  - [多机器人协同交互](#multi-humanoid-coordination)
  - [全身规划与技能学习](#whole-body-planning-skill-learning)
- [Foundations｜模型与控制基座](#foundations)
  - [测试时指令优化](#test-time-command-optimization)
  - [全身 VLA 与人类数据预训练](#whole-body-vla-human-pretraining)
  - [世界模型条件化的全身策略](#world-model-conditioned-policies)
  - [通用全身控制](#generalist-whole-body-control)
  - [人形机器人仿真基准](#humanoid-simulation-benchmarks)
- [Harness｜执行框架与技能编排](#harness)
  - [空间记忆与长程技能编排](#spatial-memory-skill-orchestration)
  - [全身遥操作与数据采集](#whole-body-teleoperation-data)
  - [执行监控与恢复](#object-memory-execution-verification)
  - [规划与控制接口](#planning-control-interfaces)
- [Iterative Improvement｜迭代改进](#iterative-improvement)
  - [执行反馈驱动的数据与策略协同改进](#execution-guided-data-policy-co-improvement)
  - [执行反馈驱动的程序改进](#execution-guided-reward-program-evolution)
  - [技能复用与记忆巩固](#skill-reuse-memory-consolidation)
  - [人类干预驱动的策略改进](#human-intervention-policy-improvement)
  - [规划器与策略后训练](#planner-policy-post-training)

<a id="retargeting"></a>
<a id="motion-retargeting动作重定向"></a>
<a id="real2sim"></a>

## Real2Sim｜真实数据到仿真参考

将人体动作、交互几何与观测适配到机器人形态，为后续学习和控制提供对齐的参考。

<a id="motion-retargeting"></a>
<a id="contact-preserving-retargeting"></a>
<a id="接触保持的重定向"></a>
<a id="contact-preserving-motion-retargeting"></a>
<a id="接触保持的动作重定向"></a>

### 接触保持的动作重定向

在跨形态适配示教动作时，保持机器人、物体与环境之间的接触关系。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**FRDV**](https://arxiv.org/abs/2610.28470)<br><sub>Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning</sub> | 2026-10<br><sub>arXiv</sub> | 人体动作与人形机器人约束 → 重定向及可选动力学修正的参考 | 结合约束逆运动学与可选的接触隐式 iLQR 修正，处理足部浮空与滑步，并将动作跟踪迁移到真实 G1。 | [Paper](https://arxiv.org/abs/2610.28470) |
| [**PriMoRetarget**](https://arxiv.org/abs/2610.12642)<br><sub>PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting</sub> | 2026-10<br><sub>arXiv</sub> | 人体动作与交互示教 → 人形机器人参考轨迹 | 通过显式目标优先级与梯度投影，在优化姿态等低优先级目标时保留足部落点和交互接触。<br><sub>标签: Prioritized optimization · Contact preservation · Multi-character interactions</sub> | [论文](https://arxiv.org/abs/2610.12642) · [项目](https://nickioan.github.io/primoretarget-page/) |
| [**OTRetarget**](https://arxiv.org/abs/2609.36602)<br><sub>OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport</sub> | 2026-09<br><sub>arXiv</sub> | 人体物体示教 → 机器人与物体联合参考轨迹 | 利用最优传输匹配表面交互，联合优化机器人与物体位姿，在形态变化后保留接触关系。<br><sub>标签: Contact preservation · Joint robot–object optimization</sub> | [论文](https://arxiv.org/abs/2609.36602) |
| [**HOI-Retarget**](https://arxiv.org/abs/2609.34674)<br><sub>HOI-Retarget: Contact-Centric Retargeting for Human-Object Interaction</sub> | 2026-09<br><sub>arXiv</sub> | 人体物体交互动作与物体系接触标注 → 人形交互参考轨迹 | 以滑动窗口轨迹优化在人体形态变化与机器人运动学约束下保留物体系接触，同时兼顾身体跟踪、足部支撑和平滑性。<br><sub>标签: Object-frame contacts · Trajectory optimization · Motion augmentation</sub> | [论文](https://arxiv.org/abs/2609.34674) · [项目](https://shinben0327.github.io/hoi-retarget/) |
| [**UMR**](https://arxiv.org/abs/2609.02134)<br><sub>Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence</sub> | 2026-09<br><sub>arXiv</sub> | 人体表面动作与接触图 → 人形机器人参考动作 | 学习人体与机器人表面的稠密对应，将其用于受约束姿态匹配和接触图迁移，统一处理不同动作来源。<br><sub>标签: Dense correspondence · Surface matching · Contact transfer</sub> | [论文](https://arxiv.org/abs/2609.02134) |
| [**SPIDER**](https://arxiv.org/abs/2511.09484)<br><sub>SPIDER: Scalable Physics-Informed Dexterous Retargeting</sub> | 2025-11<br><sub>arXiv</sub> | 人体运动学示教与机器人物理约束 → 动力学可行的人形动作与交互参考 | 用基于采样的物理优化修正接触与动作伪影，包含多种人形重定向及仿真中的拾箱、搬运和放置策略训练。 | [Paper](https://arxiv.org/abs/2511.09484) · [Project](https://facebookresearch.github.io/spider/) |
| [**OmniRetarget**](https://arxiv.org/abs/2509.26633)<br><sub>OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction</sub> | 2025-09<br><sub>ICRA 2026</sub> | 人体交互动捕 → 交互保持的参考轨迹 | 利用交互网格保留主体、物体与地形的关系，支持动作重定向与扩增。<br><sub>标签: Contact preservation · Motion augmentation</sub> | [论文](https://arxiv.org/abs/2509.26633) · [项目](https://omniretarget.github.io/) · [代码](https://github.com/amazon-far/holosoma) · [数据](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) |

**跨方向阅读：** [HumanX 与 HDMI](#interaction-learning-from-human-videos) 从视频恢复交互参考；[Weave](#dexterous-whole-body-interaction) 与 [InterMimicGen](#execution-guided-data-policy-co-improvement) 也包含接触感知重定向。

[关联视频重建与资产方法](docs/RELATED_READING.md#real2sim-zh)：EgoInfinity、EgoEngine、USDCraft。

<a id="controller-aware-demonstration-alignment"></a>

### 控制器感知的示教对齐

**范围。** 将人类观测转换为对齐的机器人动作、机载视角及控制器专属动作监督。

**阅读提示。** KODA 保留可复用的动作与视角记录；相关指令优化方法见 [TTCO](#test-time-command-optimization)。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**KODA**](https://arxiv.org/abs/2610.21152)<br><sub>KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration</sub> | 2026-10<br><sub>arXiv</sub> | 第一视角人类 RGB → 规范化机器人动作与视角 → 控制器专属动作标签 | 将合成机载视角与仿真验证动作对齐，并通过指令优化为不同控制器重新生成动作监督。<br><sub>标签: 视角动作对齐 · 指令优化 · 示教重标注</sub> | [论文](https://arxiv.org/abs/2610.21152) |
| [**EgoHumanoid-V2**](https://arxiv.org/abs/2609.37181)<br><sub>EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | 人类示教 → 控制器对齐的机器人观测与动作 | G1 真机；将人类示范经控制器回放、动力学校正和视觉对齐转成机器人训练监督。 | [论文](https://arxiv.org/abs/2609.37181) |
| [**TrajBooster**](https://arxiv.org/abs/2509.11839)<br><sub>TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning</sub> | 2025-09<br><sub>arXiv</sub> | 源机器人轨迹 → G1 动作监督与 VLA | 源平台虽含轮式机器人，但方法明确重定向并部署到 G1；只描述该人形部分。 | [论文](https://arxiv.org/abs/2509.11839) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="real2sim2real"></a>
<a id="data-generation-policy-learning"></a>
<a id="data-generation--policy-learning"></a>
<a id="data-generation--policy-learning数据生成与策略学习"></a>
<a id="harness-real2sim2real"></a>
<a id="harness--real2sim2real"></a>
<a id="simulation-policy-transfer"></a>
<a id="simulation-data-generation--policy-transfer"></a>
<a id="仿真数据生成与策略迁移"></a>

## Real2Sim2Real｜真实到仿真再到真实

从真实示教或观测构建仿真参考或校正仿真动态，在仿真中训练策略，再部署回真实机器人；数据生成与仿真器校正是这条路线中的不同环节。

**其他路线：** 从虚拟数据出发的训练与虚实混合训练见 [Sim2Real & Sim–Real Co-Training](#sim2real-co-training)，执行系统集成见 [Harness](#harness)。

<a id="contact-consistent-actuator-modeling"></a>

### 接触一致的执行器建模

**范围.** 从真实人形机器人轨迹校正仿真接触初始化与执行器动态，在校正仿真器中训练策略并部署回真机。

**阅读提示.** Contact-UAN 侧重力敏感控制的迁移，不是物体操作规划器，也不是视觉世界动作模型。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**Contact-UAN**](https://arxiv.org/abs/2610.18991)<br><sub>Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control</sub> | 2026-10<br><sub>arXiv</sub> | 真实 G1 本体感知轨迹 → 校正仿真器 → 可部署控制策略 | 以接触一致的状态初始化真机轨迹回放并学习执行器残差，再在校正后的仿真器中训练对力敏感的人形控制策略。<br><sub>标签: Actuator modeling · Contact-consistent replay · Real2Sim2Real</sub> | [论文](https://arxiv.org/abs/2610.18991) · [项目](https://contact-uan.csail.mit.edu/) |

<a id="counterfactual-video-augmentation"></a>
<a id="video-augmentation-real2sim2real"></a>
<a id="video-augmentation--real2sim2real"></a>
<a id="视频扩增与虚实迁移"></a>

### 反事实视频扩增

从真实交互视频扩增数据，重建机器人可用的参考轨迹，再将训练后的策略部署到真机。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**PRISM**](https://arxiv.org/abs/2609.38172)<br><sub>Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | 少量真实视频 → 扩增数据 → 真机策略 | 生成反事实交互视频，重建接触锚定的参考轨迹，并训练可用于真实人形机器人搬运的策略。<br><sub>标签: Video generation · Real2Sim2Real</sub> | [论文](https://arxiv.org/abs/2609.38172) |

<a id="scene-reconstruction-synthetic-demonstrations"></a>

### 场景重建与合成示教

**范围。** 重建部署场景，在相应仿真器中生成示教，并训练用于真实人形机器人的策略。

**阅读提示。** LEGS 重建场景外观；上面的 Contact-UAN 则校正执行器动态。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**VLK**](https://arxiv.org/abs/2606.30645)<br><sub>VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes</sub> | 2026-06<br><sub>arXiv</sub> | 真实场景采集 → 合成交互 → 视觉策略 | 重建真实场景、合成仿真交互，再训练感知策略并部署到 G1；完整链路明确。 | [论文](https://arxiv.org/abs/2606.30645) |
| [**LEGS**](https://arxiv.org/abs/2606.01458)<br><sub>LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World</sub> | 2026-05<br><sub>arXiv</sub> | 真实场景采集 → 校准的 3DGS 仿真器 → 合成 VLA 示教 | 将重建背景、动态网格前景与程序化动作示教结合，为真实 G1 任务微调 VLA。<br><sub>标签: 场景重建 · 高斯泼溅 · 合成示教</sub> | [论文](https://arxiv.org/abs/2606.01458) · [项目](https://hojjunekim.github.io/legs/) |
| [**DexMimicGen**](https://arxiv.org/abs/2410.24185)<br><sub>DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning</sub> | 2024-10<br><sub>arXiv</sub> | 真实示教与数字孪生 → 生成的机器人示教 | 明确包含 Fourier GR1 仿真及真机；数字孪生中扩增示范并执行回真实系统。只描述人形部分，不宣称移动或腿部控制贡献。 | [论文](https://arxiv.org/abs/2410.24185) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="sim2real-co-training"></a>
<a id="sim2real"></a>

## Sim2Real & Sim–Real Co-Training｜仿真迁移与虚实混合训练

利用仿真生成的数据或仿真训练的策略支持真机学习与部署。GRAIL 与 DemoHLM 展示仿真到现实迁移；HumanoidMimicGen 将生成的仿真数据与真实示教共同用于训练。

<a id="asset-video-interaction-synthesis"></a>
<a id="interaction-synthesis-from-3d-assets--video-priors"></a>
<a id="基于资产与视频先验的交互合成"></a>

### 资产与视频先验驱动的交互合成

从已知虚拟资产和场景出发，利用视频先验合成用于机器人学习的交互数据。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**KinoGen**](https://arxiv.org/abs/2610.20552)<br><sub>KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation</sub> | 2026-10<br><sub>arXiv</sub> | 校准的机器人与物体渲染、目标编辑 → 人形交互参考 | 由机器人场景渲染生成双视角视频，直接拟合机器人及物体模型，恢复可定制参考以训练 G1 跟踪策略。<br><sub>标签: 视频生成 · 机器人原生参考 · 目标定制</sub> | [论文](https://arxiv.org/abs/2610.20552) · [项目](https://kinogen-humanoid.github.io/) |
| [**GRAIL**](https://arxiv.org/abs/2606.05160)<br><sub>GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors</sub> | 2026-06<br><sub>CoRL 2026</sub> | 3D 资产与视频先验 → 人形机器人训练数据 | 在已知虚拟场景中合成交互，恢复具有真实尺度的 4D 轨迹，并训练可迁移至真机的人形策略。<br><sub>标签: 3D assets · Video priors · Sim-to-real</sub> | [论文](https://arxiv.org/abs/2606.05160) · [代码](https://github.com/NVlabs/GRAIL) |

<a id="simulation-demonstration-expansion"></a>

### 仿真中的示教扩增

将少量仿真机器人示教适配、扩增为大规模数据；部署可采用仿真到现实迁移或虚实数据混合训练。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanoidMimicGen**](https://arxiv.org/abs/2605.27724)<br><sub>HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning</sub> | 2026-05<br><sub>arXiv</sub> | 仿真机器人示教 → 扩增仿真数据 → 虚实混合训练 | 通过技能适配与全身规划扩增仿真示教，真机评测时再与真实示教混合训练策略。<br><sub>标签: Simulation data · Whole-body planning · Sim-and-real co-training</sub> | [论文](https://arxiv.org/abs/2605.27724) · [项目](https://humanoidmimicgen.github.io/) · [基准代码](https://github.com/NVlabs/humanoidmimicgen) |
| [**DemoHLM**](https://arxiv.org/abs/2510.11258)<br><sub>DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation</sub> | 2025-10<br><sub>arXiv</sub> | 单条仿真示教 → 合成训练数据 | 从单条仿真示教扩增任务数据，在全身控制器之上学习视觉操作策略并迁移至真机。<br><sub>标签: Simulation data · Demonstration expansion · Sim-to-real</sub> | [论文](https://arxiv.org/abs/2510.11258) · [项目](https://beingbeyond.github.io/DemoHLM/) |

**跨方向阅读：** [HumanX](#interaction-learning-from-human-videos) 也包含交互数据扩增；[InterMimicGen](#execution-guided-data-policy-co-improvement) 则将扩增与多轮执行、跟踪器更新相连。执行系统集成见 [Harness](#harness)。

<a id="visual-policy-learning-evaluation"></a>

### 视觉策略学习与评测

**范围。** 使用渲染的仿真观测训练或评测人形视觉策略，并明确其部署证据。

**阅读提示。** VIRAL 是教师学生训练方法；SIMPLE 是仿真评测与数据采集平台。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**SIMPLE**](https://arxiv.org/abs/2606.08278)<br><sub>SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation</sub> | 2026-06<br><sub>arXiv · 评测基准</sub> | 仿真任务、资产与采集接口 → 人形策略基准及训练数据 | 结合 MuJoCo 物理与 Isaac Sim 渲染，采集并评测全身人形策略，并报告相近设置下的仿真到真机迁移。<br><sub>标签: 评测基准 · 仿真数据 · 策略评测</sub> | [论文](https://arxiv.org/abs/2606.08278) · [项目](https://psi-lab.ai/SIMPLE/) |
| [**VIRAL**](https://arxiv.org/abs/2511.15200)<br><sub>VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation</sub> | 2025-11<br><sub>arXiv</sub> | 仿真特权状态轨迹 → RGB 学生策略 → 真实人形控制 | 通过大规模渲染与域随机化将仿真 RL 教师蒸馏为视觉学生，并校准手部和相机以迁移至 G1。<br><sub>标签: 视觉仿真迁移 · 教师学生学习 · 域随机化</sub> | [论文](https://arxiv.org/abs/2511.15200) · [项目](https://viral-humanoid.github.io/) |
| [**VisualMimic**](https://arxiv.org/abs/2509.20322)<br><sub>VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation</sub> | 2025-09<br><sub>arXiv</sub> | 仿真动作跟踪与渲染 → 人形视觉策略 | 仿真中的跟踪与动作生成用于训练视觉策略，并迁移到真实人形机器人的推、搬、踢等任务。 | [论文](https://arxiv.org/abs/2509.20322) |

<a id="whole-body-policy-transfer"></a>

### 全身策略迁移

**范围。** 在仿真中训练耦合移动与操作的策略，并部署到真实人形机器人。

**阅读提示。** Digit 搬箱工作展示了将拾取与携带技能迁移为完整真实任务的早期路线。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**Sim-to-Real Humanoid Box Loco-Manipulation**](https://arxiv.org/abs/2310.03191)<br><sub>Sim-to-Real Learning for Humanoid Box Loco-Manipulation</sub> | 2023-10<br><sub>arXiv</sub> | 仿真拾箱与搬运任务 → 真实 Digit 技能 | Digit 真机；拾箱、携带和跨桌搬运，直接匹配 humanoid loco-manipulation。 | [论文](https://arxiv.org/abs/2310.03191) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="interaction"></a>

## Interaction｜交互学习与控制

学习并控制人形机器人与物体、环境及队友的物理交互，覆盖身体与手部协调、团队配合及接触力调节。

<a id="interaction-learning-from-human-demonstrations"></a>
<a id="从人类视频学习交互"></a>
<a id="interaction-learning-from-human-videos"></a>
<a id="human-object-interaction"></a>
<a id="whole-body-interaction-from-demonstrations"></a>
<a id="从示教学习全身交互"></a>

### 从人类示教学习交互

从人类视频或可穿戴设备采集的示教中学习人形交互；各方法对动作恢复、接触标注与重定向的要求不同。基于捕获示教的灵巧手与全身协调见 [灵巧全身交互](#dexterous-whole-body-interaction)。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**REACT**](https://arxiv.org/abs/2610.28523)<br><sub>VLM-Guided Contact Retargeting and Generative Partner Modeling for Humanoid-Human Interaction</sub> | 2026-10<br><sub>arXiv</sub> | 人际交互示教与机载深度观测 → 人形机器人与人的接触交互策略 | 结合 VLM 引导的接触重定向、伙伴状态生成与策略蒸馏，在仿真和真实 G1 上实现击掌、拥抱等接触交互。 | [Paper](https://arxiv.org/abs/2610.28523) |
| [**VICAR**](https://arxiv.org/abs/2610.13079)<br><sub>VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills</sub> | 2026-10<br><sub>arXiv</sub> | 第三视角人类视频与接触目标 → 可适配的人形交互技能 | 在重定向时保留全局接触位姿、动作速度和碰撞间距，再学习可适配变化接触目标的条件动作。<br><sub>标签: Video imitation · Contact-aware retargeting · Contact conditioning</sub> | [论文](https://arxiv.org/abs/2610.13079) |
| [**Workhorse**](https://arxiv.org/abs/2610.09117)<br><sub>Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data</sub> | 2026-10<br><sub>arXiv</sub> | 可穿戴人体位姿与第一视角 RGB → 视觉规划器和全身跟踪器 | 以躯干、双腕和双足目标分别训练视觉规划器与 RL 跟踪器，并模拟彼此误差扩增数据，无需机器人专属重定向即可学习 G1 接触交互技能。<br><sub>标签: Robot-free demonstrations · Five-link interface · Robust tracking</sub> | [论文](https://arxiv.org/abs/2610.09117) · [项目](https://hybridrobotics.github.io/workhorse/) |
| [**HALOMI**](https://arxiv.org/abs/2606.18772)<br><sub>HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations</sub> | 2026-06<br><sub>arXiv</sub> | 第一视角与腕部观测、头手示教 → 主动感知人形策略 | 将视角对齐、控制器感知参考适配与潜在流形控制器结合，实现头手协调跟踪。<br><sub>标签: 主动感知 · 头手控制 · 示教对齐</sub> | [论文](https://arxiv.org/abs/2606.18772) · [项目](https://halomi-humanoid.github.io) |
| [**GenHOI**](https://arxiv.org/abs/2606.12995)<br><sub>GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training</sub> | 2026-06<br><sub>arXiv</sub> | 人类视频 → 优化后的接触感知机器人参考 | G1 仿真与真机；视频提取交互并优化参考，由冻结控制器执行，不能误写为重新训练任务策略。 | [论文](https://arxiv.org/abs/2606.12995) |
| [**Bifrost-UMI**](https://arxiv.org/abs/2605.03452)<br><sub>BifrostUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation</sub> | 2026-05<br><sub>arXiv</sub> | 人类示教与位姿对齐 → 全身操作 | G1 真机；人类示范与全身控制支持屈膝、退步和行走中的操作。 | [论文](https://arxiv.org/abs/2605.03452) |
| [**EgoHumanoid**](https://arxiv.org/abs/2602.10106)<br><sub>EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration</sub> | 2026-02<br><sub>arXiv</sub> | 第一视角人类示教与少量机器人数据 → 对齐后的人形 VLA 策略 | 先对齐人机视角与动作空间，再联合训练用于 G1 跨环境移动操作的 VLA。<br><sub>标签: 视角对齐 · 动作对齐 · 人机数据联合训练</sub> | [论文](https://arxiv.org/abs/2602.10106) · [项目](https://opendrivelab.com/EgoHumanoid/) |
| [**HuMI**](https://arxiv.org/abs/2602.06643)<br><sub>Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations</sub> | 2026-02<br><sub>arXiv</sub> | 便携式无机器人全身示教 → 分层人形操作策略 | 通过在线可行性预览采集人类全身动作，以分层策略学习跪姿、下蹲、投掷及行走操作。<br><sub>标签: 无机器人示教 · 可行性对齐 · 分层学习</sub> | [论文](https://arxiv.org/abs/2602.06643) · [项目](https://humanoid-manipulation-interface.github.io) |
| [**HumanX**](https://arxiv.org/abs/2602.02473)<br><sub>HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos</sub> | 2026-02<br><sub>CoRL 2026</sub> | 人类视频 → 扩增参考轨迹 → 交互技能 | 结合以锚点为中心的交互合成与交互优先的模仿学习，获得可迁移至 G1 的敏捷技能。<br><sub>标签: Video reconstruction · Data augmentation · Interaction learning</sub> | [论文](https://arxiv.org/abs/2602.02473) · [项目](https://wyhuai.github.io/human-x/) |
| [**ResMimic**](https://arxiv.org/abs/2510.05070)<br><sub>ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning</sub> | 2025-10<br><sub>arXiv</sub> | 人类交互参考与通用动作跟踪器 → 物体感知残差策略 | 在通用动作跟踪器上学习残差，利用物体几何与接触奖励提高全身交互精度。<br><sub>标签: 残差学习 · 接触奖励 · 物体跟踪</sub> | [论文](https://arxiv.org/abs/2510.05070) · [项目](https://resmimic.github.io/) |
| [**HumanoidExo**](https://arxiv.org/abs/2510.03022)<br><sub>HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton</sub> | 2025-10<br><sub>arXiv</sub> | 可穿戴外骨骼动作与相机观测 → 人形全身策略 | 将可穿戴人类数据与人形构型对齐，并结合少量机器人示教学习站立、下蹲及行走操作。<br><sub>标签: 无机器人数据 · 外骨骼 · 人机数据联合训练</sub> | [论文](https://arxiv.org/abs/2510.03022) |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | 单目 RGB 视频 → 全身交互策略 | 提取人体与物体轨迹，通过联合跟踪机器人和物体状态学习全身交互技能。<br><sub>标签: Video reconstruction · Interaction imitation · Sim-to-real</sub> | [论文](https://arxiv.org/abs/2509.16757) · [项目](https://hdmi-humanoid.github.io/) · [代码](https://github.com/LeCAR-Lab/HDMI) |
| [**Cross-Embodiment Behavior-Skill Transfer**](https://arxiv.org/abs/2412.15166)<br><sub>Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration</sub> | 2024-12<br><sub>arXiv</sub> | 人体示教与交互图 → 迁移后的机器人技能 | NAVIAI、H1、Walker 等仿真机器人搬箱；不把轮式 CURI 或人体模型结果混入描述。 | [论文](https://arxiv.org/abs/2412.15166) |

<a id="dexterous-whole-body-interaction"></a>

### 灵巧全身交互

利用捕获示教或合成的全身抓持监督，学习身体与手部接触协调。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**EmbodyHOI**](https://arxiv.org/abs/2610.27242)<br><sub>EmbodyHOI: Embodiment-Aware Generation of Hand-Object Interactions for Humanoid Dexterous Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | 人类手物交互生成先验与机器人运动学 → 人形可达的交互参考 | 用机器人逆运动学引导冻结的交互生成器调整腕部与身体根位置参考，在 G1 和 H1-2 仿真中评测灵巧操作。 | [Paper](https://arxiv.org/abs/2610.27242) |
| [**WBD**](https://arxiv.org/abs/2610.22184)<br><sub>Whole-Body Dexterity</sub> | 2026-10<br><sub>arXiv</sub> | 生成的全身抓持与目标参考 → 身体接触操作策略 | 从可行抓持训练并蒸馏物体重定位专家，使 G1 通过协调的手臂与躯干接触操纵物体。<br><sub>标签: 全身抓持 · 专家蒸馏 · 身体接触</sub> | [论文](https://arxiv.org/abs/2610.22184) |
| [**Weave**](https://arxiv.org/abs/2609.16683)<br><sub>Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions</sub> | 2026-09<br><sub>arXiv</sub> | 人体交互动捕 → 灵巧机器人与物体交互 | 结合接触感知重定向与几何感知策略，协调身体和手指关节以跟踪机器人与物体参考轨迹。<br><sub>标签: HOI motion capture · Dexterous hands · Contact-aware retargeting</sub> | [论文](https://arxiv.org/abs/2609.16683) · [项目](https://xiaohu-art.github.io/Weave/) |
| [**CoorDex**](https://arxiv.org/abs/2606.23680)<br><sub>CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | 身体与手部示教 → 潜先验协调策略 | 配备 WUJI 手的 G1；协调身体与手部先验，完成运动中的连续灵巧操作。 | [论文](https://arxiv.org/abs/2606.23680) |

<a id="contact-force-control"></a>

### 接触与力控制

在执行动作轨迹时进一步调节柔顺性与接触力。

接触力迁移所需的执行器仿真校正见 [Contact-UAN](#contact-consistent-actuator-modeling)。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**C-GMT**](https://arxiv.org/abs/2610.22119)<br><sub>Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation</sub> | 2026-10<br><sub>arXiv</sub> | 动作参考与本体感知历史 → 柔顺参考修正 | 在通用动作跟踪器上学习残差参考适配器，使回放、遥操作及 VLA 接口均可产生柔顺全身响应。<br><sub>标签: 残差参考适配 · 柔顺控制 · 通用动作跟踪</sub> | [论文](https://arxiv.org/abs/2610.22119) · [项目](https://venki1899.github.io/c-gmt/) |
| [**KPI**](https://arxiv.org/abs/2609.36151)<br><sub>KPI: A Promptable Kernel for Physical Interaction on Humanoids</sub> | 2026-09<br><sub>arXiv</sub> | 轨迹与交互约束 → 自适应接触控制 | 在保留底层全身跟踪器的基础上，按跟踪、柔顺及力范围要求调整手臂阻抗与参考量。<br><sub>标签: Impedance adaptation · Force regulation</sub> | [论文](https://arxiv.org/abs/2609.36151) · [项目](https://kpi-robot.github.io/) |
| [**CEER2**](https://arxiv.org/abs/2609.38709)<br><sub>CEER2: Directional and Tunable End-Effector and Root Compliance for Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | 运动指令与本体感知 → 方向性顺应控制 | G1 真机方向性顺应控制；没有腕部力传感器也能实现接触交互。 | [论文](https://arxiv.org/abs/2609.38709) |
| [**CEER**](https://arxiv.org/abs/2605.19981)<br><sub>CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation</sub> | 2026-05<br><sub>arXiv</sub> | 根部指令与末端姿态 → 柔顺全身控制接口 | 将动作跟踪蒸馏为末端与根部接口，支持柔顺操作及多种高层规划器接入。<br><sub>标签: 柔顺控制 · 任务空间接口 · 分层控制</sub> | [论文](https://arxiv.org/abs/2605.19981) · [项目](https://robotproject8.github.io/ceer_page/) |
| [**GentleHumanoid**](https://arxiv.org/abs/2511.04679)<br><sub>GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction</sub> | 2025-11<br><sub>arXiv</sub> | 动作参考与交互力建模 → 上半身柔顺响应 | 以弹簧模型描述引导与阻抗接触，训练全身跟踪器在身体交互中协调肩、肘、腕的柔顺响应。<br><sub>标签: 柔顺控制 · 人机接触 · 全身跟踪</sub> | [论文](https://arxiv.org/abs/2511.04679) |
| [**FALCON**](https://arxiv.org/abs/2505.06776)<br><sub>FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation</sub> | 2025-05<br><sub>arXiv</sub> | 外载作用下的根部与末端指令 → 力自适应全身控制 | 通过满足关节力矩约束的力课程联合训练上下半身智能体，支持人形机器人负载搬运、拉车与开门。<br><sub>标签: 力自适应 · 双智能体 RL · 负载操作</sub> | [论文](https://arxiv.org/abs/2505.06776) |
| [**Flow Multi-Support**](https://arxiv.org/abs/2407.12381)<br><sub>Flow Matching Imitation Learning for Multi-Support Manipulation</sub> | 2024-07<br><sub>arXiv</sub> | 示教与接触约束 → 流匹配控制 | Talos 真机；流匹配模仿学习与多接触全身控制协同完成推箱、关洗碗机抽屉及自由手支撑。 | [论文](https://arxiv.org/abs/2407.12381) |
| [**WoCoCo**](https://arxiv.org/abs/2406.06005)<br><sub>WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts</sub> | 2024-06<br><sub>arXiv</sub> | 接触阶段与任务奖励 → 全身交互策略 | 真机接触序列控制，明确覆盖搬箱；不将其另有的恐龙构型实验描述为人形结果。 | [论文](https://arxiv.org/abs/2406.06005) |

**跨方向阅读：** [PRISM](#counterfactual-video-augmentation) 与 [GRAIL](#asset-video-interaction-synthesis) 也学习交互策略，主条目侧重其数据生成贡献。[KPI](#contact-force-control) 还包含智能体驱动的轨迹与交互约束生成。

<a id="tactile-guided-manipulation"></a>

### 触觉引导的全身操作

**范围。** 使用人类接触示教或机器人触觉观测，学习人形操作及接触目标。

**阅读提示。** TACT 使用机器人触觉观测，PanTact 与 WT-UMI 迁移人类接触或力示教；[接触与力控制](#contact-force-control) 侧重执行时的动态调节。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**PanTact**](https://arxiv.org/abs/2610.12558)<br><sub>PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface</sub> | 2026-10<br><sub>arXiv</sub> | 可穿戴接触示教 → 身体接触目标与控制 | G1 真机；可穿戴接触接口学习身体支撑、推扫和负载分担，不局限于双手接触。 | [论文](https://arxiv.org/abs/2610.12558) |
| [**WT-UMI**](https://arxiv.org/abs/2606.13232)<br><sub>WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning</sub> | 2026-06<br><sub>arXiv</sub> | 可穿戴位姿与触觉示教 → 力感知执行 | G1 真机；可穿戴触觉示范提供位姿和接触力监督，由顺应控制执行。 | [论文](https://arxiv.org/abs/2606.13232) |
| [**TACT**](https://arxiv.org/abs/2506.15146)<br><sub>TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality</sub> | 2025-06<br><sub>RA-L 2025</sub> | 视觉、关节状态与分布式触觉 → 接触密集操作动作 | 为 ACT 加入上半身触觉输入，并与基于模型的双足控制结合，实现利用大面积身体接触的搬运。<br><sub>标签: 触觉反馈 · 模仿学习 · 身体接触</sub> | [论文](https://arxiv.org/abs/2506.15146) |

<a id="multi-humanoid-coordination"></a>

### 多机器人协同交互

**范围。** 协调共享物体或工作空间的多个人形机器人完成物理交互。

**阅读提示。** PingpongDuo 将交替击球与队友让位、碰撞风险筛选结合；球飞行与接触参数校准是其迁移的辅助环节。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**OmniInteract**](https://arxiv.org/abs/2610.26043)<br><sub>OmniInteract: Towards Unified Whole-Body Interaction Control for Dual Humanoids</sub> | 2026-10<br><sub>arXiv</sub> | 双人交互示教与伙伴状态 → 统一的双人形接触交互策略 | 重定向时保持表面接触，并统一冻结控制器上的伙伴条件残差策略，在两台真实 G1 上实现击掌、拥抱与扶肩。 | [Paper](https://arxiv.org/abs/2610.26043) |
| [**PingpongDuo**](https://arxiv.org/abs/2610.20579)<br><sub>PingpongDuo: Agile Humanoid Table Tennis Doubles with Safe Team Coordination</sub> | 2026-10<br><sub>arXiv</sub> | 人类动作参考、球状态与队友状态 → 协同步法及击球 | 结合风险筛选的团队规划器、相互初始化的步法与击球技能及持拍臂残差，使两台 G1 协调完成交替双打。<br><sub>标签: 多人形协调 · 动态交互 · 风险感知规划</sub> | [论文](https://arxiv.org/abs/2610.20579) |

<a id="whole-body-planning-skill-learning"></a>

### 全身规划与技能学习

**范围。** 规划接触或学习任务策略，协调移动、平衡与物体交互。

**阅读提示。** BOPI 处理未知动力学下的重规划，SkillBlender 组合可复用技能，Opt2Skill 连接轨迹优化与策略学习。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HS-MoDP / G1Exo**](https://arxiv.org/abs/2610.26169)<br><sub>Compositional Humanoid Manipulation through Isomorphic Teleoperation and Independent Skill Routing</sub> | 2026-10<br><sub>arXiv</sub> | 同构外骨骼示教与分臂语义条件 → 组合式操作策略 | 结合 G1Exo 示教与两臂独立路由的共享策略专家，在真实 G1 上完成利用手臂和躯干接触的操作。 | [Paper](https://arxiv.org/abs/2610.26169) |
| [**FIBER**](https://arxiv.org/abs/2610.24675)<br><sub>Action-Aligned Latent Planning for Versatile Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | 任务专家的动作响应与视觉观测 → 冻结行为模型潜空间中的计划 | 将任务专家对齐到冻结行为基础模型并离线训练统一视觉潜空间规划器，在仿真与真实 G1 上评测开门、拾取和搬运。 | [Paper](https://arxiv.org/abs/2610.24675) |
| [**BOPI**](https://arxiv.org/abs/2610.13087)<br><sub>Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | 交互观测与目标 → 信念条件化规划 | G1 仿真及真机推车；信念更新与流模型重规划处理未知交互动力学。 | [论文](https://arxiv.org/abs/2610.13087) |
| [**MotionDisco**](https://arxiv.org/abs/2606.06139)<br><sub>MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | 场景几何与任务目标 → 接触规划与全身动作 | G1 接触规划与运动求解；将环境支撑接触和物体交互纳入全身运动发现，区分求解与策略训练。 | [论文](https://arxiv.org/abs/2606.06139) |
| [**LadderMan**](https://arxiv.org/abs/2606.05873)<br><sub>LadderMan: Learning Humanoid Perceptive Ladder Climbing</sub> | 2026-06<br><sub>CoRL 2026</sub> | 单条攀爬示教、深度观测与操作员目标 → 感知攀爬与稳定的梯上操作 | 将攀爬专家蒸馏为基于深度观测的 G1 策略，并将下肢稳定与遥操作上肢控制分离，实现梯上操作。 | [Paper](https://arxiv.org/abs/2606.05873) · [Project](https://ladderman-robot.github.io/) |
| [**DreamControl**](https://arxiv.org/abs/2509.14353)<br><sub>DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion</sub> | 2025-09<br><sub>arXiv</sub> | 人体动作扩散先验与任务奖励 → 交互策略 | G1 实验；人类动作扩散先验引导强化学习完成抽屉、拾取等身体与物体交互。 | [论文](https://arxiv.org/abs/2509.14353) |
| [**SkillBlender**](https://arxiv.org/abs/2506.09366)<br><sub>SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending</sub> | 2025-06<br><sub>arXiv</sub> | 预训练低层技能与任务目标 → 组合行为 | 明确采用 H1、G1、H1-2 机器人模型；复用低层技能组合完成操作，标注仿真证据。 | [论文](https://arxiv.org/abs/2506.09366) |
| [**Whole-Body Dynamic Throwing**](https://arxiv.org/abs/2410.05681)<br><sub>Whole-Body Dynamic Throwing with Legged Manipulators</sub> | 2024-10<br><sub>arXiv</sub> | 目标位置与机器人状态 → 动态全身投掷 | Chuck 双足双臂人形真机；通过全身动量提升投掷。论文同时含四足实验，只描述人形部分。 | [论文](https://arxiv.org/abs/2410.05681) |
| [**OGMP**](https://arxiv.org/abs/2410.01030)<br><sub>Preferenced Oracle Guided Multi-mode Policies for Dynamic Bipedal Loco-Manipulation</sub> | 2024-10<br><sub>arXiv</sub> | 混合任务预言与偏好转换 → 多模式策略 | 在 G1、H1 等机器人模型上统一多模式动态操作与接触转换；包含足球和移动箱体，标注仿真范围。 | [论文](https://arxiv.org/abs/2410.01030) |
| [**Opt2Skill**](https://arxiv.org/abs/2409.20514)<br><sub>Opt2Skill: Imitating Dynamically-feasible Whole-Body Trajectories for Versatile Humanoid Loco-Manipulation</sub> | 2024-09<br><sub>arXiv</sub> | 接触一致的优化轨迹 → 跟踪策略 | Digit；优化生成动力学可行、接触一致的参考轨迹，再训练跟踪策略，含力相关接触操作及真机验证。 | [论文](https://arxiv.org/abs/2409.20514) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="foundations"></a>

## Foundations｜模型与控制基座

收录直接支撑人形全身技能的可复用模型与控制接口，区分测试时指令优化、人体数据预训练的 VLA、世界模型条件化策略和通用运动控制器。

<a id="test-time-command-optimization"></a>

### 测试时指令优化

在不重新训练行为基础模型（BFM）的条件下，利用额外测试时计算适配输入指令，并为下游策略学习生成模型专属动作标签。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**TTCO**](https://arxiv.org/abs/2610.14896)<br><sub>Test-Time Compute for Humanoid Behavior Foundation Models</sub> | 2026-10<br><sub>arXiv</sub> | 期望动作或机器人轨迹与冻结 BFM → 优化指令与动作标签 | 通过闭环仿真中的采样优化调整冻结 BFM 的输入指令，缩小执行轨迹偏差，并生成支持跨 BFM 示教复用的动作标签。<br><sub>标签: Test-time compute · Command optimization · Demonstration relabeling</sub> | [论文](https://arxiv.org/abs/2610.14896) · [项目](https://bfmttc.github.io/) |

<a id="whole-body-vla-human-pretraining"></a>
<a id="whole-body-action-models"></a>
<a id="全身动作模型"></a>

### 全身 VLA 与人类数据预训练

通过人类视频预训练与异构示教联合训练，学习全身视觉语言动作策略。世界模型条件化的路线见 [MotionWAM](#world-model-conditioned-policies)。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**SP-HLM**](https://arxiv.org/abs/2610.30044)<br><sub>SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | 多模态观测与语言 → 稀疏位姿、运动先验及全身动作 | 以五点稀疏位姿和潜在运动先验连接 VLA、运动生成与全身跟踪，在八项仿真任务和四项真实 G1 移动操作任务中评测。 | [论文](https://arxiv.org/abs/2610.30044) |
| [**λ₀**](https://arxiv.org/abs/2610.00438)<br><sub>Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining</sub> | 2026-09<br><sub>arXiv</sub> | 第一视角身体与手部数据 → 全身 VLA | 通过分阶段人体数据预训练与形态适配，学习协调全身和手部动作的策略。<br><sub>标签: VLA · Human-data pretraining · Embodiment adaptation</sub> | [论文](https://arxiv.org/abs/2610.00438) |
| [**OpenHLM**](https://arxiv.org/abs/2606.22174)<br><sub>OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | 全身遥操作与异构示教 → 面向人形全身的 VLA | 系统研究关节级遥操作、VLA 动作设计与异构数据联合训练，以单一学习策略指挥人形全身。<br><sub>标签: 全身 VLA · 异构联合训练 · 动作接口</sub> | [论文](https://arxiv.org/abs/2606.22174) · [项目](https://openhlm-project.github.io/) |
| [**HEX**](https://arxiv.org/abs/2604.07993)<br><sub>HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation</sub> | 2026-04<br><sub>arXiv</sub> | 异构构型数据 → 人形对齐专家策略 | Tienkung 2.0/3.0 双足人形实验；异构数据及专家模型学习协调身体、腰腿和操作。 | [论文](https://arxiv.org/abs/2604.07993) |
| [**Ψ₀**](https://arxiv.org/abs/2603.12263)<br><sub>Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation</sub> | 2026-03<br><sub>arXiv</sub> | 第一视角人类视频与人形轨迹 → 分阶段 VLA 及全身动作指令 | 先预训练视觉动作表征，再训练流式动作专家，将手臂与手部指令和 RL 下半身控制器结合，支持 G1 移动操作。<br><sub>标签: 分阶段训练 · 人类视频预训练 · 全身 VLA</sub> | [论文](https://arxiv.org/abs/2603.12263) |
| [**GR00T N1.6**](https://research.nvidia.com/labs/gear/gr00t-n1_6/)<br><sub>GR00T N1.6</sub> | 2025-12<br><sub>技术报告</sub> | 异构机器人数据与任务示教 → 可适配的 VLA 策略 | 结合更新的视觉语言骨干、更大的动作 Transformer 和包含 G1 移动操作的扩展机器人数据，并通过任务专属后训练部署。<br><sub>标签: 跨构型预训练 · G1 移动操作 · 模型报告</sub> | [报告](https://research.nvidia.com/labs/gear/gr00t-n1_6/) |
| [**WholeBodyVLA**](https://arxiv.org/abs/2512.11047)<br><sub>WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control</sub> | 2025-12<br><sub>arXiv</sub> | 无动作标签的第一视角视频与机器人示教 → 潜在动作 VLA 及移动控制 | 从第一视角视频学习潜在动作，将 VLA 与面向移动操作的控制器结合，支持大范围协调任务。<br><sub>标签: 潜在动作 · 第一视角视频 · 全身 VLA</sub> | [论文](https://arxiv.org/abs/2512.11047) |

<a id="world-model-conditioned-policies"></a>

### 世界模型条件化的全身策略

结合视觉动态预测与动作先验，学习用于协调全身控制的世界动作模型。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**Ropedia W0**](https://arxiv.org/abs/2610.26855)<br><sub>Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience</sub> | 2026-10<br><sub>arXiv</sub> | 第一视角人类经验与异构机器人数据 → 运动学条件世界模型 | 利用人类经验训练跨构型世界模型，人形部分包含 G1–Inspire 移动操作数据及真实 G1 的规划与世界动作模型初始化实验。 | [Paper](https://arxiv.org/abs/2610.26855) |
| [**Language-Forcing**](https://arxiv.org/abs/2610.23894)<br><sub>Language-Forcing: Advancing Humanoid Loco-Manipulation via Semantic Alignment of Whole-Body World Action Models</sub> | 2026-09<br><sub>arXiv</sub> | 视觉观测与语言监督 → 语义对齐的全身世界动作模型 | 训练时以任务进展语言对齐预测视觉特征，在 G1 真机与 HumanoidArena 中评测，推理时不使用辅助语言模块。 | [Paper](https://arxiv.org/abs/2610.23894) |
| [**WholeBodyWAM**](https://arxiv.org/abs/2609.18197)<br><sub>WholeBodyWAM: Learning Whole-Body World Action Models with Scalable Motion Priors</sub> | 2026-09<br><sub>arXiv</sub> | 人体及人形动作预训练与机器人示教 → 全身世界动作模型 | 先用异构动作预训练运动专家，再结合运动、视频和动作专家，生成适配目标构型的全身动作。<br><sub>标签: Motion pretraining · World-action model · Whole-body coordination</sub> | [论文](https://arxiv.org/abs/2609.18197) · [项目](https://zbzyjya.github.io/WholeBodyWAM/) |
| [**ω-0**](https://arxiv.org/abs/2608.06375)<br><sub>ω-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation</sub> | 2026-08<br><sub>arXiv</sub> | 视觉观测、语言与机器人状态 → 预测潜变量及全身动作 | 联合预测未来视觉嵌入与全身动作潜变量，支持 G1 人形机器人在移动过程中执行操作。<br><sub>标签: Latent world model · Whole-body actions · Concurrent loco-manipulation</sub> | [论文](https://arxiv.org/abs/2608.06375) |
| [**MotionWAM**](https://arxiv.org/abs/2606.09215)<br><sub>MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | 第一视角视频 → 统一全身动作 token | 利用视频世界模型特征驱动统一全身策略，实时协调移动、躯干、足部与手部动作。<br><sub>标签: Video world model · Unified whole-body actions</sub> | [论文](https://arxiv.org/abs/2606.09215) |

<a id="generalist-whole-body-control"></a>

### 通用全身控制

面向多种指令接口、遥操作或任务目标提供可复用运动控制；各方法支持的接口有所不同。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**I-BFM**](https://arxiv.org/abs/2610.06129)<br><sub>I-BFM: Reward-Conditioned Robust Humanoid Interaction via Unsupervised Reinforcement Learning</sub> | 2026-10<br><sub>arXiv</sub> | 交互经验与奖励条件 → 可复用行为策略 | G1 真机；奖励条件交互基础策略支持多种移动操作与技能串联，无须逐任务重训。 | [论文](https://arxiv.org/abs/2610.06129) |
| [**OMG**](https://arxiv.org/abs/2606.10340)<br><sub>OMG: Omni-Modal Motion Generation for Generalist Humanoid Control</sub> | 2026-06<br><sub>arXiv</sub> | 语言、音频或动作条件 → 人形动作生成 | G1 运动表示与生成基础；可解释已收录 HumanoidTTT 所使用的底层生成能力。 | [论文](https://arxiv.org/abs/2606.10340) |
| [**ULTRA**](https://arxiv.org/abs/2603.03279)<br><sub>ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation</sub> | 2026-03<br><sub>IROS 2026</sub> | 动作参考或稀疏目标 → 全身控制 | 将动作跟踪技能蒸馏为多模态控制器，支持从稀疏目标和第一视角感知产生自主行为。<br><sub>标签: Multimodal control · Sparse goals · Motion tracking</sub> | [论文](https://arxiv.org/abs/2603.03279) |
| [**SONIC**](https://arxiv.org/abs/2511.07820)<br><sub>SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control</sub> | 2025-11<br><sub>arXiv</sub> | 多模态运动指令 → 统一 G1 控制 | G1 通用运动与多模态控制基础；具有移动操作接口，和当前高层方法的依赖关系明确。 | [论文](https://arxiv.org/abs/2511.07820) |
| [**BFM-Zero**](https://arxiv.org/abs/2511.04131)<br><sub>BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning</sub> | 2025-11<br><sub>arXiv</sub> | 动作、目标或奖励提示 → 共享潜变量条件化的全身策略 | 用无监督前向–后向表征统一真实 G1 上的动作跟踪、目标触达与奖励条件行为，提供可复用的控制基座。 | [Paper](https://arxiv.org/abs/2511.04131) · [Project](https://lecar-lab.github.io/BFM-Zero/) |
| [**ULC**](https://arxiv.org/abs/2507.06905)<br><sub>ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation</sub> | 2025-07<br><sub>arXiv</sub> | 根部速度与高度、躯干姿态及手臂目标 → 单一全身策略 | 通过渐进式指令课程与手臂残差动作，以统一人形控制器跟踪移动、躯干及双臂指令。<br><sub>标签: 统一控制 · 指令跟踪 · 负载随机化</sub> | [论文](https://arxiv.org/abs/2507.06905) · [项目](https://hellod035.github.io/ULC/) |
| [**AMO**](https://arxiv.org/abs/2505.03738)<br><sub>AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control</sub> | 2025-05<br><sub>arXiv</sub> | 动作目标与机器人状态 → 自适应全身控制 | G1 全身控制与数据接口；底层控制器服务遥操作和自主操作，补齐基础控制路线。 | [论文](https://arxiv.org/abs/2505.03738) |
| [**HOVER**](https://arxiv.org/abs/2410.21229)<br><sub>HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</sub> | 2024-10<br><sub>ICRA 2025</sub> | 多种指令空间 → 单一全身控制器 | 以运动学动作模仿为共同基础，将多种控制模式蒸馏到同一策略中。<br><sub>标签: Multi-mode control · Policy distillation</sub> | [论文](https://arxiv.org/abs/2410.21229) · [项目](https://hover-versatile-humanoid.github.io/) |
| [**Masked Humanoid Controller / MHC**](https://arxiv.org/abs/2408.07295)<br><sub>Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots</sub> | 2024-07<br><sub>arXiv</sub> | 掩码目标轨迹 → 多模态全身控制器 | Digit V3 真机通用控制接口；掩码目标轨迹支持高层规划、参考轨迹和遥操作等条件。 | [论文](https://arxiv.org/abs/2408.07295) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858)<br><sub>OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</sub> | 2024-06<br><sub>CoRL 2024</sub> | 运动学位姿指令 → 全身遥操作与技能学习 | 提供统一位姿接口与可部署的全身控制器，支持遥操作及从示教学得自主技能。<br><sub>标签: Teleoperation · Whole-body control · Imitation learning</sub> | [论文](https://arxiv.org/abs/2406.08858) · [项目](https://omni.human2humanoid.com/) |
| [**HumanPlus**](https://arxiv.org/abs/2406.10454)<br><sub>HumanPlus: Humanoid Shadowing and Imitation from Humans</sub> | 2024-06<br><sub>arXiv</sub> | 人体动作与跟随示教 → 自主视觉技能 | 定制全尺寸双足人形；人类动作跟踪收集全身示范，再学习自主视觉策略，含站起行走和货架操作。 | [论文](https://arxiv.org/abs/2406.10454) |

**跨方向阅读：** [InterMimicGen](#execution-guided-data-policy-co-improvement) 除迭代数据循环外，也训练通用交互跟踪器。

[关联模型与学习基础](docs/RELATED_READING.md#foundations-zh)：Astranomy、InternW0-Δ、Diffusion Policy、Dreamer、InterMimic。

<a id="humanoid-simulation-benchmarks"></a>

### 人形机器人仿真基准

**范围。** 使用明确的人形机器人模型评估学习与控制，覆盖场景交互及多机器人操作。

**阅读提示。** HumanoidBench 与 Mimicking-Bench 评估单机器人技能，CoHuB 面向协作；这些条目是仿真基准，不代表真机结果。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**CoHuB**](https://arxiv.org/abs/2609.34782)<br><sub>CoHuB: A Simulation Benchmark for Multi-Humanoid Collaboration</sub> | 2026-09<br><sub>arXiv · Benchmark</sub> | 多机器人仿真任务 → 协作操作评测 | 采用 G1 与 Dex3-1 的多机协作操作仿真评测；不能写成真实双机部署结果。 | [论文](https://arxiv.org/abs/2609.34782) |
| [**HumanoidArena**](https://arxiv.org/abs/2606.17833)<br><sub>HumanoidArena: Benchmarking Egocentric Hierarchical Whole-body Learning</sub> | 2026-06<br><sub>arXiv · Benchmark</sub> | 仿真任务与控制后端 → 人形策略基准 | G1 仿真多任务操作基准，接入 TWIST2/SONIC 等控制后端；只作为评测贡献收录。 | [论文](https://arxiv.org/abs/2606.17833) |
| [**Mimicking-Bench**](https://arxiv.org/abs/2412.17730)<br><sub>Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking</sub> | 2024-12<br><sub>arXiv · Benchmark</sub> | 人体交互参考与多样物体 → 场景交互基准 | Unitree H1 仿真，六类家居全身场景交互任务；不是仅有人体动画数据。 | [论文](https://arxiv.org/abs/2412.17730) |
| [**HumanoidBench**](https://arxiv.org/abs/2403.10506)<br><sub>HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation</sub> | 2024-03<br><sub>arXiv · Benchmark</sub> | 仿真人形机器人模型与任务 → 学习基准 | H1 加灵巧手的 MuJoCo 仿真，含移动与全身操作，并提供 Digit 模型；标注仿真。 | [论文](https://arxiv.org/abs/2403.10506) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="harness"></a>
<a id="systems"></a>
<a id="systems系统与技能编排"></a>

## Harness｜执行框架与技能编排

将感知、控制接口、可复用技能和执行反馈组织为人形机器人系统，支持自主执行或人类引导的数据采集。

<a id="spatial-memory-skill-orchestration"></a>
<a id="agentic-skill-orchestration"></a>
<a id="智能体技能编排"></a>

### 空间记忆与长程技能编排

利用空间记忆与技能执行结果，规划并调整长时程任务执行。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HomeBody**](https://tml.stanford.edu/homebody/)<br><sub>HomeBody: A Humanoid That Explores, Remembers, and Acts on Its Own</sub> | 2026-09<br><sub>项目报告</sub> | 空间记忆与技能库 → 长时程任务执行 | 将 VLM 与导航、操作技能相连，用空间记忆和执行结果协调 G1 的长时程任务。<br><sub>标签: Spatial memory · Skill orchestration · Execution feedback</sub> | [项目报告](https://tml.stanford.edu/homebody/) |

**跨方向阅读：** [OmniH2O](#generalist-whole-body-control) 连接遥操作与技能学习；[KPI](#contact-force-control) 连接智能体生成的参考轨迹与接触调节。

**跨方向阅读：** [TTCO](#test-time-command-optimization) 通过外围仿真搜索适配冻结控制基座的输入指令，主条目见 Foundations。

[关联执行与训练方法](docs/RELATED_READING.md#harness-zh)：RoboICL、Recova、SGS。

<a id="whole-body-teleoperation-data"></a>

### 全身遥操作与数据采集

**范围。** 集成人类操作接口、感知与全身控制，执行并记录人形示教。

**阅读提示。** HOMIE 使用外骨骼座舱；TWIST2 使用 VR 动作采集与主动第一视角视觉。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HuMiT**](https://arxiv.org/abs/2610.29903)<br><sub>HuMiT: Low-Latency Whole-Body Humanoid Teleoperation via Compact Reference Tracking</sub> | 2026-10<br><sub>arXiv</sub> | 实时操作者动作 → 紧凑参考与统一全身遥操作 | 以当前帧根部指令和四个关键点位姿驱动统一跟踪，无需在线优化重定向或未来帧，在真实 G1 上遥操作完成搬运、推椅、坐椅和挂衣。 | [论文](https://arxiv.org/abs/2610.29903) |
| [**ExtremControl**](https://arxiv.org/abs/2602.11321)<br><sub>ExtremControl: Low-Latency Humanoid Teleoperation with Scaled Velocity Feedforward</sub> | 2026-02<br><sub>arXiv</sub> | 实时人体动作 → 末端位姿指令与低延迟全身遥操作 | 结合缩放速度前馈与闭式位姿映射，在 G1 真机上遥操作完成移动中接物、合作抬箱和乒乓球交互；仿真与真机评测验证控制响应。 | [论文](https://arxiv.org/abs/2602.11321) |
| [**TWIST2**](https://arxiv.org/abs/2511.02832)<br><sub>TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System</sub> | 2025-11<br><sub>arXiv</sub> | VR 全身动作与第一视角反馈 → 人形示教数据及视觉动作策略 | 结合便携式 VR 全身遥操作、主动颈部与分层视觉动作学习，支持 G1 协调示教采集及自主技能。<br><sub>标签: 全身遥操作 · 主动视觉 · 示教采集</sub> | [论文](https://arxiv.org/abs/2511.02832) · [项目](https://yanjieze.com/projects/TWIST2/) |
| [**HOMIE**](https://arxiv.org/abs/2502.13013)<br><sub>HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit</sub> | 2025-02<br><sub>arXiv</sub> | 外骨骼、手套与踏板指令 → 人形全身遥操作及示教数据 | 将同构手臂控制、手指感知与支持行走和下蹲的 RL 控制器集成，采集人形移动操作示教。<br><sub>标签: 遥操作 · 外骨骼 · 数据采集</sub> | [论文](https://arxiv.org/abs/2502.13013) · [项目](https://homietele.github.io/) |
| [**Mobile-TeleVision**](https://arxiv.org/abs/2412.07773)<br><sub>Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control</sub> | 2024-12<br><sub>arXiv</sub> | 遥操作上身目标 → 协调行走与操作 | 预测上身运动先验与下身运动控制解耦，支持人形机器人边行走边操作。 | [论文](https://arxiv.org/abs/2412.07773) |
| [**Mixed Reality Teleoperation Assistance**](https://arxiv.org/abs/2411.01014)<br><sub>Mixed Reality Teleoperation Assistance for Direct Control of Humanoids</sub> | 2024-11<br><sub>arXiv</sub> | 混合现实指令与物体可供性 → 辅助遥操作 | Nadia；混合现实、概率动作基元与物体/可供性检测协助遥操作。 | [论文](https://arxiv.org/abs/2411.01014) |
| [**TRILL**](https://arxiv.org/abs/2309.01952)<br><sub>Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation</sub> | 2023-09<br><sub>arXiv</sub> | VR 示教与全身控制 → 视觉运动策略 | 人形全身控制将 VR 任务空间指令变为关节力矩，再从示范学习移动操作；包含仿真和真机验证。 | [论文](https://arxiv.org/abs/2309.01952) |
| [**iCub3 Avatar System**](https://arxiv.org/abs/2203.06972)<br><sub>iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots</sub> | 2022-03<br><sub>arXiv</sub> | 远程操作指令与多模态反馈 → 具身机器人执行 | iCub3 远程全身具身遥操作；明确涉及行走、操作、多模态反馈及搬运负载的真实场景。 | [论文](https://arxiv.org/abs/2203.06972) |

<a id="object-memory-execution-verification"></a>
<a id="execution-monitoring-recovery"></a>

### 执行监控与恢复

**范围。** 通过持久物体状态或技能级执行检查，监控物理任务效果并触发恢复。

**阅读提示。** POT-VLA 在动作片段执行后形成验证闭环；持久物体状态与上面的空间记忆、技能编排互补。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**FRAMES**](https://arxiv.org/abs/2609.22538)<br><sub>FRAMES: Failure Recovery And Monitoring of Embodied Skills for Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | 技能执行观测 → 监控与恢复决策 | G1 的执行监控与失败恢复监督层，工作在底层全身控制器之上。 | [论文](https://arxiv.org/abs/2609.22538) |
| [**POT-VLA**](https://arxiv.org/abs/2607.18016)<br><sub>Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation</sub> | 2026-07<br><sub>arXiv</sub> | RGB-D 观测、任务角色与机器人状态 → 物体条件化动作及执行检查 | 维护持久三维物体记录，同时供 G1 动作专家与几何谓词检查使用，在动作片段执行后验证结果并进行局部恢复。<br><sub>标签: 物体记忆 · Token 条件化 VLA · 执行验证</sub> | [论文](https://arxiv.org/abs/2607.18016) |

<a id="planning-control-interfaces"></a>

### 规划与控制接口

**范围。** 将任务推理与感知转化为可执行的全身规划和控制器指令。

**阅读提示。** KINO 使用关键帧，iGPC 以几何信息支撑执行，开门系统使用可复用行为树。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**GPT-6-Astra Embodied Evaluation**](https://arxiv.org/abs/2610.22471)<br><sub>Has GPT-6-Astra Achieved Embodied Intelligence?</sub> | 2026-10<br><sub>arXiv</sub> | 观测、示教与反馈 → 经执行接口下发的模型动作 | 研究上下文学习、交互预算与执行接口，包含 SIMPLE 中的 G1 仿真移动操作；真机 G1 的操作与行走分别评测。 | [论文](https://arxiv.org/abs/2610.22471) |
| [**Inertially Significant Humanoid Teleoperation**](https://arxiv.org/abs/2610.22176)<br><sub>Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation</sub> | 2026-10<br><sub>arXiv</sub> | VR 位姿指令与机器人反馈 → 负载自适应的全身 MPC 指令 | 在 23 自由度双足人形机器人上结合全身 MPC 与基于 EKF 的在线惯性估计，真机负载测试使用手工安装的前臂配重。 | [Paper](https://arxiv.org/abs/2610.22176) |
| [**iGPC**](https://arxiv.org/abs/2610.08120)<br><sub>iGPC: Generative Motion Priors for Object-Aware Humanoid Interaction</sub> | 2026-10<br><sub>arXiv</sub> | 几何观测与目标 → 几何落地的全身执行 | G1 真机；以几何感知和已有运动先验协调规划与控制，覆盖抓扶手、推箱及坐站。 | [论文](https://arxiv.org/abs/2610.08120) |
| [**Praxis**](https://arxiv.org/abs/2609.30735)<br><sub>Praxis: Distilling Physical Interaction Priors from Egocentric Videos for Generalizable Whole-Body Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | 感知与任务请求 → 协调技能执行 | G1 EDU 与 Revo2 手的真实系统；将感知、导航、校准和操作连接为可执行任务流程。 | [论文](https://arxiv.org/abs/2609.30735) |
| [**KINO**](https://arxiv.org/abs/2609.18869)<br><sub>KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | VLM 生成的关键帧 → 全身拾取与搬运 | G1 仿真及真机；关键帧作为 VLM 规划与全身控制之间的接口，完成拾取、搬运、放置。 | [论文](https://arxiv.org/abs/2609.18869) |
| [**Fast Humanoid Robot Door Traversals**](https://arxiv.org/abs/2411.03532)<br><sub>A Behavior Architecture for Fast Humanoid Robot Door Traversals</sub> | 2024-11<br><sub>arXiv</sub> | 门体感知与行为树 → 协调开门穿越 | Nadia 真机；感知、行为树与全身行走/操作控制实现不同类型门的穿越。 | [论文](https://arxiv.org/abs/2411.03532) |
| [**OKAMI**](https://arxiv.org/abs/2410.11792)<br><sub>OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation</sub> | 2024-10<br><sub>arXiv</sub> | 单段 RGB-D 示教 → 物体感知规划与视觉策略 | Fourier GR1 与 Inspire 手；单个 RGB-D 视频通过物体感知重定向生成执行，再学习视觉策略。主要是操作贡献，不宣称自主移动。 | [论文](https://arxiv.org/abs/2410.11792) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="iterative-improvement"></a>
<a id="rsi"></a>

## Iterative Improvement｜迭代改进

利用跨轮次保留的执行反馈改进后续数据、策略、奖励程序或技能保留策略，明确改进对象与机制；迭代数据飞轮不等于不受限的递归自我改进（RSI）。

<a id="execution-guided-data-policy-co-improvement"></a>
<a id="self-evolving-data-engines"></a>
<a id="execution-guided-data--policy-improvement"></a>
<a id="执行反馈驱动的数据与策略改进"></a>

### 执行反馈驱动的数据与策略协同改进

保留成功执行结果，作为后续轮次数据扩增与跟踪策略更新的起点。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimicGen**](https://arxiv.org/abs/2610.06850)<br><sub>InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</sub> | 2026-10<br><sub>arXiv</sub> | 交互参考与执行结果 → 扩增动作及改进后的跟踪器 | 迭代扰动交互参考、微调通用跟踪器，并保留成功执行的变体作为下一轮扩增种子。<br><sub>标签: Contact-aware retargeting · Generalist tracking · Iterative augmentation</sub> | [论文](https://arxiv.org/abs/2610.06850) · [项目](https://sirui-xu.github.io/InterMimicGen/) |
| [**HumanoidDART**](https://arxiv.org/abs/2606.26855)<br><sub>Humanoid-DART: Humanoid Loco-Manipulation using Diffusion-guided Augmentation through Relabeling and Tracking</sub> | 2026-06<br><sub>arXiv</sub> | 生成的交互参考与执行回放 → 改进后的生成器与跟踪器 | G1 真机；生成器与跟踪器通过执行反馈交替更新，覆盖推、踢、拾放。 | [论文](https://arxiv.org/abs/2606.26855) |

[关联程序与执行框架演进](docs/RELATED_READING.md#rsi-zh)：HarnessPAI、PhysEvo。它们提供可借鉴的机制，评测范围与人形全身控制有所不同。

<a id="execution-guided-reward-program-evolution"></a>
<a id="execution-guided-program-refinement"></a>

### 执行反馈驱动的程序改进

**范围。** 依据执行反馈修订奖励、控制或协作程序，并说明跨轮次保留的程序与经验。

**阅读提示。** InterEvolve 修订奖励程序，HuGo 修订控制代码，CoEvolve 在仿真中修订团队协作并保留验证经验。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**InterEvolve**](https://arxiv.org/abs/2610.02196)<br><sub>InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | 任务请求、仿真反馈与技能库 → 修订后的奖励程序 | 用 LLM 与数值搜索修订分阶段奖励程序，在固定控制器上验证，并保留成功程序供后续任务复用。<br><sub>标签: 奖励程序 · 测试时搜索 · 持久技能库</sub> | [论文](https://arxiv.org/abs/2610.02196) · [项目](https://sirui-xu.github.io/InterEvolve/) |
| [**CoEvolve**](https://arxiv.org/abs/2610.23288)<br><sub>CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots</sub> | 2026-10<br><sub>arXiv</sub> | 固定运动技能与验证反馈 → 演化后的协作代码 | 两个仿真 G1 协作搬运；验证失败后修订协调代码并保留经验，没有真机结果声明。 | [论文](https://arxiv.org/abs/2610.23288) |
| [**HuGo**](https://arxiv.org/abs/2609.30594)<br><sub>HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | 任务请求与执行回放 → 修订后的控制程序 | G1 真机；利用执行反馈修改并验证控制代码；跨任务技能记忆仍是未来工作，不宣称已实现。 | [论文](https://arxiv.org/abs/2609.30594) |

<a id="skill-reuse-memory-consolidation"></a>

### 技能复用与记忆巩固

**范围。** 从适用的初始状态复用经过执行验证的全身动作，并在存储容量受限时学习保留哪些能力。

**阅读提示。** HumanoidTTT 改进技能保留策略，动作生成器与跟踪器保持固定。该路线与[技能编排](#spatial-memory-skill-orchestration)互补；论文真机示例验证的是全身动作复用，而非物体操作。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanoidTTT**](https://arxiv.org/abs/2610.00198)<br><sub>HumanoidTTT: Test-Time Capability Reuse for Efficient Humanoid Control</sub> | 2026-09<br><sub>arXiv</sub> | 动作请求、初始状态与复用反馈 → 已验证动作复用及技能保留 | 通过初始状态适用性检查决定完整动作能否复用，并利用后续成功复用反馈学习有限技能库的保留策略，生成器与跟踪器保持固定。<br><sub>标签: 能力复用 · 在线巩固 · 有限记忆</sub> | [论文](https://arxiv.org/abs/2610.00198) · [代码](https://github.com/AIGeeksGroup/HumanoidTTT) |

<a id="human-intervention-policy-improvement"></a>

### 人类干预驱动的策略改进

**范围。** 利用部署尝试和不完美的人工纠正，跨轮次更新人形策略。

**阅读提示。** ROVE 从混合质量经验改进策略与价值函数；其改进对象不同于保留动作或在运动控制器固定时修订奖励程序。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**ROVE**](https://arxiv.org/abs/2606.17011)<br><sub>ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning</sub> | 2026-06<br><sub>arXiv</sub> | 人形执行轨迹、人工干预与人类视频 → 价值引导的 VLA 更新 | 从混合质量经验学习乐观价值估计，通过优势条件化策略更新，跨执行与人工干预轮次改进人形操作。<br><sub>标签: 人类干预 · 价值估计 · 迭代后训练</sub> | [论文](https://arxiv.org/abs/2606.17011) |

<a id="planner-policy-post-training"></a>

### 规划器与策略后训练

**范围。** 通过显式后训练保留规划器或策略更新，并与回合内指令搜索区分。

**阅读提示。** DiPLO 针对冻结跟踪器更新扩散规划器，HAF 在冻结 VLA 上更新潜空间策略；二者均不直接等同于严格 RSI。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**DiPLO**](https://arxiv.org/abs/2610.24847)<br><sub>DiPLO: Self-distilled Diffusion Planning for Loco-manipulation</sub> | 2026-10<br><sub>arXiv</sub> | 预训练扩散规划器与跟踪器 → 后训练规划器 | G1 真机；扩散规划器经过自蒸馏与强化学习后训练，并对齐冻结跟踪器的执行能力。 | [论文](https://arxiv.org/abs/2610.24847) |
| [**HAF**](https://arxiv.org/abs/2608.16837)<br><sub>HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL</sub> | 2026-08<br><sub>arXiv</sub> | 通用 VLA 与离线/在线经验 → 适配后的全身策略 | Tienkung 2.0/3.0 真机；分层动作流加冻结 VLA 潜空间的离线到在线强化学习。 | [论文](https://arxiv.org/abs/2608.16837) |
| [**FADA**](https://arxiv.org/abs/2606.28476)<br><sub>FADA: Few-Shot Domain Adaptation via Dynamics Alignment for Humanoid Control</sub> | 2026-06<br><sub>arXiv</sub> | 规划器–逆动力学模型策略与短时目标域轨迹 → 动力学适配的执行模型 | 冻结规划器，仅用执行轨迹进行监督微调逆动力学模型，在真实 G1 搬运杂货和 Booster T1 拉筐任务中评测。 | [Paper](https://arxiv.org/abs/2606.28476) · [Project](https://lecar-lab.github.io/FADA-humanoid/) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

---

**更多资源：** [关联方法与基础阅读](docs/RELATED_READING.md#中文) · [历史数据引擎清单（2026-10-08）](docs/DATA_ENGINE_READING_LIST.md) · [贡献指南](CONTRIBUTING.md) · [主题模板](docs/TOPIC_TEMPLATE.md)。

**参考仓库：** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation)。

**许可：** 原创整理文字与资产采用 [MIT 许可](LICENSE)；链接中的研究与资源保留各自许可。



