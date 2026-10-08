<p align="center">
  <img src="assets/banner.svg" alt="Human demonstrations, whole-body motion, and humanoid interaction" width="100%">
</p>

<h1 align="center">Awesome Humanoid Loco-Manipulation</h1>

<p align="center">
  <strong>专注于人形机器人全身操作与交互的论文资源清单。</strong>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Loco--Manipulation-087f8c?style=flat-square" alt="Focus: Loco-Manipulation">
  <img src="https://img.shields.io/badge/Entries-17-4263eb?style=flat-square" alt="17 curated entries">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

人形移动操作将**移动、平衡与操作**协同起来，例如边走边搬物体、用全身姿态完成伸手操作，或与环境产生接触。本仓库先整理支撑这些技能的数据流程，后续可继续增加其他研究主题。

**初版整理：** 2026-10-08 · **17 项资源** · 精选收录，简介独立撰写，链接优先采用论文与作者官方资源。

### 目录

- [Humanoid Interaction Locomanipulation Data Engine](#humanoid-interaction-locomanipulation-data-engine)
  - [数据生成与交互保持重定向](#generation)
  - [示教采集与人体到人形迁移](#capture)
  - [人体交互数据集与物理基础](#foundation)
- [参与贡献与新增主题](#contributing)
- [相关仓库](#related)

## Humanoid Interaction Locomanipulation Data Engine

**收录范围。** 面向人形全身交互与移动操作的示教采集、重建、重定向、修正与扩增方法，以及相关数据资源。这里的 data engine 可以是学习流程中的一个环节，不要求端到端生成全部数据。

**阅读建议。** 交互保持动作数据可先看 **InterMimicGen / OmniRetarget**；基于规划的示教扩增看 **HumanoidMimicGen**；基于视频的合成看 **GRAIL / HumanX**；采集接口看 **TWIST2 / HuMI**。

**表格说明。** 各组按首次公开时间从新到旧排列，首次公开时间与发表年份分开记录。“arXiv”表示这里尚未记录会议或期刊。资源链接指向作者提供的材料，但项目页或仓库链接不代表全部代码和数据均已发布；详细来源与发布情况见 [来源说明](docs/SOURCES.md)。

<a id="generation"></a>

### 数据生成与交互保持重定向

通过重定向、合成或规划，生成和扩增机器人参考动作与示教轨迹。

| 论文 | 首次公开 / 发表 | 数据来源 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimicGen**](https://arxiv.org/abs/2610.06850)<br><sub>Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</sub> | 2026-10<br><sub>arXiv</sub> | 人体交互动捕 → 可执行机器人动作 | 将接触保持重定向、通用动作跟踪与执行验证后的数据扩增组成闭环，持续扩展带灵巧手的人形全身交互动作。 | [论文](https://arxiv.org/abs/2610.06850) · [项目](https://sirui-xu.github.io/InterMimicGen/) |
| [**OTRetarget**](https://arxiv.org/abs/2609.36602)<br><sub>Joint Robot and Object Motion Retargeting via Optimal Transport</sub> | 2026-09<br><sub>arXiv</sub> | 人体与物体运动 → 机器人与物体运动 | 通过最优传输与约束逆运动学联合调整机器人和物体轨迹，在跨形态迁移时保留表面交互关系。 | [论文](https://arxiv.org/abs/2609.36602) |
| [**GRAIL**](https://arxiv.org/abs/2606.05160)<br><sub>Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors</sub> | 2026-06<br><sub>arXiv</sub> | 三维资产与视频先验 → 机器人轨迹 | 从已知三维场景和生成式交互视频出发，经四维重建与重定向得到人形训练动作，形成全虚拟数据生成流程。 | [论文](https://arxiv.org/abs/2606.05160) · [项目](https://nvlabs.github.io/GRAIL/) · [代码](https://github.com/NVlabs/GRAIL) |
| [**HumanoidMimicGen**](https://arxiv.org/abs/2605.27724)<br><sub>Data Generation for Loco-Manipulation via Whole-Body Planning</sub> | 2026-05<br><sub>arXiv</sub> | 少量机器人示教 → 新场景示教 | 结合示教技能适配与全身移动、操作规划，将少量示教扩增为适应不同场景布局的稳定、无碰撞轨迹。 | [论文](https://arxiv.org/abs/2605.27724) · [项目](https://humanoidmimicgen.github.io/) · [基准代码](https://github.com/NVlabs/humanoidmimicgen) |
| [**HumanX**](https://arxiv.org/abs/2602.02473)<br><sub>Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos</sub> | 2026-02<br><sub>CoRL 2026</sub> | 人类视频 → 扩增后的交互动作 | 将 XGen 交互数据合成与扩增和 XMimic 模仿学习结合，从人类视频获得可迁移至真实机器人的敏捷交互技能。 | [论文](https://arxiv.org/abs/2602.02473) · [项目](https://wyhuai.github.io/human-x/) · [代码](https://github.com/wyhuai/HumanX) |
| [**DemoHLM**](https://arxiv.org/abs/2510.11258)<br><sub>From One Demonstration to Generalizable Humanoid Loco-Manipulation</sub> | 2025-10<br><sub>arXiv</sub> | 单条仿真示教 → 合成训练数据 | 从单条仿真示教生成任务数据，在通用全身控制器之上训练视觉操作策略，并迁移到真实人形机器人。 | [论文](https://arxiv.org/abs/2510.11258) · [项目](https://beingbeyond.github.io/DemoHLM/) |
| [**OmniRetarget**](https://arxiv.org/abs/2509.26633)<br><sub>Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction</sub> | 2025-09<br><sub>ICRA 2026</sub> | 人体交互动捕 → 交互保持的参考轨迹 | 利用交互网格保留主体、物体与地形的空间和接触关系，支持跨物体、地形及机器人形态的重定向与扩增。 | [论文](https://arxiv.org/abs/2509.26633) · [项目](https://omniretarget.github.io/) · [代码](https://github.com/amazon-far/holosoma) · [数据](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) |

<a id="capture"></a>

### 示教采集与人体到人形迁移

侧重采集示教，或将观察到的人体交互转化为训练参考，包括动作、视角与机器人形态的对齐。

| 论文 | 首次公开 / 发表 | 数据来源 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**EgoHumanoid**](https://arxiv.org/abs/2602.10106)<br><sub>Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration</sub> | 2026-02<br><sub>RSS 2026</sub> | 第一视角人体示教与机器人数据 → 对齐训练数据 | 对齐人体与机器人的视角和动作空间，利用大量无需机器人的第一视角示教与少量机器人数据联合训练移动操作策略。 | [论文](https://arxiv.org/abs/2602.10106) · [项目](https://opendrivelab.com/EgoHumanoid/) · [代码](https://github.com/OpenDriveLab/EgoHumanoid) |
| [**HuMI**](https://arxiv.org/abs/2602.06643)<br><sub>Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations</sub> | 2026-02<br><sub>arXiv</sub> | 便携人体动作采集 → 全身示教 | 用便携硬件采集无需机器人的人体动作，并通过分层学习转化为可执行的人形全身操作技能。 | [论文](https://arxiv.org/abs/2602.06643) · [项目](https://humanoid-manipulation-interface.github.io/) |
| [**TWIST2**](https://arxiv.org/abs/2511.02832)<br><sub>Scalable, Portable, and Holistic Humanoid Data Collection System</sub> | 2025-11<br><sub>arXiv</sub> | VR 全身遥操作 → 机器人示教 | 结合便携 VR 遥操作、全身跟踪与第一视角感知，采集用于人形机器人自主视觉动作学习的示教数据。 | [论文](https://arxiv.org/abs/2511.02832) · [项目](https://yanjieze.com/TWIST2) · [代码](https://github.com/amazon-far/TWIST2) · [数据](https://twist-data.github.io/) |
| [**HumanoidExo**](https://arxiv.org/abs/2510.03022)<br><sub>Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton</sub> | 2025-10<br><sub>ICRA 2026</sub> | 可穿戴外骨骼采集 → 人形训练数据 | 用与机器人形态对齐的可穿戴外骨骼采集人体示教，再结合少量机器人数据训练全身操作策略。 | [论文](https://arxiv.org/abs/2510.03022) · [项目](https://humanoid-exo.github.io/) |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | 单目 RGB 视频 → 机器人与物体参考轨迹 | 从单目视频提取并重定向人体与物体轨迹，通过联合跟踪机器人和物体状态学习全身交互技能。 | [论文](https://arxiv.org/abs/2509.16757) · [项目](https://hdmi-humanoid.github.io/) · [代码](https://github.com/LeCAR-Lab/HDMI) |

<a id="foundation"></a>

### 人体交互数据集与物理基础

**相关基础工作。** 这组主要面向人体动作或仿真人体，为机器人学习提供交互源数据、接触表示或物理修正方法；并非每项都是机器人数据引擎，也不都包含真实机器人部署。

| 论文 | 首次公开 / 发表 | 数据来源 → 产出 | 一句话简介 | 资源 |
| :--- | :--- | :--- | :--- | :--- |
| [**InterAct**](https://arxiv.org/abs/2509.09555)<br><sub>Advancing Large-Scale Versatile 3D Human-Object Interaction Generation</sub> | 2025-06<br><sub>CVPR 2025</sub> | 多个人体交互数据集 → 修正与扩增后的人体数据 | 统一多个人体物体交互数据集，以优化修正接触和手部动作，再进行接触保持的数据扩增与生成任务评测。 | [论文](https://arxiv.org/abs/2509.09555) · [项目](https://sirui-xu.github.io/InterAct/) · [代码](https://github.com/wzyabcas/InterAct) |
| [**InterMimic**](https://arxiv.org/abs/2502.20390)<br><sub>Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions</sub> | 2025-02<br><sub>CVPR 2025</sub> | 不完美的人体交互动捕 → 物理修正后的交互 | 用教师策略修正不完美的交互动捕并蒸馏可扩展的仿真人体控制器，为物理约束下的交互数据提供基础。 | [论文](https://arxiv.org/abs/2502.20390) · [项目](https://sirui-xu.github.io/InterMimic/) · [代码](https://github.com/Sirui-Xu/InterMimic) |
| [**OMOMO**](https://arxiv.org/abs/2309.16237)<br><sub>Object Motion Guided Human Motion Synthesis</sub> | 2023-09<br><sub>SIGGRAPH Asia 2023</sub> | 物体轨迹 → 人体全身操作动作 | 以手部位置为中间条件生成全身操作动作，并提供可用于机器人重定向的人体物体交互动捕数据。 | [论文](https://arxiv.org/abs/2309.16237) · [代码](https://github.com/lijiaman/omomo_release) |
| [**CHAIRS**](https://arxiv.org/abs/2212.10621)<br><sub>Full-Body Articulated Human-Object Interaction</sub> | 2022-12<br><sub>ICCV 2023</sub> | 动捕与关节物体 → 全身交互数据 | 提供同步的人体全身与关节物体几何及运动数据，用于研究坐下、椅子操作等全身交互。 | [论文](https://arxiv.org/abs/2212.10621) · [项目](https://jnnan.github.io/chairs/) · [代码](https://github.com/jnnan/chairs) |
| [**BEHAVE**](https://openaccess.thecvf.com/content/CVPR2022/html/Bhatnagar_BEHAVE_Dataset_and_Method_for_Tracking_Human_Object_Interactions_CVPR_2022_paper.html)<br><sub>Dataset and Method for Tracking Human Object Interactions</sub> | 2022<br><sub>CVPR 2022</sub> | 多视角 RGB-D → 人体物体拟合与接触标注 | 将多视角 RGB-D 观测与三维人体、物体拟合及接触标注配对，为全身人体物体交互研究提供源数据。 | [论文](https://openaccess.thecvf.com/content/CVPR2022/html/Bhatnagar_BEHAVE_Dataset_and_Method_for_Tracking_Human_Object_Interactions_CVPR_2022_paper.html) |

[↑ 返回目录](#目录)

<a id="contributing"></a>

## 参与贡献与新增主题

欢迎通过 issue 或 pull request 推荐论文、修正链接与补充发表信息。请提供论文一手来源，并用一句话说明其与人形移动操作的关系。

添加论文见 [CONTRIBUTING.md](CONTRIBUTING.md)。新增主题时复制 [主题模板](docs/TOPIC_TEMPLATE.md)，在中英文 README 中增加一个 H2 标题和目录入口，沿用五列表格即可，无需改动现有主题。

<a id="related"></a>

## 相关仓库

本仓库的范围与展示方式参考了以下更广泛的论文清单：

- [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning)：覆盖更广的人形学习与控制研究。
- [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation)：提供广泛的操作分类及表格化论文资源展示。

## 许可

本仓库原创的整理文字与资产使用 [MIT 许可](LICENSE)。链接中的论文、代码、模型及数据集保留各自的许可；使用研究成果时请引用原论文。
