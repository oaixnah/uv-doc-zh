---
subtitle: The pip interface
description: 一份关于 uv 与 `pip` 和 `pip-tools` 之间兼容性的指南，包括已知差异、解决方法和未来的兼容性意图声明。
---

# pip 接口

uv 为常见的 `pip`、`pip-tools` 和 `virtualenv` 命令提供了一个直接的替代品。这些命令直接在虚拟环境中工作，与 uv 的主要接口（其中虚拟环境是自动管理的）形成对比。`uv pip` 接口向高级用户和尚未准备好从 `pip` 和 `pip-tools` 过渡的项目开放了 uv 的速度和功能。

以下各节讨论了使用 `uv pip` 的基础知识：

- [创建和使用环境](./environments.md)
- [安装和管理包](./packages.md)
- [检查环境和包](./inspection.md)
- [声明包依赖](./dependencies.md)
- [锁定和同步环境](./compile.md)

请注意，这些命令并**不完全**实现它们所基于的工具的接口和行为。您越是偏离常见的工作流程，就越有可能遇到差异。有关详细信息，请参阅 [pip 兼容性指南](./compatibility.md)。

!!! important

    uv 不依赖也不调用 pip。pip 接口之所以如此命名，是为了突出其提供与 pip 接口匹配的低级命令的专门目的，并将其与 uv 的其余命令（在更高的抽象级别上操作）分开。
