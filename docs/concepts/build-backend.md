---
subtitle: Build backend
description: 学习如何使用uv作为Python项目的构建后端，包括默认构建后端、构建后端的作用、uv 构建后端的优势和配置选项。完整指南帮助您选择和使用 uv 构建后端。
---

# uv 构建后端

构建后端（build backend）负责将源代码树（即一个目录）转换为源代码分发版（source distribution）或 wheel 包。

uv 支持所有构建后端（遵循 [PEP 517](https://peps.python.org/pep-0517/) 规范），但也提供了一个原生构建后端（`uv_build`），它与 uv 紧密集成，能够提升性能和用户体验。

## 选择构建后端

uv 构建后端是大多数 Python 项目的理想选择。它拥有合理的默认配置，目标是为大多数用户实现零配置即可使用，同时提供灵活的配置选项以适应大多数 Python 项目结构。它与 uv 紧密集成，能够改善提示信息和用户体验。它会验证项目的元数据和结构，帮助避免常见错误。最后，它的速度非常快。

uv 构建后端目前**仅支持纯 Python 代码**。如果要构建[带扩展模块的库](../concepts/projects/init.md#projects-with-extension-modules)，则需要使用其他构建后端。

!!! tip

    虽然 uv 构建后端支持多种配置选项来调整项目结构，但当需要构建脚本或更灵活的项目布局时，建议考虑使用
    [hatchling](https://hatch.pypa.io/latest/config/build/#build-system) 构建后端。

## 使用 uv 构建后端

要在现有项目中使用 uv 作为构建后端，请在 `pyproject.toml` 的
[`[build-system]`](../concepts/projects/config.md#build-systems) 部分中添加 `uv_build`：

```toml title="pyproject.toml"
[build-system]
requires = ["uv_build>=0.11.23,<0.12"]
build-backend = "uv_build"
```

!!! note

    uv 构建后端遵循与 uv 相同的[版本策略](../reference/policies/versioning.md)。为 `uv_build` 设置版本上限可以确保在新版本发布时，你的包仍然能够正确构建。

要创建一个使用 uv 构建后端的新项目，请使用 `uv init`：

```console
$ uv init
```

当项目被构建时（例如通过 [`uv build`](../guides/package.md)），uv 构建后端将用于创建源代码分发版和 wheel 包。

## 内置构建后端

构建后端作为一个独立的包（`uv_build`）发布，针对可移植性和较小的二进制体积进行了优化。然而，`uv` 可执行文件本身也包含了一份构建后端的副本，在 uv 执行的构建过程中（例如 `uv build`），如果其版本与 `uv_build` 的要求兼容，则会使用该内置副本。如果不兼容，则会使用兼容版本的 `uv_build` 包。其他构建前端（如 `python -m build`）则始终使用 `uv_build` 包，通常会选择最新的兼容版本。

## 模块（Modules）

Python 包应包含一个或多个 Python 模块，即包含 `__init__.py` 的目录。默认情况下，期望在 `src/<package_name>/__init__.py` 处有一个单一的根模块。

例如，一个名为 `foo` 的项目结构如下：

```text
pyproject.toml
src
└── foo
    └── __init__.py
```

uv 会对包名进行规范化以确定默认的模块名：包名会被转换为小写，点号和连字符会被替换为下划线，例如 `Foo-Bar` 会被转换为 `foo_bar`。

`src/` 目录是模块发现的默认目录。

这些默认值可以通过 `module-name` 和 `module-root` 设置进行更改。例如，若要在根目录下使用 `FOO` 模块，项目结构如下：

```text
pyproject.toml
FOO
└── __init__.py
```

正确的构建配置如下：

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-name = "FOO"
module-root = ""
```

## 命名空间包（Namespace packages）

命名空间包适用于多个包将模块写入共享命名空间的场景。

命名空间包模块通过 `module-name` 中的 `.` 来标识。例如，要将模块 `bar` 打包在共享命名空间 `foo` 中，项目结构如下：

```text
pyproject.toml
src
└── foo
    └── bar
        └── __init__.py
```

而 `module-name` 配置如下：

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-name = "foo.bar"
```

!!! important

    `foo` 目录中不包含 `__init__.py` 文件，因为它是共享命名空间模块。

也可以使用包含多个根模块的复杂命名空间包，例如项目结构如下：

```text
pyproject.toml
src
├── foo
│   └── __init__.py
└── bar
    └── __init__.py
```

虽然我们不推荐这种结构（即，建议改用包含多个包的工作空间（workspace）），但可以通过将 `module-name` 设置为名称列表来支持：

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-name = ["foo", "bar"]
```

对于包含许多模块或复杂命名空间的包，可以使用 `namespace = true` 选项来避免显式声明每个模块名，例如：

```toml title="pyproject.toml"
[tool.uv.build-backend]
namespace = true
```

!!! warning

    使用 `namespace = true` 会禁用安全检查。除非是遗留项目，否则强烈建议使用显式的模块名列表。

`namespace` 选项也可以与 `module-name` 结合使用来显式声明根模块，例如项目结构如下：

```text
pyproject.toml
src
└── foo
    ├── bar
    │   └── __init__.py
    └── baz
        └── __init__.py
```

推荐的配置如下：

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-name = "foo"
namespace = true
```

## 类型存根包（Stub packages）

构建后端也支持构建类型存根包（type stub packages），通过包名或模块名上的 `-stubs` 后缀来标识，例如 `foo-stubs`。类型存根包的模块名必须以 `-stubs` 结尾，因此 uv 不会将 `-` 规范化为下划线。此外，uv 会搜索 `__init__.pyi` 文件。例如，项目结构如下：

```text
pyproject.toml
src
└── foo-stubs
    └── __init__.pyi
```

[命名空间包](#namespace-packages)也支持类型存根模块。

## 文件包含与排除

构建后端负责决定源代码树中的哪些文件应被打包到分发版中。

要确定源代码分发版中包含哪些文件，uv 首先添加要包含的文件和目录，然后移除要排除的文件和目录。这意味着排除规则始终优先于包含规则。

默认情况下，uv 会排除 `__pycache__`、`*.pyc` 和 `*.pyo`。

在构建源代码分发版（source distribution）时，以下文件和目录会被包含：

- `pyproject.toml`。如果 uv 检测到仅限 TOML 1.1 的语法，会发出警告并自动启用 `toml-backwards-compatibility` 预览功能：`pyproject.toml` 会被重新格式化以保持向后兼容性，原始文件则保留为 `pyproject.toml.orig`。传入 `--preview-feature toml-backwards-compatibility` 可以显式启用该功能并抑制警告。
- [`tool.uv.build-backend.module-root`](../reference/settings/project-metadata.md#build-backend_module-root) 下的[模块](#modules)。
- `project.license-files` 和 `project.readme` 引用的文件。
- [`tool.uv.build-backend.data`](../reference/settings/project-metadata.md#build-backend_data) 下的所有目录。
- 匹配 [`tool.uv.build-backend.source-include`](../reference/settings/project-metadata.md#build-backend_source-include) 模式的所有文件。

然后，从这些内容中移除匹配 [`tool.uv.build-backend.source-exclude`](../reference/settings/project-metadata.md#build-backend_source-exclude) 和[默认排除规则](../reference/settings/project-metadata.md#build-backend_default-excludes)的项目。

在构建 wheel 包时，以下文件和目录会被包含：

- [`tool.uv.build-backend.module-root`](../reference/settings/project-metadata.md#build-backend_module-root) 下的[模块](#modules)
- `project.license-files` 引用的文件，会被复制到 `.dist-info` 目录中。
- `project.readme`，会被复制到项目元数据中。
- [`tool.uv.build-backend.data`](../reference/settings/project-metadata.md#build-backend_data) 下的所有目录，会被复制到 `.data` 目录中。

然后，从这些内容中移除 [`tool.uv.build-backend.source-exclude`](../reference/settings/project-metadata.md#build-backend_source-exclude)、[`tool.uv.build-backend.wheel-exclude`](../reference/settings/project-metadata.md#build-backend_wheel-exclude) 和默认排除规则。应用源代码分发版排除规则是为了避免从源代码树直接构建 wheel 时包含比"源代码树 → 源代码分发版 → wheel"流程更多的文件。

wheel 没有特定的包含规则。只能有一个顶层模块，并且所有数据文件必须位于模块根目录下或相应的[数据目录](../reference/settings/project-metadata.md#build-backend_data)中。大多数包会将小型数据文件与源代码一起存储在模块根目录下。

!!! tip

    当通过非 uv 的构建前端（如 pip 或 `python -m build`）使用 uv 构建后端时，可以通过环境变量启用调试日志：`RUST_LOG=uv=debug` 或 `RUST_LOG=uv=verbose`。当通过 uv 使用时，uv 构建后端会共享 uv 的详细程度级别。

### 包含与排除语法

包含规则是锚定的（anchored），这意味着 `pyproject.toml` 仅包含 `<root>/pyproject.toml`，而不会包含 `<root>/bar/pyproject.toml`。要递归包含目录下的所有文件，请使用 `/**` 后缀，例如 `src/**`。递归包含同样是锚定的，例如 `assets/**/sample.csv` 会包含 `<root>/assets` 目录或其任何子目录中的所有 `sample.csv` 文件。

!!! note

    为了性能和可复现性，请避免使用无锚点的模式，如 `**/sample.csv`。

排除规则是非锚定的，这意味着 `__pycache__` 会排除所有名为 `__pycache__` 的目录，无论其父目录是什么。排除目录的所有子项也会被一并排除。要锚定一个目录，请使用 `/` 前缀，例如 `/dist` 将仅排除 `<root>/dist`。

所有接受模式的字段都使用 [PEP 639](https://peps.python.org/pep-0639/#add-license-FILES-key) 中定义的简化可移植 glob 语法，并额外支持使用反斜杠转义字符。
