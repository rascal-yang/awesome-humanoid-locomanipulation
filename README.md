<a id="top"></a>

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
  <img src="https://img.shields.io/badge/Core_entries-127-4263eb?style=flat-square" alt="127 core entries">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

Humanoid loco-manipulation coordinates **locomotion, balance, and manipulation**. This list organizes **127 core works** across seven directions, with a primary entry for each work and cross-links for overlapping contributions. A separate [13-entry related reading list](docs/RELATED_READING.md) explains relevant methods from robot arms, simulated humans, and general learning.

**Scope:** direct contributions to humanoid whole-body manipulation, contact interaction, retargeting, training and transfer, or execution systems. Papers and project reports are distinguished; category assignments are editorial judgments.

**Classification checked: 2026-10-16.** Dates are first public release months, with independently verified venues recorded separately—not reading dates. Resource links do not promise a complete implementation; see [source and selection notes](docs/SOURCES.md).

**Latest additions: 2026-10-27 (MOTIO; see [scope and evidence](docs/SOURCES.md#motio-addition-2026-10-27)).**

H2 sections describe broad research directions, technical routes, or system paradigms; H3 subgroups describe concrete methods within them and may contain a single work. Cross-links and tags identify overlapping contributions.

<p align="center">
  <img src="assets/paper-growth.svg?v=20261027-127" alt="Cumulative core works by first public release, with five curves and the three simulation routes combined" width="100%">
</p>

<sub>Growth of the curated reading list by first public release month; includes papers and reports. The blue Simulation & Transfer curve combines Real2Sim, Real2Sim2Real, and Sim2Real & Sim–Real Co-Training; the seven README categories remain separate. [Monthly data by H2](docs/paper-growth.csv) · [Counting and automatic updates](docs/CHART.md).</sub>

**Fixed H2 structure:** Keep the names, order, and heading levels of these seven H2 sections unchanged: **Real2Sim**, **Real2Sim2Real**, **Sim2Real & Sim–Real Co-Training**, **Interaction**, **Foundations**, **Harness**, and **Iterative Improvement**. Add or refine H3 subgroups, move paper entries, and use cross-links and tags within this structure. Changes to H2 sections require an explicit maintainer request.

**Contents**

- [Real2Sim](#real2sim)
  - [Contact-Preserving Motion Retargeting](#motion-retargeting)
  - [Controller-Aware Demonstration Alignment](#controller-aware-demonstration-alignment)
- [Real2Sim2Real](#real2sim2real)
  - [Contact-Consistent Actuator Modeling](#contact-consistent-actuator-modeling)
  - [Counterfactual Video Augmentation](#counterfactual-video-augmentation)
  - [Scene Reconstruction & Synthetic Demonstrations](#scene-reconstruction-synthetic-demonstrations)
- [Sim2Real & Sim–Real Co-Training](#sim2real-co-training)
  - [Asset- and Video-Prior-Based Interaction Synthesis](#asset-video-interaction-synthesis)
  - [Demonstration Expansion in Simulation](#simulation-demonstration-expansion)
  - [Visual Policy Learning & Evaluation](#visual-policy-learning-evaluation)
  - [Whole-Body Policy Transfer](#whole-body-policy-transfer)
- [Interaction](#interaction)
  - [Interaction Learning from Human Demonstrations](#interaction-learning-from-human-videos)
  - [Dexterous Whole-Body Interaction](#dexterous-whole-body-interaction)
  - [Contact & Force Control](#contact-force-control)
  - [Tactile-Guided Whole-Body Manipulation](#tactile-guided-manipulation)
  - [Multi-Humanoid Coordination](#multi-humanoid-coordination)
  - [Whole-Body Planning & Skill Learning](#whole-body-planning-skill-learning)
- [Foundations](#foundations)
  - [Test-Time Command Optimization](#test-time-command-optimization)
  - [Whole-Body VLA & Human-Data Pretraining](#whole-body-vla-human-pretraining)
  - [World-Model-Conditioned Whole-Body Policies](#world-model-conditioned-policies)
  - [Generalist Whole-Body Control](#generalist-whole-body-control)
  - [Humanoid Simulation Benchmarks](#humanoid-simulation-benchmarks)
- [Harness](#harness)
  - [Spatial Memory & Long-Horizon Skill Orchestration](#spatial-memory-skill-orchestration)
  - [Whole-Body Teleoperation & Data Collection](#whole-body-teleoperation-data)
  - [Execution Monitoring & Recovery](#object-memory-execution-verification)
  - [Planning & Control Interfaces](#planning-control-interfaces)
- [Iterative Improvement](#iterative-improvement)
  - [Execution-Guided Data–Policy Co-Improvement](#execution-guided-data-policy-co-improvement)
  - [Execution-Guided Program Refinement](#execution-guided-reward-program-evolution)
  - [Skill Reuse & Memory Consolidation](#skill-reuse-memory-consolidation)
  - [Policy Improvement from Human Interventions](#human-intervention-policy-improvement)
  - [Planner & Policy Post-Training](#planner-policy-post-training)

<a id="retargeting"></a>
<a id="motion-retargeting动作重定向"></a>
<a id="real2sim"></a>

## Real2Sim

Adapt human motion, interaction geometry, and observations to robot embodiments, producing aligned references for downstream learning and control.

<a id="motion-retargeting"></a>
<a id="contact-preserving-retargeting"></a>
<a id="接触保持的重定向"></a>
<a id="contact-preserving-motion-retargeting"></a>
<a id="接触保持的动作重定向"></a>

### Contact-Preserving Motion Retargeting

Preserve robot–object and environment contacts while adapting demonstrated motion across embodiments.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**CoCarry**](https://arxiv.org/abs/2610.32460)<br><sub>CoCarry: Contact-Support-Structured Retargeting for Dual-Humanoid Cooperative Carrying</sub> | 2026-10<br><sub>arXiv</sub> | Synchronized two-person carrying demonstrations → coordinated dual-humanoid references | Jointly retargets both humanoids using shared-object hand anchors and contact-support structure, with A3/G1 reference evaluation and cooperative carrying in simulation and on two real A3 robots. | [Paper](https://arxiv.org/abs/2610.32460) |
| [**STR / STRL**](https://arxiv.org/abs/2610.30540)<br><sub>Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Human-object demonstrations → contact-preserving robot references and tracking policies | Allocates retargeting effort by keyframes and body parts, refines contact anchors with an object-wrench approximation, and trains stage-aware interaction policies; evaluated on simulated G1 and real R1 box carrying. | [Paper](https://arxiv.org/abs/2610.30540) |
| [**FRDV**](https://arxiv.org/abs/2610.28470)<br><sub>Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning</sub> | 2026-10<br><sub>arXiv</sub> | Human motion and humanoid constraints → retargeted and optionally dynamics-refined references | Combines constrained inverse kinematics with optional contact-implicit iLQR refinement to address foot floating and sliding, with motion tracking transferred to a real G1. | [Paper](https://arxiv.org/abs/2610.28470) |
| [**PriMoRetarget**](https://arxiv.org/abs/2610.12642)<br><sub>PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting</sub> | 2026-10<br><sub>arXiv</sub> | Human motion and interaction demonstrations → humanoid reference trajectories | Uses an explicit objective hierarchy and gradient projection to preserve foot placement and interaction contacts while optimizing lower-priority pose objectives.<br><sub>Tags: Prioritized optimization · Contact preservation · Multi-character interactions</sub> | [Paper](https://arxiv.org/abs/2610.12642) · [Project](https://nickioan.github.io/primoretarget-page/) |
| [**OTRetarget**](https://arxiv.org/abs/2609.36602)<br><sub>OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport</sub> | 2026-09<br><sub>arXiv</sub> | Human–object demonstrations → joint robot–object references | Transfers surface interactions with optimal transport and jointly optimizes robot and object poses to preserve contacts across embodiments.<br><sub>Tags: Contact preservation · Joint robot–object optimization</sub> | [Paper](https://arxiv.org/abs/2609.36602) |
| [**HOI-Retarget**](https://arxiv.org/abs/2609.34674)<br><sub>HOI-Retarget: Contact-Centric Retargeting for Human-Object Interaction</sub> | 2026-09<br><sub>arXiv</sub> | HOI motion and object-frame contact labels → humanoid interaction references | Uses windowed trajectory optimization to preserve object-frame contacts under humanoid kinematic limits while balancing body tracking, foot support, and smoothness.<br><sub>Tags: Object-frame contacts · Trajectory optimization · Motion augmentation</sub> | [Paper](https://arxiv.org/abs/2609.34674) · [Project](https://shinben0327.github.io/hoi-retarget/) |
| [**UMR**](https://arxiv.org/abs/2609.02134)<br><sub>Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence</sub> | 2026-09<br><sub>arXiv</sub> | Human surface motion and contact maps → humanoid reference motion | Learns dense human–robot surface correspondences and reuses them for constrained pose matching and contact-map transfer across motion sources.<br><sub>Tags: Dense correspondence · Surface matching · Contact transfer</sub> | [Paper](https://arxiv.org/abs/2609.02134) |
| [**SPIDER**](https://arxiv.org/abs/2511.09484)<br><sub>SPIDER: Scalable Physics-Informed Dexterous Retargeting</sub> | 2025-11<br><sub>arXiv</sub> | Kinematic human demonstrations and robot physics → dynamically feasible humanoid motion and interaction references | Uses sampling-based physics optimization to correct contact and motion artifacts, with retargeting across humanoid embodiments and simulated box pickup, transport, and placement policy training. | [Paper](https://arxiv.org/abs/2511.09484) · [Project](https://facebookresearch.github.io/spider/) |
| [**OmniRetarget**](https://arxiv.org/abs/2509.26633)<br><sub>OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction</sub> | 2025-09<br><sub>ICRA 2026</sub> | HOI motion capture → interaction-preserving references | Preserves agent–object–terrain relationships with interaction meshes for motion retargeting and augmentation.<br><sub>Tags: Contact preservation · Motion augmentation</sub> | [Paper](https://arxiv.org/abs/2509.26633) · [Project](https://omniretarget.github.io/) · [Code](https://github.com/amazon-far/holosoma) · [Data](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) |

**Across directions:** [HumanX and HDMI](#interaction-learning-from-human-videos) recover interaction references from video; [Weave](#dexterous-whole-body-interaction) and [InterMimicGen](#execution-guided-data-policy-co-improvement) also use contact-aware retargeting.

[Related video reconstruction and asset methods](docs/RELATED_READING.md#real2sim): EgoInfinity, EgoEngine, USDCraft.

<a id="controller-aware-demonstration-alignment"></a>

### Controller-Aware Demonstration Alignment

**Scope.** Convert human observations into aligned robot motion, onboard views, and controller-specific action supervision.

**Reading guide.** KODA preserves a reusable motion/view record; [TTCO](#test-time-command-optimization) provides the related command-optimization perspective.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**KODA**](https://arxiv.org/abs/2610.21152)<br><sub>KODA: Kinematics--Observation Data Alignment for Humanoid Learning from Human Egocentric Demonstration</sub> | 2026-10<br><sub>arXiv</sub> | Egocentric human RGB → canonical robot motion/views → controller-specific action labels | Aligns synthesized onboard views with simulator-checked motion and regenerates action supervision for each controller through command optimization.<br><sub>Tags: View–motion alignment · Command optimization · Demonstration relabeling</sub> | [Paper](https://arxiv.org/abs/2610.21152) |
| [**EgoHumanoid-V2**](https://arxiv.org/abs/2609.37181)<br><sub>EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | Human demonstrations → controller-aligned robot observations and actions | Aligns demonstrated motion through controller rollouts, dynamics-aware correction, and rendered robot views to learn coordinated G1 skills without target-task robot demonstrations. | [Paper](https://arxiv.org/abs/2609.37181) |
| [**TrajBooster**](https://arxiv.org/abs/2509.11839)<br><sub>TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning</sub> | 2025-09<br><sub>arXiv</sub> | Source robot trajectories → G1 action supervision and VLA | Retargets source end-effector trajectories through G1 simulation control and combines aligned data with limited target demonstrations for whole-body deployment. | [Paper](https://arxiv.org/abs/2509.11839) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="real2sim2real"></a>
<a id="data-generation-policy-learning"></a>
<a id="data-generation--policy-learning"></a>
<a id="data-generation--policy-learning数据生成与策略学习"></a>
<a id="harness-real2sim2real"></a>
<a id="harness--real2sim2real"></a>
<a id="simulation-policy-transfer"></a>
<a id="simulation-data-generation--policy-transfer"></a>
<a id="仿真数据生成与策略迁移"></a>

## Real2Sim2Real

Use real demonstrations or observations to construct simulation references or calibrate simulation dynamics, train policies in simulation, and deploy them back to real robots. Data generation and simulator correction are distinct components of this route.

**Other routes:** virtual-source training and mixed-data deployment are under [Sim2Real & Sim–Real Co-Training](#sim2real-co-training); execution-system integration is under [Harness](#harness).

<a id="contact-consistent-actuator-modeling"></a>

### Contact-Consistent Actuator Modeling

**Scope.** Use real humanoid trajectories to correct contact initialization and actuator dynamics in simulation, then train policies for hardware deployment.

**Reading guide.** Contact-UAN supports force-sensitive control transfer; it is distinct from object-task planning and visual world-action models.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**Contact-UAN**](https://arxiv.org/abs/2610.18991)<br><sub>Contact-UAN: Unsupervised Actuator Networks as a Residual World Model for Humanoid Control</sub> | 2026-10<br><sub>arXiv</sub> | Real G1 proprioceptive trajectories → corrected simulator → deployable control policies | Initializes hardware replay with consistent contacts and learns actuator residuals, then trains policies in the corrected simulator for force-sensitive humanoid control.<br><sub>Tags: Actuator modeling · Contact-consistent replay · Real2Sim2Real</sub> | [Paper](https://arxiv.org/abs/2610.18991) · [Project](https://contact-uan.csail.mit.edu/) |

<a id="counterfactual-video-augmentation"></a>
<a id="video-augmentation-real2sim2real"></a>
<a id="video-augmentation--real2sim2real"></a>
<a id="视频扩增与虚实迁移"></a>

### Counterfactual Video Augmentation

Expand real interaction videos, reconstruct robot-compatible references, and transfer the resulting policies to real robots.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**PRISM**](https://arxiv.org/abs/2609.38172)<br><sub>Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | A few real videos → augmented data → real-robot policy | Generates counterfactual interaction videos, reconstructs contact-anchored references, and trains policies for real humanoid object carrying.<br><sub>Tags: Video generation · Real2Sim2Real</sub> | [Paper](https://arxiv.org/abs/2609.38172) |

<a id="scene-reconstruction-synthetic-demonstrations"></a>

### Scene Reconstruction & Synthetic Demonstrations

**Scope.** Reconstruct deployment scenes, generate demonstrations in the resulting simulator, and train policies for real humanoids.

**Reading guide.** LEGS reconstructs scene appearance; Contact-UAN above instead corrects actuator dynamics.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**VLK**](https://arxiv.org/abs/2606.30645)<br><sub>VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes</sub> | 2026-06<br><sub>arXiv</sub> | Real scene capture → synthetic interactions → visual policy | Synthesizes interactions inside reconstructed deployment scenes and trains perception-based policies for navigation and object transport on a physical G1. | [Paper](https://arxiv.org/abs/2606.30645) |
| [**LEGS**](https://arxiv.org/abs/2606.01458)<br><sub>LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World</sub> | 2026-05<br><sub>arXiv</sub> | Real scene captures → calibrated 3DGS simulator → synthetic VLA demonstrations | Composites reconstructed backgrounds with dynamic mesh foregrounds and procedural motion demonstrations to fine-tune VLAs for real G1 tasks.<br><sub>Tags: Scene reconstruction · Gaussian splatting · Synthetic demonstrations</sub> | [Paper](https://arxiv.org/abs/2606.01458) · [Project](https://hojjunekim.github.io/legs/) |
| [**DexMimicGen**](https://arxiv.org/abs/2410.24185)<br><sub>DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning</sub> | 2024-10<br><sub>arXiv</sub> | Real demonstrations and digital twin → generated robot demonstrations | Expands demonstrations in simulation and validates digital-twin-assisted data collection and policy learning on Fourier GR1, alongside separate dual-arm experiments. | [Paper](https://arxiv.org/abs/2410.24185) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="sim2real-co-training"></a>
<a id="sim2real"></a>

## Sim2Real & Sim–Real Co-Training

Use simulation-generated data or simulation-trained policies for real-robot learning and deployment. GRAIL and DemoHLM report sim-to-real transfer; HumanoidMimicGen combines generated simulation data with real demonstrations for co-training.

<a id="asset-video-interaction-synthesis"></a>
<a id="interaction-synthesis-from-3d-assets--video-priors"></a>
<a id="基于资产与视频先验的交互合成"></a>

### Asset- and Video-Prior-Based Interaction Synthesis

Start from specified virtual assets and scenes, then use video priors to synthesize interactions for robot learning.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**KinoGen**](https://arxiv.org/abs/2610.20552)<br><sub>KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation</sub> | 2026-10<br><sub>arXiv</sub> | Calibrated robot/object renders and goal edits → humanoid interaction references | Generates two-view videos from robot-scene renders and fits robot/object models directly to recover customizable references for G1 tracking-policy learning.<br><sub>Tags: Video generation · Robot-native references · Goal customization</sub> | [Paper](https://arxiv.org/abs/2610.20552) · [Project](https://kinogen-humanoid.github.io/) |
| [**GRAIL**](https://arxiv.org/abs/2606.05160)<br><sub>GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors</sub> | 2026-06<br><sub>CoRL 2026</sub> | 3D assets + video priors → humanoid training data | Synthesizes interactions in known virtual scenes, recovers metric 4D trajectories, and trains humanoid policies for sim-to-real deployment.<br><sub>Tags: 3D assets · Video priors · Sim-to-real</sub> | [Paper](https://arxiv.org/abs/2606.05160) · [Code](https://github.com/NVlabs/GRAIL) |

<a id="simulation-demonstration-expansion"></a>

### Demonstration Expansion in Simulation

Adapt a small set of simulated robot demonstrations into larger datasets. Deployment may use sim-to-real transfer or sim-and-real co-training.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanoidMimicGen**](https://arxiv.org/abs/2605.27724)<br><sub>HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning</sub> | 2026-05<br><sub>arXiv</sub> | Simulated robot demonstrations → expanded simulation data → sim-and-real co-training | Expands simulated demonstrations through skill adaptation and whole-body planning, then co-trains policies with real demonstrations for real-robot evaluation.<br><sub>Tags: Simulation data · Whole-body planning · Sim-and-real co-training</sub> | [Paper](https://arxiv.org/abs/2605.27724) · [Project](https://humanoidmimicgen.github.io/) · [Benchmark](https://github.com/NVlabs/humanoidmimicgen) |
| [**DemoHLM**](https://arxiv.org/abs/2510.11258)<br><sub>DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation</sub> | 2025-10<br><sub>arXiv</sub> | One simulated demonstration → synthetic training data | Expands one simulated demonstration into task data and learns visual manipulation above a whole-body controller for real-robot transfer.<br><sub>Tags: Simulation data · Demonstration expansion · Sim-to-real</sub> | [Paper](https://arxiv.org/abs/2510.11258) · [Project](https://beingbeyond.github.io/DemoHLM/) |

**Across directions:** [HumanX](#interaction-learning-from-human-videos) also augments interaction data; [InterMimicGen](#execution-guided-data-policy-co-improvement) couples augmentation to repeated execution and tracker updates. For execution-system integration, see [Harness](#harness).

<a id="visual-policy-learning-evaluation"></a>

### Visual Policy Learning & Evaluation

**Scope.** Use rendered simulation observations to train or benchmark humanoid visual policies, with explicit deployment evidence.

**Reading guide.** VIRAL is a teacher–student training method; SIMPLE is a simulation benchmark and data-collection platform.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**SIMPLE**](https://arxiv.org/abs/2606.08278)<br><sub>SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation</sub> | 2026-06<br><sub>arXiv · Benchmark</sub> | Simulated tasks, assets, and collection interfaces → humanoid policy benchmark and training data | Couples MuJoCo physics with Isaac Sim rendering to collect and evaluate whole-body humanoid policies, including reported sim-to-real transfer under matched settings.<br><sub>Tags: Benchmark · Simulation data · Policy evaluation</sub> | [Paper](https://arxiv.org/abs/2606.08278) · [Project](https://psi-lab.ai/SIMPLE/) |
| [**VIRAL**](https://arxiv.org/abs/2511.15200)<br><sub>VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation</sub> | 2025-11<br><sub>arXiv</sub> | Privileged simulation rollouts → RGB student policy → real humanoid control | Distills a simulation RL teacher into a visual student using large-scale rendering and domain randomization, with hand and camera alignment for G1 transfer.<br><sub>Tags: Visual sim-to-real · Teacher–student learning · Domain randomization</sub> | [Paper](https://arxiv.org/abs/2511.15200) · [Project](https://viral-humanoid.github.io/) |
| [**VisualMimic**](https://arxiv.org/abs/2509.20322)<br><sub>VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation</sub> | 2025-09<br><sub>arXiv</sub> | Simulated motion tracking and rendering → visual humanoid policy | Combines motion tracking and generation to train visual policies in simulation for real humanoid lifting, pushing, dribbling, and kicking. | [Paper](https://arxiv.org/abs/2509.20322) |

<a id="whole-body-policy-transfer"></a>

### Whole-Body Policy Transfer

**Scope.** Train coupled locomotion and manipulation policies in simulation and deploy them on physical humanoids.

**Reading guide.** Digit box transport provides an early example of transferring pickup and carrying skills as a complete task.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**Sim-to-Real Humanoid Box Loco-Manipulation**](https://arxiv.org/abs/2310.03191)<br><sub>Sim-to-Real Learning for Humanoid Box Loco-Manipulation</sub> | 2023-10<br><sub>arXiv</sub> | Simulated pickup and carrying tasks → real Digit skills | Learns box pickup and carrying with balance-aware reinforcement learning and combines the skills for real table-to-table box transport. | [Paper](https://arxiv.org/abs/2310.03191) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="interaction"></a>

## Interaction

Learn and control physical interactions between humanoids, objects, and their environment, including body–hand coordination, teammate coordination, and force regulation.

<a id="interaction-learning-from-human-demonstrations"></a>
<a id="从人类视频学习交互"></a>
<a id="interaction-learning-from-human-videos"></a>
<a id="human-object-interaction"></a>
<a id="whole-body-interaction-from-demonstrations"></a>
<a id="从示教学习全身交互"></a>

### Interaction Learning from Human Demonstrations

Learn humanoid interactions from human videos or wearable demonstrations; methods differ in motion recovery, contact annotation, and retargeting requirements. For captured demonstrations with dexterous hand coordination, see [Dexterous Whole-Body Interaction](#dexterous-whole-body-interaction).

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**REACT**](https://arxiv.org/abs/2610.28523)<br><sub>VLM-Guided Contact Retargeting and Generative Partner Modeling for Humanoid-Human Interaction</sub> | 2026-10<br><sub>arXiv</sub> | Human–human demonstrations and onboard depth → humanoid–human contact policies | Combines VLM-guided contact retargeting with generative partner-state modeling and policy distillation for contact interactions in simulation and on a real G1. | [Paper](https://arxiv.org/abs/2610.28523) |
| [**VICAR**](https://arxiv.org/abs/2610.13079)<br><sub>VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills</sub> | 2026-10<br><sub>arXiv</sub> | Third-person human video and contact targets → adaptive humanoid interaction skills | Preserves global contact poses, speed, and collision clearance during retargeting, then learns contact-conditioned motions that adapt to moved contact targets.<br><sub>Tags: Video imitation · Contact-aware retargeting · Contact conditioning</sub> | [Paper](https://arxiv.org/abs/2610.13079) |
| [**Workhorse**](https://arxiv.org/abs/2610.09117)<br><sub>Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data</sub> | 2026-10<br><sub>arXiv</sub> | Wearable human poses and egocentric RGB → visual planner and whole-body tracker | Trains a visual planner and an RL tracker on shared torso, wrist, and foot targets, using mutual error augmentation for contact-rich G1 skills without robot-specific retargeting.<br><sub>Tags: Robot-free demonstrations · Five-link interface · Robust tracking</sub> | [Paper](https://arxiv.org/abs/2610.09117) · [Project](https://hybridrobotics.github.io/workhorse/) |
| [**HALOMI**](https://arxiv.org/abs/2606.18772)<br><sub>HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations</sub> | 2026-06<br><sub>arXiv</sub> | Egocentric/wrist observations and head–hand demonstrations → active-perception humanoid policy | Combines view alignment and controller-aware reference adaptation with a latent-manifold controller for coordinated head–hand tracking.<br><sub>Tags: Active perception · Head–hand control · Demonstration alignment</sub> | [Paper](https://arxiv.org/abs/2606.18772) · [Project](https://halomi-humanoid.github.io) |
| [**GenHOI**](https://arxiv.org/abs/2606.12995)<br><sub>GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training</sub> | 2026-06<br><sub>arXiv</sub> | Human video → optimized contact-aware robot references | Recovers interactions from video and optimizes references for a frozen closed-loop tracker, with G1 simulation and hardware evaluation rather than task-specific policy training. | [Paper](https://arxiv.org/abs/2606.12995) |
| [**Bifrost-UMI**](https://arxiv.org/abs/2605.03452)<br><sub>BifrostUMI: Bridging Robot-Free Demonstrations and Humanoid Whole-Body Manipulation</sub> | 2026-05<br><sub>arXiv</sub> | Human demonstrations and pose alignment → whole-body manipulation | Couples demonstration transfer and whole-body execution for physical G1 tasks involving bending, stepping, and manipulation while walking. | [Paper](https://arxiv.org/abs/2605.03452) |
| [**EgoHumanoid**](https://arxiv.org/abs/2602.10106)<br><sub>EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration</sub> | 2026-02<br><sub>arXiv</sub> | Egocentric human demonstrations and limited robot data → aligned humanoid VLA policy | Aligns human and robot viewpoints and action spaces before co-training a VLA for G1 loco-manipulation across environments.<br><sub>Tags: View alignment · Action alignment · Human–robot co-training</sub> | [Paper](https://arxiv.org/abs/2602.10106) · [Project](https://opendrivelab.com/EgoHumanoid/) |
| [**HuMI**](https://arxiv.org/abs/2602.06643)<br><sub>Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations</sub> | 2026-02<br><sub>arXiv</sub> | Portable robot-free whole-body demonstrations → hierarchical humanoid manipulation policy | Captures human whole-body motion with an online feasibility preview and learns hierarchical policies for coordinated kneeling, squatting, tossing, and walking manipulation.<br><sub>Tags: Robot-free demonstrations · Feasibility alignment · Hierarchical learning</sub> | [Paper](https://arxiv.org/abs/2602.06643) · [Project](https://humanoid-manipulation-interface.github.io) |
| [**HumanX**](https://arxiv.org/abs/2602.02473)<br><sub>HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos</sub> | 2026-02<br><sub>CoRL 2026</sub> | Human video → augmented references → interaction skills | Pairs anchor-centric interaction synthesis with interaction-prioritized imitation to learn agile skills that transfer to a G1.<br><sub>Tags: Video reconstruction · Data augmentation · Interaction learning</sub> | [Paper](https://arxiv.org/abs/2602.02473) · [Project](https://wyhuai.github.io/human-x/) |
| [**ResMimic**](https://arxiv.org/abs/2510.05070)<br><sub>ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning</sub> | 2025-10<br><sub>arXiv</sub> | Human interaction references and a general motion tracker → object-aware residual policy | Adds a learned residual to a general motion tracker, using object geometry and contact rewards to improve whole-body interaction precision.<br><sub>Tags: Residual learning · Contact rewards · Object tracking</sub> | [Paper](https://arxiv.org/abs/2510.05070) · [Project](https://resmimic.github.io/) |
| [**HumanoidExo**](https://arxiv.org/abs/2510.03022)<br><sub>HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton</sub> | 2025-10<br><sub>arXiv</sub> | Wearable exoskeleton motion and camera observations → humanoid whole-body policy | Aligns wearable human data with the humanoid and combines it with limited robot demonstrations to learn coordinated standing, squatting, and walking manipulation.<br><sub>Tags: Robot-free data · Exoskeleton · Human–robot co-training</sub> | [Paper](https://arxiv.org/abs/2510.03022) |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | Monocular RGB video → whole-body interaction policy | Extracts human–object trajectories and learns interaction skills by jointly tracking robot and object states.<br><sub>Tags: Video reconstruction · Interaction imitation · Sim-to-real</sub> | [Paper](https://arxiv.org/abs/2509.16757) · [Project](https://hdmi-humanoid.github.io/) · [Code](https://github.com/LeCAR-Lab/HDMI) |
| [**Cross-Embodiment Behavior-Skill Transfer**](https://arxiv.org/abs/2412.15166)<br><sub>Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration</sub> | 2024-12<br><sub>arXiv</sub> | Human demonstrations and interaction graphs → transferred robot skills | Decomposes behavior primitives and fine-tunes interaction skills across robot embodiments, including simulated H1 and NAVIAI box carrying. | [Paper](https://arxiv.org/abs/2412.15166) |

<a id="dexterous-whole-body-interaction"></a>

### Dexterous Whole-Body Interaction

Coordinate body and hand contacts through captured demonstrations or synthesized whole-body grasp supervision.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**EmbodyHOI**](https://arxiv.org/abs/2610.27242)<br><sub>EmbodyHOI: Embodiment-Aware Generation of Hand-Object Interactions for Humanoid Dexterous Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Human hand–object generation prior and robot kinematics → reachable humanoid interaction references | Guides a frozen interaction generator with robot inverse kinematics to adjust wrist and root references, evaluated for dexterous manipulation in G1 and H1-2 simulation. | [Paper](https://arxiv.org/abs/2610.27242) |
| [**WBD**](https://arxiv.org/abs/2610.22184)<br><sub>Whole-Body Dexterity</sub> | 2026-10<br><sub>arXiv</sub> | Generated whole-body grasps and goal references → body-contact manipulation policy | Trains and distills repositioning experts from feasible grasps so a G1 can manipulate objects through coordinated arm and torso contacts.<br><sub>Tags: Whole-body grasps · Expert distillation · Body contact</sub> | [Paper](https://arxiv.org/abs/2610.22184) |
| [**Weave**](https://arxiv.org/abs/2609.16683)<br><sub>Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions</sub> | 2026-09<br><sub>arXiv</sub> | Captured HOI → dexterous robot–object interaction | Combines contact-aware retargeting with a geometry-aware policy that coordinates body and finger joints to track robot–object references.<br><sub>Tags: HOI motion capture · Dexterous hands · Contact-aware retargeting</sub> | [Paper](https://arxiv.org/abs/2609.16683) · [Project](https://xiaohu-art.github.io/Weave/) |
| [**CoorDex**](https://arxiv.org/abs/2606.23680)<br><sub>CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | Body and hand demonstrations → coordinated latent-prior policy | Coordinates frozen body and hand priors through residual learning for continuous manipulation on a G1 equipped with WUJI dexterous hands. | [Paper](https://arxiv.org/abs/2606.23680) |

<a id="contact-force-control"></a>

### Contact & Force Control

Regulate compliance and contact forces during execution, beyond following a motion trajectory.

For actuator-model correction that improves force transfer, see [Contact-UAN](#contact-consistent-actuator-modeling).

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**C-GMT**](https://arxiv.org/abs/2610.22119)<br><sub>Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation</sub> | 2026-10<br><sub>arXiv</sub> | Motion references and proprioceptive history → compliant reference corrections | Learns a residual reference adapter above a general motion tracker to produce compliant whole-body responses across playback, teleoperation, and VLA interfaces.<br><sub>Tags: Residual reference adaptation · Compliance · General motion tracking</sub> | [Paper](https://arxiv.org/abs/2610.22119) · [Project](https://venki1899.github.io/c-gmt/) |
| [**KPI**](https://arxiv.org/abs/2609.36151)<br><sub>KPI: A Promptable Kernel for Physical Interaction on Humanoids</sub> | 2026-09<br><sub>arXiv</sub> | Trajectory + interaction contract → adaptive contact control | Adapts arm impedance and references to tracking, compliance, and force-range requests while retaining the underlying whole-body tracker.<br><sub>Tags: Impedance adaptation · Force regulation</sub> | [Paper](https://arxiv.org/abs/2609.36151) · [Project](https://kpi-robot.github.io/) |
| [**CEER2**](https://arxiv.org/abs/2609.38709)<br><sub>CEER2: Directional and Tunable End-Effector and Root Compliance for Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | Motion commands and proprioception → directionally compliant control | Regulates direction-dependent whole-body compliance on a real G1 without requiring wrist force-torque sensors. | [Paper](https://arxiv.org/abs/2609.38709) |
| [**CEER**](https://arxiv.org/abs/2605.19981)<br><sub>CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation</sub> | 2026-05<br><sub>arXiv</sub> | Root commands and end-effector poses → compliant whole-body control interface | Distills motion tracking into an end-effector–root interface that supports compliant manipulation and integration with heterogeneous high-level planners.<br><sub>Tags: Compliance · Task-space interface · Hierarchical control</sub> | [Paper](https://arxiv.org/abs/2605.19981) · [Project](https://robotproject8.github.io/ceer_page/) |
| [**GentleHumanoid**](https://arxiv.org/abs/2511.04679)<br><sub>GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction</sub> | 2025-11<br><sub>arXiv</sub> | Motion references and modeled interaction forces → compliant upper-body responses | Trains a whole-body tracker with spring-based guiding and resistive contacts to coordinate shoulder, elbow, and wrist compliance during physical interaction.<br><sub>Tags: Compliance · Human–robot contact · Whole-body tracking</sub> | [Paper](https://arxiv.org/abs/2511.04679) |
| [**FALCON**](https://arxiv.org/abs/2505.06776)<br><sub>FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation</sub> | 2025-05<br><sub>arXiv</sub> | Root and end-effector commands under external loads → force-adaptive whole-body control | Jointly trains lower- and upper-body agents with a torque-feasible force curriculum for payload transport, cart pulling, and door opening on humanoids.<br><sub>Tags: Force adaptation · Dual-agent RL · Load handling</sub> | [Paper](https://arxiv.org/abs/2505.06776) |
| [**Flow Multi-Support**](https://arxiv.org/abs/2407.12381)<br><sub>Flow Matching Imitation Learning for Multi-Support Manipulation</sub> | 2024-07<br><sub>arXiv</sub> | Demonstrations and contact constraints → flow-matching control | Combines flow-matching imitation with multi-contact whole-body optimization for Talos pushing and drawer closing with supporting hand contacts. | [Paper](https://arxiv.org/abs/2407.12381) |
| [**WoCoCo**](https://arxiv.org/abs/2406.06005)<br><sub>WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts</sub> | 2024-06<br><sub>arXiv</sub> | Contact stages and task rewards → whole-body interaction policies | Decomposes sequential contacts into stages for reinforcement learning, with real humanoid box loco-manipulation among its evaluated tasks. | [Paper](https://arxiv.org/abs/2406.06005) |

**Across directions:** [PRISM](#counterfactual-video-augmentation) and [GRAIL](#asset-video-interaction-synthesis) also learn interaction policies, with their main entries emphasizing data generation. [KPI](#contact-force-control) includes agent-driven trajectory and interaction-contract generation.

<a id="tactile-guided-manipulation"></a>

### Tactile-Guided Whole-Body Manipulation

**Scope.** Use human contact demonstrations or robot tactile observations to learn humanoid manipulation and contact goals.

**Reading guide.** TACT uses robot tactile observations; PanTact and WT-UMI transfer human contact or force demonstrations. [Contact & Force Control](#contact-force-control) focuses on regulating execution dynamics.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**PanTact**](https://arxiv.org/abs/2610.12558)<br><sub>PanTact: Teaching Whole-Body Dexterity with a Wearable Contact Interface</sub> | 2026-10<br><sub>arXiv</sub> | Wearable contact demonstrations → body-contact goals and control | Learns contact goals from a wearable interface and executes support, pushing, sweeping, and load-sharing on G1 without added body-contact sensors. | [Paper](https://arxiv.org/abs/2610.12558) |
| [**WT-UMI**](https://arxiv.org/abs/2606.13232)<br><sub>WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning</sub> | 2026-06<br><sub>arXiv</sub> | Wearable pose and tactile demonstrations → force-aware execution | Uses demonstrated poses and contact forces to supervise planning with admittance execution for real G1 manipulation. | [Paper](https://arxiv.org/abs/2606.13232) |
| [**TACT**](https://arxiv.org/abs/2506.15146)<br><sub>TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality</sub> | 2025-06<br><sub>RA-L 2025</sub> | Vision, joint states, and distributed tactile sensing → contact-rich manipulation actions | Extends ACT with upper-body tactile inputs and integrates the learned manipulation policy with model-based biped control for carrying with broad body contacts.<br><sub>Tags: Tactile feedback · Imitation learning · Body contact</sub> | [Paper](https://arxiv.org/abs/2506.15146) |

<a id="multi-humanoid-coordination"></a>

### Multi-Humanoid Coordination

**Scope.** Coordinate multiple humanoids sharing objects or workspace during physical interaction.

**Reading guide.** PingpongDuo couples alternating ball contact with teammate clearance and collision-risk filtering; its ball-flight/contact calibration is a supporting transfer component.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HoloBoxing**](https://arxiv.org/abs/2610.32909)<br><sub>HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training</sub> | 2026-10<br><sub>arXiv</sub> | Measured robot and opponent states → compact planner over a frozen whole-body controller | Initializes a latent-action planner by imitation and refines boxing decisions with RL above frozen HoloMotion v2; G1 contact-boxing evaluation is simulation-only, and the seven-minute budget excludes controller pretraining. | [Paper](https://arxiv.org/abs/2610.32909) |
| [**OmniInteract**](https://arxiv.org/abs/2610.26043)<br><sub>OmniInteract: Towards Unified Whole-Body Interaction Control for Dual Humanoids</sub> | 2026-10<br><sub>arXiv</sub> | Paired interaction demonstrations and partner state → unified dual-humanoid contact policy | Preserves surface contacts during retargeting and unifies partner-conditioned residual policies over a frozen controller, with two real G1 robots performing high-fives, hugs, and shoulder holds. | [Paper](https://arxiv.org/abs/2610.26043) |
| [**PingpongDuo**](https://arxiv.org/abs/2610.20579)<br><sub>PingpongDuo: Agile Humanoid Table Tennis Doubles with Safe Team Coordination</sub> | 2026-10<br><sub>arXiv</sub> | Human motion references, ball state, and teammate state → coordinated footwork and strikes | Combines a risk-filtered team planner, mutually initialized footwork/striking skills, and racket-arm residuals for alternating doubles play with two G1 humanoids.<br><sub>Tags: Multi-humanoid coordination · Dynamic interaction · Risk-aware planning</sub> | [Paper](https://arxiv.org/abs/2610.20579) |

<a id="whole-body-planning-skill-learning"></a>

### Whole-Body Planning & Skill Learning

**Scope.** Plan contacts or learn task policies that coordinate locomotion, balance, and object interaction.

**Reading guide.** BOPI replans under uncertain dynamics; SkillBlender composes reusable skills; Opt2Skill connects trajectory optimization to policy learning.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**Attention-based Contacts**](https://arxiv.org/abs/2610.31608)<br><sub>Humanoid Mobility via Attention-based Contacts</sub> | 2026-10<br><sub>arXiv</sub> | Terrain perception and goals → multi-body contact plans and whole-body control | Learns a contact planner and contact-conditioned tracker for G1 ladder climbing, hand-supported vaulting, box climbing, and sit-stand interaction, with simulated evaluation and onboard real-robot deployment. | [Paper](https://arxiv.org/abs/2610.31608) |
| [**HS-MoDP / G1Exo**](https://arxiv.org/abs/2610.26169)<br><sub>Compositional Humanoid Manipulation through Isomorphic Teleoperation and Independent Skill Routing</sub> | 2026-10<br><sub>arXiv</sub> | Isomorphic exoskeleton demonstrations and per-arm semantic conditions → compositional manipulation policy | Combines G1Exo demonstrations with independent arm-wise routing through shared policy experts for real G1 manipulation involving arm and torso contacts. | [Paper](https://arxiv.org/abs/2610.26169) |
| [**FIBER**](https://arxiv.org/abs/2610.24675)<br><sub>Action-Aligned Latent Planning for Versatile Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Task-expert action responses and visual observations → plans in a frozen behavior-model latent space | Aligns task experts with a frozen behavior foundation model and trains a unified perceptive latent planner offline, with simulated and real G1 door opening, pickup, and carrying. | [Paper](https://arxiv.org/abs/2610.24675) |
| [**BOPI**](https://arxiv.org/abs/2610.13087)<br><sub>Belief-Overlap Partial Inversion: Object-Centric Flow Replanning for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Interaction observations and goals → belief-conditioned plans | Updates a belief over uncertain interaction dynamics and replans with a flow-based model for cart translation and turning on G1. | [Paper](https://arxiv.org/abs/2610.13087) |
| [**MotionDisco**](https://arxiv.org/abs/2606.06139)<br><sub>MotionDisco: Motion Discovery for Extreme Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | Scene geometry and task goals → contact plans and full-body motion | Discovers G1 motions by planning object and environmental support contacts and solving the resulting whole-body motion constraints. | [Paper](https://arxiv.org/abs/2606.06139) |
| [**LadderMan**](https://arxiv.org/abs/2606.05873)<br><sub>LadderMan: Learning Humanoid Perceptive Ladder Climbing</sub> | 2026-06<br><sub>CoRL 2026</sub> | A single climbing demonstration, depth observations, and operator targets → perceptive climbing and stable on-ladder manipulation | Distills climbing experts into a depth-based G1 policy and separates lower-body stabilization from teleoperated upper-body manipulation on ladders. | [Paper](https://arxiv.org/abs/2606.05873) · [Project](https://ladderman-robot.github.io/) |
| [**DreamControl**](https://arxiv.org/abs/2509.14353)<br><sub>DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion</sub> | 2025-09<br><sub>arXiv</sub> | Human motion diffusion prior and task reward → interaction policy | Guides reinforcement learning with a human motion diffusion prior for coordinated lower- and upper-body scene interaction, evaluated on G1. | [Paper](https://arxiv.org/abs/2509.14353) |
| [**SkillBlender**](https://arxiv.org/abs/2506.09366)<br><sub>SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending</sub> | 2025-06<br><sub>arXiv</sub> | Pretrained low-level skills and task goals → composed behavior | Learns a higher-level policy over reusable skills for whole-body tasks using H1, G1, and H1-2 simulation models. | [Paper](https://arxiv.org/abs/2506.09366) |
| [**Whole-Body Dynamic Throwing**](https://arxiv.org/abs/2410.05681)<br><sub>Whole-Body Dynamic Throwing with Legged Manipulators</sub> | 2024-10<br><sub>arXiv</sub> | Target locations and robot state → dynamic whole-body throws | Uses reinforcement learning and curriculum training to exploit whole-body momentum on the two-legged, two-armed Chuck robot; quadruped results are separate. | [Paper](https://arxiv.org/abs/2410.05681) |
| [**OGMP**](https://arxiv.org/abs/2410.01030)<br><sub>Preferenced Oracle Guided Multi-mode Policies for Dynamic Bipedal Loco-Manipulation</sub> | 2024-10<br><sub>arXiv</sub> | Hybrid task oracles and preferred transitions → multi-mode policy | Guides policy learning with hybrid references and transition preferences for simulated humanoid soccer and box movement, including G1 and H1. | [Paper](https://arxiv.org/abs/2410.01030) |
| [**Opt2Skill**](https://arxiv.org/abs/2409.20514)<br><sub>Opt2Skill: Imitating Dynamically-feasible Whole-Body Trajectories for Versatile Humanoid Loco-Manipulation</sub> | 2024-09<br><sub>arXiv</sub> | Contact-consistent optimized trajectories → tracking policies | Trains Digit policies to track dynamically feasible trajectory-optimization references, including torque supervision for contact-sensitive tasks. | [Paper](https://arxiv.org/abs/2409.20514) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="foundations"></a>

## Foundations

Reusable learned models and control interfaces with direct whole-body humanoid relevance. Separate test-time command optimization, human-data-pretrained VLAs, world-model-conditioned policies, and generalist motor controllers.

<a id="test-time-command-optimization"></a>

### Test-Time Command Optimization

Use additional test-time computation to adapt commands to existing behavior foundation models (BFMs), without retraining them, and produce model-specific action labels for downstream policy learning.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**TTCO**](https://arxiv.org/abs/2610.14896)<br><sub>Test-Time Compute for Humanoid Behavior Foundation Models</sub> | 2026-10<br><sub>arXiv</sub> | Desired motions or robot trajectories + frozen BFM → optimized commands and action labels | Optimizes commands to a frozen BFM through sampled closed-loop simulations, reducing execution mismatch and generating action labels for demonstration reuse across BFMs.<br><sub>Tags: Test-time compute · Command optimization · Demonstration relabeling</sub> | [Paper](https://arxiv.org/abs/2610.14896) · [Project](https://bfmttc.github.io/) |

<a id="whole-body-vla-human-pretraining"></a>
<a id="whole-body-action-models"></a>
<a id="全身动作模型"></a>

### Whole-Body VLA & Human-Data Pretraining

Learn whole-body vision-language-action policies through human-video pretraining and heterogeneous demonstration co-training. For the world-model-conditioned route, see [MotionWAM](#world-model-conditioned-policies).

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**SP-HLM**](https://arxiv.org/abs/2610.30044)<br><sub>SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Multimodal observations and language → sparse poses, motion priors, and whole-body actions | Connects a VLA, motion generator, and whole-body tracker through five sparse poses and a latent motion prior, evaluated on eight simulated tasks and four real G1 loco-manipulation tasks. | [Paper](https://arxiv.org/abs/2610.30044) |
| [**λ₀**](https://arxiv.org/abs/2610.00438)<br><sub>Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining</sub> | 2026-09<br><sub>arXiv</sub> | Egocentric body/hand data → whole-body VLA | Uses staged human-data pretraining and embodiment adaptation to learn a policy coordinating whole-body and hand actions.<br><sub>Tags: VLA · Human-data pretraining · Embodiment adaptation</sub> | [Paper](https://arxiv.org/abs/2610.00438) |
| [**OpenHLM**](https://arxiv.org/abs/2606.22174)<br><sub>OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | Whole-body teleoperation and heterogeneous demonstrations → humanoid-native VLA | Studies joint-level teleoperation, VLA action design, and heterogeneous co-training to command the humanoid's full body through one learned policy.<br><sub>Tags: Whole-body VLA · Heterogeneous co-training · Action interface</sub> | [Paper](https://arxiv.org/abs/2606.22174) · [Project](https://openhlm-project.github.io/) |
| [**HEX**](https://arxiv.org/abs/2604.07993)<br><sub>HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation</sub> | 2026-04<br><sub>arXiv</sub> | Heterogeneous embodiment data → humanoid-aligned expert policy | Uses predictive state conditioning and embodiment-aware experts, with whole-body manipulation evaluated on the legged Tienkung 2.0 and 3.0 platforms. | [Paper](https://arxiv.org/abs/2604.07993) |
| [**Ψ₀**](https://arxiv.org/abs/2603.12263)<br><sub>Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation</sub> | 2026-03<br><sub>arXiv</sub> | Egocentric human videos and humanoid trajectories → staged VLA and whole-body action commands | Pretrains visual-action representations before training a flow-based action expert, combining arm/hand commands with an RL lower-body controller for G1 loco-manipulation.<br><sub>Tags: Staged training · Human-video pretraining · Whole-body VLA</sub> | [Paper](https://arxiv.org/abs/2603.12263) |
| [**GR00T N1.6**](https://research.nvidia.com/labs/gear/gr00t-n1_6/)<br><sub>GR00T N1.6</sub> | 2025-12<br><sub>Technical report</sub> | Heterogeneous robot data and task demonstrations → adaptable VLA policy | Combines an updated vision-language backbone, a larger action transformer, and expanded robot data, including G1 loco-manipulation, with task-specific post-training.<br><sub>Tags: Cross-embodiment pretraining · G1 loco-manipulation · Model report</sub> | [Report](https://research.nvidia.com/labs/gear/gr00t-n1_6/) |
| [**WholeBodyVLA**](https://arxiv.org/abs/2512.11047)<br><sub>WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control</sub> | 2025-12<br><sub>arXiv</sub> | Action-free egocentric videos and robot demonstrations → latent VLA with locomotion control | Learns latent actions from egocentric video and couples a VLA with a loco-manipulation-oriented controller for coordinated large-workspace tasks.<br><sub>Tags: Latent actions · Egocentric video · Whole-body VLA</sub> | [Paper](https://arxiv.org/abs/2512.11047) |

<a id="world-model-conditioned-policies"></a>

### World-Model-Conditioned Whole-Body Policies

Combine predictive visual dynamics and motion priors in world-action models for coordinated whole-body control.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**Ropedia W0**](https://arxiv.org/abs/2610.26855)<br><sub>Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience</sub> | 2026-10<br><sub>arXiv</sub> | Egocentric human experience and heterogeneous robot data → kinematics-conditioned world model | Uses human experience to train a cross-embodiment world model, with G1–Inspire loco-manipulation data and real G1 planning and world-action-model initialization experiments. | [Paper](https://arxiv.org/abs/2610.26855) |
| [**Language-Forcing**](https://arxiv.org/abs/2610.23894)<br><sub>Language-Forcing: Advancing Humanoid Loco-Manipulation via Semantic Alignment of Whole-Body World Action Models</sub> | 2026-09<br><sub>arXiv</sub> | Visual observations and language supervision → semantically aligned whole-body world-action model | Aligns predicted visual features with task-progress language during training, with G1 hardware and HumanoidArena evaluation and no auxiliary language modules at inference. | [Paper](https://arxiv.org/abs/2610.23894) |
| [**WholeBodyWAM**](https://arxiv.org/abs/2609.18197)<br><sub>WholeBodyWAM: Learning Whole-Body World Action Models with Scalable Motion Priors</sub> | 2026-09<br><sub>arXiv</sub> | Human/humanoid motion pretraining and robot demonstrations → whole-body world-action model | Pretrains a motion expert on heterogeneous motion, then couples motion, video, and action experts to generate embodiment-specific whole-body actions.<br><sub>Tags: Motion pretraining · World-action model · Whole-body coordination</sub> | [Paper](https://arxiv.org/abs/2609.18197) · [Project](https://zbzyjya.github.io/WholeBodyWAM/) |
| [**ω-0**](https://arxiv.org/abs/2608.06375)<br><sub>ω-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation</sub> | 2026-08<br><sub>arXiv</sub> | Visual observations, language, and robot state → predictive latents and whole-body actions | Jointly predicts future visual embeddings and whole-body action latents to support manipulation while moving on a G1 humanoid.<br><sub>Tags: Latent world model · Whole-body actions · Concurrent loco-manipulation</sub> | [Paper](https://arxiv.org/abs/2608.06375) |
| [**MotionWAM**](https://arxiv.org/abs/2606.09215)<br><sub>MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | Egocentric video → unified whole-body motion tokens | Conditions a unified whole-body policy on video-world-model features to coordinate locomotion, torso, feet, and hands in real time.<br><sub>Tags: Video world model · Unified whole-body actions</sub> | [Paper](https://arxiv.org/abs/2606.09215) |

<a id="generalist-whole-body-control"></a>

### Generalist Whole-Body Control

Provide reusable motor control across command interfaces, teleoperation, or task goals; the supported interfaces differ by method.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**I-BFM**](https://arxiv.org/abs/2610.06129)<br><sub>I-BFM: Reward-Conditioned Robust Humanoid Interaction via Unsupervised Reinforcement Learning</sub> | 2026-10<br><sub>arXiv</sub> | Interaction experience and reward conditions → reusable behavior policy | Learns a reward-conditioned interaction foundation policy supporting G1 loco-manipulation, recovery, and task chaining without task-specific retraining. | [Paper](https://arxiv.org/abs/2610.06129) |
| [**OMG**](https://arxiv.org/abs/2606.10340)<br><sub>OMG: Omni-Modal Motion Generation for Generalist Humanoid Control</sub> | 2026-06<br><sub>arXiv</sub> | Language, audio, or motion conditions → generated humanoid motion | Pairs a multimodal diffusion motion generator with reactive tracking for G1 control, providing a motion-generation foundation rather than a complete manipulation agent. | [Paper](https://arxiv.org/abs/2606.10340) |
| [**ULTRA**](https://arxiv.org/abs/2603.03279)<br><sub>ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation</sub> | 2026-03<br><sub>IROS 2026</sub> | Motion references or sparse goals → whole-body control | Distills motion-tracking skills into a multimodal controller that also supports autonomous behavior from sparse goals and egocentric perception.<br><sub>Tags: Multimodal control · Sparse goals · Motion tracking</sub> | [Paper](https://arxiv.org/abs/2603.03279) |
| [**SONIC**](https://arxiv.org/abs/2511.07820)<br><sub>SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control</sub> | 2025-11<br><sub>arXiv</sub> | Multimodal motion commands → unified G1 control | Scales motion tracking and command interfaces into a reusable G1 controller supporting teleoperation and downstream loco-manipulation. | [Paper](https://arxiv.org/abs/2511.07820) |
| [**BFM-Zero**](https://arxiv.org/abs/2511.04131)<br><sub>BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning</sub> | 2025-11<br><sub>arXiv</sub> | Motion, goal, or reward prompts → a shared latent-conditioned whole-body policy | Uses unsupervised forward–backward representations to unify tracking, goal reaching, and reward-conditioned behavior on a real G1, providing a reusable control foundation. | [Paper](https://arxiv.org/abs/2511.04131) · [Project](https://lecar-lab.github.io/BFM-Zero/) |
| [**ULC**](https://arxiv.org/abs/2507.06905)<br><sub>ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation</sub> | 2025-07<br><sub>arXiv</sub> | Root velocity/height, torso orientation, and arm targets → one whole-body policy | Uses progressive command curricula and residual arm actions to track locomotion, torso, and dual-arm commands with a unified humanoid controller.<br><sub>Tags: Unified control · Command tracking · Load randomization</sub> | [Paper](https://arxiv.org/abs/2507.06905) · [Project](https://hellod035.github.io/ULC/) |
| [**AMO**](https://arxiv.org/abs/2505.03738)<br><sub>AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control</sub> | 2025-05<br><sub>arXiv</sub> | Motion targets and robot state → adaptive whole-body control | Combines trajectory optimization and sim-to-real reinforcement learning for stable G1 control over an expanded manipulation workspace. | [Paper](https://arxiv.org/abs/2505.03738) |
| [**HOVER**](https://arxiv.org/abs/2410.21229)<br><sub>HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</sub> | 2024-10<br><sub>ICRA 2025</sub> | Multiple command spaces → one whole-body controller | Distills diverse control modes into one policy using kinematic motion imitation as a common basis.<br><sub>Tags: Multi-mode control · Policy distillation</sub> | [Paper](https://arxiv.org/abs/2410.21229) · [Project](https://hover-versatile-humanoid.github.io/) |
| [**Masked Humanoid Controller / MHC**](https://arxiv.org/abs/2408.07295)<br><sub>Learning Multi-Modal Whole-Body Control for Real-World Humanoid Robots</sub> | 2024-07<br><sub>arXiv</sub> | Masked target trajectories → multimodal whole-body controller | Exposes one learned command interface for selected robot-state targets and demonstrates multimodal control on a real Digit V3. | [Paper](https://arxiv.org/abs/2408.07295) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858)<br><sub>OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</sub> | 2024-06<br><sub>CoRL 2024</sub> | Kinematic pose commands → whole-body teleoperation and learning | Provides a common pose interface and deployable whole-body controller for teleoperation and learning autonomous skills from demonstrations.<br><sub>Tags: Teleoperation · Whole-body control · Imitation learning</sub> | [Paper](https://arxiv.org/abs/2406.08858) · [Project](https://omni.human2humanoid.com/) |
| [**HumanPlus**](https://arxiv.org/abs/2406.10454)<br><sub>HumanPlus: Humanoid Shadowing and Imitation from Humans</sub> | 2024-06<br><sub>arXiv</sub> | Human motion and shadowed demonstrations → autonomous visual skills | Uses whole-body shadowing to collect demonstrations and learns autonomous skills on a full-sized humanoid, including standing, walking, and shelf manipulation. | [Paper](https://arxiv.org/abs/2406.10454) |

**Across directions:** [InterMimicGen](#execution-guided-data-policy-co-improvement) also trains a generalist interaction tracker, alongside its iterative data loop.

[Related models and learning foundations](docs/RELATED_READING.md#foundations): Astranomy, InternW0-Δ, Diffusion Policy, Dreamer, InterMimic.

<a id="humanoid-simulation-benchmarks"></a>

### Humanoid Simulation Benchmarks

**Scope.** Evaluate learning and control with explicit humanoid robot models, including scene interaction and multi-robot manipulation.

**Reading guide.** HumanoidBench and Mimicking-Bench evaluate single-robot skills; CoHuB addresses collaboration. These entries are benchmarks, not hardware claims.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**LocoManiLab**](https://arxiv.org/abs/2610.30876)<br><sub>LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Humanoid tasks, demonstrations, policies, and controllers → unified evaluation testbed | Provides 234 atomic and compositional tasks with 51.5 hours of simulated teleoperation, evaluates policies and controllers on G1, and compares three tasks with separately trained real-robot counterparts. | [Paper](https://arxiv.org/abs/2610.30876) |
| [**CoHuB**](https://arxiv.org/abs/2609.34782)<br><sub>CoHuB: A Simulation Benchmark for Multi-Humanoid Collaboration</sub> | 2026-09<br><sub>arXiv · Benchmark</sub> | Multi-robot simulated tasks → cooperative manipulation evaluation | Benchmarks cooperative manipulation with simulated G1 robots and Dex3-1 hands, without claiming physical multi-robot deployment. | [Paper](https://arxiv.org/abs/2609.34782) |
| [**HumanoidArena**](https://arxiv.org/abs/2606.17833)<br><sub>HumanoidArena: Benchmarking Egocentric Hierarchical Whole-body Learning</sub> | 2026-06<br><sub>arXiv · Benchmark</sub> | Simulated tasks and controller backends → humanoid policy benchmark | Provides G1 manipulation tasks and demonstrations with TWIST2 and SONIC controller backends for standardized simulation evaluation. | [Paper](https://arxiv.org/abs/2606.17833) |
| [**Mimicking-Bench**](https://arxiv.org/abs/2412.17730)<br><sub>Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking</sub> | 2024-12<br><sub>arXiv · Benchmark</sub> | Human interaction references and diverse objects → scene-interaction benchmark | Benchmarks retargeting, tracking, and skill learning on six household interaction tasks using a simulated Unitree H1. | [Paper](https://arxiv.org/abs/2412.17730) |
| [**HumanoidBench**](https://arxiv.org/abs/2403.10506)<br><sub>HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation</sub> | 2024-03<br><sub>arXiv · Benchmark</sub> | Simulated humanoid models and tasks → learning benchmark | Provides whole-body locomotion and manipulation tasks around an H1 model with dexterous hands, with additional Digit models and hierarchical baselines. | [Paper](https://arxiv.org/abs/2403.10506) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="harness"></a>
<a id="systems"></a>
<a id="systems系统与技能编排"></a>

## Harness

Connect perception, control interfaces, reusable skills, and execution feedback into humanoid systems for autonomous execution or operator-guided data collection.

<a id="spatial-memory-skill-orchestration"></a>
<a id="agentic-skill-orchestration"></a>
<a id="智能体技能编排"></a>

### Spatial Memory & Long-Horizon Skill Orchestration

Use remembered spatial context and skill outcomes to plan and revise long-horizon execution.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**WholeBodyMem / HuMeGo**](https://arxiv.org/abs/2610.31166)<br><sub>Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Object-event history and current observations → memory-conditioned whole-body VLA actions | Selects history frames by object events and reads them with object tokens inside the action expert, retaining cues lost during turning and walking; HuMeGo evaluates six simulated and six real G1 memory-dependent tasks. | [Paper](https://arxiv.org/abs/2610.31166) |
| [**HomeBody**](https://tml.stanford.edu/homebody/)<br><sub>HomeBody: A Humanoid That Explores, Remembers, and Acts on Its Own</sub> | 2026-09<br><sub>Project report</sub> | Spatial memory + skill library → long-horizon execution | Connects a VLM to navigation and manipulation skills, using spatial memory and execution outcomes to coordinate tasks on a G1.<br><sub>Tags: Spatial memory · Skill orchestration · Execution feedback</sub> | [Report](https://tml.stanford.edu/homebody/) |

**Across directions:** [OmniH2O](#generalist-whole-body-control) connects teleoperation and skill learning; [KPI](#contact-force-control) connects agent-generated references to contact regulation.

**Across directions:** [TTCO](#test-time-command-optimization) wraps a frozen controller with simulation-based command search; its primary entry is under Foundations.

[Related execution and training methods](docs/RELATED_READING.md#harness): RoboICL, Recova, SGS.

<a id="whole-body-teleoperation-data"></a>

### Whole-Body Teleoperation & Data Collection

**Scope.** Integrate operator interfaces, perception, and whole-body control to execute and record humanoid demonstrations.

**Reading guide.** HOMIE uses an exoskeleton cockpit; TWIST2 uses VR motion capture with active egocentric vision.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HuMiT**](https://arxiv.org/abs/2610.29903)<br><sub>HuMiT: Low-Latency Whole-Body Humanoid Teleoperation via Compact Reference Tracking</sub> | 2026-10<br><sub>arXiv</sub> | Live operator motion → compact references and unified whole-body teleoperation | Tracks current-frame root commands and four keypoint poses without online optimization-based retargeting or future frames, demonstrating real G1 load carrying, chair pushing, sitting, and coat hanging under teleoperation. | [Paper](https://arxiv.org/abs/2610.29903) |
| [**ExtremControl**](https://arxiv.org/abs/2602.11321)<br><sub>ExtremControl: Low-Latency Humanoid Teleoperation with Scaled Velocity Feedforward</sub> | 2026-02<br><sub>arXiv</sub> | Live human motion → extremity pose targets and low-latency whole-body teleoperation | Combines scaled velocity feedforward with closed-form pose mapping for G1 teleoperation, demonstrating moving catches, cooperative box lifting, and ping-pong interaction alongside simulated and real control evaluation. | [Paper](https://arxiv.org/abs/2602.11321) |
| [**TWIST2**](https://arxiv.org/abs/2511.02832)<br><sub>TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System</sub> | 2025-11<br><sub>arXiv</sub> | VR whole-body motion and egocentric feedback → humanoid demonstrations and visuomotor policy | Combines portable whole-body VR teleoperation, an actuated neck, and a hierarchical visuomotor learner for coordinated G1 data collection and autonomous skills.<br><sub>Tags: Whole-body teleoperation · Active vision · Demonstration collection</sub> | [Paper](https://arxiv.org/abs/2511.02832) · [Project](https://yanjieze.com/projects/TWIST2/) |
| [**HOMIE**](https://arxiv.org/abs/2502.13013)<br><sub>HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit</sub> | 2025-02<br><sub>arXiv</sub> | Exoskeleton, gloves, and pedal commands → humanoid teleoperation and demonstrations | Integrates joint-matched arm control and finger sensing with an RL walking-and-squatting controller to collect humanoid loco-manipulation demonstrations.<br><sub>Tags: Teleoperation · Exoskeleton · Data collection</sub> | [Paper](https://arxiv.org/abs/2502.13013) · [Project](https://homietele.github.io/) |
| [**Mobile-TeleVision**](https://arxiv.org/abs/2412.07773)<br><sub>Mobile-TeleVision: Predictive Motion Priors for Humanoid Whole-Body Control</sub> | 2024-12<br><sub>arXiv</sub> | Teleoperated upper-body targets → coordinated walking and manipulation | Conditions locomotion on predictive upper-body motion priors while using retargeting and inverse kinematics for precise manipulation. | [Paper](https://arxiv.org/abs/2412.07773) |
| [**Mixed Reality Teleoperation Assistance**](https://arxiv.org/abs/2411.01014)<br><sub>Mixed Reality Teleoperation Assistance for Direct Control of Humanoids</sub> | 2024-11<br><sub>arXiv</sub> | Mixed-reality commands and object affordances → assisted teleoperation | Combines movement primitives, object detection, and affordance templates to assist physical Nadia teleoperation. | [Paper](https://arxiv.org/abs/2411.01014) |
| [**TRILL**](https://arxiv.org/abs/2309.01952)<br><sub>Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation</sub> | 2023-09<br><sub>arXiv</sub> | VR demonstrations and whole-body control → visuomotor policy | Learns task-space actions above a stabilizing whole-body controller, with simulated loco-manipulation and real DRACO 3 contact-rich manipulation. | [Paper](https://arxiv.org/abs/2309.01952) |
| [**iCub3 Avatar System**](https://arxiv.org/abs/2203.06972)<br><sub>iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots</sub> | 2022-03<br><sub>arXiv</sub> | Remote operator commands and multimodal feedback → avatar execution | Integrates locomotion, manipulation, and sensory feedback on iCub3, including remote public demonstrations with payload carrying. | [Paper](https://arxiv.org/abs/2203.06972) |

<a id="object-memory-execution-verification"></a>
<a id="execution-monitoring-recovery"></a>

### Execution Monitoring & Recovery

**Scope.** Monitor physical task effects and trigger recovery, using persistent object state or skill-level execution checks.

**Reading guide.** POT-VLA closes the loop after action chunks; persistent object state complements the spatial memory and skill orchestration above.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**FRAMES**](https://arxiv.org/abs/2609.22538)<br><sub>FRAMES: Failure Recovery And Monitoring of Embodied Skills for Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | Skill execution observations → monitoring and recovery decisions | Supervises CEER-based G1 skills with failure monitoring and recovery above the low-level whole-body controller. | [Paper](https://arxiv.org/abs/2609.22538) |
| [**POT-VLA**](https://arxiv.org/abs/2607.18016)<br><sub>Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation</sub> | 2026-07<br><sub>arXiv</sub> | RGB-D observations, task roles, and robot state → object-conditioned actions and execution checks | Maintains persistent 3D object records shared by a G1 action expert and geometric predicate checks, enabling verification and local recovery after action chunks.<br><sub>Tags: Object memory · Token-conditioned VLA · Execution verification</sub> | [Paper](https://arxiv.org/abs/2607.18016) |

<a id="planning-control-interfaces"></a>

### Planning & Control Interfaces

**Scope.** Translate task reasoning and perception into executable whole-body plans and controller commands.

**Reading guide.** KINO uses keyframes; iGPC grounds execution geometrically; door traversal uses reusable behavior trees.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**GPT-6-Astra Embodied Evaluation**](https://arxiv.org/abs/2610.22471)<br><sub>Has GPT-6-Astra Achieved Embodied Intelligence?</sub> | 2026-10<br><sub>arXiv</sub> | Observations, demonstrations, and feedback → model-issued actions through execution interfaces | Studies in-context learning, interaction budgets, and execution interfaces, including simulated G1 loco-manipulation in SIMPLE; real G1 manipulation and walking are evaluated separately. | [Paper](https://arxiv.org/abs/2610.22471) |
| [**Inertially Significant Humanoid Teleoperation**](https://arxiv.org/abs/2610.22176)<br><sub>Inertially Significant Humanoid Teleoperation via Whole Body Model Predictive Control and Online Parameter Estimation</sub> | 2026-10<br><sub>arXiv</sub> | VR pose commands and robot feedback → payload-adaptive whole-body MPC commands | Combines whole-body MPC with EKF-based online inertial estimation on a 23-DoF bipedal humanoid, with hardware payload tests using manually mounted forearm weights. | [Paper](https://arxiv.org/abs/2610.22176) |
| [**iGPC**](https://arxiv.org/abs/2610.08120)<br><sub>iGPC: Generative Motion Priors for Object-Aware Humanoid Interaction</sub> | 2026-10<br><sub>arXiv</sub> | Geometry observations and goals → grounded whole-body execution | Combines geometry-aware planning with existing motor priors on G1 for rail grasping, box pushing, and sitting or standing. | [Paper](https://arxiv.org/abs/2610.08120) |
| [**Praxis**](https://arxiv.org/abs/2609.30735)<br><sub>Praxis: Distilling Physical Interaction Priors from Egocentric Videos for Generalizable Whole-Body Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | Perception and task requests → coordinated skill execution | Integrates navigation, calibration, and manipulation into a real G1 EDU system equipped with Revo2 hands. | [Paper](https://arxiv.org/abs/2609.30735) |
| [**KINO**](https://arxiv.org/abs/2609.18869)<br><sub>KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | VLM-generated keyframes → whole-body pickup and transport | Uses keyframes as the interface between semantic planning and whole-body control for pickup, transport, and placement in simulation and on G1. | [Paper](https://arxiv.org/abs/2609.18869) |
| [**Fast Humanoid Robot Door Traversals**](https://arxiv.org/abs/2411.03532)<br><sub>A Behavior Architecture for Fast Humanoid Robot Door Traversals</sub> | 2024-11<br><sub>arXiv</sub> | Door perception and behavior trees → coordinated traversal | Integrates perception, reusable behavior trees, and whole-body walking and manipulation for real Nadia door traversal. | [Paper](https://arxiv.org/abs/2411.03532) |
| [**OKAMI**](https://arxiv.org/abs/2410.11792)<br><sub>OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation</sub> | 2024-10<br><sub>arXiv</sub> | Single RGB-D demonstration → object-aware plan and visual policy | Retargets body and hand motion around task objects on Fourier GR1 and uses execution trajectories to train closed-loop manipulation policies. | [Paper](https://arxiv.org/abs/2410.11792) |

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="iterative-improvement"></a>
<a id="rsi"></a>

## Iterative Improvement

Use persistent execution feedback to improve later data, policies, reward programs, or capability retention. Describe the object and mechanism of improvement explicitly; an iterative data flywheel does not establish unrestricted recursive self-improvement (RSI).

<a id="execution-guided-data-policy-co-improvement"></a>
<a id="self-evolving-data-engines"></a>
<a id="execution-guided-data--policy-improvement"></a>
<a id="执行反馈驱动的数据与策略改进"></a>

### Execution-Guided Data–Policy Co-Improvement

Retain successful executions to seed further data augmentation and tracking-policy updates across rounds.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimicGen**](https://arxiv.org/abs/2610.06850)<br><sub>InterMimicGen: Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</sub> | 2026-10<br><sub>arXiv</sub> | HOI references + execution results → expanded motions and tracker | Iteratively perturbs interaction references, fine-tunes a generalist tracker, and retains successful executions to seed the next round.<br><sub>Tags: Contact-aware retargeting · Generalist tracking · Iterative augmentation</sub> | [Paper](https://arxiv.org/abs/2610.06850) · [Project](https://sirui-xu.github.io/InterMimicGen/) |
| [**HumanoidDART**](https://arxiv.org/abs/2606.26855)<br><sub>Humanoid-DART: Humanoid Loco-Manipulation using Diffusion-guided Augmentation through Relabeling and Tracking</sub> | 2026-06<br><sub>arXiv</sub> | Generated interaction references and rollouts → improved generator and tracker | Alternates interaction generation and tracking-policy updates using execution feedback, with real G1 pushing, kicking, and pick-and-place. | [Paper](https://arxiv.org/abs/2606.26855) |

[Related program and harness evolution](docs/RELATED_READING.md#rsi): HarnessPAI and PhysEvo. These offer transferable mechanisms, with evaluation scopes distinct from humanoid whole-body control.

<a id="execution-guided-reward-program-evolution"></a>
<a id="execution-guided-program-refinement"></a>

### Execution-Guided Program Refinement

**Scope.** Revise reward, control, or coordination programs from execution feedback, identifying which programs or experience persist.

**Reading guide.** InterEvolve revises rewards; HuGo revises control code; CoEvolve revises team coordination and retains verified experience in simulation.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**MOTIO**](https://arxiv.org/abs/2610.33446)<br><sub>MOTIO: Agentic Skill Engineering for Reality-Grounded Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Human videos, metric assets, and execution feedback → revised staged humanoid skill programs | Revises body, hand, and contact programs using physics execution, multi-frame inspection, and human approval, with real G1 bottle disposal and door/cart transport plus a distilled shared reference policy evaluated on 18 simulated tasks. | [Paper](https://arxiv.org/abs/2610.33446) |
| [**InterEvolve**](https://arxiv.org/abs/2610.02196)<br><sub>InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Task requests, simulated feedback, and a skill library → revised reward programs | Revises staged reward programs with an LLM and numerical search, verifying them on a fixed controller and retaining successful programs for later tasks.<br><sub>Tags: Reward programs · Test-time search · Persistent skill library</sub> | [Paper](https://arxiv.org/abs/2610.02196) · [Project](https://sirui-xu.github.io/InterEvolve/) |
| [**CoEvolve**](https://arxiv.org/abs/2610.23288)<br><sub>CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots</sub> | 2026-10<br><sub>arXiv</sub> | Fixed motor skills and verification feedback → evolved coordination code | Revises executable team coordination from verified checkpoints and retains experience for two simulated G1 robots carrying a shared payload. | [Paper](https://arxiv.org/abs/2610.23288) |
| [**HuGo**](https://arxiv.org/abs/2609.30594)<br><sub>HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation</sub> | 2026-09<br><sub>arXiv</sub> | Task requests and execution rollouts → revised control programs | Generates and revises executable G1 control code using verified rollout and hardware feedback; cross-task skill memory remains future work. | [Paper](https://arxiv.org/abs/2609.30594) |

<a id="skill-reuse-memory-consolidation"></a>

### Skill Reuse & Memory Consolidation

**Scope.** Reuse execution-validated whole-body motions from applicable entry states, and learn which capabilities to retain under bounded storage.

**Reading guide.** HumanoidTTT improves its retention policy while keeping motion generation and tracking fixed. This complements [skill orchestration](#spatial-memory-skill-orchestration); its reported physical examples concern whole-body motion reuse rather than object manipulation.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanoidTTT**](https://arxiv.org/abs/2610.00198)<br><sub>HumanoidTTT: Test-Time Capability Reuse for Efficient Humanoid Control</sub> | 2026-09<br><sub>arXiv</sub> | Motion requests, entry states, and reuse feedback → validated motion reuse and capability retention | Gates complete-motion reuse by entry applicability and learns bounded-store retention from subsequent successful reuse while keeping the generator and tracker fixed.<br><sub>Tags: Capability reuse · Online consolidation · Bounded memory</sub> | [Paper](https://arxiv.org/abs/2610.00198) · [Code](https://github.com/AIGeeksGroup/HumanoidTTT) |

<a id="human-intervention-policy-improvement"></a>

### Policy Improvement from Human Interventions

**Scope.** Use deployment attempts and imperfect human corrections to update humanoid policies across rounds.

**Reading guide.** ROVE improves the actor and critic from mixed-quality experience; this differs from retaining motions or revising reward programs while keeping the motor controller fixed.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**ROVE**](https://arxiv.org/abs/2606.17011)<br><sub>ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning</sub> | 2026-06<br><sub>arXiv</sub> | Humanoid rollouts, human interventions, and human videos → value-guided VLA updates | Learns optimistic values from mixed-quality experience and uses advantage-conditioned policy updates to improve humanoid manipulation across rollout–intervention rounds.<br><sub>Tags: Human intervention · Value estimation · Iterative post-training</sub> | [Paper](https://arxiv.org/abs/2606.17011) |

<a id="planner-policy-post-training"></a>

### Planner & Policy Post-Training

**Scope.** Retain planner or policy updates learned through explicit post-training; distinguish these from within-rollout command search.

**Reading guide.** DiPLO updates a diffusion planner against a frozen tracker; HAF updates a latent policy over a frozen VLA. Neither alone establishes strict RSI.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**ViT-H**](https://arxiv.org/abs/2610.32966)<br><sub>ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback</sub> | 2026-10<br><sub>arXiv</sub> | Monocular videos and tracking outcomes → preference-post-trained humanoid motion generator | Generates G1 reference motions directly from video and uses tracking feedback for DPO post-training; an autoregressive variant enables real-robot video teleoperation including box transport, sweeping, kicking, and sit-stand interaction. | [Paper](https://arxiv.org/abs/2610.32966) |
| [**DiPLO**](https://arxiv.org/abs/2610.24847)<br><sub>DiPLO: Self-distilled Diffusion Planning for Loco-manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Pretrained diffusion planner and tracker → post-trained planner | Self-distills and reinforcement-fine-tunes a diffusion planner to improve task success and match a frozen tracker, with G1 hardware deployment. | [Paper](https://arxiv.org/abs/2610.24847) |
| [**HAF**](https://arxiv.org/abs/2608.16837)<br><sub>HAF: Adapting Generalist VLAs to Humanoid Whole-Body Loco-manipulation via Hierarchical Action Flow and Spectral Latent RL</sub> | 2026-08<br><sub>arXiv</sub> | Generalist VLA and offline/online experience → adapted whole-body policy | Combines hierarchical action flow with latent-space reinforcement learning over a frozen VLA on Tienkung 2.0 and 3.0 humanoids. | [Paper](https://arxiv.org/abs/2608.16837) |
| [**FADA**](https://arxiv.org/abs/2606.28476)<br><sub>FADA: Few-Shot Domain Adaptation via Dynamics Alignment for Humanoid Control</sub> | 2026-06<br><sub>arXiv</sub> | Planner–IDM policy and short target-domain rollouts → dynamics-adapted execution model | Freezes the planner and finetunes only the inverse dynamics model with supervised rollout data, evaluated on real G1 grocery carrying and Booster T1 basket pulling. | [Paper](https://arxiv.org/abs/2606.28476) · [Project](https://lecar-lab.github.io/FADA-humanoid/) |

<p align="right"><a href="#top">↑ Back to top</a></p>

---

**More resources:** [Related methods and foundations](docs/RELATED_READING.md) · [Historical data-engine list (2026-10-08)](docs/DATA_ENGINE_READING_LIST.md) · [Contributing](CONTRIBUTING.md) · [Topic template](docs/TOPIC_TEMPLATE.md).

**Inspired by:** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation).

**License:** Original curation text and assets use the [MIT License](LICENSE). Linked research and resources retain their respective licenses.






