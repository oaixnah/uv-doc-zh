---
subtitle: Configuration files
description: 学习如何使用uv配置Python项目，包括项目级别和用户级别配置文件、配置选项和优先级。完整指南帮助您自定义uv的行为，以满足您的项目需求。
---

# 配置文件

uv 在项目级别和用户级别都支持持久化配置文件。

具体来说，uv 会在当前目录或最近的父目录中搜索 `pyproject.toml` 或 `uv.toml` 文件。

!!! note

    对于在用户级别操作的 `tool` 命令，本地配置文件将被忽略。相反，uv 将专门从用户级配置（例如 `~/.config/uv/uv.toml`）和系统级配置（例如 `/etc/uv/uv.toml`）中读取。

在工作区中，uv 将从工作区根目录开始搜索，忽略在工作区成员中定义的任何配置。由于工作区被锁定为单个单元，因此配置在所有成员之间共享。

如果找到 `pyproject.toml` 文件，uv 将从 `[tool.uv]` 表中读取配置。例如，要设置持久的索引 URL，请将以下内容添加到 `pyproject.toml` 中：

```toml title="pyproject.toml"
[[tool.uv.index]]
url = "https://test.pypi.org/simple"
default = true
```

（如果没有这样的表，`pyproject.toml` 文件将被忽略，uv 将继续在目录层次结构中搜索。）

uv 还会搜索 `uv.toml` 文件，这些文件遵循相同的结构，但省略了 `[tool.uv]` 前缀。例如：

```toml title="uv.toml"
[[index]]
url = "https://test.pypi.org/simple"
default = true
```

!!! note

    `uv.toml` 文件优先于 `pyproject.toml` 文件，因此如果目录中同时存在 `uv.toml` 和 `pyproject.toml` 文件，则将从 `uv.toml` 读取配置，而附带的 `pyproject.toml` 中的 `[tool.uv]` 部分将被忽略。

uv 还将发现用户级配置，位于 `~/.config/uv/uv.toml`（或 `$XDG_CONFIG_HOME/uv/uv.toml`）在 macOS 和 Linux 上，或 `%APPDATA%\uv\uv.toml` 在 Windows 上；以及系统级配置，位于 `/etc/uv/uv.toml`（或 `$XDG_CONFIG_DIRS/uv/uv.toml`）在 macOS 和 Linux 上，或 `%SYSTEMDRIVE%\ProgramData\uv\uv.toml` 在 Windows 上。

用户级和系统级配置必须使用 `uv.toml` 格式，而不是 `pyproject.toml` 格式，因为 `pyproject.toml` 旨在定义一个 Python _项目_。

如果同时找到项目级、用户级和系统级配置文件，这些设置将被合并，项目级配置优先于用户级配置，用户级配置优先于系统级配置。（如果找到多个系统级配置文件，例如在 `/etc/uv/uv.toml` 和 `$XDG_CONFIG_DIRS/uv/uv.toml` 中都存在，则只会使用第一个发现的文件，XDG 优先。）

例如，如果一个字符串、数字或布尔值同时存在于项目级和用户级配置表中，则将使用项目级的值，而忽略用户级的值。如果一个数组同时存在于两个表中，则数组将被连接起来，项目级的设置会出现在合并后数组的前面。

通过环境变量提供的设置优先于持久化配置，而通过命令行提供的设置则优先于两者。

uv 接受一个 `--no-config` 命令行参数，提供该参数后，将禁用任何持久化配置的发现。

uv 还接受一个 `--config-file` 命令行参数，它接受一个 `uv.toml` 文件的路径作为配置文件。提供该参数后，此文件将替代_任何_已发现的配置文件（例如，用户级配置将被忽略）。

## 设置

有关可用设置的枚举，请参阅[设置](../reference/settings/configuration.md)。

## `.env`

`uv run` 可以从 dotenv 文件（例如 `.env`、`.env.local`、`.env.development`）加载环境变量，由 [`dotenvy`](https://github.com/allan2/dotenvy) crate 提供支持。

要从专用位置加载 `.env` 文件，请设置 `UV_ENV_FILE` 环境变量，或将 `--env-file` 标志传递给 `uv run`。

例如，要从当前工作目录中的 `.env` 文件加载环境变量：

```console
$ echo "MY_VAR='Hello, world!'" > .env
$ uv run --env-file .env -- python -c 'import os; print(os.getenv("MY_VAR"))'
Hello, world!
```

`--env-file` 标志可以多次提供，后续文件会覆盖先前文件中定义的值。要通过 `UV_ENV_FILE` 环境变量提供多个文件，请用空格分隔路径（例如 `UV_ENV_FILE="/path/to/file1 /path/to/file2"`）。

要禁用 dotenv 加载（例如，覆盖 `UV_ENV_FILE` 或 `--env-file` 命令行参数），请将 `UV_NO_ENV_FILE` 环境变量设置为 `1`，或将 `--no-env-file` 标志传递给 `uv run`。

如果同一个变量在环境和 `.env` 文件中都有定义，则环境中的值将优先。

## 配置 pip 接口

提供了一个专用的 [`[tool.uv.pip]`](../pip/index.md) 部分，用于配置_仅_ `uv pip` 命令行界面。此部分中的设置不会应用于 `uv pip` 命名空间之外的 `uv` 命令。但是，此部分中的许多设置在顶级命名空间中都有对应的设置，这些设置_确实_适用于 `uv pip` 接口，除非它们被 `uv.pip` 部分中的值覆盖。

`uv.pip` 设置旨在与 pip 的接口紧密保持一致，并单独声明以保持兼容性，同时允许全局设置使用替代设计（例如 `--no-build`）。

例如，在 `[tool.uv.pip]` 下设置 `index-url`，如下面的 `pyproject.toml` 所示，将只影响 `uv pip` 子命令（例如 `uv pip install`，但不影响 `uv sync`、`uv lock` 或 `uv run`）：

```toml title="pyproject.toml"
[tool.uv.pip]
index-url = "https://test.pypi.org/simple"
```
