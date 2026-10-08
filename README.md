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
  <img src="https://img.shields.io/badge/Examples-5-4263eb?style=flat-square" alt="5 illustrative papers">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-64748b?style=flat-square" alt="MIT license"></a>
</p>

Humanoid loco-manipulation coordinates **locomotion, balance, and manipulation**. This collection is organized around five broad research directions, with **five illustrative papers** to show the scope of each. Papers may span several directions; each example is listed once under its primary contribution.

**Contents**

- [Real2Sim](#real2sim)
- [Harness & Real2Sim2Real](#harness-real2sim2real)
- [Interaction](#interaction)
- [Foundations](#foundations)
- [RSI](#rsi)

**Table notes.** First release and venue are recorded separately. Official resource links do not imply a complete code or data release. See [source notes](docs/SOURCES.md) for details.

<a id="real2sim"></a>

## Real2Sim

Capture real-world demonstrations and reconstruct or retarget them into simulation-ready motion and scene representations.

| Paper | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**OmniRetarget**](https://arxiv.org/abs/2509.26633)<br><sub>Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction</sub> | 2025-09<br><sub>ICRA 2026</sub> | HOI MoCap → interaction-preserving references | Preserves agent–object–terrain relationships with interaction meshes, enabling motion retargeting and augmentation across objects, terrains, and robot embodiments. | [Paper](https://arxiv.org/abs/2509.26633) · [Project](https://omniretarget.github.io/) · [Code](https://github.com/amazon-far/holosoma) · [Data](https://huggingface.co/datasets/omniretarget/OmniRetarget_Dataset) |

<a id="harness-real2sim2real"></a>

## Harness & Real2Sim2Real

Simulation task infrastructure, training and evaluation workflows, and policy transfer from simulated demonstrations to real robots.

| Paper | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**DemoHLM**](https://arxiv.org/abs/2510.11258)<br><sub>From One Demonstration to Generalizable Humanoid Loco-Manipulation</sub> | 2025-10<br><sub>arXiv</sub> | One simulated demo → synthetic training data | Generates task data from one simulated demonstration and trains visual manipulation policies above a universal whole-body controller for real-robot transfer. | [Paper](https://arxiv.org/abs/2510.11258) · [Project](https://beingbeyond.github.io/DemoHLM/) |

<a id="interaction"></a>

## Interaction

Whole-body interactions with objects and environments, including contact-aware representation and control.

| Paper | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**HDMI**](https://arxiv.org/abs/2509.16757)<br><sub>Learning Interactive Humanoid Whole-Body Control from Human Videos</sub> | 2025-09<br><sub>arXiv</sub> | Monocular RGB videos → robot–object references | Extracts and retargets human–object trajectories from monocular videos, then learns interaction skills by jointly tracking robot and object states. | [Paper](https://arxiv.org/abs/2509.16757) · [Project](https://hdmi-humanoid.github.io/) · [Code](https://github.com/LeCAR-Lab/HDMI) |

<a id="foundations"></a>

## Foundations

Reusable models and generalist policies that support downstream whole-body skills. The example below is a simulated-human interaction controller, included as a related policy foundation.

| Paper | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimic**](https://arxiv.org/abs/2502.20390)<br><sub>Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions</sub> | 2025-02<br><sub>CVPR 2025</sub> | Imperfect HOI MoCap → physics-refined interactions | Refines imperfect interaction motion through teacher policies and distills a scalable simulated-human controller, providing a foundation for physically grounded interaction data. | [Paper](https://arxiv.org/abs/2502.20390) · [Project](https://sirui-xu.github.io/InterMimic/) · [Code](https://github.com/Sirui-Xu/InterMimic) |

<a id="rsi"></a>

## RSI

**Recursive Self-Improvement:** feedback loops that use execution results to improve training data and policies. InterMimicGen illustrates self-evolving motion imitation within this direction.

| Paper | First release / venue | Input → output | One-sentence takeaway | Resources |
| :--- | :--- | :--- | :--- | :--- |
| [**InterMimicGen**](https://arxiv.org/abs/2610.06850)<br><sub>Scaling Humanoid Loco-Manipulation through Self-Evolving Motion Imitation</sub> | 2026-10<br><sub>arXiv</sub> | HOI MoCap → executable robot motions | Closes a data flywheel between contact-preserving retargeting, generalist tracking, and execution-filtered augmentation to grow dexterous whole-body interaction motions. | [Paper](https://arxiv.org/abs/2610.06850) · [Project](https://sirui-xu.github.io/InterMimicGen/) |

---

**More resources:** [Initial 17-entry data-engine reading list](docs/DATA_ENGINE_READING_LIST.md) · [Contributing](CONTRIBUTING.md) · [Topic template](docs/TOPIC_TEMPLATE.md).

**Inspired by:** [Awesome Humanoid Robot Learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) · [Awesome Robotics Manipulation](https://github.com/BaiShuanghao/Awesome-Robotics-Manipulation).

**License:** Original curation text and assets use the [MIT License](LICENSE). Linked research and resources retain their respective licenses.
