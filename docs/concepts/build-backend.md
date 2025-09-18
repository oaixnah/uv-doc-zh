---
subtitle: Build backend
---

# 构建后端

!!! note

    目前，`uv init` 的默认构建后端是
    [hatchling](https://pypi.org/project/hatchling/)。在未来的版本中，这将更改为 `uv`。

构建后端将源树（即目录）转换为源发行版或 wheel。

uv 支持所有构建后端（由 [PEP 517](https://peps.python.org/pep-0517/) 指定），但也提供了一个原生的构建后端（`uv_build`），它与 uv 紧密集成以提高性能和用户体验。

## 选择构建后端

对于大多数 Python 项目来说，uv 构建后端是一个很好的选择。它有合理的默认值，目标是为大多数用户实现零配置，但提供了灵活的配置以适应大多数 Python 项目结构。它与 uv 紧密集成，以改善消息传递和用户体验。它验证项目元数据和结构，防止常见错误。而且，最后，它非常快。

uv 构建后端目前**只支持纯 Python 代码**。构建[带有扩展模块的库](../concepts/projects/init.md#_6)需要一个替代后端。

!!! tip

    虽然后端支持许多用于配置项目结构的选项，但当需要构建脚本或更灵活的项目布局时，请考虑改用 [hatchling](https://hatch.pypa.io/latest/config/build/#build-system) 构建后端。

## 使用 uv 构建后端

要在现有项目中使用 uv 作为构建后端，请将 `uv_build` 添加到 `pyproject.toml` 中的 [`[build-system]`](../concepts/projects/config.md#build-systems) 部分：

```toml title="pyproject.toml"
[build-system]
requires = ["uv_build>=0.8.18,<0.8.0"]
build-backend = "uv_build"
```

!!! note

    uv 构建后端遵循与 uv 相同的[版本控制策略](../reference/policies/versioning.md)。在 `uv_build` 版本上包含一个上限可确保您的包在新版本发布时能够继续正确构建。

要创建一个使用 uv 构建后端的新项目，请使用 `uv init`：

```console
$ uv init --build-backend uv
```

当项目构建时，例如使用 [`uv build`](../guides/package.md)，uv 构建后端将用于创建源发行版和 wheel。

## 捆绑的构建后端

构建后端作为单独的包（`uv_build`）发布，该包针对可移植性和较小的二进制大小进行了优化。但是，`uv` 可执行文件也包含构建后端的一个副本，在 uv 执行构建期间（例如，在 `uv build` 期间），如果其版本与 `uv_build` 要求兼容，则将使用该副本。如果不兼容，则将使用 `uv_build` 包的兼容版本。其他构建前端，例如 `python -m build`，将始终使用 `uv_build` 包，通常选择最新的兼容版本。

## 模块

Python 包应包含一个或多个 Python 模块，这些模块是包含 `__init__.py` 的目录。默认情况下，单个根模块应位于 `src/<package_name>/__init__.py`。

例如，名为 `foo` 的项目的结构将是：

```text
pyproject.toml
src
└── foo
    └── __init__.py
```

uv 会规范化包名称以确定默认模块名称：包名称将转换为小写，点和短划线将替换为下划线，例如，`Foo-Bar` 将转换为 `foo_bar`。

`src/` 目录是模块发现的默认目录。

可以使用 `module-name` 和 `module-root` 设置更改这些默认值。例如，要在根目录中使用 `FOO` 模块，如项目结构所示：

```text
pyproject.toml
FOO
└── __init__.py
```

正确的构建配置将是：

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-name = "FOO"
module-root = ""
```

## 命名空间包

命名空间包旨在用于多个包将模块写入共享命名空间的用例。

命名空间包模块由 `module-name` 中的 `.` 标识。例如，要将模块 `bar` 打包到共享命名空间 `foo` 中，项目结构将是：

```text
pyproject.toml
src
└── foo
    └── bar
        └── __init__.py
```

`module-name` 配置将是：

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-name = "foo.bar"
```

!!! important

    `__init__.py` 文件不包含在 `foo` 中，因为它是共享的命名空间模块。

也可能有一个具有多个根模块的复杂命名空间包，例如，项目结构如下：

```text
pyproject.toml
src
├── foo
│   └── __init__.py
└── bar
    └── __init__.py
```

虽然我们不推荐这种结构（即，您应该改用具有多个包的工作区），但它通过 `namespace` 选项得到支持：

```toml title="pyproject.toml"
[tool.uv.build-backend]
namespace = true
```

## 存根包

构建后端还支持构建类型存根包，这些包由包或模块名称上的 `-stubs` 后缀标识，例如 `foo-stubs`。类型存根包的模块名称必须
以 `-stubs` 结尾，因此 uv 不会将 `-` 规范化为下划线。此外，uv 将搜索 `__init__.pyi` 文件。例如，项目结构将是：

```text
pyproject.toml
src
└── foo-stubs
    └── __init__.pyi
```

[命名空间包](#namespace-packages)也支持类型存根模块。

## 文件包含和排除

构建后端负责确定源树中的哪些文件应打包到发行版中。

为了确定在源发行版中包含哪些文件，uv 首先添加包含的文件和目录，然后删除排除的文件和目录。这意味着排除项始终优先于包含项。

默认情况下，uv 排除 `__pycache__`、`*.pyc` 和 `*.pyo`。

构建源发行版时，将包含以下文件和目录：

- `pyproject.toml`
- [`tool.uv.build-backend.module-root`](../reference/settings.md#build-backend_module-root) 下的[模块](#_4)。
- `project.license-files` 和 `project.readme` 引用的文件。
- [`tool.uv.build-backend.data`](../reference/settings.md#build-backend_data) 下的所有目录。
- 与 [`tool.uv.build-backend.source-include`](../reference/settings.md#build-backend_source-include) 中的模式匹配的所有文件。

从中删除与 [`tool.uv.build-backend.source-exclude`](../reference/settings.md#build-backend_source-exclude) 和
[默认排除项](../reference/settings.md#build-backend_default-excludes)匹配的项目。

构建 wheel 时，将包含以下文件和目录：

- [`tool.uv.build-backend.module-root`](../reference/settings.md#build-backend_module-root) 下的[模块](#_4)
- `project.license-files` 引用的文件，这些文件将复制到 `.dist-info` 目录中。
- `project.readme`，它将复制到项目元数据中。
- [`tool.uv.build-backend.data`](../reference/settings.md#build-backend_data) 下的所有目录，
  这些目录将复制到 `.data` 目录中。

从中删除 [`tool.uv.build-backend.source-exclude`](../reference/settings.md#build-backend_source-exclude)、[`tool.uv.build-backend.wheel-exclude`](../reference/settings.md#build-backend_wheel-exclude) 和默认排除项。应用源发行版排除项是为了避免从源树到 wheel 源的构建包含比从源树到源发行版到 wheel 的构建更多的文件。

没有特定的 wheel 包含项。只能有一个顶级模块，所有数据文件必须位于模块根目录下或适当的[数据目录](../reference/settings.md#build-backend_data)中。大多数包将小数据存储在模块根目录中，与源代码放在一起。

### 包含和排除语法

包含是锚定的，这意味着 `pyproject.toml` 仅包含 `<root>/pyproject.toml` 而不是 `<root>/bar/pyproject.toml`。要递归包含目录下的所有文件，请使用 `/**` 后缀，例如 `src/**`。递归包含也是锚定的，例如，`assets/**/sample.csv` 包含 `<root>/assets` 或其任何子目录中的所有 `sample.csv` 文件。

!!! note

    为了性能和可再现性，请避免使用没有锚点的模式，例如 `**/sample.csv`。

排除不是锚定的，这意味着 `__pycache__` 排除所有名为 `__pycache__` 的目录，而不管其父目录如何。排除项的所有子项也被排除。要锚定目录，请使用 `/` 前缀，例如，`/dist` 将仅排除 `<root>/dist`。

所有接受模式的字段都使用来自 [PEP 639](https://peps.python.org/pep-0639/#add-license-FILES-key) 的简化的可移植 glob 语法，另外，字符可以用反斜杠转义。
