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

Humanoid loco-manipulation coordinates **locomotion, balance, and manipulation**. This list organizes **17 core works** across five directions, each listed once by its primary contribution. A separate [13-entry related reading list](docs/RELATED_READING.md) explains relevant methods from robot arms, simulated humans, and general learning.

**Scope:** direct contributions to humanoid whole-body manipulation, contact interaction, retargeting, training and transfer, or execution systems. Papers and project reports are distinguished; category assignments are editorial judgments.

**Last checked: 2026-10-15.** Dates are first public release months, with independently verified venues recorded separately—not reading dates. Resource links do not promise a complete implementation; see [source and selection notes](docs/SOURCES.md).

**Contents**

- [Real2Sim](#real2sim)
  - [Contact-Preserving Motion Retargeting](#motion-retargeting)
- [Harness & Real2Sim2Real](#harness-real2sim2real)
  - [Simulation Data Generation & Policy Transfer](#simulation-policy-transfer)
  - [Agentic Skill Orchestration](#agentic-skill-orchestration)
- [Interaction](#interaction)
  - [Whole-Body Interaction from Demonstrations](#human-object-interaction)
  - [Contact & Force Control](#contact-force-control)
- [Foundations](#foundations)
  - [Whole-Body Action Models](#whole-body-action-models)
  - [Generalist Whole-Body Control](#generalist-whole-body-control)
- [RSI](#rsi)
  - [Execution-Guided Data & Policy Improvement](#self-evolving-data-engines)

<a id="real2sim"></a>

## Real2Sim

Reconstruct and retarget real demonstrations into robot-compatible motion and interaction references.

<a id="motion-retargeting"></a>

### Contact-Preserving Motion Retargeting

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**OTRetarget**](https://arxiv.org/abs/2609.36602)<br><sub>OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport</sub> | 2026-09<br><sub>arXiv</sub> | Human–object demonstrations → joint robot–object references | Transfers surface interactions with optimal transport and jointly optimizes robot and object poses to preserve contacts across embodiments. | [Paper](https://arxiv.org/abs/2609.36602) |
| [**OmniRetarget**](https://arxiv.org/abs/2509.26633)<br><sub>OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction</sub> | 2025-09<br><sub>ICRA 2026</sub> | HOI motion capture → interaction-preserving references | Preserves agent–object–terrain relationships with interaction meshes for motion retargeting and augmentation. | [Paper](https://arxiv.org/abs/2509.26633) · [Project](https://omniretarget.github.io/) · [Code](https://github.com/amazon-far/holosoma) · [Data](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) |

[Related video reconstruction and asset methods](docs/RELATED_READING.md#real2sim): EgoInfinity, EgoEngine, USDCraft.


<a id="harness-real2sim2real"></a>

## Harness & Real2Sim2Real

Build simulation data and transfer workflows, or connect perception, memory, skills, and execution feedback into a working humanoid system.

<a id="simulation-policy-transfer"></a>

### Simulation Data Generation & Policy Transfer

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**PRISM**](https://arxiv.org/abs/2609.38172)<br><sub>Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | A few real videos → augmented data → real-robot policy | Generates counterfactual interaction videos, reconstructs contact-anchored references, and trains policies for real humanoid object carrying. | [Paper](https://arxiv.org/abs/2609.38172) |
| [**GRAIL**](https://arxiv.org/abs/2606.05160)<br><sub>GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors</sub> | 2026-06<br><sub>CoRL 2026</sub> | 3D assets + video priors → humanoid training data | Synthesizes interactions in known virtual scenes, recovers metric 4D trajectories, and trains humanoid policies for sim-to-real deployment. | [Paper](https://arxiv.org/abs/2606.05160) · [Code](https://github.com/NVlabs/GRAIL) |
| [**HumanoidMimicGen**](https://arxiv.org/abs/2605.27724)<br><sub>HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning</sub> | 2026-05<br><sub>arXiv</sub> | Few robot demonstrations → diverse whole-body demonstrations | Combines demonstrated skill adaptation with locomotion and manipulation planning to generate humanoid demonstrations across layouts. | [Paper](https://arxiv.org/abs/2605.27724) · [Project](https://humanoidmimicgen.github.io/) · [Benchmark](https://github.com/NVlabs/humanoidmimicgen) |
| [**DemoHLM**](https://arxiv.org/abs/2510.11258)<br><sub>DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation</sub> | 2025-10<br><sub>arXiv</sub> | One simulated demonstration → synthetic training data | Expands one simulated demonstration into task data and learns visual manipulation above a whole-body controller for real-robot transfer. | [Paper](https://arxiv.org/abs/2510.11258) · [Project](https://beingbeyond.github.io/DemoHLM/) |

<a id="agentic-skill-orchestration"></a>

### Agentic Skill Orchestration

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HomeBody**](https://tml.stanford.edu/homebody/)<br><sub>HomeBody: A Humanoid That Explores, Remembers, and Acts on Its Own</sub> | 2026-09<br><sub>Project report</sub> | Spatial memory + skill library → long-horizon execution | Connects a VLM to navigation and manipulation skills, using spatial memory and execution outcomes to coordinate tasks on a G1. | [Report](https://tml.stanford.edu/homebody/) |

[Related execution and training methods](docs/RELATED_READING.md#harness): RoboICL, Recova, SGS.


<a id="interaction"></a>

## Interaction

Learn and control physical interactions between a humanoid, objects, and its environment, including body–hand coordination and force regulation.

<a id="human-object-interaction"></a>

### Whole-Body Interaction from Demonstrations

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**Weave**](https://arxiv.org/abs/2609.16683)<br><sub>Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions</sub> | 2026-09<br><sub>arXiv</sub> | Captured HOI → dexterous robot–object interaction | Combines contact-aware retargeting with a geometry-aware policy that coordinates body and finger joints to track robot–object references. | [Paper](https://arxiv.org/abs/2609.16683) · [Project](https://xiaohu-art.github.io/Weave/) |
| [**HumanX**](https://arxiv.org/abs/2602.02473)<br><sub>HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos</sub> | 2026-02<br><sub>CoRL 2026</sub> | Human video → augmented references → interaction skills | Pairs anchor-centric interaction synthesis with interaction-prioritized imitation to learn agile skills that transfer to a G1. | [Paper](https://arxiv.org/abs/2602.02473) · [Project](https://wyhuai.github.io/human-x/) |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | Monocular RGB video → whole-body interaction policy | Extracts human–object trajectories and learns interaction skills by jointly tracking robot and object states. | [Paper](https://arxiv.org/abs/2509.16757) · [Project](https://hdmi-humanoid.github.io/) · [Code](https://github.com/LeCAR-Lab/HDMI) |

<a id="contact-force-control"></a>

### Contact & Force Control

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**KPI**](https://arxiv.org/abs/2609.36151)<br><sub>KPI: A Promptable Kernel for Physical Interaction on Humanoids</sub> | 2026-09<br><sub>arXiv</sub> | Trajectory + interaction contract → adaptive contact control | Adapts arm impedance and references to tracking, compliance, and force-range requests while retaining the underlying whole-body tracker. | [Paper](https://arxiv.org/abs/2609.36151) · [Project](https://kpi-robot.github.io/) |


<a id="foundations"></a>

## Foundations

Reusable control interfaces and learned models with direct whole-body humanoid relevance. General arm policies and simulated-human foundations are in related reading.

<a id="whole-body-action-models"></a>

### Whole-Body Action Models

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**λ₀**](https://arxiv.org/abs/2610.00438)<br><sub>Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining</sub> | 2026-09<br><sub>arXiv</sub> | Egocentric body/hand data → whole-body VLA | Uses staged human-data pretraining and embodiment adaptation to learn a policy coordinating whole-body and hand actions. | [Paper](https://arxiv.org/abs/2610.00438) |
| [**MotionWAM**](https://arxiv.org/abs/2606.09215)<br><sub>MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | Egocentric video → unified whole-body motion tokens | Conditions a unified whole-body policy on video-world-model features to coordinate locomotion, torso, feet, and hands in real time. | [Paper](https://arxiv.org/abs/2606.09215) |

<a id="generalist-whole-body-control"></a>

### Generalist Whole-Body Control

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**ULTRA**](https://arxiv.org/abs/2603.03279)<br><sub>ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation</sub> | 2026-03<br><sub>IROS 2026</sub> | Motion references or sparse goals → whole-body control | Distills motion-tracking skills into a multimodal controller that also supports autonomous behavior from sparse goals and egocentric perception. | [Paper](https://arxiv.org/abs/2603.03279) |
| [**HOVER**](https://arxiv.org/abs/2410.21229)<br><sub>HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</sub> | 2024-10<br><sub>ICRA 2025</sub> | Multiple command spaces → one whole-body controller | Distills diverse control modes into one policy using kinematic motion imitation as a common basis. | [Paper](https://arxiv.org/abs/2410.21229) · [Project](https://hover-versatile-humanoid.github.io/) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858)<br><sub>OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</sub> | 2024-06<br><sub>CoRL 2024</sub> | Kinematic pose commands → whole-body teleoperation and learning | Provides a common pose interface and deployable whole-body controller for teleoperation and learning autonomous skills from demonstrations. | [Paper](https://arxiv.org/abs/2406.08858) · [Project](https://omni.human2humanoid.com/) |

[Related models and learning foundations](docs/RELATED_READING.md#foundations): Astranomy, InternW0-Δ, Diffusion Policy, Dreamer, InterMimic.


<a id="rsi"></a>

## RSI

Recursive Self-Improvement, used here for persistent feedback loops that improve later data, policies, or executable skills. One-shot data generation and ordinary within-rollout correction are not sufficient.

<a id="self-evolving-data-engines"></a>

### Execution-Guided Data & Policy Improvement

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimicGen**](https://arxiv.org/abs/2610.06850)<br><sub>InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</sub> | 2026-10<br><sub>arXiv</sub> | HOI references + execution results → expanded motions and tracker | Iteratively perturbs interaction references, fine-tunes a generalist tracker, and retains successful executions to seed the next round. | [Paper](https://arxiv.org/abs/2610.06850) · [Project](https://sirui-xu.github.io/InterMimicGen/) |

[Related program and harness evolution](docs/RELATED_READING.md#rsi): HarnessPAI and PhysEvo. These offer transferable mechanisms, with evaluation scopes distinct from humanoid whole-body control.

---

**More resources:** [Related methods and foundations](docs/RELATED_READING.md) · [Historical data-engine list (2026-10-08)](docs/DATA_ENGINE_READING_LIST.md) · [Contributing](CONTRIBUTING.md) · [Topic template](docs/TOPIC_TEMPLATE.md).

**Inspired by:** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation).

**License:** Original curation text and assets use the [MIT License](LICENSE). Linked research and resources retain their respective licenses.
