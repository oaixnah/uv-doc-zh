---
subtitle: Using workspaces
---

# 使用工作区

受同名 [Cargo](https://doc.rust-lang.org/cargo/reference/workspaces.html) 概念的启发，工作区是“一个或多个包的集合，称为 _工作区成员_，它们被一起管理。”

工作区通过将大型代码库拆分为具有共同依赖项的多个包来组织它们。想象一下：一个基于 FastAPI 的 Web 应用程序，以及一系列作为独立 Python 包进行版本控制和维护的库，所有这些都在同一个 Git 仓库中。

在工作区中，每个包都定义了自己的 `pyproject.toml`，但工作区共享一个锁文件，确保工作区使用一组一致的依赖项运行。

因此，`uv lock` 一次性对整个工作区进行操作，而 `uv run` 和 `uv sync` 默认在工作区根目录上操作，不过两者都接受 `--package` 参数，允许您从任何工作区目录在特定的工作区成员中运行命令。

## 入门

要创建工作区，请将 `tool.uv.workspace` 表添加到 `pyproject.toml` 中，这将隐式地在该包中创建一个以其为根的工作区。

!!! tip

    默认情况下，在现有包内运行 `uv init` 会将新创建的成员添加到工作区，如果工作区根目录中尚不存在 `tool.uv.workspace` 表，则会创建一个。

在定义工作区时，您必须指定 `members`（必需）和 `exclude`（可选）键，它们分别指示工作区包含或排除特定目录作为成员，并接受 glob 列表：

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

`members` glob 包含（且未被 `exclude` glob 排除）的每个目录都必须包含一个 `pyproject.toml` 文件。但是，工作区成员可以是[应用程序](./init.md#_3)或[库](./init.md#_5)；两者在工作区上下文中都受支持。

每个工作区都需要一个根，它_也_是一个工作区成员。在上面的示例中，`albatross` 是工作区根，工作区成员包括 `packages` 目录下的所有项目，`seeds` 除外。

默认情况下，`uv run` 和 `uv sync` 在工作区根目录上操作。例如，在上面的示例中，`uv run` 和 `uv run --package albatross` 是等效的，而 `uv run --package bird-feeder` 将在 `bird-feeder` 包中运行命令。

## 工作区源

在工作区中，对工作区成员的依赖关系通过 [`tool.uv.sources`](./dependencies.md) 来实现，如下所示：

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
requires = ["hatchling"]
build-backend = "hatchling.build"
```

在此示例中，`albatross` 项目依赖于 `bird-feeder` 项目，后者是工作区的成员。`tool.uv.sources` 表中的 `workspace = true` 键值对表示 `bird-feeder` 依赖项应由工作区提供，而不是从 PyPI 或其他注册表获取。

!!! note

    工作区成员之间的依赖关系是可编辑的。

工作区根目录中的任何 `tool.uv.sources` 定义都适用于所有成员，除非在特定成员的 `tool.uv.sources` 中被覆盖。例如，给定以下 `pyproject.toml`：

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
requires = ["hatchling"]
build-backend = "hatchling.build"
```

默认情况下，每个工作区成员都会从 GitHub 安装 `tqdm`，除非特定成员在其自己的 `tool.uv.sources` 表中覆盖 `tqdm` 条目。

!!! note

    如果工作区成员为某个依赖项提供了 `tool.uv.sources`，它将忽略工作区根目录中该依赖项的任何 `tool.uv.sources`，即使该成员的源受与当前平台不匹配的[标记](dependencies.md#_13)限制。

## 工作区布局

最常见的工作区布局可以被认为是一个根项目以及一系列附带的库。

例如，继续上面的示例，此工作区在 `albatross` 处有一个显式根，在 `packages` 目录中有两个库（`bird-feeder` 和 `seeds`）：

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

由于 `seeds` 在 `pyproject.toml` 中被排除了，因此工作区总共有两个成员：`albatross`（根）和 `bird-feeder`。

## 何时（不）使用工作区

工作区旨在促进在单个存储库中开发多个相互关联的包。随着代码库复杂性的增长，将其拆分为更小、可组合的包可能会有所帮助，每个包都有自己的依赖项和版本约束。

工作区有助于强制隔离和关注点分离。例如，在 uv 中，我们为核心库和命令行界面提供了单独的包，使我们能够独立于 CLI 测试核心库，反之亦然。

工作区的其他常见用例包括：

- 一个库，其性能关键的子例程在扩展模块（Rust、C++ 等）中实现。
- 一个带有插件系统的库，其中每个插件都是一个单独的工作区包，对根有依赖关系。

工作区_不_适用于成员具有冲突要求或希望为每个成员提供单独的虚拟环境的情况。在这种情况下，路径依赖通常是更可取的。例如，您可以始终将每个包定义为自己独立的项目，而不是将 `albatross` 及其成员分组在工作区中，包间依赖关系在 `tool.uv.sources` 中定义为路径依赖：

```toml title="pyproject.toml"
[project]
name = "albatross"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["bird-feeder", "tqdm>=4,<5"]

[tool.uv.sources]
bird-feeder = { path = "packages/bird-feeder" }

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

这种方法传达了许多相同的好处，但允许对依赖关系解析和虚拟环境管理进行更细粒度的控制（缺点是 `uv run --package` 不再可用；相反，必须从相关的包目录运行命令）。

最后，uv 的工作区为整个工作区强制执行单个 `requires-python`，取所有成员 `requires-python` 值的交集。如果您需要支持在工作区其余部分不支持的 Python 版本上测试给定成员，则可能需要使用 `uv pip` 在单独的虚拟环境中安装该成员。

!!! note

    由于 Python 不提供依赖隔离，uv 无法确保包使用其声明的依赖项而没有其他依赖项。特别是对于工作区，uv 无法确保包不会导入由另一个工作区成员声明的依赖项。
