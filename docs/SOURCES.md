# Source notes / 来源与收录说明

Curation date: **2026-10-15**. Classification review: **2026-10-16** (existing resource-release and venue checks retain their original scope). The current reading set contains **18 core entries and 13 related entries**. This is a selected reading list, not an exhaustive survey. Summaries are original paraphrases of primary research sources. Resource links are entry points, not promises of a complete code or data release.

Latest entry update: **2026-10-17** (PriMoRetarget only; earlier source checks retain their recorded dates).

## Selection boundaries / 收录边界

The homepage uses seven H2 directions: Real2Sim, Real2Sim2Real, Sim2Real & Sim–Real Co-Training, Interaction, Foundations, Harness, and Iterative Improvement. H2 headings describe broad research directions, technical routes, or system paradigms; H3 headings describe concrete methods within them. It prioritizes direct humanoid whole-body relevance. Each work has a primary table entry and may be cross-linked from other directions; contribution tags describe overlap rather than exclusive membership. The taxonomy is editorial, not an author-supplied classification.

- **Real2Sim:** adapt real demonstrations into robot-compatible simulation references, with contact-preserving motion retargeting as a concrete method.
- **Real2Sim2Real:** reconstruct simulation references from real inputs, train in simulation, and deploy back to real robots; PRISM uses counterfactual video augmentation within this route.
- **Sim2Real & Sim–Real Co-Training:** use virtual-source data for real-robot learning and deployment; distinguish asset/video-prior synthesis (GRAIL) from simulation-demonstration expansion (HumanoidMimicGen and DemoHLM), and distinguish transfer from mixed-data training.
- **Interaction:** distinguish learning from human videos, dexterous whole-body interaction from captured demonstrations, and contact/force regulation.
- **Foundations:** distinguish human-data-pretrained whole-body VLAs, world-model-conditioned policies, and generalist whole-body controllers.
- **Harness:** coordinate perception, spatial memory, reusable skills, and execution feedback through an execution framework; HomeBody illustrates spatial memory and skill orchestration.
- **Iterative Improvement:** identify persistent execution-driven changes to later data or policies. An iterative data–policy loop is not a claim of unrestricted recursive self-improvement (RSI).

The 2026-10-16 hierarchy revision places Real2Sim, Real2Sim2Real, and Harness at H2. Counterfactual video augmentation, interaction synthesis from assets and video priors, and simulation-demonstration expansion remain H3 methods within their corresponding routes. The broad “Data Generation & Policy Learning” umbrella is split into Real2Sim2Real and Sim2Real & Sim–Real Co-Training, while the former Systems section is named Harness. Prior distinctions among dexterous interaction, human-data-pretrained VLAs, and world-model-conditioned policies remain part of the collection. Existing explicit anchors and cross-links are preserved.

