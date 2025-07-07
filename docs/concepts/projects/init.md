---
title: 创建项目
subtitle: Creating projects
---

# 创建项目

uv 支持使用 `uv init` 创建项目。

创建项目时，uv 支持两种基本模板：[**应用程序**](#_3)和[**库**](#_5)。默认情况下，uv 会为应用程序创建一个项目。可以使用 `--lib` 标志来为库创建一个项目。

## 目标目录

uv 会在工作目录中创建一个项目，或者通过提供名称在目标目录中创建一个项目，例如 `uv init foo`。如果目标目录中已存在项目，即存在 `pyproject.toml`，uv 将退出并显示错误。

## 应用程序

应用程序项目适用于 Web 服务器、脚本和命令行界面。

应用程序是 `uv init` 的默认目标，但也可以使用 `--app` 标志指定。

```console
$ uv init example-app
```

该项目包括一个 `pyproject.toml`、一个示例文件 (`main.py`)、一个自述文件和一个 Python 版本锁定文件 (`.python-version`)。

```console
$ tree example-app
example-app
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

!!! note

    在 v0.6.0 之前，uv 创建一个名为 `hello.py` 的文件而不是 `main.py`。

`pyproject.toml` 包括基本元数据。它不包括构建系统，它不是一个[包](./config.md#project-packaging)，也不会被安装到环境中：

```toml title="pyproject.toml"
[project]
name = "example-app"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []
```

示例文件定义了一个带有一些标准样板代码的 `main` 函数：

```python title="main.py"
def main():
    print("Hello from example-app!")


if __name__ == "__main__":
    main()
```

可以使用 `uv run` 执行 Python 文件：

```console
$ cd example-app
$ uv run main.py
Hello from example-project!
```

## 打包应用程序

许多用例需要一个[包](./config.md#_8)。例如，如果您正在创建一个将发布到 PyPI 的命令行界面，或者您想在专用目录中定义测试。

可以使用 `--package` 标志来创建一个打包的应用程序：

```console
$ uv init --package example-pkg
```

源代码被移动到一个 `src` 目录中，其中包含一个模块目录和一个 `__init__.py` 文件：

```console
$ tree example-pkg
example-pkg
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── example_pkg
        └── __init__.py
```

定义了一个[构建系统](./config.md#_6)，因此项目将被安装到环境中：

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
requires = ["hatchling"]
build-backend = "hatchling.build"
```

!!! tip

    可以使用 `--build-backend` 选项来请求替代的构建系统。

包含一个[命令](./config.md#entry-points)定义：

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
requires = ["hatchling"]
build-backend = "hatchling.build"
```

可以使用 `uv run` 执行该命令：

```console
$ cd example-pkg
$ uv run example-pkg
Hello from example-pkg!
```

## 库

库为其他项目提供要使用的函数和对象。库旨在被构建和分发，例如，通过将它们上传到 PyPI。

可以使用 `--lib` 标志创建库：

```console
$ uv init --lib example-lib
```

!!! note

    使用 `--lib` 意味着 `--package`。库总是需要一个打包的项目。

与[打包的应用程序](#_4)一样，使用 `src` 布局。包含一个 `py.typed` 标记，以向消费者指示可以从库中读取类型：

```console
$ tree example-lib
example-lib
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── example_lib
        ├── py.typed
        └── __init__.py
```

!!! note

    在开发库时，`src` 布局特别有价值。它确保库与项目根目录中的任何 `python` 调用隔离，并且分发的库代码与项目源的其余部分很好地分离。

定义了一个[构建系统](./config.md#_6)，因此项目将被安装到环境中：

```toml title="pyproject.toml" hl_lines="12-14"
[project]
name = "example-lib"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

!!! tip

    您可以通过将 `--build-backend` 与 `hatchling`、`uv_build`、`flit-core`、`pdm-backend`、`setuptools`、`maturin` 或 `scikit-build-core` 一起使用来选择不同的构建后端模板。如果您想创建一个[带扩展模块的库](#_6)，则需要一个替代后端。

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

## 带扩展模块的项目

大多数 Python 项目都是“纯 Python”，这意味着它们不定义其他语言（如 C、C++、FORTRAN 或 Rust）的模块。但是，带扩展模块的项目通常用于性能敏感的代码。

创建带扩展模块的项目需要选择替代的构建系统。uv 支持使用以下支持构建扩展模块的构建系统创建项目：

- [`maturin`](https://www.maturin.rs) 用于带 Rust 的项目
- [`scikit-build-core`](https://github.com/scikit-build/scikit-build-core) 用于带 C、C++、FORTRAN、Cython 的项目

使用 `--build-backend` 标志指定构建系统：

```console
$ uv init --build-backend maturin example-ext
```

!!! note

    使用 `--build-backend` 意味着 `--package`。

除了典型的 Python 项目文件外，该项目还包含一个 `Cargo.toml` 和一个 `lib.rs` 文件：

```console
$ tree example-ext
example-ext
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

    如果使用 `scikit-build-core`，您将看到 CMake 配置和一个 `main.cpp` 文件。

Rust 库定义了一个简单的函数：

```rust title="src/lib.rs"
use pyo3::prelude::*;

#[pyfunction]
fn hello_from_bin() -> String {
    "Hello from example-ext!".to_string()
}

#[pymodule]
fn _core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_from_bin, m)?)?;
    Ok(())
}
```

Python 模块导入它：

```python title="src/example_ext/__init__.py"
from example_ext._core import hello_from_bin


def main() -> None:
    print(hello_from_bin())
```

可以使用 `uv run` 执行该命令：

```console
$ cd example-ext
$ uv run example-ext
Hello from example-ext!
```

!!! important

    对 `lib.rs` 或 `main.cpp` 中的扩展代码的更改将需要运行 `--reinstall` 来重新构建它们。

## 创建一个最小的项目

如果您只想创建一个 `pyproject.toml`，请使用 `--bare` 选项：

```console
$ uv init example --bare
```

uv 将跳过创建 Python 版本锁定文件、README 以及任何源目录或文件。此外，uv 不会初始化版本控制系统（即 `git`）。

```console
$ tree example-bare
example-bare
└── pyproject.toml
```

uv 也不会向 `pyproject.toml` 添加额外的元数据，例如 `description` 或 `authors`。

```toml
[project]
name = "example"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []
```

`--bare` 选项可以与其他选项（如 `--lib` 或 `--build-backend`）一起使用——在这些情况下，uv 仍将配置构建系统，但不会创建预期的文件结构。

当使用 `--bare` 时，仍然可以选择使用其他功能：

```console
$ uv init example --bare --description "Hello world" --author-from git --vcs git --python-pin
```
