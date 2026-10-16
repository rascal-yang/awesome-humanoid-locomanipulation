<p align="center">
  <img src="assets/banner.svg" alt="Human demonstrations, whole-body motion, and humanoid interaction" width="100%">
</p>

<h1 align="center">Awesome-Humanoid-Locomanipulation</h1>

<p align="center">
  <strong>A focused reading list for humanoid whole-body manipulation and interaction.</strong>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Loco--Manipulation-087f8c?style=flat-square" alt="Focus: Loco-Manipulation">
  <img src="https://img.shields.io/badge/Core_entries-17-4263eb?style=flat-square" alt="17 core entries">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

Humanoid loco-manipulation coordinates **locomotion, balance, and manipulation**. This list organizes **17 core works** across six directions, with a primary entry for each work and cross-links for overlapping contributions. A separate [13-entry related reading list](docs/RELATED_READING.md) explains relevant methods from robot arms, simulated humans, and general learning.

**Scope:** direct contributions to humanoid whole-body manipulation, contact interaction, retargeting, training and transfer, or execution systems. Papers and project reports are distinguished; category assignments are editorial judgments.

**Classification checked: 2026-10-16.** Dates are first public release months, with independently verified venues recorded separately—not reading dates. Resource links do not promise a complete implementation; see [source and selection notes](docs/SOURCES.md).

Subgroups describe a research question or data-generation route, and may contain a single work. Tags identify overlapping contributions without requiring a paper to fit one exclusive category.

**Contents**