主页以 H2 表示宏观研究方向、技术路线或系统范式，以 H3 表示其中的具体方法。Real2Sim、Real2Sim2Real 与 Harness 位于 H2；反事实视频扩增、资产与视频先验驱动的交互合成、仿真示教扩增位于对应路线下的 H3。数据生成与策略学习贯穿多条路线，不再作为这几类方法的统一 H2。仿真迁移和虚实混合训练仍分别说明，保留旧链接与跨方向引用。机械臂、仿真人体及通用学习方法仍放入 [关联阅读](RELATED_READING.md#中文)，并注明适用边界。

## Pipeline evidence for reclassification / 重分类的流程证据

| Entry | Primary evidence | Classification implication |
| :--- | :--- | :--- |
| HumanoidMimicGen | [Paper §6.4](https://arxiv.org/html/2605.27724v1#S6.SS4): each real-world task uses one simulation demonstration to generate additional simulation demonstrations, then combines them with real-world demonstrations for policy training. [§7](https://arxiv.org/html/2605.27724v1#S7) describes manually designed co-training simulation environments. | Simulation-demonstration expansion with sim-and-real co-training; the reported training route does not establish a real-scene-to-simulation reconstruction stage. |
| DemoHLM | [Paper](https://arxiv.org/abs/2510.11258): starts from a single demonstration in simulation and reports transfer to a real G1. | Simulation-demonstration expansion and sim-to-real transfer. |
| GRAIL | [Paper](https://arxiv.org/abs/2606.05160): begins with specified 3D assets and scenes, synthesizes videos, and remains virtual until deployment. | Asset- and video-prior-based synthesis; reconstruction of generated videos is not real-world video reconstruction. |
| PRISM | [Paper](https://arxiv.org/abs/2609.38172): explicitly describes a real-to-sim-to-real framework with real-video-driven counterfactual generation and contact-anchored reconstruction. | Video augmentation and Real2Sim2Real. |

HumanoidMimicGen 的真实数据用于和仿真数据共同训练，不应据此推断其存在真实场景重建到仿真的步骤。GRAIL 的 4D 恢复处理已知虚拟场景生成的视频，也应与从真实视频重建的流程区分。

## Dates and evidence / 日期与证据

The homepage uses the first arXiv submission month unless another first public release is explicitly documented. Venue is recorded separately and only when supported by an author or conference source. Personal reading dates are not publication dates. A linked preprint is not a claim of peer review. HomeBody is explicitly a project report; Astranomy is an official research report/blog.

首次公开时间、修订时间、会议年份及个人阅读时间分别处理。论文编号的月份也不必等于首次提交月份，例如 λ₀ 的首次提交日期是 2026-09-30。涉及人体角色、仿真机器人和真机的结果分别描述。

## Current core entries

| Entry | Primary sources | Verification and scope notes |
| :--- | :--- | :--- |
| OTRetarget | [Paper](https://arxiv.org/abs/2609.36602) | First preprint: 2026-09-29. The paper reports physical G1 transfer; joint object optimization distinguishes it from body-only retargeting. |
| OmniRetarget | [Paper](https://arxiv.org/abs/2509.26633) · [Project](https://omniretarget.github.io/) · [Code](https://github.com/amazon-far/holosoma) · [Data](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) | Venue is recorded on the official project page. See the archived source note for the distinction between generated and publicly released data. |
| PRISM | [Paper](https://arxiv.org/abs/2609.38172) | First preprint: 2026-09-29. PRISM is the method name, not the paper title. The reported pipeline includes real-robot transfer. |
| GRAIL | [Paper](https://arxiv.org/abs/2606.05160) · [Code](https://github.com/NVlabs/GRAIL) | First preprint: 2026-06-03; CoRL 2026 is listed by the official repository. A synthetic-data pipeline is not, by itself, recursive self-improvement. |
| HumanoidMimicGen | [Paper](https://arxiv.org/abs/2605.27724) · [Project](https://humanoidmimicgen.github.io/) · [Benchmark](https://github.com/NVlabs/humanoidmimicgen) | First preprint: 2026-05-26. Classification reviewed against §6.4 and §7: simulation-demonstration expansion and sim-and-real co-training. The official repository is labeled Benchmark; linking it does not assert that the full generation algorithm is released. |
| DemoHLM | [Paper](https://arxiv.org/abs/2510.11258) · [Project](https://beingbeyond.github.io/DemoHLM/) | Preprint and official project page support the data-generation and deployment description. |
| HomeBody | [Report](https://tml.stanford.edu/homebody/) | Official page dated September 2026. A functioning paper/arXiv link was not verified on 2026-10-15; this entry is a project report, not a confirmed arXiv paper. |
| KPI | [Paper](https://arxiv.org/abs/2609.36151) · [Project](https://kpi-robot.github.io/) | First preprint: 2026-09-28. The contribution is contact control between a trajectory source and an unchanged whole-body tracker. |
| Weave | [Paper](https://arxiv.org/abs/2609.16683) · [Project](https://xiaohu-art.github.io/Weave/) | First preprint: 2026-09-15. The row describes reference-conditioned interaction learning and makes no unsupported zero-shot real-world claim. |
| HumanX | [Paper](https://arxiv.org/abs/2602.02473) · [Project](https://wyhuai.github.io/human-x/) | First preprint: 2026-02-02; revised 2026-10-09. CoRL 2026 is verified on the official project page. |
| HDMI | [Paper](https://arxiv.org/abs/2509.16757) · [Project](https://hdmi-humanoid.github.io/) · [Code](https://github.com/LeCAR-Lab/HDMI) | First preprint: 2025-09-20. Real-robot G1 evaluation is reported in the paper. |
| λ₀ | [Paper](https://arxiv.org/abs/2610.00438) | First submission: 2026-09-30 despite the 2610 arXiv identifier. λ₀ is the policy name. The abstract promises future releases, so no code/data availability is claimed. |
| MotionWAM | [Paper](https://arxiv.org/abs/2606.09215) | First preprint: 2026-06-08. Real-world G1 tasks are reported; a video prediction model alone would not meet the homepage scope. |
| ULTRA | [Paper](https://arxiv.org/abs/2603.03279) | First preprint: 2026-03-03; revision: 2026-09-18. IROS 2026 is recorded in the arXiv comments; September is not the initial release. |
| HOVER | [Paper](https://arxiv.org/abs/2410.21229) · [Project](https://hover-versatile-humanoid.github.io/) | First preprint: 2024-10-28. ICRA 2025 is stated on the official project page; this is a motor-control foundation rather than a complete autonomous agent. |
| OmniH2O | [Paper](https://arxiv.org/abs/2406.08858) · [Project](https://omni.human2humanoid.com/) | First preprint: 2024-06-13. CoRL 2024 is stated on the official project page. |
| PriMoRetarget | [Paper](https://arxiv.org/abs/2610.12642) · [Project](https://nickioan.github.io/primoretarget-page/) | First arXiv submission: 2026-10-08. Checked 2026-10-17. Prioritized optimization preserves higher-priority motion objectives during lower-priority updates; fits contact-preserving motion retargeting. The author project reports selected G1 hardware demonstrations and labels code “coming soon”; no code or data release is claimed. |
| InterMimicGen | [Paper](https://arxiv.org/abs/2610.06850) · [Project](https://sirui-xu.github.io/InterMimicGen/) | First preprint: 2026-10-05. This is an execution-filtered motion/data feedback loop, not a claim of unrestricted recursive self-improvement. |

## Related entries

| Entry | Primary source | Scope note |
| :--- | :--- | :--- |
| USDCraft | [Paper](https://arxiv.org/abs/2610.11322) | Useful asset infrastructure; does not itself establish whole-body humanoid control. |
| EgoInfinity | [Paper](https://arxiv.org/abs/2606.17385) | Hand–object and manipulator transfer; not equivalent to body–object contact and bipedal balance. |
| EgoEngine | [Paper](https://arxiv.org/abs/2606.12604) | A useful video-to-robot data pipeline; whole-body humanoid transfer needs separate evidence. |
| RoboICL | [Paper](https://arxiv.org/abs/2609.34261) | RoboDojo manipulation evaluation; in-context adaptation is not persistent program or weight evolution. |
| Recova | [Paper](https://arxiv.org/abs/2610.01178) | Relevant to recovery and data collection; reported manipulation results do not establish humanoid locomotion and balance. |
| SGS | [Paper](https://arxiv.org/abs/2610.12465) | An adaptive curriculum for simulated RL and transfer; not strict recursive self-improvement or a humanoid-specific method. |
| Astranomy | [Official report](https://research.nvidia.com/labs/srl/projects/astranomy/) | Official research report/blog; RoboLab DROID-arm simulations do not establish humanoid whole-body control. |
| InternW0-Δ | [Paper](https://arxiv.org/abs/2609.31394) | Relevant world-action-model architecture; no blanket humanoid loco-manipulation claim. |
| Diffusion Policy | [Author project](https://diffusion-policy.cs.columbia.edu/) | General imitation-learning method and baseline, rather than a humanoid-specific controller. |
| Dreamer series | [Author project](https://danijar.com/project/dreamerv3/) | General model-based RL background; task-specific humanoid evidence is still needed. |
| InterMimic | [Paper](https://arxiv.org/abs/2502.20390) | The original CVPR paper primarily studies simulated human characters; later robot support should be distinguished from that evidence. |
| PhysEvo | [Paper](https://arxiv.org/abs/2610.08995) | Explicit physical RSI around frozen model weights; real deployment is demonstrated on a PiPER arm. |
| HarnessPAI | [Paper](https://arxiv.org/abs/2609.29166) | A transferable harness-evolution mechanism; it should not be presented as a humanoid whole-body policy. |

## Historical data-engine list

The [17-entry data-engine document](DATA_ENGINE_READING_LIST.md) is retained as a **2026-10-08 snapshot** for source datasets, collection systems, and related avatar methods. It is not included in the current 18 + 13 counts and has not been fully re-audited in this update. The notes below are retained from that earlier curation.

历史清单保留于独立文件，标注为 2026-10-08 快照；其资源发布状态不表示在本轮全部重新核查，也不计入当前主页与关联阅读数量。

| Entry | Primary sources | Notes |
| :--- | :--- | :--- |
| InterMimicGen | [Paper](https://arxiv.org/abs/2610.06850) · [Project](https://sirui-xu.github.io/InterMimicGen/) | New October 2026 preprint; a project page is linked without asserting a code or dataset release. |
| OTRetarget | [Paper](https://arxiv.org/abs/2609.36602) | Summary paraphrased from the paper abstract and/or author materials; linked resources have their own release scope and licenses. |
| GRAIL | [Paper](https://arxiv.org/abs/2606.05160) · [Project](https://nvlabs.github.io/GRAIL/) · [Code](https://github.com/NVlabs/GRAIL) | Summary paraphrased from the paper abstract and/or author materials; linked resources have their own release scope and licenses. |
| HumanoidMimicGen | [Paper](https://arxiv.org/abs/2605.27724) · [Project](https://humanoidmimicgen.github.io/) · [Code](https://github.com/NVlabs/humanoidmimicgen) | Official linked repository currently describes benchmark environments and playback; it is labeled Benchmark rather than full generation code. |
| HumanX | [Paper](https://arxiv.org/abs/2602.02473) · [Project](https://wyhuai.github.io/human-x/) · [Code](https://github.com/wyhuai/HumanX) | CoRL 2026 recorded from the official project page. |
| DemoHLM | [Paper](https://arxiv.org/abs/2510.11258) · [Project](https://beingbeyond.github.io/DemoHLM/) | Summary paraphrased from the paper abstract and/or author materials; linked resources have their own release scope and licenses. |
| OmniRetarget | [Paper](https://arxiv.org/abs/2509.26633) · [Project](https://omniretarget.github.io/) · [Code](https://github.com/amazon-far/holosoma) · [Data](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) | Official project links to holosoma. Paper reports over 9 hours generated; the linked public dataset card lists 4 hours. The README deliberately avoids equating these totals. |
| EgoHumanoid | [Paper](https://arxiv.org/abs/2602.10106) · [Project](https://opendrivelab.com/EgoHumanoid/) · [Code](https://github.com/OpenDriveLab/EgoHumanoid) | RSS 2026 recorded from the official author repository. |
| HuMI | [Paper](https://arxiv.org/abs/2602.06643) · [Project](https://humanoid-manipulation-interface.github.io/) | Summary paraphrased from the paper abstract and/or author materials; linked resources have their own release scope and licenses. |
| TWIST2 | [Paper](https://arxiv.org/abs/2511.02832) · [Project](https://yanjieze.com/TWIST2) · [Code](https://github.com/amazon-far/TWIST2) · [Data](https://twist-data.github.io/) | Summary paraphrased from the paper abstract and/or author materials; linked resources have their own release scope and licenses. |
| HumanoidExo | [Paper](https://arxiv.org/abs/2510.03022) · [Project](https://humanoid-exo.github.io/) | ICRA 2026 recorded from the official project page. |
| HDMI | [Paper](https://arxiv.org/abs/2509.16757) · [Project](https://hdmi-humanoid.github.io/) · [Code](https://github.com/LeCAR-Lab/HDMI) | Summary paraphrased from the paper abstract and/or author materials; linked resources have their own release scope and licenses. |
| InterAct | [Paper](https://arxiv.org/abs/2509.09555) · [Project](https://sirui-xu.github.io/InterAct/) · [Code](https://github.com/wzyabcas/InterAct) | First known conference publication: June 2025 (CVPR proceedings); the linked arXiv upload followed in September 2025. Primary conference record: https://openaccess.thecvf.com/content/CVPR2025/html/Xu_InterAct_Advancing_Large-Scale_Versatile_3D_Human-Object_Interaction_Generation_CVPR_2025_paper.html |
| InterMimic | [Paper](https://arxiv.org/abs/2502.20390) · [Project](https://sirui-xu.github.io/InterMimic/) · [Code](https://github.com/Sirui-Xu/InterMimic) | Primarily physics-based simulated-human interaction; placed among related foundations, without a blanket real-robot claim. |
| OMOMO | [Paper](https://arxiv.org/abs/2309.16237) · [Code](https://github.com/lijiaman/omomo_release) | Summary paraphrased from the paper abstract and/or author materials; linked resources have their own release scope and licenses. |
| CHAIRS | [Paper](https://arxiv.org/abs/2212.10621) · [Project](https://jnnan.github.io/chairs/) · [Code](https://github.com/jnnan/chairs) | First preprint: December 2022; conference: ICCV 2023. |
| BEHAVE | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Bhatnagar_BEHAVE_Dataset_and_Method_for_Tracking_Human_Object_Interactions_CVPR_2022_paper.html) | Year-only date follows CVPR 2022; the original preprint month was not verified in this curation. |

## Related lists

- [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning)
- [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation)

These lists support discovery; individual claims are grounded in the primary sources above. Original curation text follows the repository license; linked research keeps its own license.
