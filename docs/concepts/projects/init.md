---
title: 创建项目
subtitle: Creating projects
description: 学习如何使用 uv 创建 Python 项目，包括应用程序、库项目以及带扩展模块的项目。了解项目结构、打包应用、命令入口点、构建系统和最小化项目创建。完整指南帮助您高效地组织和发布 Python 代码。
---

# 创建项目 {#creating-projects}

uv 支持使用 `uv init` 创建项目。

创建项目时，uv 支持两种基本模板：[**应用程序**](#applications)（applications）和 [**库**](#libraries)（libraries）。默认情况下，uv 会创建一个应用程序项目。可以使用 `--lib` 标志来创建库项目。

## 目标目录 {#target-directory}

uv 将在工作目录中创建项目，或者通过提供名称在目标目录中创建，
例如 `uv init foo`。可以使用 `--directory` 选项修改工作目录，这将使目标目录路径相对于指定的工作目录进行解析。如果目标目录中已经存在一个项目（即存在 `pyproject.toml`），uv 将报错退出。

## 应用程序 {#applications}

应用程序项目适用于 Web 服务器、脚本和命令行接口。

应用程序是 `uv init` 的默认目标，但也可以通过 `--app` 标志显式指定。

```console
$ uv init example-app
```

项目包含一个 `pyproject.toml`、一个示例文件（`main.py`）、一个自述文件和一个 Python 版本固定文件（`.python-version`）。

```console
$ tree example-app
example-app/
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

!!! note

    在 v0.6.0 之前，uv 创建的文件名为 `hello.py` 而非 `main.py`。

`pyproject.toml` 包含基本元数据。它不包含构建系统，因此它不是一个[包](./config.md#project-packaging)，也不会被安装到环境中：

```toml title="pyproject.toml"
[project]
name = "example-app"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []
```

示例文件定义了一个 `main` 函数，包含一些标准样板代码：

```python title="main.py"
def main():
    print("Hello from example-app!")


if __name__ == "__main__":
    main()
```

Python 文件可以使用 `uv run` 执行：

```console
$ cd example-app
$ uv run main.py
Hello from example-project!
```

## 打包应用程序 {#packaged-applications}

许多用例需要一个[包](./config.md#project-packaging)。例如，如果您正在创建一个将发布到 PyPI 的命令行接口，或者想要在专用目录中定义测试。

可以使用 `--package` 标志来创建打包应用程序：

```console
$ uv init --package example-pkg
```

源代码被移入 `src` 目录，包含一个模块目录和一个 `__init__.py` 文件：

```console
$ tree example-pkg
example-pkg/
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── example_pkg
        └── __init__.py
```

定义了[构建系统](./config.md#build-systems)，因此项目将被安装到环境中：

```toml title="pyproject.toml" hl_lines="12-14"
[project]
name = "example-pkg"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[project.scripts]
example-pkg = "example_pkg:main"

[build-system]
requires = ["uv_build>=0.11.23,<0.12"]
build-backend = "uv_build"
```

!!! tip

    可以使用 `--build-backend` 选项来指定替代的构建系统。

包含了一个[命令](./config.md#entry-points)定义：

```toml title="pyproject.toml" hl_lines="9 10"
[project]
name = "example-pkg"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[project.scripts]
example-pkg = "example_pkg:main"

[build-system]
requires = ["uv_build>=0.11.23,<0.12"]
build-backend = "uv_build"
```

该命令可以通过 `uv run` 执行：

```console
$ cd example-pkg
$ uv run example-pkg
Hello from example-pkg!
```

## 库 {#libraries}

库为其他项目提供函数和对象以供使用。库旨在被构建和分发，例如通过上传到 PyPI。

可以通过使用 `--lib` 标志来创建库：

```console
$ uv init --lib example-lib
```

!!! note

    使用 `--lib` 隐含了 `--package`。库始终需要打包项目。

与[打包应用程序](#packaged-applications)一样，使用 `src` 布局。包含一个 `py.typed` 标记，用于向使用者表明可以从库中读取类型信息：

```console
$ tree example-lib
example-lib/
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── example_lib
        ├── py.typed
        └── __init__.py
```

!!! note

    `src` 布局在开发库时特别有价值。它确保库与项目根目录中的任何 `python` 调用隔离开来，并且分发的库代码与项目源代码的其他部分良好分离。

定义了[构建系统](./config.md#build-systems)，因此项目将被安装到环境中：

```toml title="pyproject.toml" hl_lines="12-14"
[project]
name = "example-lib"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["uv_build>=0.11.23,<0.12"]
build-backend = "uv_build"
```

!!! tip

    您可以通过 `--build-backend` 选择不同的构建后端模板，可选值包括 `hatchling`、
    `uv_build`、`flit-core`、`pdm-backend`、`setuptools`、`maturin` 或 `scikit-build-core`。如果您想创建[带扩展模块的库](#projects-with-extension-modules)，则需要使用替代后端。

创建的模块定义了一个简单的 API 函数：

```python title="__init__.py"
def hello() -> str:
    return "Hello from example-lib!"
```

您可以使用 `uv run` 导入并执行它：

```console
$ cd example-lib
$ uv run python -c "import example_lib; print(example_lib.hello())"
Hello from example-lib!
```

## 带扩展模块的项目 {#projects-with-extension-modules}

大多数 Python 项目是"纯 Python"（pure Python）的，这意味着它们不定义其他语言（如 C、C++、FORTRAN 或 Rust）的模块。然而，带扩展模块的项目通常用于性能敏感的代码。

创建带扩展模块的项目需要选择替代的构建系统。uv 支持使用以下支持构建扩展模块的构建系统来创建项目：

- [`maturin`](https://www.maturin.rs) — 用于 Rust 项目
- [`scikit-build-core`](https://github.com/scikit-build/scikit-build-core) — 用于 C、C++、
  FORTRAN、Cython 项目

使用 `--build-backend` 标志指定构建系统：

```console
$ uv init --build-backend maturin example-ext
```

!!! note

    使用 `--build-backend` 隐含了 `--package`。

除了典型的 Python 项目文件外，项目还包含一个 `Cargo.toml` 和一个 `lib.rs` 文件：

```console
$ tree example-ext
example-ext/
├── .python-version
├── Cargo.toml
├── README.md
├── pyproject.toml
└── src
    ├── lib.rs
    └── example_ext
        ├── __init__.py
        └── _core.pyi
```

!!! note

    如果使用 `scikit-build-core`，您将看到 CMake 配置文件和一个 `main.cpp` 文件。

Rust 库定义了一个简单的函数：

```rust title="src/lib.rs"
use pyo3::prelude::*;

#[pymodule]
mod _core {
    use pyo3::prelude::*;

    #[pyfunction]
    fn hello_from_bin() -> String {
        "Hello from example-ext!".to_string()
    }
}
```

Python 模块则导入它：

```python title="src/example_ext/__init__.py"
from example_ext._core import hello_from_bin


def main() -> None:
    print(hello_from_bin())
```

该命令可以通过 `uv run` 执行：

```console
$ cd example-ext
$ uv run example-ext
Hello from example-ext!
```

!!! important

    当使用 maturin 或 scikit-build-core 创建项目时，uv 会配置 [`tool.uv.cache-keys`](https://docs.astral.sh/uv/reference/settings/#cache-keys)
    来包含常见的源文件类型。要强制重新构建（例如在更改 `cache-keys` 之外的文件或未使用 `cache-keys` 时），请使用 `--reinstall`。

## 创建最小项目 {#creating-a-minimal-project}

如果您只想创建一个 `pyproject.toml`，请使用 `--bare` 选项：

```console
$ uv init example-bare --bare
```

uv 将跳过创建 Python 版本固定文件、README 以及任何源目录或文件。此外，uv 不会初始化版本控制系统（即 `git`）。

```console
$ tree example-bare
example-bare
└── pyproject.toml
```

uv 也不会向 `pyproject.toml` 添加额外元数据，如 `description` 或 `authors`。

```toml
[project]
name = "example-bare"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []
```

`--bare` 选项可以与其他选项（如 `--lib` 或 `--build-backend`）一起使用——在这些情况下，uv 仍会配置构建系统，但不会创建预期的文件结构。

当使用 `--bare` 时，仍然可以选择性地启用其他功能：

```console
$ uv init example-bare --bare --description "Hello world" --author-from git --vcs git --python-pin
```
