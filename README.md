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
  <img src="https://img.shields.io/badge/Core_entries-49-4263eb?style=flat-square" alt="49 core entries">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

Humanoid loco-manipulation coordinates **locomotion, balance, and manipulation**. This list organizes **49 core works** across seven directions, with a primary entry for each work and cross-links for overlapping contributions. A separate [13-entry related reading list](docs/RELATED_READING.md) explains relevant methods from robot arms, simulated humans, and general learning.

**Scope:** direct contributions to humanoid whole-body manipulation, contact interaction, retargeting, training and transfer, or execution systems. Papers and project reports are distinguished; category assignments are editorial judgments.

**Classification checked: 2026-10-16.** Dates are first public release months, with independently verified venues recorded separately—not reading dates. Resource links do not promise a complete implementation; see [source and selection notes](docs/SOURCES.md).

**Latest additions: 2026-10-18 (HumanoidTTT; see source notes for scope and evidence).**

H2 sections describe broad research directions, technical routes, or system paradigms; H3 subgroups describe concrete methods within them and may contain a single work. Cross-links and tags identify overlapping contributions.

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
- [Interaction](#interaction)
  - [Interaction Learning from Human Demonstrations](#interaction-learning-from-human-videos)
  - [Dexterous Whole-Body Interaction](#dexterous-whole-body-interaction)
  - [Contact & Force Control](#contact-force-control)
  - [Tactile-Guided Whole-Body Manipulation](#tactile-guided-manipulation)
- [Foundations](#foundations)
  - [Test-Time Command Optimization](#test-time-command-optimization)
  - [Whole-Body VLA & Human-Data Pretraining](#whole-body-vla-human-pretraining)
  - [World-Model-Conditioned Whole-Body Policies](#world-model-conditioned-policies)
  - [Generalist Whole-Body Control](#generalist-whole-body-control)
- [Harness](#harness)
  - [Spatial Memory & Long-Horizon Skill Orchestration](#spatial-memory-skill-orchestration)
  - [Whole-Body Teleoperation & Data Collection](#whole-body-teleoperation-data)
- [Iterative Improvement](#iterative-improvement)
  - [Execution-Guided Data–Policy Co-Improvement](#execution-guided-data-policy-co-improvement)
  - [Execution-Guided Reward Program Evolution](#execution-guided-reward-program-evolution)
  - [Skill Reuse & Memory Consolidation](#skill-reuse-memory-consolidation)

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
| [**PriMoRetarget**](https://arxiv.org/abs/2610.12642)<br><sub>PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting</sub> | 2026-10<br><sub>arXiv</sub> | Human motion and interaction demonstrations → humanoid reference trajectories | Uses an explicit objective hierarchy and gradient projection to preserve foot placement and interaction contacts while optimizing lower-priority pose objectives.<br><sub>Tags: Prioritized optimization · Contact preservation · Multi-character interactions</sub> | [Paper](https://arxiv.org/abs/2610.12642) · [Project](https://nickioan.github.io/primoretarget-page/) |
| [**OTRetarget**](https://arxiv.org/abs/2609.36602)<br><sub>OTRetarget: Joint Robot and Object Motion Retargeting via Optimal Transport</sub> | 2026-09<br><sub>arXiv</sub> | Human–object demonstrations → joint robot–object references | Transfers surface interactions with optimal transport and jointly optimizes robot and object poses to preserve contacts across embodiments.<br><sub>Tags: Contact preservation · Joint robot–object optimization</sub> | [Paper](https://arxiv.org/abs/2609.36602) |
| [**HOI-Retarget**](https://arxiv.org/abs/2609.34674)<br><sub>HOI-Retarget: Contact-Centric Retargeting for Human-Object Interaction</sub> | 2026-09<br><sub>arXiv</sub> | HOI motion and object-frame contact labels → humanoid interaction references | Uses windowed trajectory optimization to preserve object-frame contacts under humanoid kinematic limits while balancing body tracking, foot support, and smoothness.<br><sub>Tags: Object-frame contacts · Trajectory optimization · Motion augmentation</sub> | [Paper](https://arxiv.org/abs/2609.34674) · [Project](https://shinben0327.github.io/hoi-retarget/) |
| [**UMR**](https://arxiv.org/abs/2609.02134)<br><sub>Unified Motion Retargeting for Humanoids with Learned Point Cloud Correspondence</sub> | 2026-09<br><sub>arXiv</sub> | Human surface motion and contact maps → humanoid reference motion | Learns dense human–robot surface correspondences and reuses them for constrained pose matching and contact-map transfer across motion sources.<br><sub>Tags: Dense correspondence · Surface matching · Contact transfer</sub> | [Paper](https://arxiv.org/abs/2609.02134) |
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
| [**LEGS**](https://arxiv.org/abs/2606.01458)<br><sub>LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World</sub> | 2026-05<br><sub>arXiv</sub> | Real scene captures → calibrated 3DGS simulator → synthetic VLA demonstrations | Composites reconstructed backgrounds with dynamic mesh foregrounds and procedural motion demonstrations to fine-tune VLAs for real G1 tasks.<br><sub>Tags: Scene reconstruction · Gaussian splatting · Synthetic demonstrations</sub> | [Paper](https://arxiv.org/abs/2606.01458) · [Project](https://hojjunekim.github.io/legs/) |

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

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="interaction"></a>

## Interaction

Learn and control physical interactions between a humanoid, objects, and its environment, including body–hand coordination and force regulation.

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
| [**VICAR**](https://arxiv.org/abs/2610.13079)<br><sub>VICAR: Video Imitation with Contact-Aware Retargeting for Humanoid Interactive Skills</sub> | 2026-10<br><sub>arXiv</sub> | Third-person human video and contact targets → adaptive humanoid interaction skills | Preserves global contact poses, speed, and collision clearance during retargeting, then learns contact-conditioned motions that adapt to moved contact targets.<br><sub>Tags: Video imitation · Contact-aware retargeting · Contact conditioning</sub> | [Paper](https://arxiv.org/abs/2610.13079) |
| [**Workhorse**](https://arxiv.org/abs/2610.09117)<br><sub>Workhorse: Learning Robust Whole-Body Humanoid Loco-Manipulation from Human Data</sub> | 2026-10<br><sub>arXiv</sub> | Wearable human poses and egocentric RGB → visual planner and whole-body tracker | Trains a visual planner and an RL tracker on shared torso, wrist, and foot targets, using mutual error augmentation for contact-rich G1 skills without robot-specific retargeting.<br><sub>Tags: Robot-free demonstrations · Five-link interface · Robust tracking</sub> | [Paper](https://arxiv.org/abs/2610.09117) · [Project](https://hybridrobotics.github.io/workhorse/) |
| [**HALOMI**](https://arxiv.org/abs/2606.18772)<br><sub>HALOMI: Learning Humanoid Loco-Manipulation with Active Perception from Human Demonstrations</sub> | 2026-06<br><sub>arXiv</sub> | Egocentric/wrist observations and head–hand demonstrations → active-perception humanoid policy | Combines view alignment and controller-aware reference adaptation with a latent-manifold controller for coordinated head–hand tracking.<br><sub>Tags: Active perception · Head–hand control · Demonstration alignment</sub> | [Paper](https://arxiv.org/abs/2606.18772) · [Project](https://halomi-humanoid.github.io) |
| [**EgoHumanoid**](https://arxiv.org/abs/2602.10106)<br><sub>EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration</sub> | 2026-02<br><sub>arXiv</sub> | Egocentric human demonstrations and limited robot data → aligned humanoid VLA policy | Aligns human and robot viewpoints and action spaces before co-training a VLA for G1 loco-manipulation across environments.<br><sub>Tags: View alignment · Action alignment · Human–robot co-training</sub> | [Paper](https://arxiv.org/abs/2602.10106) · [Project](https://opendrivelab.com/EgoHumanoid/) |
| [**HuMI**](https://arxiv.org/abs/2602.06643)<br><sub>Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations</sub> | 2026-02<br><sub>arXiv</sub> | Portable robot-free whole-body demonstrations → hierarchical humanoid manipulation policy | Captures human whole-body motion with an online feasibility preview and learns hierarchical policies for coordinated kneeling, squatting, tossing, and walking manipulation.<br><sub>Tags: Robot-free demonstrations · Feasibility alignment · Hierarchical learning</sub> | [Paper](https://arxiv.org/abs/2602.06643) · [Project](https://humanoid-manipulation-interface.github.io) |
| [**HumanX**](https://arxiv.org/abs/2602.02473)<br><sub>HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos</sub> | 2026-02<br><sub>CoRL 2026</sub> | Human video → augmented references → interaction skills | Pairs anchor-centric interaction synthesis with interaction-prioritized imitation to learn agile skills that transfer to a G1.<br><sub>Tags: Video reconstruction · Data augmentation · Interaction learning</sub> | [Paper](https://arxiv.org/abs/2602.02473) · [Project](https://wyhuai.github.io/human-x/) |
| [**ResMimic**](https://arxiv.org/abs/2510.05070)<br><sub>ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning</sub> | 2025-10<br><sub>arXiv</sub> | Human interaction references and a general motion tracker → object-aware residual policy | Adds a learned residual to a general motion tracker, using object geometry and contact rewards to improve whole-body interaction precision.<br><sub>Tags: Residual learning · Contact rewards · Object tracking</sub> | [Paper](https://arxiv.org/abs/2510.05070) · [Project](https://resmimic.github.io/) |
| [**HumanoidExo**](https://arxiv.org/abs/2510.03022)<br><sub>HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton</sub> | 2025-10<br><sub>arXiv</sub> | Wearable exoskeleton motion and camera observations → humanoid whole-body policy | Aligns wearable human data with the humanoid and combines it with limited robot demonstrations to learn coordinated standing, squatting, and walking manipulation.<br><sub>Tags: Robot-free data · Exoskeleton · Human–robot co-training</sub> | [Paper](https://arxiv.org/abs/2510.03022) |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | Monocular RGB video → whole-body interaction policy | Extracts human–object trajectories and learns interaction skills by jointly tracking robot and object states.<br><sub>Tags: Video reconstruction · Interaction imitation · Sim-to-real</sub> | [Paper](https://arxiv.org/abs/2509.16757) · [Project](https://hdmi-humanoid.github.io/) · [Code](https://github.com/LeCAR-Lab/HDMI) |

<a id="dexterous-whole-body-interaction"></a>

### Dexterous Whole-Body Interaction

Coordinate body and hand contacts through captured demonstrations or synthesized whole-body grasp supervision.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**WBD**](https://arxiv.org/abs/2610.22184)<br><sub>Whole-Body Dexterity</sub> | 2026-10<br><sub>arXiv</sub> | Generated whole-body grasps and goal references → body-contact manipulation policy | Trains and distills repositioning experts from feasible grasps so a G1 can manipulate objects through coordinated arm and torso contacts.<br><sub>Tags: Whole-body grasps · Expert distillation · Body contact</sub> | [Paper](https://arxiv.org/abs/2610.22184) |
| [**Weave**](https://arxiv.org/abs/2609.16683)<br><sub>Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions</sub> | 2026-09<br><sub>arXiv</sub> | Captured HOI → dexterous robot–object interaction | Combines contact-aware retargeting with a geometry-aware policy that coordinates body and finger joints to track robot–object references.<br><sub>Tags: HOI motion capture · Dexterous hands · Contact-aware retargeting</sub> | [Paper](https://arxiv.org/abs/2609.16683) · [Project](https://xiaohu-art.github.io/Weave/) |

<a id="contact-force-control"></a>

### Contact & Force Control

Regulate compliance and contact forces during execution, beyond following a motion trajectory.

For actuator-model correction that improves force transfer, see [Contact-UAN](#contact-consistent-actuator-modeling).

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**C-GMT**](https://arxiv.org/abs/2610.22119)<br><sub>Compliant GMT: Making General Motion Tracking Compliant via Residual Reference Adaptation</sub> | 2026-10<br><sub>arXiv</sub> | Motion references and proprioceptive history → compliant reference corrections | Learns a residual reference adapter above a general motion tracker to produce compliant whole-body responses across playback, teleoperation, and VLA interfaces.<br><sub>Tags: Residual reference adaptation · Compliance · General motion tracking</sub> | [Paper](https://arxiv.org/abs/2610.22119) · [Project](https://venki1899.github.io/c-gmt/) |
| [**KPI**](https://arxiv.org/abs/2609.36151)<br><sub>KPI: A Promptable Kernel for Physical Interaction on Humanoids</sub> | 2026-09<br><sub>arXiv</sub> | Trajectory + interaction contract → adaptive contact control | Adapts arm impedance and references to tracking, compliance, and force-range requests while retaining the underlying whole-body tracker.<br><sub>Tags: Impedance adaptation · Force regulation</sub> | [Paper](https://arxiv.org/abs/2609.36151) · [Project](https://kpi-robot.github.io/) |
| [**CEER**](https://arxiv.org/abs/2605.19981)<br><sub>CEER: Compliant End-Effector and Root Control as a Unified Interface for Hierarchical Humanoid Loco-Manipulation</sub> | 2026-05<br><sub>arXiv</sub> | Root commands and end-effector poses → compliant whole-body control interface | Distills motion tracking into an end-effector–root interface that supports compliant manipulation and integration with heterogeneous high-level planners.<br><sub>Tags: Compliance · Task-space interface · Hierarchical control</sub> | [Paper](https://arxiv.org/abs/2605.19981) · [Project](https://robotproject8.github.io/ceer_page/) |
| [**GentleHumanoid**](https://arxiv.org/abs/2511.04679)<br><sub>GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction</sub> | 2025-11<br><sub>arXiv</sub> | Motion references and modeled interaction forces → compliant upper-body responses | Trains a whole-body tracker with spring-based guiding and resistive contacts to coordinate shoulder, elbow, and wrist compliance during physical interaction.<br><sub>Tags: Compliance · Human–robot contact · Whole-body tracking</sub> | [Paper](https://arxiv.org/abs/2511.04679) |
| [**FALCON**](https://arxiv.org/abs/2505.06776)<br><sub>FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation</sub> | 2025-05<br><sub>arXiv</sub> | Root and end-effector commands under external loads → force-adaptive whole-body control | Jointly trains lower- and upper-body agents with a torque-feasible force curriculum for payload transport, cart pulling, and door opening on humanoids.<br><sub>Tags: Force adaptation · Dual-agent RL · Load handling</sub> | [Paper](https://arxiv.org/abs/2505.06776) |

**Across directions:** [PRISM](#counterfactual-video-augmentation) and [GRAIL](#asset-video-interaction-synthesis) also learn interaction policies, with their main entries emphasizing data generation. [KPI](#contact-force-control) includes agent-driven trajectory and interaction-contract generation.

<a id="tactile-guided-manipulation"></a>

### Tactile-Guided Whole-Body Manipulation

**Scope.** Use distributed body-contact sensing as policy input for humanoid object manipulation.

**Reading guide.** TACT learns from tactile observations; [Contact & Force Control](#contact-force-control) focuses on regulating interaction dynamics.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**TACT**](https://arxiv.org/abs/2506.15146)<br><sub>TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality</sub> | 2025-06<br><sub>RA-L 2025</sub> | Vision, joint states, and distributed tactile sensing → contact-rich manipulation actions | Extends ACT with upper-body tactile inputs and integrates the learned manipulation policy with model-based biped control for carrying with broad body contacts.<br><sub>Tags: Tactile feedback · Imitation learning · Body contact</sub> | [Paper](https://arxiv.org/abs/2506.15146) |

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
| [**λ₀**](https://arxiv.org/abs/2610.00438)<br><sub>Towards a General Humanoid Loco-Manipulation Model via Egocentric Whole-Body Human Data Pretraining</sub> | 2026-09<br><sub>arXiv</sub> | Egocentric body/hand data → whole-body VLA | Uses staged human-data pretraining and embodiment adaptation to learn a policy coordinating whole-body and hand actions.<br><sub>Tags: VLA · Human-data pretraining · Embodiment adaptation</sub> | [Paper](https://arxiv.org/abs/2610.00438) |
| [**OpenHLM**](https://arxiv.org/abs/2606.22174)<br><sub>OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | Whole-body teleoperation and heterogeneous demonstrations → humanoid-native VLA | Studies joint-level teleoperation, VLA action design, and heterogeneous co-training to command the humanoid's full body through one learned policy.<br><sub>Tags: Whole-body VLA · Heterogeneous co-training · Action interface</sub> | [Paper](https://arxiv.org/abs/2606.22174) · [Project](https://openhlm-project.github.io/) |
| [**WholeBodyVLA**](https://arxiv.org/abs/2512.11047)<br><sub>WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control</sub> | 2025-12<br><sub>arXiv</sub> | Action-free egocentric videos and robot demonstrations → latent VLA with locomotion control | Learns latent actions from egocentric video and couples a VLA with a loco-manipulation-oriented controller for coordinated large-workspace tasks.<br><sub>Tags: Latent actions · Egocentric video · Whole-body VLA</sub> | [Paper](https://arxiv.org/abs/2512.11047) |

<a id="world-model-conditioned-policies"></a>

### World-Model-Conditioned Whole-Body Policies

Combine predictive visual dynamics and motion priors in world-action models for coordinated whole-body control.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**WholeBodyWAM**](https://arxiv.org/abs/2609.18197)<br><sub>WholeBodyWAM: Learning Whole-Body World Action Models with Scalable Motion Priors</sub> | 2026-09<br><sub>arXiv</sub> | Human/humanoid motion pretraining and robot demonstrations → whole-body world-action model | Pretrains a motion expert on heterogeneous motion, then couples motion, video, and action experts to generate embodiment-specific whole-body actions.<br><sub>Tags: Motion pretraining · World-action model · Whole-body coordination</sub> | [Paper](https://arxiv.org/abs/2609.18197) · [Project](https://zbzyjya.github.io/WholeBodyWAM/) |
| [**ω-0**](https://arxiv.org/abs/2608.06375)<br><sub>ω-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation</sub> | 2026-08<br><sub>arXiv</sub> | Visual observations, language, and robot state → predictive latents and whole-body actions | Jointly predicts future visual embeddings and whole-body action latents to support manipulation while moving on a G1 humanoid.<br><sub>Tags: Latent world model · Whole-body actions · Concurrent loco-manipulation</sub> | [Paper](https://arxiv.org/abs/2608.06375) |
| [**MotionWAM**](https://arxiv.org/abs/2606.09215)<br><sub>MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation</sub> | 2026-06<br><sub>arXiv</sub> | Egocentric video → unified whole-body motion tokens | Conditions a unified whole-body policy on video-world-model features to coordinate locomotion, torso, feet, and hands in real time.<br><sub>Tags: Video world model · Unified whole-body actions</sub> | [Paper](https://arxiv.org/abs/2606.09215) |

<a id="generalist-whole-body-control"></a>

### Generalist Whole-Body Control

Provide reusable motor control across command interfaces, teleoperation, or task goals; the supported interfaces differ by method.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**ULTRA**](https://arxiv.org/abs/2603.03279)<br><sub>ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation</sub> | 2026-03<br><sub>IROS 2026</sub> | Motion references or sparse goals → whole-body control | Distills motion-tracking skills into a multimodal controller that also supports autonomous behavior from sparse goals and egocentric perception.<br><sub>Tags: Multimodal control · Sparse goals · Motion tracking</sub> | [Paper](https://arxiv.org/abs/2603.03279) |
| [**ULC**](https://arxiv.org/abs/2507.06905)<br><sub>ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation</sub> | 2025-07<br><sub>arXiv</sub> | Root velocity/height, torso orientation, and arm targets → one whole-body policy | Uses progressive command curricula and residual arm actions to track locomotion, torso, and dual-arm commands with a unified humanoid controller.<br><sub>Tags: Unified control · Command tracking · Load randomization</sub> | [Paper](https://arxiv.org/abs/2507.06905) · [Project](https://hellod035.github.io/ULC/) |
| [**HOVER**](https://arxiv.org/abs/2410.21229)<br><sub>HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots</sub> | 2024-10<br><sub>ICRA 2025</sub> | Multiple command spaces → one whole-body controller | Distills diverse control modes into one policy using kinematic motion imitation as a common basis.<br><sub>Tags: Multi-mode control · Policy distillation</sub> | [Paper](https://arxiv.org/abs/2410.21229) · [Project](https://hover-versatile-humanoid.github.io/) |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858)<br><sub>OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning</sub> | 2024-06<br><sub>CoRL 2024</sub> | Kinematic pose commands → whole-body teleoperation and learning | Provides a common pose interface and deployable whole-body controller for teleoperation and learning autonomous skills from demonstrations.<br><sub>Tags: Teleoperation · Whole-body control · Imitation learning</sub> | [Paper](https://arxiv.org/abs/2406.08858) · [Project](https://omni.human2humanoid.com/) |

**Across directions:** [InterMimicGen](#execution-guided-data-policy-co-improvement) also trains a generalist interaction tracker, alongside its iterative data loop.

[Related models and learning foundations](docs/RELATED_READING.md#foundations): Astranomy, InternW0-Δ, Diffusion Policy, Dreamer, InterMimic.

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
| [**TWIST2**](https://arxiv.org/abs/2511.02832)<br><sub>TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System</sub> | 2025-11<br><sub>arXiv</sub> | VR whole-body motion and egocentric feedback → humanoid demonstrations and visuomotor policy | Combines portable whole-body VR teleoperation, an actuated neck, and a hierarchical visuomotor learner for coordinated G1 data collection and autonomous skills.<br><sub>Tags: Whole-body teleoperation · Active vision · Demonstration collection</sub> | [Paper](https://arxiv.org/abs/2511.02832) · [Project](https://yanjieze.com/projects/TWIST2/) |
| [**HOMIE**](https://arxiv.org/abs/2502.13013)<br><sub>HOMIE: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit</sub> | 2025-02<br><sub>arXiv</sub> | Exoskeleton, gloves, and pedal commands → humanoid teleoperation and demonstrations | Integrates joint-matched arm control and finger sensing with an RL walking-and-squatting controller to collect humanoid loco-manipulation demonstrations.<br><sub>Tags: Teleoperation · Exoskeleton · Data collection</sub> | [Paper](https://arxiv.org/abs/2502.13013) · [Project](https://homietele.github.io/) |

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

[Related program and harness evolution](docs/RELATED_READING.md#rsi): HarnessPAI and PhysEvo. These offer transferable mechanisms, with evaluation scopes distinct from humanoid whole-body control.

<a id="execution-guided-reward-program-evolution"></a>

### Execution-Guided Reward Program Evolution

**Scope.** Revise executable task rewards using rollout feedback and retain verified programs for later tasks.

**Reading guide.** InterEvolve changes reward programs and its skill library while keeping the motor controller fixed during search.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**InterEvolve**](https://arxiv.org/abs/2610.02196)<br><sub>InterEvolve: Test-Time Evolution of Reward Programs for Humanoid Loco-Manipulation</sub> | 2026-10<br><sub>arXiv</sub> | Task requests, simulated feedback, and a skill library → revised reward programs | Revises staged reward programs with an LLM and numerical search, verifying them on a fixed controller and retaining successful programs for later tasks.<br><sub>Tags: Reward programs · Test-time search · Persistent skill library</sub> | [Paper](https://arxiv.org/abs/2610.02196) · [Project](https://sirui-xu.github.io/InterEvolve/) |

<a id="skill-reuse-memory-consolidation"></a>

### Skill Reuse & Memory Consolidation

**Scope.** Reuse execution-validated whole-body motions from applicable entry states, and learn which capabilities to retain under bounded storage.

**Reading guide.** HumanoidTTT improves its retention policy while keeping motion generation and tracking fixed. This complements [skill orchestration](#spatial-memory-skill-orchestration); its reported physical examples concern whole-body motion reuse rather than object manipulation.

| Paper / project | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HumanoidTTT**](https://arxiv.org/abs/2610.00198)<br><sub>HumanoidTTT: Test-Time Capability Reuse for Efficient Humanoid Control</sub> | 2026-09<br><sub>arXiv</sub> | Motion requests, entry states, and reuse feedback → validated motion reuse and capability retention | Gates complete-motion reuse by entry applicability and learns bounded-store retention from subsequent successful reuse while keeping the generator and tracker fixed.<br><sub>Tags: Capability reuse · Online consolidation · Bounded memory</sub> | [Paper](https://arxiv.org/abs/2610.00198) · [Code](https://github.com/AIGeeksGroup/HumanoidTTT) |

<p align="right"><a href="#top">↑ Back to top</a></p>

---

**More resources:** [Related methods and foundations](docs/RELATED_READING.md) · [Historical data-engine list (2026-10-08)](docs/DATA_ENGINE_READING_LIST.md) · [Contributing](CONTRIBUTING.md) · [Topic template](docs/TOPIC_TEMPLATE.md).

**Inspired by:** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation).

**License:** Original curation text and assets use the [MIT License](LICENSE). Linked research and resources retain their respective licenses.
