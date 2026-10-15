# Related Methods & Foundations / 关联方法与基础阅读

[Core list](../README.md) · [核心清单](../README.zh-CN.md) · [中文](#中文)

Last checked / 最近核对：**2026-10-15**.

These 13 entries offer useful components or conceptual foundations. Their evaluation scope differs from the humanoid whole-body focus of the homepage. Placement here is a scope decision, not a quality ranking. Each entry links to its primary paper or official report; the boundary column explains the distinction.

<a id="real2sim"></a>

### Video Reconstruction & Simulation Assets

| Paper / series | Transferable idea | Scope boundary |
| :--- | :--- | :--- |
| [**USDCraft**](https://arxiv.org/abs/2610.11322)<br><sub>USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation</sub> | Programs and revises articulated simulation assets from partial geometry. | Useful asset infrastructure; does not itself establish whole-body humanoid control. |
| [**EgoInfinity**](https://arxiv.org/abs/2606.17385)<br><sub>EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning</sub> | Lifts internet videos to structured 4D hand–object trajectories for robot learning. | Hand–object and manipulator transfer; not equivalent to body–object contact and bipedal balance. |
| [**EgoEngine**](https://arxiv.org/abs/2606.12604)<br><sub>EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations</sub> | Produces aligned robot-view observations and executable actions from human video through a digital twin. | A useful video-to-robot data pipeline; whole-body humanoid transfer needs separate evidence. |

<a id="harness"></a>

### Execution Harnesses, Recovery & Training

| Paper / series | Transferable idea | Scope boundary |
| :--- | :--- | :--- |
| [**RoboICL**](https://arxiv.org/abs/2609.34261)<br><sub>RoboICL: Embodied In-Context Learning with GPT-6 Astra</sub> | Combines demonstration context and anchored interaction memory for frozen-model robot control. | RoboDojo manipulation evaluation; in-context adaptation is not persistent program or weight evolution. |
| [**Recova**](https://arxiv.org/abs/2610.01178)<br><sub>Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation</sub> | Develops task and recovery behaviors in a digital twin, then improves policies with physical experience. | Relevant to recovery and data collection; reported manipulation results do not establish humanoid locomotion and balance. |
| [**SGS**](https://arxiv.org/abs/2610.12465)<br><sub>A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control</sub> | Success Guided Sampling focuses training resets near the policy's current capability frontier. | An adaptive curriculum for simulated RL and transfer; not strict recursive self-improvement or a humanoid-specific method. |

<a id="foundations"></a>

### General Models & Learning Foundations

| Paper / series | Transferable idea | Scope boundary |
| :--- | :--- | :--- |
| [**Astranomy**](https://research.nvidia.com/labs/srl/projects/astranomy/)<br><sub>Astranomy: The study of GPT-6 Astra as a native robot policy</sub> | Studies direct, agentic, and orchestrated control interfaces for a general-purpose multimodal model. | Official research report/blog; RoboLab DROID-arm simulations do not establish humanoid whole-body control. |
| [**InternW0-Δ**](https://arxiv.org/abs/2609.31394)<br><sub>InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data</sub> | Couples visual dynamics and action prediction using action-relevant future-change representations. | Relevant world-action-model architecture; no blanket humanoid loco-manipulation claim. |
| [**Diffusion Policy**](https://diffusion-policy.cs.columbia.edu/)<br><sub>Diffusion Policy: Visuomotor Policy Learning via Action Diffusion</sub> | Learns action-sequence distributions with conditional diffusion. | General imitation-learning method and baseline, rather than a humanoid-specific controller. |
| [**Dreamer series**](https://danijar.com/project/dreamerv3/)<br><sub>Dreamer / DreamerV2 / DreamerV3</sub> | Learns policies through imagined trajectories in a learned latent world model. | General model-based RL background; task-specific humanoid evidence is still needed. |
| [**InterMimic**](https://arxiv.org/abs/2502.20390)<br><sub>InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions</sub> | Refines captured interactions with teacher policies and distills a generalist physics-based interaction controller. | The original CVPR paper primarily studies simulated human characters; later robot support should be distinguished from that evidence. |

<a id="rsi"></a>

### Program & Harness Self-Improvement

| Paper / series | Transferable idea | Scope boundary |
| :--- | :--- | :--- |
| [**PhysEvo**](https://arxiv.org/abs/2610.08995)<br><sub>PhysEvo: Astra Can Act, Let It</sub> | Uses a meta-agent to diagnose execution and persist tested revisions to tools, skills, and diagnostic tools. | Explicit physical RSI around frozen model weights; real deployment is demonstrated on a PiPER arm. |
| [**HarnessPAI**](https://arxiv.org/abs/2609.29166)<br><sub>HarnessPAI: An Evolving Harness for Physical AI</sub> | Revises executable task programs across rollouts and stores reusable repair skills while action backends stay frozen. | A transferable harness-evolution mechanism; it should not be presented as a humanoid whole-body policy. |

<a id="中文"></a>

## 中文

以下 13 项工作提供可借鉴的组件或基础方法，评测范围与主页的人形全身操作主线有所区别。放在此处是范围选择，不是质量排序；每项给出论文或官方报告及适用边界。

<a id="real2sim-zh"></a>

### 视频重建与仿真资产

| 论文 / 系列 | 可借鉴之处 | 收录边界 |
| :--- | :--- | :--- |
| [**USDCraft**](https://arxiv.org/abs/2610.11322)<br><sub>USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation</sub> | 根据局部几何编写并修订关节化仿真资产。 | 可用于资产构建，本身不构成全身人形控制方法。 |
| [**EgoInfinity**](https://arxiv.org/abs/2606.17385)<br><sub>EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning</sub> | 将互联网视频转为可用于机器人学习的结构化 4D 手物轨迹。 | 聚焦手物交互与机械臂迁移，尚不能等同于全身接触与双足平衡。 |
| [**EgoEngine**](https://arxiv.org/abs/2606.12604)<br><sub>EgoEngine: From Egocentric Human Videos to High-Fidelity Dexterous Robot Demonstrations</sub> | 借助数字孪生，将人类视频转为对齐的机器人观测与可执行动作。 | 可借鉴的视频到机器人数据管线，全身人形迁移需单独验证。 |

<a id="harness-zh"></a>

### 执行框架、故障恢复与训练

| 论文 / 系列 | 可借鉴之处 | 收录边界 |
| :--- | :--- | :--- |
| [**RoboICL**](https://arxiv.org/abs/2609.34261)<br><sub>RoboICL: Embodied In-Context Learning with GPT-6 Astra</sub> | 结合示范上下文与锚定交互记忆，实现冻结模型的机器人控制。 | 评测聚焦 RoboDojo 操作；上下文适应不等于程序或模型权重的持续演进。 |
| [**Recova**](https://arxiv.org/abs/2610.01178)<br><sub>Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation</sub> | 在数字孪生中开发任务与恢复行为，再利用真实执行经验改进策略。 | 与恢复及数据采集相关，操作实验本身不证明人形移动与平衡能力。 |
| [**SGS**](https://arxiv.org/abs/2610.12465)<br><sub>A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control</sub> | Success Guided Sampling 将训练重置采样集中到策略当前能力边界附近。 | 属于仿真强化学习的自适应课程与迁移方法，不作为严格 RSI 或人形专用方法。 |

<a id="foundations-zh"></a>

### 通用模型与学习基础

| 论文 / 系列 | 可借鉴之处 | 收录边界 |
| :--- | :--- | :--- |
| [**Astranomy**](https://research.nvidia.com/labs/srl/projects/astranomy/)<br><sub>Astranomy: The study of GPT-6 Astra as a native robot policy</sub> | 研究通用多模态模型的直接控制、智能体控制与策略编排接口。 | 官方研究报告／博客；RoboLab 中 DROID 机械臂仿真不等于人形全身控制。 |
| [**InternW0-Δ**](https://arxiv.org/abs/2609.31394)<br><sub>InternW0-Δ: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data</sub> | 通过与动作相关的未来变化表示，耦合视觉动态与动作预测。 | 可借鉴世界动作模型结构，不泛化为已验证的人形移动操作能力。 |
| [**Diffusion Policy**](https://diffusion-policy.cs.columbia.edu/)<br><sub>Diffusion Policy: Visuomotor Policy Learning via Action Diffusion</sub> | 使用条件扩散学习动作序列分布。 | 通用模仿学习方法与基线，非人形专用控制器。 |
| [**Dreamer series**](https://danijar.com/project/dreamerv3/)<br><sub>Dreamer / DreamerV2 / DreamerV3</sub> | 在学得的潜在世界模型中通过想象轨迹学习策略。 | 通用基于模型的强化学习背景，人形应用仍需专门实验。 |
| [**InterMimic**](https://arxiv.org/abs/2502.20390)<br><sub>InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions</sub> | 通过教师策略修正交互动作，并蒸馏通用物理交互控制器。 | 原 CVPR 论文主要研究仿真人体角色，应区分这些结果与后续机器人支持。 |

<a id="rsi-zh"></a>

### 程序与执行框架的自我改进

| 论文 / 系列 | 可借鉴之处 | 收录边界 |
| :--- | :--- | :--- |
| [**PhysEvo**](https://arxiv.org/abs/2610.08995)<br><sub>PhysEvo: Astra Can Act, Let It</sub> | 由元智能体诊断执行，并保存经过测试的工具、技能及诊断工具修订。 | 围绕冻结模型权重进行明确的物理 RSI；真机演示使用 PiPER 机械臂。 |
| [**HarnessPAI**](https://arxiv.org/abs/2609.29166)<br><sub>HarnessPAI: An Evolving Harness for Physical AI</sub> | 在动作后端冻结时跨轮次修订任务程序，并保存可复用的修复技能。 | 可迁移的执行框架演进机制，不应表述为人形全身策略。 |

## Reading notes / 阅读提示

- **Feedback ≠ RSI:** RoboICL uses within-rollout context; SGS changes the training distribution; HarnessPAI and PhysEvo retain validated program or tool revisions across rollouts. / 回合内记忆、自适应课程与跨轮次程序演进应分别描述。
- **Report ≠ peer-reviewed paper:** Astranomy is linked as an official research report/blog. / Astranomy 按官方研究报告／博客收录，不标注未经核实的论文发表信息。
- **Simulation ≠ hardware:** human avatars, arm benchmarks, and whole-body humanoid deployment provide different evidence. / 仿真人体、机械臂基准与人形全身真机部署提供不同层次的证据。

See [source notes](SOURCES.md) for selection and release details. / 更多核对细节见 [来源说明](SOURCES.md)。
