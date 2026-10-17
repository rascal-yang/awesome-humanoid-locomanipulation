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
  <img src="https://img.shields.io/badge/Core_entries-48-4263eb?style=flat-square" alt="48 core entries">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

人形移动操作将**移动、平衡与操作**协同起来。本清单按七个研究方向组织 **48 项核心工作**，每项设一个主条目，并用交叉链接呈现重叠贡献；另提供 [13 项关联方法](docs/RELATED_READING.md#中文)，说明机械臂、仿真人体与通用学习方法对本主题的参考价值。

**收录范围：** 优先选择直接研究人形全身操作、接触交互、重定向、训练迁移或执行系统的工作。论文与项目报告明确区分，分类属于编辑判断。

**分类核对：2026-10-16。** 表中为首次公开月份与单独核实的发表信息，不是阅读日期。资源链接不保证完整实现已发布，见 [来源与收录说明](docs/SOURCES.md)。

**最新收录：2026-10-17（从 2025 年至今的检索新增 22 项；日期与筛选边界见来源说明）。**

H2 表示宏观研究方向、技术路线或系统范式，H3 表示其中的具体方法，小节可以只有一项工作；交叉链接与标签呈现重叠贡献。

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
- [Interaction｜交互学习与控制](#interaction)
  - [从人类示教学习交互](#interaction-learning-from-human-videos)
  - [灵巧全身交互](#dexterous-whole-body-interaction)
  - [接触与力控制](#contact-force-control)
  - [触觉引导的全身操作](#tactile-guided-manipulation)
- [Foundations｜模型与控制基座](#foundations)
  - [测试时指令优化](#test-time-command-optimization)
  - [全身 VLA 与人类数据预训练](#whole-body-vla-human-pretraining)
  - [世界模型条件化的全身策略](#world-model-conditioned-policies)
  - [通用全身控制](#generalist-whole-body-control)
- [Harness｜执行框架与技能编排](#harness)
  - [空间记忆与长程技能编排](#spatial-memory-skill-orchestration)
  - [全身遥操作与数据采集](#whole-body-teleoperation-data)
- [Iterative Improvement｜迭代改进](#iterative-improvement)
  - [执行反馈驱动的数据与策略协同改进](#execution-guided-data-policy-co-improvement)
  - [执行反馈驱动的奖励程序演化](#execution-guided-reward-program-evolution)

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
| [**PriMoRetarget**](https://arxiv.org/abs/2610.12642)<br><sub>PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting</sub> | 2026-10<br><sub>arXiv</sub> | 人体动作与交互示教 → 人形机器人参考轨迹 | 通过显式目标优先级与梯度投影，在优化姿态等低优先级目标时保留足部落点和交互接触。<br><sub>标签: Prioritized optimization · Contact preservation · Multi-character interactions</sub> | [论文](https://arxiv.org/abs/2610.12642) · [项目](https://nickioan.github.io/primoretarget-page/) |
| [**OTRetarget**](https://arxiv.org/abs/2609.36602)<br><sub>OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport</sub> | 2026-09<br><sub>arXiv</sub> | 人体物体示教 → 机器人与物体联合参考轨迹 | 利用最优传输匹配表面交互，联合优化机器人与物体位姿，在形态变化后保留接触关系。<br><sub>标签: Contact preservation · Joint robot–object optimization</sub> | [论文](https://arxiv.org/abs/2609.36602) |
| [**HOI-Retarget**](https://arxiv.org/abs/2609.34674)<br><sub>HOI-Retarget: Contact-Centric Retargeting for Human-Object Interaction</sub> | 2026-09<br><sub>arXiv</sub> | 人体物体交互动作与物体系接触标注 → 人形交互参考轨迹 | 以滑动窗口轨迹优化在人体形态变化与机器人运动学约束下保留物体系接触，同时兼顾身体跟踪、足部支撑和平滑性。<br><sub>标签: Object-frame contacts · Trajectory optimization · Motion augmentation</sub> | [论文](https://arxiv.org/abs/2609.34674) · [项目](https://shinben0327.github.io/hoi-retarget/) |
| [**UMR**](https://arxiv.org/abs/2609.02134)<br><sub>Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence</sub> | 2026-09<br><sub>arXiv</sub> | 人体表面动作与接触图 → 人形机器人参考动作 | 学习人体与机器人表面的稠密对应，将其用于受约束姿态匹配和接触图迁移，统一处理不同动作来源。<br><sub>标签: Dense correspondence · Surface matching · Contact transfer</sub> | [论文](https://arxiv.org/abs/2609.02134) |
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
| [**LEGS**](https://arxiv.org/abs/2606.01458)<br><sub>LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World</sub> | 2026-05<br><sub>arXiv</sub> | 真实场景采集 → 校准的 3DGS 仿真器 → 合成 VLA 示教 | 将重建背景、动态网格前景与程序化动作示教结合，为真实 G1 任务微调 VLA。<br><sub>标签: 场景重建 · 高斯泼溅 · 合成示教</sub> | [论文](https://arxiv.org/abs/2606.01458) · [项目](https://hojjunekim.github.io/legs/) |

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

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="interaction"></a>

## Interaction｜交互学习与控制

学习并控制人形机器人与物体、环境的物理交互，覆盖身体与手部协调及接触力调节。

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
| [**VICAR**](https://arxiv.org/abs/2610.13079)<br><sub>VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills</sub> | 2026-10<br><sub>arXiv</sub> | 第三视角人类视频与接触目标 → 可适配的人形交互技能 | 在重定向时保留全局接触位姿、动作速度和碰撞间距，再学习可适配变化接触目标的条件动作。<br><sub>标签: Video imitation · Contact-aware retargeting · Contact conditioning</sub> | [论文](https://arxiv.org/abs/2610.13079) |
| [**Workhorse**](https://arxiv.org/abs/2610.09117)<br><sub>Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data</sub> | 2026-10<br><sub>arXiv</sub> | 可穿戴人体位姿与第一视角 RGB → 视觉规划器和全身跟踪器 | 以躯干、双腕和双足目标分别训练视觉规划器与 RL 跟踪器，并模拟彼此误差扩增数据，无需机器人专属重定向即可学习 G1 接触交互技能。<br><sub>标签: Robot-free demonstrations · Five-link interface · Robust tracking</sub> | [论文](https://arxiv.org/abs/2610.09117) · [项目](https://hybridrobotics.github.io/workhorse/) |
| [**HALOMI**](https://arxiv.org/abs/2606.18772)<br><sub>HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations</sub> | 2026-06<br><sub>arXiv</sub> | 第一视角与腕部观测、头手示教 → 主动感知人形策略 | 将视角对齐、控制器感知参考适配与潜在流形控制器结合，实现头手协调跟踪。<br><sub>标签: 主动感知 · 头手控制 · 示教对齐</sub> | [论文](https://arxiv.org/abs/2606.18772) · [项目](https://halomi-humanoid.github.io) |
| [**EgoHumanoid**](https://arxiv.org/abs/2602.10106)<br><sub>EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration</sub> | 2026-02<br><sub>arXiv</sub> | 第一视角人类示教与少量机器人数据 → 对齐后的人形 VLA 策略 | 先对齐人机视角与动作空间，再联合训练用于 G1 跨环境移动操作的 VLA。<br><sub>标签: 视角对齐 · 动作对齐 · 人机数据联合训练</sub> | [论文](https://arxiv.org/abs/2602.10106) · [项目](https://opendrivelab.com/EgoHumanoid/) |
| [**HuMI**](https://arxiv.org/abs/2602.06643)<br><sub>Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations</sub> | 2026-02<br><sub>arXiv</sub> | 便携式无机器人全身示教 → 分层人形操作策略 | 通过在线可行性预览采集人类全身动作，以分层策略学习跪姿、下蹲、投掷及行走操作。<br><sub>标签: 无机器人示教 · 可行性对齐 · 分层学习</sub> | [论文](https://arxiv.org/abs/2602.06643) · [项目](https://humanoid-manipulation-interface.github.io) |
| [**HumanX**](https://arxiv.org/abs/2602.02473)<br><sub>HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos</sub> | 2026-02<br><sub>CoRL 2026</sub> | 人类视频 → 扩增参考轨迹 → 交互技能 | 结合以锚点为中心的交互合成与交互优先的模仿学习，获得可迁移至 G1 的敏捷技能。<br><sub>标签: Video reconstruction · Data augmentation · Interaction learning</sub> | [论文](https://arxiv.org/abs/2602.02473) · [项目](https://wyhuai.github.io/human-x/) |
| [**ResMimic**](https://arxiv.org/abs/2510.05070)<br><sub>ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning</sub> | 2025-10<br><sub>arXiv</sub> | 人类交互参考与通用动作跟踪器 → 物体感知残差策略 | 在通用动作跟踪器上学习残差，利用物体几何与接触奖励提高全身交互精度。<br><sub>标签: 残差学习 · 接触奖励 · 物体跟踪</sub> | [论文](https://arxiv.org/abs/2510.05070) · [项目](https://resmimic.github.io/) |
| [**HumanoidExo**](https://arxiv.org/abs/2510.03022)<br><sub>HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton</sub> | 2025-10<br><sub>arXiv</sub> | 可穿戴外骨骼动作与相机观测 → 人形全身策略 | 将可穿戴人类数据与人形构型对齐，并结合少量机器人示教学习站立、下蹲及行走操作。<br><sub>标签: 无机器人数据 · 外骨骼 · 人机数据联合训练</sub> | [论文](https://arxiv.org/abs/2510.03022) |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | 单目 RGB 视频 → 全身交互策略 | 提取人体与物体轨迹，通过联合跟踪机器人和物体状态学习全身交互技能。<br><sub>标签: Video reconstruction · Interaction imitation · Sim-to-real</sub> | [论文](https://arxiv.org/abs/2509.16757) · [项目](https://hdmi-humanoid.github.io/) · [代码](https://github.com/LeCAR-Lab/HDMI) |

<a id="dexterous-whole-body-interaction"></a>

### 灵巧全身交互

利用捕获示教或合成的全身抓持监督，学习身体与手部接触协调。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**WBD**](https://arxiv.org/abs/2610.22184)<br><sub>Whole-Body Dexterity</sub> | 2026-10<br><sub>arXiv</sub> | 生成的全身抓持与目标参考 → 身体接触操作策略 | 从可行抓持训练并蒸馏物体重定位专家，使 G1 通过协调的手臂与躯干接触操纵物体。<br><sub>标签: 全身抓持 · 专家蒸馏 · 身体接触</sub> | [论文](https://arxiv.org/abs/2610.22184) |
| [**Weave**](https://arxiv.org/abs/2609.16683)<br><sub>Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions</sub> | 2026-09<br><sub>arXiv</sub> | 人体交互动捕 → 灵巧机器人与物体交互 | 结合接触感知重定向与几何感知策略，协调身体和手指关节以跟踪机器人与物体参考轨迹。<br><sub>标签: HOI motion capture · Dexterous hands · Contact-aware retargeting</sub> | [论文](https://arxiv.org/abs/2609.16683) · [项目](https://xiaohu-art.github.io/Weave/) |

<a id="contact-force-control"></a>

### 接触与力控制

在执行动作轨迹时进一步调节柔顺性与接触力。

接触力迁移所需的执行器仿真校正见 [Contact-UAN](#contact-consistent-actuator-modeling)。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**C-GMT**](https://arxiv.org/abs/2610.22119)<br><sub>Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation</sub> | 2026-10<br><sub>arXiv</sub> | 动作参考与本体感知历史 → 柔顺参考修正 | 在通用动作跟踪器上学习残差参考适配器，使回放、遥操作及 VLA 接口均可产生柔顺全身响应。<br><sub>标签: 残差参考适配 · 柔顺控制 · 通用动作跟踪</sub> | [论文](https://arxiv.org/abs/2610.22119) · [项目](https://venki1899.github.io/c-gmt/) |
| [**KPI**](https://arxiv.org/abs/2609.36151)<br><sub>KPI: A Promptable Kernel for Physical Interaction on Humanoids</sub> | 2026-09<br><sub>arXiv</sub> | 轨迹与交互约束 → 自适应接触控制 | 在保留底层全身跟踪器的基础上，按跟踪、柔顺及力范围要求调整手臂阻抗与参考量。<br><sub>标签: Impedance adaptation · Force regulation</sub> | [论文](https://arxiv.org/abs/2609.36151) · [项目](https://kpi-robot.github.io/) |
| [**CEER**](https://arxiv.org/abs/2605.19981)<br><sub>CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation</sub> | 2026-05<br><sub>arXiv</sub> | 根部指令与末端姿态 → 柔顺全身控制接口 | 将动作跟踪蒸馏为末端与根部接口，支持柔顺操作及多种高层规划器接入。<br><sub>标签: 柔顺控制 · 任务空间接口 · 分层控制</sub> | [论文](https://arxiv.org/abs/2605.19981) · [项目](https://robotproject8.github.io/ceer_page/) |
| [**GentleHumanoid**](https://arxiv.org/abs/2511.04679)<br><sub>GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction</sub> | 2025-11<br><sub>arXiv</sub> | 动作参考与交互力建模 → 上半身柔顺响应 | 以弹簧模型描述引导与阻抗接触，训练全身跟踪器在身体交互中协调肩、肘、腕的柔顺响应。<br><sub>标签: 柔顺控制 · 人机接触 · 全身跟踪</sub> | [论文](https://arxiv.org/abs/2511.04679) |
| [**FALCON**](https://arxiv.org/abs/2505.06776)<br><sub>FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation</sub> | 2025-05<br><sub>arXiv</sub> | 外载作用下的根部与末端指令 → 力自适应全身控制 | 通过满足关节力矩约束的力课程联合训练上下半身智能体，支持人形机器人负载搬运、拉车与开门。<br><sub>标签: 力自适应 · 双智能体 RL · 负载操作</sub> | [论文](https://arxiv.org/abs/2505.06776) |

**跨方向阅读：** [PRISM](#counterfactual-video-augmentation) 与 [GRAIL](#asset-video-interaction-synthesis) 也学习交互策略，主条目侧重其数据生成贡献。[KPI](#contact-force-control) 还包含智能体驱动的轨迹与交互约束生成。

<a id="tactile-guided-manipulation"></a>

### 触觉引导的全身操作

**范围。** 以分布式身体接触感知作为策略输入，学习人形物体操作。

**阅读提示。** TACT 从触觉观测学习；[接触与力控制](#contact-force-control) 侧重交互动态调节。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**TACT**](https://arxiv.org/abs/2506.15146)<br><sub>TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality</sub> | 2025-06<br><sub>RA-L 2025</sub> | 视觉、关节状态与分布式触觉 → 接触密集操作动作 | 为 ACT 加入上半身触觉输入，并与基于模型的双足控制结合，实现利用大面积身体接触的搬运。<br><sub>标签: 触觉反馈 · 模仿学习 · 身体接触</sub> | [论文](https://arxiv.org/abs/2506.15146) |

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
| [**λ₀**](https://arxiv.org/abs/2610.00438)<br><sub>Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining</sub> | 2026-09<br><sub>arXiv</sub> | 第一视角身体与手部数据 → 全身 VLA | 通过分阶段人体数据预训练与形态适配，学习协调全身和手部动作的策略。<br><sub>标签: VLA · Human-data pretraining · Embodiment adaptation</sub> | [论文](https://arxiv.org/abs/2610.00438) |
| [**OpenHLM**](https://arxiv.org/abs/2606.22174)<br><sub>OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | 全身遥操作与异构示教 → 面向人形全身的 VLA | 系统研究关节级遥操作、VLA 动作设计与异构数据联合训练，以单一学习策略指挥人形全身。<br><sub>标签: 全身 VLA · 异构联合训练 · 动作接口</sub> | [论文](https://arxiv.org/abs/2606.22174) · [项目](https://openhlm-project.github.io/) |
| [**WholeBodyVLA**](https://arxiv.org/abs/2512.11047)<br><sub>WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control</sub> | 2025-12<br><sub>arXiv</sub> | 无动作标签的第一视角视频与机器人示教 → 潜在动作 VLA 及移动控制 | 从第一视角视频学习潜在动作，将 VLA 与面向移动操作的控制器结合，支持大范围协调任务。<br><sub>标签: 潜在动作 · 第一视角视频 · 全身 VLA</sub> | [论文](https://arxiv.org/abs/2512.11047) |

<a id="world-model-conditioned-policies"></a>

### 世界模型条件化的全身策略

结合视觉动态预测与动作先验，学习用于协调全身控制的世界动作模型。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**WholeBodyWAM**](https://arxiv.org/abs/2609.18197)<br><sub>WholeBodyWAM: Learning Whole-Body World Action Models with Scalable Motion Priors</sub> | 2026-09<br><sub>arXiv</sub> | 人体及人形动作预训练与机器人示教 → 全身世界动作模型 | 先用异构动作预训练运动专家，再结合运动、视频和动作专家，生成适配目标构型的全身动作。<br><sub>标签: Motion pretraining · World-action model · Whole-body coordination</sub> | [论文](https://arxiv.org/abs/2609.18197) · [项目](https://zbzyjya.github.io/WholeBodyWAM/) |
| [**ω-0**](https://arxiv.org/abs/2608.06375)<br><sub>ω-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation</sub> | 2026-08<br><sub>arXiv</sub> | 视觉观测、语言与机器人状态 → 预测潜变量及全身动作 | 联合预测未来视觉嵌入与全身动作潜变量，支持 G1 人形机器人在移动过程中执行操作。<br><sub>标签: Latent world model · Whole-body actions · Concurrent loco-manipulation</sub> | [论文](https://arxiv.org/abs/2608.06375) |
| [**MotionWAM**](https://arxiv.org/abs/2606.09215)<br><sub>MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | 第一视角视频 → 统一全身动作 token | 利用视频世界模型特征驱动统一全身策略，实时协调移动、躯干、足部与手部动作。<br><sub>标签: Video world model · Unified whole-body actions</sub> | [论文](https://arxiv.org/abs/2606.09215) |

<a id="generalist-whole-body-control"></a>

### 通用全身控制

面向多种指令接口、遥操作或任务目标提供可复用运动控制；各方法支持的接口有所不同。

| 论文 / 项目 | 首次公开 / 发表 | 输入 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**ULTRA**](https://arxiv.org/abs/2603.03279)<br><sub>ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation</sub> | 2026-03<br><sub>IROS 2026</sub> | 动作参考或稀疏目标 → 全身控制 | 将动作跟踪技能蒸馏为多模态控制器，支持从稀疏目标和第一视角感知产生自主行为。<br><sub>标签: Multimodal control · Sparse goals · Motion tracking</sub> | [论文](https://arxiv.org/abs/2603.03279) |
| [**ULC**](https://arxiv.org/abs/2507.06905)<br><sub>ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation</sub> | 2025-07<br><sub>arXiv</sub> | 根部速度与高度、躯干姿态及手臂目标 → 单一全身策略 | 通过渐进式指令课程与手臂残差动作，以统一人形控制器跟踪移动、躯干及双臂指令。<br><sub>标签: 统一控制 · 指令跟踪 · 负载随机化</sub> | [论文](https://arxiv.org/abs/2507.06905) · [项目](https://hellod035.github.io/ULC/) |
| [**HOVER**](https://arxiv.org/abs/2410.21229)<br><sub>HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</sub> | 2024-10<br><sub>ICRA 2025</sub> | 多种指令空间 → 单一全身控制器 | 以运动学动作模仿为共同基础，将多种控制模式蒸馏到同一策略中。<br><sub>标签: Multi-mode control · Policy distillation</sub> | [论文](https://arxiv.org/abs/2410.21229) · [项目](https://hover-versatile-humanoid.github.io/) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858)<br><sub>OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</sub> | 2024-06<br><sub>CoRL 2024</sub> | 运动学位姿指令 → 全身遥操作与技能学习 | 提供统一位姿接口与可部署的全身控制器，支持遥操作及从示教学得自主技能。<br><sub>标签: Teleoperation · Whole-body control · Imitation learning</sub> | [论文](https://arxiv.org/abs/2406.08858) · [项目](https://omni.human2humanoid.com/) |

**跨方向阅读：** [InterMimicGen](#execution-guided-data-policy-co-improvement) 除迭代数据循环外，也训练通用交互跟踪器。

[关联模型与学习基础](docs/RELATED_READING.md#foundations-zh)：Astranomy、InternW0-Δ、Diffusion Policy、Dreamer、InterMimic。

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
| [**TWIST2**](https://arxiv.org/abs/2511.02832)<br><sub>TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System</sub> | 2025-11<br><sub>arXiv</sub> | VR 全身动作与第一视角反馈 → 人形示教数据及视觉动作策略 | 结合便携式 VR 全身遥操作、主动颈部与分层视觉动作学习，支持 G1 协调示教采集及自主技能。<br><sub>标签: 全身遥操作 · 主动视觉 · 示教采集</sub> | [论文](https://arxiv.org/abs/2511.02832) · [项目](https://yanjieze.com/projects/TWIST2/) |
| [**HOMIE**](https://arxiv.org/abs/2502.13013)<br><sub>HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit</sub> | 2025-02<br><sub>arXiv</sub> | 外骨骼、手套与踏板指令 → 人形全身遥操作及示教数据 | 将同构手臂控制、手指感知与支持行走和下蹲的 RL 控制器集成，采集人形移动操作示教。<br><sub>标签: 遥操作 · 外骨骼 · 数据采集</sub> | [论文](https://arxiv.org/abs/2502.13013) · [项目](https://homietele.github.io/) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

<a id="iterative-improvement"></a>
<a id="rsi"></a>

## Iterative Improvement｜迭代改进

利用跨轮次保留的执行反馈改进后续数据、策略或奖励程序，明确改进对象与机制；迭代数据飞轮不等于不受限的递归自我改进（RSI）。

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

<a id="execution-guided-reward-program-evolution"></a>

### 执行反馈驱动的奖励程序演化

**范围。** 利用执行轨迹反馈修订任务奖励，并保留验证后的程序供后续任务使用。

**阅读提示。** InterEvolve 在搜索期间保持运动控制器固定，改进的是奖励程序与技能库。

| 论文 / 项目 | 首次公开 / 发表信息 | 输入 → 输出 | 一句话概括 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**InterEvolve**](https://arxiv.org/abs/2610.02196)<br><sub>InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | 任务请求、仿真反馈与技能库 → 修订后的奖励程序 | 用 LLM 与数值搜索修订分阶段奖励程序，在固定控制器上验证，并保留成功程序供后续任务复用。<br><sub>标签: 奖励程序 · 测试时搜索 · 持久技能库</sub> | [论文](https://arxiv.org/abs/2610.02196) · [项目](https://sirui-xu.github.io/InterEvolve/) |

<p align="right"><a href="#top">↑ 回到顶部</a></p>

---

**更多资源：** [关联方法与基础阅读](docs/RELATED_READING.md#中文) · [历史数据引擎清单（2026-10-08）](docs/DATA_ENGINE_READING_LIST.md) · [贡献指南](CONTRIBUTING.md) · [主题模板](docs/TOPIC_TEMPLATE.md)。

**参考仓库：** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation)。

**许可：** 原创整理文字与资产采用 [MIT 许可](LICENSE)；链接中的研究与资源保留各自许可。