- [Motion Retargeting](#retargeting)
  - [Contact-Preserving Retargeting](#motion-retargeting)
- [Data Generation & Policy Learning](#data-generation-policy-learning)
  - [Video Augmentation & Real2Sim2Real](#video-augmentation-real2sim2real)
  - [Interaction Synthesis from 3D Assets & Video Priors](#asset-video-interaction-synthesis)
  - [Demonstration Expansion in Simulation](#simulation-demonstration-expansion)
- [Interaction](#interaction)
  - [Interaction Learning from Human Videos](#interaction-learning-from-human-videos)
  - [Dexterous Whole-Body Interaction](#dexterous-whole-body-interaction)
  - [Contact & Force Control](#contact-force-control)
- [Foundations](#foundations)
  - [Whole-Body VLA & Human-Data Pretraining](#whole-body-vla-human-pretraining)
  - [World-Model-Conditioned Whole-Body Policies](#world-model-conditioned-policies)
  - [Generalist Whole-Body Control](#generalist-whole-body-control)
- [Systems](#systems)
  - [Spatial Memory & Long-Horizon Skill Orchestration](#spatial-memory-skill-orchestration)
- [Iterative Improvement](#iterative-improvement)
  - [Execution-Guided Data–Policy Co-Improvement](#execution-guided-data-policy-co-improvement)

<a id="retargeting"></a>
<a id="real2sim"></a>

## Motion Retargeting

Adapt human motion and interaction geometry to robot embodiments, producing references for downstream learning and control.

<a id="motion-retargeting"></a>
<a id="contact-preserving-motion-retargeting"></a>
<a id="接触保持的动作重定向"></a>

### Contact-Preserving Retargeting

Preserve robot–object and environment contacts while adapting demonstrated motion across embodiments.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**OTRetarget**](https://arxiv.org/abs/2609.36602)<br><sub>OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport</sub> | 2026-09<br><sub>arXiv</sub> | Human–object demonstrations → joint robot–object references | Transfers surface interactions with optimal transport and jointly optimizes robot and object poses to preserve contacts across embodiments.<br><sub>Tags: Contact preservation · Joint robot–object optimization</sub> | [Paper](https://arxiv.org/abs/2609.36602) |
| [**OmniRetarget**](https://arxiv.org/abs/2509.26633)<br><sub>OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction</sub> | 2025-09<br><sub>ICRA 2026</sub> | HOI motion capture → interaction-preserving references | Preserves agent–object–terrain relationships with interaction meshes for motion retargeting and augmentation.<br><sub>Tags: Contact preservation · Motion augmentation</sub> | [Paper](https://arxiv.org/abs/2509.26633) · [Project](https://omniretarget.github.io/) · [Code](https://github.com/amazon-far/holosoma) · [Data](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) |

**Across directions:** [HumanX and HDMI](#interaction-learning-from-human-videos) recover interaction references from video; [Weave](#dexterous-whole-body-interaction) and [InterMimicGen](#execution-guided-data-policy-co-improvement) also use contact-aware retargeting.

[Related video reconstruction and asset methods](docs/RELATED_READING.md#real2sim): EgoInfinity, EgoEngine, USDCraft.

<a id="data-generation-policy-learning"></a>
<a id="harness-real2sim2real"></a>
<a id="harness--real2sim2real"></a>
<a id="simulation-policy-transfer"></a>
<a id="simulation-data-generation--policy-transfer"></a>
<a id="仿真数据生成与策略迁移"></a>

## Data Generation & Policy Learning

Organize data-generation methods by their source and mechanism. Real-video reconstruction, fully virtual synthesis, and simulation-demonstration expansion are distinct routes; real-data co-training does not by itself imply Real2Sim.

<a id="video-augmentation-real2sim2real"></a>

### Video Augmentation & Real2Sim2Real

Expand real interaction videos, reconstruct robot-compatible references, and transfer the resulting policies to real robots.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**PRISM**](https://arxiv.org/abs/2609.38172)<br><sub>Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | A few real videos → augmented data → real-robot policy | Generates counterfactual interaction videos, reconstructs contact-anchored references, and trains policies for real humanoid object carrying.<br><sub>Tags: Video generation · Real2Sim2Real</sub> | [Paper](https://arxiv.org/abs/2609.38172) |

<a id="asset-video-interaction-synthesis"></a>

### Interaction Synthesis from 3D Assets & Video Priors

Start from specified virtual assets and scenes, then use video priors to synthesize interactions for robot learning.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**GRAIL**](https://arxiv.org/abs/2606.05160)<br><sub>GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors</sub> | 2026-06<br><sub>CoRL 2026</sub> | 3D assets + video priors → humanoid training data | Synthesizes interactions in known virtual scenes, recovers metric 4D trajectories, and trains humanoid policies for sim-to-real deployment.<br><sub>Tags: 3D assets · Video priors · Sim-to-real</sub> | [Paper](https://arxiv.org/abs/2606.05160) · [Code](https://github.com/NVlabs/GRAIL) |

<a id="simulation-demonstration-expansion"></a>

### Demonstration Expansion in Simulation

Adapt a small set of simulated robot demonstrations into larger datasets. Deployment may use sim-to-real transfer or sim-and-real co-training.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanoidMimicGen**](https://arxiv.org/abs/2605.27724)<br><sub>HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning</sub> | 2026-05<br><sub>arXiv</sub> | Simulated robot demonstrations → expanded simulation data → sim-and-real co-training | Expands simulated demonstrations through skill adaptation and whole-body planning, then co-trains policies with real demonstrations for real-robot evaluation.<br><sub>Tags: Simulation data · Whole-body planning · Sim-and-real co-training</sub> | [Paper](https://arxiv.org/abs/2605.27724) · [Project](https://humanoidmimicgen.github.io/) · [Benchmark](https://github.com/NVlabs/humanoidmimicgen) |
| [**DemoHLM**](https://arxiv.org/abs/2510.11258)<br><sub>DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation</sub> | 2025-10<br><sub>arXiv</sub> | One simulated demonstration → synthetic training data | Expands one simulated demonstration into task data and learns visual manipulation above a whole-body controller for real-robot transfer.<br><sub>Tags: Simulation data · Demonstration expansion · Sim-to-real</sub> | [Paper](https://arxiv.org/abs/2510.11258) · [Project](https://beingbeyond.github.io/DemoHLM/) |

**Across directions:** [HumanX](#interaction-learning-from-human-videos) also augments interaction data; [InterMimicGen](#execution-guided-data-policy-co-improvement) couples augmentation to repeated execution and tracker updates. For execution-system integration, see [Systems](#systems).

<a id="interaction"></a>

## Interaction

Learn and control physical interactions between a humanoid, objects, and its environment, including body–hand coordination and force regulation.

<a id="interaction-learning-from-human-videos"></a>
<a id="human-object-interaction"></a>
<a id="whole-body-interaction-from-demonstrations"></a>
<a id="从示教学习全身交互"></a>

### Interaction Learning from Human Videos

Recover human–object interaction references from video and learn policies that execute those interactions. For captured demonstrations with dexterous hand coordination, see [Dexterous Whole-Body Interaction](#dexterous-whole-body-interaction).

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanX**](https://arxiv.org/abs/2602.02473)<br><sub>HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos</sub> | 2026-02<br><sub>CoRL 2026</sub> | Human video → augmented references → interaction skills | Pairs anchor-centric interaction synthesis with interaction-prioritized imitation to learn agile skills that transfer to a G1.<br><sub>Tags: Video reconstruction · Data augmentation · Interaction learning</sub> | [Paper](https://arxiv.org/abs/2602.02473) · [Project](https://wyhuai.github.io/human-x/) |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | Monocular RGB video → whole-body interaction policy | Extracts human–object trajectories and learns interaction skills by jointly tracking robot and object states.<br><sub>Tags: Video reconstruction · Interaction imitation · Sim-to-real</sub> | [Paper](https://arxiv.org/abs/2509.16757) · [Project](https://hdmi-humanoid.github.io/) · [Code](https://github.com/LeCAR-Lab/HDMI) |

<a id="dexterous-whole-body-interaction"></a>

### Dexterous Whole-Body Interaction

Coordinate whole-body motion and dexterous hand contacts when learning interactions from captured demonstrations.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**Weave**](https://arxiv.org/abs/2609.16683)<br><sub>Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions</sub> | 2026-09<br><sub>arXiv</sub> | Captured HOI → dexterous robot–object interaction | Combines contact-aware retargeting with a geometry-aware policy that coordinates body and finger joints to track robot–object references.<br><sub>Tags: HOI motion capture · Dexterous hands · Contact-aware retargeting</sub> | [Paper](https://arxiv.org/abs/2609.16683) · [Project](https://xiaohu-art.github.io/Weave/) |

<a id="contact-force-control"></a>

### Contact & Force Control

Regulate compliance and contact forces during execution, beyond following a motion trajectory.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**KPI**](https://arxiv.org/abs/2609.36151)<br><sub>KPI: A Promptable Kernel for Physical Interaction on Humanoids</sub> | 2026-09<br><sub>arXiv</sub> | Trajectory + interaction contract → adaptive contact control | Adapts arm impedance and references to tracking, compliance, and force-range requests while retaining the underlying whole-body tracker.<br><sub>Tags: Impedance adaptation · Force regulation</sub> | [Paper](https://arxiv.org/abs/2609.36151) · [Project](https://kpi-robot.github.io/) |

**Across directions:** [PRISM](#video-augmentation-real2sim2real) and [GRAIL](#asset-video-interaction-synthesis) also learn interaction policies, with their main entries emphasizing data generation. [KPI](#contact-force-control) includes agent-driven trajectory and interaction-contract generation.

<a id="foundations"></a>

## Foundations

Reusable learned models and control interfaces with direct whole-body humanoid relevance. Separate human-data-pretrained VLAs, world-model-conditioned policies, and generalist motor controllers.

<a id="whole-body-vla-human-pretraining"></a>
<a id="whole-body-action-models"></a>
<a id="全身动作模型"></a>

### Whole-Body VLA & Human-Data Pretraining

Use human experience to pretrain whole-body vision-language-action policies and adapt them to robot embodiments. For the world-model-conditioned route, see [MotionWAM](#world-model-conditioned-policies).

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**λ₀**](https://arxiv.org/abs/2610.00438)<br><sub>Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining</sub> | 2026-09<br><sub>arXiv</sub> | Egocentric body/hand data → whole-body VLA | Uses staged human-data pretraining and embodiment adaptation to learn a policy coordinating whole-body and hand actions.<br><sub>Tags: VLA · Human-data pretraining · Embodiment adaptation</sub> | [Paper](https://arxiv.org/abs/2610.00438) |

<a id="world-model-conditioned-policies"></a>

### World-Model-Conditioned Whole-Body Policies

Condition coordinated whole-body action prediction on learned visual dynamics features.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**MotionWAM**](https://arxiv.org/abs/2606.09215)<br><sub>MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | Egocentric video → unified whole-body motion tokens | Conditions a unified whole-body policy on video-world-model features to coordinate locomotion, torso, feet, and hands in real time.<br><sub>Tags: Video world model · Unified whole-body actions</sub> | [Paper](https://arxiv.org/abs/2606.09215) |

<a id="generalist-whole-body-control"></a>

### Generalist Whole-Body Control

Provide reusable motor control across command interfaces, teleoperation, or task goals; the supported interfaces differ by method.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**ULTRA**](https://arxiv.org/abs/2603.03279)<br><sub>ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation</sub> | 2026-03<br><sub>IROS 2026</sub> | Motion references or sparse goals → whole-body control | Distills motion-tracking skills into a multimodal controller that also supports autonomous behavior from sparse goals and egocentric perception.<br><sub>Tags: Multimodal control · Sparse goals · Motion tracking</sub> | [Paper](https://arxiv.org/abs/2603.03279) |
| [**HOVER**](https://arxiv.org/abs/2410.21229)<br><sub>HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</sub> | 2024-10<br><sub>ICRA 2025</sub> | Multiple command spaces → one whole-body controller | Distills diverse control modes into one policy using kinematic motion imitation as a common basis.<br><sub>Tags: Multi-mode control · Policy distillation</sub> | [Paper](https://arxiv.org/abs/2410.21229) · [Project](https://hover-versatile-humanoid.github.io/) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858)<br><sub>OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</sub> | 2024-06<br><sub>CoRL 2024</sub> | Kinematic pose commands → whole-body teleoperation and learning | Provides a common pose interface and deployable whole-body controller for teleoperation and learning autonomous skills from demonstrations.<br><sub>Tags: Teleoperation · Whole-body control · Imitation learning</sub> | [Paper](https://arxiv.org/abs/2406.08858) · [Project](https://omni.human2humanoid.com/) |

**Across directions:** [InterMimicGen](#execution-guided-data-policy-co-improvement) also trains a generalist interaction tracker, alongside its iterative data loop.

[Related models and learning foundations](docs/RELATED_READING.md#foundations): Astranomy, InternW0-Δ, Diffusion Policy, Dreamer, InterMimic.

<a id="systems"></a>

## Systems

Connect perception, memory, reusable skills, and execution feedback into a working humanoid system.

<a id="spatial-memory-skill-orchestration"></a>
<a id="agentic-skill-orchestration"></a>
<a id="智能体技能编排"></a>

### Spatial Memory & Long-Horizon Skill Orchestration

Use remembered spatial context and skill outcomes to plan and revise long-horizon execution.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HomeBody**](https://tml.stanford.edu/homebody/)<br><sub>HomeBody: A Humanoid That Explores, Remembers, and Acts on Its Own</sub> | 2026-09<br><sub>Project report</sub> | Spatial memory + skill library → long-horizon execution | Connects a VLM to navigation and manipulation skills, using spatial memory and execution outcomes to coordinate tasks on a G1.<br><sub>Tags: Spatial memory · Skill orchestration · Execution feedback</sub> | [Report](https://tml.stanford.edu/homebody/) |

**Across directions:** [OmniH2O](#generalist-whole-body-control) connects teleoperation and skill learning; [KPI](#contact-force-control) connects agent-generated references to contact regulation.

[Related execution and training methods](docs/RELATED_READING.md#harness): RoboICL, Recova, SGS.

<a id="iterative-improvement"></a>
<a id="rsi"></a>

## Iterative Improvement

Use persistent execution feedback to improve later data or policies. Describe the object and mechanism of improvement explicitly; an iterative data flywheel does not establish unrestricted recursive self-improvement (RSI).

<a id="execution-guided-data-policy-co-improvement"></a>
<a id="self-evolving-data-engines"></a>
<a id="execution-guided-data--policy-improvement"></a>
<a id="执行反馈驱动的数据与策略改进"></a>

### Execution-Guided Data–Policy Co-Improvement

Retain successful executions to seed further data augmentation and tracking-policy updates across rounds.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimicGen**](https://arxiv.org/abs/2610.06850)<br><sub>InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</sub> | 2026-10<br><sub>arXiv</sub> | HOI references + execution results → expanded motions and tracker | Iteratively perturbs interaction references, fine-tunes a generalist tracker, and retains successful executions to seed the next round.<br><sub>Tags: Contact-aware retargeting · Generalist tracking · Iterative augmentation</sub> | [Paper](https://arxiv.org/abs/2610.06850) · [Project](https://sirui-xu.github.io/InterMimicGen/) |

[Related program and harness evolution](docs/RELATED_READING.md#rsi): HarnessPAI and PhysEvo. These offer transferable mechanisms, with evaluation scopes distinct from humanoid whole-body control.

---

**More resources:** [Related methods and foundations](docs/RELATED_READING.md) · [Historical data-engine list (2026-10-08)](docs/DATA_ENGINE_READING_LIST.md) · [Contributing](CONTRIBUTING.md) · [Topic template](docs/TOPIC_TEMPLATE.md).

**Inspired by:** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation).

**License:** Original curation text and assets use the [MIT License](LICENSE). Linked research and resources retain their respective licenses.
