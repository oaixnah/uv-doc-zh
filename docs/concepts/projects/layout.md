---
title: 项目结构与文件
subtitle: Structure and files
description: 学习Python项目的结构和文件布局，包括`pyproject.toml`、`uv.lock`、`uv.toml`和`.venv`目录。了解如何组织项目代码、管理依赖项、配置项目和构建分发版。完整指南帮助您高效地组织和发布Python代码。
---

# 项目结构与文件

## `pyproject.toml`

Python 项目的元数据定义在 [`pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) 文件中。uv 需要此文件来识别项目的根目录。

!!! tip

    可以使用 `uv init` 创建新项目。详见[创建项目](./init.md)。

一个最小的项目定义包含名称和版本：

```toml title="pyproject.toml"
[project]
name = "example"
version = "0.1.0"
```

其他项目元数据和配置包括：

- [Python 版本要求](./config.md#python-version-requirement)
- [依赖项](./dependencies.md)
- [构建系统](./config.md#build-systems)
- [入口点（命令）](./config.md#entry-points)

## 项目环境

在使用 uv 处理项目时，uv 会根据需要创建虚拟环境。虽然某些 uv 命令会创建临时环境（例如 `uv run --isolated`），但 uv 也会在 `pyproject.toml` 旁边的 `.venv` 目录中管理一个包含项目及其依赖项的持久化环境。该环境存储在项目内部，以便编辑器能够轻松找到它——编辑器需要该环境来提供代码补全和类型提示。不建议将 `.venv` 目录纳入版本控制；uv 会通过内置的 `.gitignore` 文件自动将其从 `git` 中排除。

要在项目环境中运行命令，请使用 `uv run`。或者，也可以像普通虚拟环境一样激活项目环境。

当调用 `uv run` 时，如果项目环境尚不存在，它会创建项目环境；如果已存在，则确保其是最新的。也可以使用 `uv sync` 显式创建项目环境。详见[锁定与同步](./sync.md)文档。

_不_建议手动修改项目环境，例如使用 `uv pip install`。对于项目依赖项，请使用 `uv add` 将包添加到环境中。对于一次性需求，请使用 [`uvx`](../../guides/tools.md) 或 [`uv run --with`](./run.md#requesting-additional-dependencies)。

!!! tip

    如果您不希望 uv 管理项目环境，可以设置 [`managed = false`](../../reference/settings.md#managed) 来禁用项目的自动锁定和同步。例如：

    ```toml title="pyproject.toml"
    [tool.uv]
    managed = false
    ```

## 锁文件

uv 会在 `pyproject.toml` 旁边创建一个 `uv.lock` 文件。

`uv.lock` 是一个_通用_或_跨平台_的锁文件，它记录了在所有可能的 Python 标记（marker）条件下（如操作系统、架构和 Python 版本）将会安装的包。

与用于指定项目广泛需求的 `pyproject.toml` 不同，锁文件包含安装在项目环境中的确切已解析版本。此文件应纳入版本控制，以便在不同机器上实现一致且可复现的安装。

锁文件确保参与项目的开发人员使用一致的包版本集。此外，当将项目作为应用程序部署时，它确保所使用的确切包版本集是已知的。

锁文件会在使用项目环境的 uv 调用过程中[自动创建和更新](./sync.md#automatic-lock-and-sync)，即 `uv sync` 和 `uv run`。也可以使用 `uv lock` 显式更新锁文件。

`uv.lock` 是一个人类可读的 TOML 文件，但由 uv 管理，不应手动编辑。`uv.lock` 格式是 uv 特有的，无法被其他工具使用。

### 与 `pylock.toml` 的关系

在 [PEP 751](https://peps.python.org/pep-0751/) 中，Python 标准化了一种新的解析文件格式 `pylock.toml`。

`pylock.toml` 是一种解析输出格式，旨在替代 `requirements.txt`（例如在 `uv pip compile` 的上下文中，通过一组输入依赖项生成一个"已锁定"的 `requirements.txt` 文件）。`pylock.toml` 是标准化的且与工具无关的，因此将来，由 uv 生成的 `pylock.toml` 文件可以被其他工具安装，反之亦然。

uv 的某些功能无法在 `pylock.toml` 格式中表达；因此，uv 将继续在项目接口中使用 `uv.lock` 格式。

不过，uv 支持将 `pylock.toml` 作为导出目标以及在 `uv pip` CLI 中使用。例如：

- 要将 `uv.lock` 导出为 `pylock.toml` 格式，请运行：`uv export -o pylock.toml`
- 要从一组依赖项生成 `pylock.toml` 文件，请运行：`uv pip compile requirements.in -o pylock.toml`
- 要从 `pylock.toml` 文件安装，请运行：`uv pip sync pylock.toml` 或 `uv pip install -r pylock.toml`
