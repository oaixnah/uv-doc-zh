---
subtitle: Using workspaces
description: 学习如何使用uv创建和管理Python项目的工作区，包括定义工作区成员、排除目录、锁定和同步依赖项。完整指南帮助您高效地组织和发布Python代码。
---

# 使用工作区

受 [Cargo](https://doc.rust-lang.org/cargo/reference/workspaces.html) 同名概念的启发，工作区（workspace）是"一个或多个包（package）的集合，称为_工作区成员_（workspace members），它们被统一管理。"

工作区通过将大型代码库拆分为多个具有公共依赖的包来组织代码。可以这样理解：一个基于 FastAPI 的 Web 应用程序，以及一系列作为独立 Python 包进行版本管理和维护的库，所有这些都位于同一个 Git 仓库中。

在工作区中，每个包定义自己的 `pyproject.toml`，但工作区共享一个单一的锁文件（lockfile），确保工作区使用一组一致的依赖项运行。

因此，`uv lock` 会一次性对整个工作区进行操作，而 `uv run` 和 `uv sync` 默认对工作区根目录进行操作，不过两者都接受 `--package` 参数，允许你从工作区的任意目录在特定工作区成员中运行命令。

## 入门

要创建工作区，请在 `pyproject.toml` 中添加一个 `tool.uv.workspace` 表，这将隐式地在所在包处创建一个工作区根目录。

!!! tip

    默认情况下，在现有包内运行 `uv init` 会将新创建的成员添加到工作区中，如果工作区根目录中尚不存在 `tool.uv.workspace` 表，则会自动创建。

在定义工作区时，你必须指定 `members`（必需）和 `exclude`（可选）键，它们分别指示工作区包含或排除特定目录作为成员，并接受 glob 列表：

```toml title="pyproject.toml"
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder", "tqdm>=4,<5"]

[tool.uv.sources]
bird-feeder = { workspace = true }

[tool.uv.workspace]
members = ["packages/*"]
exclude = ["packages/seeds"]
```

每个被 `members` glob 包含（且未被 `exclude` glob 排除）的目录都必须包含一个 `pyproject.toml` 文件。不过，工作区成员可以是[应用程序](./init.md#applications)或[库](./init.md#libraries)；两者在工作区上下文中都受支持。

每个工作区都需要一个根目录，该根目录_也_是工作区成员。在上面的示例中，`albatross` 是工作区根目录，工作区成员包括 `packages` 目录下的所有项目，但 `seeds` 除外。

默认情况下，`uv run` 和 `uv sync` 对工作区根目录进行操作。例如，在上面的示例中，`uv run` 和 `uv run --package albatross` 是等价的，而 `uv run --package bird-feeder` 则会在 `bird-feeder` 包中运行命令。

## 工作区源

在工作区内，对工作区成员的依赖通过 [`tool.uv.sources`](./dependencies.md) 来配置，如下所示：

```toml title="pyproject.toml"
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder", "tqdm>=4,<5"]

[tool.uv.sources]
bird-feeder = { workspace = true }

[tool.uv.workspace]
members = ["packages/*"]

[build-system]
requires = ["uv_build>=0.11.23,<0.12"]
build-backend = "uv_build"
```

在此示例中，`albatross` 项目依赖于 `bird-feeder` 项目，后者是工作区的一个成员。`tool.uv.sources` 表中的 `workspace = true` 键值对表示 `bird-feeder` 依赖应由工作区提供，而不是从 PyPI 或其他注册源获取。

!!! note

    工作区成员之间的依赖是可编辑的（editable）。

工作区根目录中的任何 `tool.uv.sources` 定义都会应用于所有成员，除非在特定成员的 `tool.uv.sources` 中被覆盖。例如，给定以下 `pyproject.toml`：

```toml title="pyproject.toml"
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder", "tqdm>=4,<5"]

[tool.uv.sources]
bird-feeder = { workspace = true }
tqdm = { git = "https://github.com/tqdm/tqdm" }

[tool.uv.workspace]
members = ["packages/*"]

[build-system]
requires = ["uv_build>=0.11.23,<0.12"]
build-backend = "uv_build"
```

默认情况下，每个工作区成员都会从 GitHub 安装 `tqdm`，除非某个特定成员在其自己的 `tool.uv.sources` 表中覆盖了 `tqdm` 条目。

!!! note

    如果某个工作区成员为某个依赖提供了 `tool.uv.sources`，它将忽略工作区根目录中针对同一依赖的任何 `tool.uv.sources`，即使该成员的源受到与当前平台不匹配的[标记（marker）](dependencies.md#platform-specific-sources)限制也是如此。

## 工作区布局

最常见的工作区布局可以理解为一个根项目加上一系列附属库。

例如，继续上面的示例，此工作区在 `albatross` 处有一个显式的根目录，在 `packages` 目录中有两个库（`bird-feeder` 和 `seeds`）：

```text
albatross
├── packages
│   ├── bird-feeder
│   │   ├── pyproject.toml
│   │   └── src
│   │       └── bird_feeder
│   │           ├── __init__.py
│   │           └── foo.py
│   └── seeds
│       ├── pyproject.toml
│       └── src
│           └── seeds
│               ├── __init__.py
│               └── bar.py
├── pyproject.toml
├── README.md
├── uv.lock
└── src
    └── albatross
        └── main.py
```

由于 `seeds` 在 `pyproject.toml` 中被排除了，该工作区共有两个成员：`albatross`（根目录）和 `bird-feeder`。

## 何时（不）使用工作区

工作区旨在促进在单个仓库中开发多个相互关联的包。随着代码库复杂性的增长，将其拆分为更小的、可组合的包会很有帮助，每个包都有自己的依赖项和版本约束。

工作区有助于强制隔离和关注点分离。例如，在 uv 中，我们为核心库和命令行界面分别设置了独立的包，这使我们能够独立于 CLI 测试核心库，反之亦然。

工作区的其他常见用例包括：

- 一个库，其性能关键的子程序在扩展模块（Rust、C++ 等）中实现。
- 一个带有插件系统的库，其中每个插件都是一个独立的工作区包，并依赖于根包。

工作区_不_适合成员之间存在冲突需求，或者希望每个成员拥有独立虚拟环境的情况。在这种情况下，路径依赖通常是更好的选择。例如，与其将 `albatross` 及其成员分组到一个工作区中，你始终可以将每个包定义为其自己的独立项目，并在 `tool.uv.sources` 中将包间依赖定义为路径依赖：

```toml title="pyproject.toml"
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder", "tqdm>=4,<5"]

[tool.uv.sources]
bird-feeder = { path = "packages/bird-feeder" }

[build-system]
requires = ["uv_build>=0.11.23,<0.12"]
build-backend = "uv_build"
```

这种方法传达了许多相同的好处，但允许对依赖解析和虚拟环境管理进行更细粒度的控制（缺点是 `uv run --package` 不再可用；相反，命令必须从相关包目录中运行）。

最后，uv 的工作区为整个工作区强制执行单一的 `requires-python`，取所有成员的 `requires-python` 值的交集。如果你需要支持在不受工作区其余部分支持的 Python 版本上测试某个成员，你可能需要使用 `uv pip` 在单独的虚拟环境中安装该成员。

!!! note

    由于 Python 不提供依赖隔离，uv 无法确保某个包仅使用其声明的依赖项而不使用其他内容。特别是对于工作区，uv 无法确保包不会导入由另一个工作区成员声明的依赖项。
