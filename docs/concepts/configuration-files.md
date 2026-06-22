---
subtitle: Configuration files
description: 学习如何使用uv配置Python项目，包括项目级别和用户级别配置文件、配置选项和优先级。完整指南帮助您自定义uv的行为，以满足您的项目需求。
---

# 配置文件

uv 支持在项目级别和用户级别使用持久化配置文件。

具体来说，uv 会在当前目录或最近的父目录中搜索 `pyproject.toml` 或 `uv.toml` 文件。

!!! note

    对于 `tool` 命令（在用户级别运行），本地配置文件将被忽略。相反，uv 将仅读取用户级别配置
    （例如 `~/.config/uv/uv.toml`）和系统级别配置（例如 `/etc/uv/uv.toml`）。

在工作空间（workspace）中，uv 将从工作空间根目录开始搜索，忽略工作空间成员中定义的任何配置。由于工作空间作为单个单元进行锁定，因此配置在所有成员之间共享。

如果找到 `pyproject.toml` 文件，uv 将从 `[tool.uv]` 表中读取配置。例如，要设置一个持久化的索引 URL，可以将以下内容添加到 `pyproject.toml` 中：

```toml title="pyproject.toml"
[[tool.uv.index]]
url = "https://test.pypi.org/simple"
default = true
```

（如果没有这样的表，则 `pyproject.toml` 文件将被忽略，uv 将继续在目录层级中向上搜索。）

uv 还会搜索 `uv.toml` 文件，该文件遵循相同的结构，但省略了 `[tool.uv]` 前缀。例如：

```toml title="uv.toml"
[[index]]
url = "https://test.pypi.org/simple"
default = true
```

!!! note

    `uv.toml` 文件优先于 `pyproject.toml` 文件，因此如果目录中同时存在 `uv.toml` 和
    `pyproject.toml` 文件，配置将从 `uv.toml` 读取，而相应的 `pyproject.toml` 中的
    `[tool.uv]` 部分将被忽略。

uv 还会在用户级别和系统级别的[配置目录](../reference/storage.md#configuration-directories)中发现 `uv.toml` 配置文件，例如，在 macOS 和 Linux 上，用户级别配置位于 `~/.config/uv/uv.toml`，在 Windows 上位于 `%APPDATA%\uv\uv.toml`；系统级别配置在 macOS 和 Linux 上位于 `/etc/uv/uv.toml`，在 Windows 上位于 `%PROGRAMDATA%\uv\uv.toml`。

!!! important

    用户级别和系统级别的配置文件不能使用 `pyproject.toml` 格式。

如果同时找到项目级别、用户级别和系统级别的配置文件，设置将被合并，其中项目级别配置优先于用户级别配置，用户级别配置优先于系统级别配置。（如果找到多个系统级别配置文件，例如同时在 `/etc/uv/uv.toml` 和 `$XDG_CONFIG_DIRS/uv/uv.toml` 中，则仅使用第一个发现的文件，其中 XDG 优先。）

例如，如果字符串、数字或布尔值同时出现在项目级别和用户级别配置表中，将使用项目级别的值，用户级别的值将被忽略。如果数组同时出现在两个表中，数组将被合并，项目级别的设置将出现在合并后数组的前面。

通过环境变量提供的设置优先于持久化配置，而通过命令行提供的设置优先于两者。

uv 接受 `--no-config` 命令行参数，当提供该参数时，将禁用任何持久化配置的发现。

uv 还接受 `--config-file` 命令行参数，该参数接受一个 `uv.toml` 文件路径作为配置文件。当提供该参数时，此文件将替代*任何*已发现的配置文件（例如，用户级别配置将被忽略）。

## 设置

请参阅[设置参考](../reference/settings.md)了解可用设置的完整列表。

## 环境变量文件

`uv run` 可以从 dotenv 文件（例如 `.env`、`.env.local`、`.env.development`）加载环境变量，该功能由 [`dotenvy`](https://github.com/allan2/dotenvy) crate 提供支持。

要从指定位置加载 `.env` 文件，可以设置 `UV_ENV_FILE` 环境变量，或向 `uv run` 传递 `--env-file` 标志。

例如，从当前工作目录中的 `.env` 文件加载环境变量：

```console
$ echo "MY_VAR='Hello, world!'" > .env
$ uv run --env-file .env -- python -c 'import os; print(os.getenv("MY_VAR"))'
Hello, world!
```

`--env-file` 标志可以多次提供，后续文件会覆盖之前文件中定义的值。要通过 `UV_ENV_FILE` 环境变量提供多个文件，请用空格分隔路径（例如 `UV_ENV_FILE="/path/to/file1 /path/to/file2"`）。

要禁用 dotenv 加载（例如，覆盖 `UV_ENV_FILE` 或 `--env-file` 命令行参数），请将 `UV_NO_ENV_FILE` 环境变量设置为 `1`，或向 `uv run` 传递 `--no-env-file` 标志。

如果同一个变量在环境变量和 `.env` 文件中都有定义，环境变量中的值将优先。

## 配置 pip 接口

提供了一个专门的 [`[tool.uv.pip]`](../reference/settings.md#pip) 部分，用于配置*仅* `uv pip` 命令行接口。此部分中的设置不会应用于 `uv pip` 命名空间之外的 `uv` 命令。但是，此部分中的许多设置在顶级命名空间中都有对应的设置，这些设置*会*应用于 `uv pip` 接口，除非被 `uv.pip` 部分中的值覆盖。

`uv.pip` 设置旨在紧密遵循 pip 的接口，并单独声明以保持兼容性，同时允许全局设置使用替代设计（例如 `--no-build`）。

例如，在 `[tool.uv.pip]` 下设置 `index-url`，如下面的 `pyproject.toml` 所示，将仅影响 `uv pip` 子命令（例如 `uv pip install`，但不会影响 `uv sync`、`uv lock` 或 `uv run`）：

```toml title="pyproject.toml"
[tool.uv.pip]
index-url = "https://test.pypi.org/simple"
```
