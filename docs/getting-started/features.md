---
subtitle: Features
---

# 功能概述

uv 为 Python 开发提供了基本功能 —— 从安装 Python、编写简单脚本，到支持多个 Python 版本和平台的大型项目。

uv 的界面可以分为几个部分，它们可以独立使用，也可以一起使用。

## Python 版本

安装和管理 Python 本身。

- `uv python install`：安装 Python 版本。
- `uv python list`：查看可用的 Python 版本。
- `uv python find`：查找已安装的 Python 版本。
- `uv python pin`：将当前项目固定为使用特定的 Python 版本。
- `uv python uninstall`：卸载 Python 版本。

请参阅[安装 Python 指南](../guides/install-python.md)开始。

## 脚本

执行独立的 Python 脚本，例如 `example.py`。

- `uv run`：运行脚本。
- `uv add --script`：向脚本添加依赖项。
- `uv remove --script`：从脚本中删除依赖项。

请参阅[运行脚本指南](../guides/scripts.md)开始。

## 项目

创建和处理 Python 项目，即带有 `pyproject.toml` 的项目。

- `uv init`：创建一个新的 Python 项目。
- `uv add`：向项目添加依赖项。
- `uv remove`：从项目中删除依赖项。
- `uv sync`：将项目的依赖项与环境同步。
- `uv lock`：为项目的依赖项创建锁文件。
- `uv run`：在项目环境中运行命令。
- `uv tree`：查看项目的依赖关系树。
- `uv build`：将项目构建为分发归档。
- `uv publish`：将项目发布到包索引。

请参阅[项目指南](../guides/projects.md)开始。

## 工具

运行和安装发布到 Python 包索引的工具，例如 `ruff` 或 `black`。

- `uvx` / `uv tool run`：在临时环境中运行工具。
- `uv tool install`：在用户范围内安装工具。
- `uv tool uninstall`：卸载工具。
- `uv tool list`：列出已安装的工具。
- `uv tool update-shell`：更新 shell 以包含工具可执行文件。

请参阅[工具指南](../guides/tools.md)开始。

## pip 接口

手动管理环境和包——旨在用于传统工作流程或高级命令无法提供足够控制的情况。

创建虚拟环境（取代 `venv` 和 `virtualenv`）：

- `uv venv`：创建一个新的虚拟环境。

有关详细信息，请参阅[使用环境](../pip/environments.md)的文档。

管理环境中的包（取代 [`pip`](https://github.com/pypa/pip) 和 [`pipdeptree`](https://github.com/tox-dev/pipdeptree)）：

- `uv pip install`：将包安装到当前环境中。
- `uv pip show`：显示有关已安装包的详细信息。
- `uv pip freeze`：列出已安装的包及其版本。
- `uv pip check`：检查当前环境是否具有兼容的包。
- `uv pip list`：列出已安装的包。
- `uv pip uninstall`：卸载包。
- `uv pip tree`：查看环境的依赖关系树。

有关详细信息，请参阅[管理包](../pip/packages.md)的文档。

锁定环境中的包（取代 [`pip-tools`](https://github.com/jazzband/pip-tools)）：

- `uv pip compile`：将需求编译为锁文件。
- `uv pip sync`：将环境与锁文件同步。

有关详细信息，请参阅[锁定环境](../pip/compile.md)的文档。

!!! important

    这些命令并未完全实现其所基于工具的接口和行为。您越偏离常见的工作流程，就越有可能遇到差异。有关详细信息，请参阅 [pip 兼容性指南](../pip/compatibility.md)。

## 实用工具

管理和检查 uv 的状态，例如缓存、存储目录或执行自我更新：

- `uv cache clean`：删除缓存条目。
- `uv cache prune`：删除过时的缓存条目。
- `uv cache dir`：显示 uv 缓存目录路径。
- `uv tool dir`：显示 uv 工具目录路径。
- `uv python dir`：显示 uv 已安装的 Python 版本路径。
- `uv self update`：将 uv 更新到最新版本。

## 后续步骤

阅读[使用指南](../guides/index.md)以了解每个功能的介绍，查看[概念总览](../concepts/index.md)页面以获取有关 uv 功能的深入详细信息，或了解如何在遇到任何问题时[获取帮助](./help.md)。
