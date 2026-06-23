---
title: 处理项目
subtitle: Working on projects
description: 使用 uv 创建和管理 Python 项目的完整指南。涵盖项目初始化、项目结构（pyproject.toml、.venv、uv.lock）、依赖项管理（添加/移除/升级）、查看版本、运行命令和脚本、构建分发包等核心功能的详细中文说明。
---

# 处理项目 {#working-on-projects}

uv 支持管理 Python 项目，这些项目在 `pyproject.toml` 文件中定义其依赖项。

## 创建新项目 {#creating-a-new-project}

你可以使用 `uv init` 命令创建一个新的 Python 项目：

```console
$ uv init hello-world
$ cd hello-world
```

或者，你也可以在当前工作目录中初始化项目：

```console
$ mkdir hello-world
$ cd hello-world
$ uv init
```

uv 将创建以下文件和目录：

```text
├── .git/
├── .gitignore
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

`main.py` 文件包含一个简单的"Hello world"程序。使用 `uv run` 来试试看：

```console
$ uv run main.py
Hello from hello-world!
```

## 项目结构 {#project-structure}

一个项目由几个重要的部分组成，它们协同工作，使 uv 能够管理你的项目。
除了 `uv init` 创建的文件外，当你首次运行项目命令（即 `uv run`、
`uv sync` 或 `uv lock`）时，uv 还会在项目根目录中创建虚拟环境和 `uv.lock` 文件。

完整的目录结构如下所示：

```text
.
├── .git/
├── .venv/
│   ├── bin
│   ├── lib
│   └── pyvenv.cfg
├── .gitignore
├── .python-version
├── README.md
├── main.py
├── pyproject.toml
└── uv.lock
```

### `pyproject.toml` {#pyproject-toml}

`pyproject.toml` 包含项目的元数据：

```toml title="pyproject.toml"
[project]
name = "hello-world"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
dependencies = []
```

你将使用此文件来指定依赖项，以及项目的详细信息，例如描述或许可证。你可以手动编辑此文件，
也可以使用 `uv add` 和 `uv remove` 等命令从终端管理项目。

!!! tip

    有关 `pyproject.toml` 格式入门的更多详细信息，请参阅官方
    [`pyproject.toml` 指南](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)。

你还将使用此文件在 `[tool.uv]` 部分中指定 uv 的[配置选项](../concepts/configuration-files.md)。
更多信息请参阅 [`[tool.uv]`](../reference/settings/configuration.md) 部分。

### `.python-version` {#python-version}

`.python-version` 文件包含项目的默认 Python 版本。此文件告诉 uv 在创建项目的虚拟环境时应使用哪个 Python 版本。

### `.venv` {#venv}

`.venv` 文件夹包含项目的虚拟环境，这是一个与系统其余部分隔离的 Python 环境。
uv 将在此处安装项目的依赖项。

有关更多详细信息，请参阅[项目环境](../concepts/projects/layout.md#the-project-environment)文档。

### `uv.lock` {#uv-lock}

`uv.lock` 是一个跨平台锁文件，包含有关项目依赖项的精确信息。
与用于指定项目广泛需求的 `pyproject.toml` 不同，锁文件包含项目环境中安装的确切已解析版本。
此文件应纳入版本控制，以便在不同机器上实现一致且可复现的安装。

`uv.lock` 是一个人类可读的 TOML 文件，但它由 uv 管理，不应手动编辑。

有关更多详细信息，请参阅[锁文件](../concepts/projects/layout.md#the-lockfile)文档。

## 管理依赖项 {#managing-dependencies}

你可以使用 `uv add` 命令将依赖项添加到 `pyproject.toml` 中。这也会同时更新锁文件和项目环境：

```console
$ uv add requests
```

你还可以指定版本约束或替代源：

```console
$ # 指定版本约束
$ uv add 'requests==2.31.0'

$ # 添加 Git 依赖项
$ uv add git+https://github.com/psf/requests
```

如果你正在从 `requirements.txt` 文件迁移，可以使用 `uv add` 的 `-r` 标志来添加文件中的所有依赖项：

```console
$ # 添加 `requirements.txt` 中的所有依赖项。
$ uv add -r requirements.txt -c constraints.txt
```

要移除包，可以使用 `uv remove`：

```console
$ uv remove requests
```

要升级包，可以使用 `--upgrade-package` 标志运行 `uv lock`：

```console
$ uv lock --upgrade-package requests
```

`--upgrade-package` 标志将尝试将指定的包更新到最新的兼容版本，同时保持锁文件的其余部分不变。

有关更多详细信息，请参阅[管理依赖项](../concepts/projects/dependencies.md)文档。

## 查看版本 {#viewing-your-version}

`uv version` 命令可用于查看包的版本。

要获取包的版本，运行 `uv version`：

```console
$ uv version
hello-world 0.7.0
```

要获取不含包名的版本，使用 `--short` 选项：

```console
$ uv version --short
0.7.0
```

要以 JSON 格式获取版本信息，使用 `--output-format json` 选项：

```console
$ uv version --output-format json
{
    "package_name": "hello-world",
    "version": "0.7.0",
    "commit_info": null
}
```

有关更新包版本的详细信息，请参阅[发布指南](./package.md#updating-your-version)。

## 运行命令 {#running-commands}

`uv run` 可用于在项目环境中运行任意脚本或命令。

在每次 `uv run` 调用之前，uv 会验证锁文件是否与 `pyproject.toml` 保持同步，以及环境是否与锁文件保持同步，
从而无需手动干预即可保持项目同步。`uv run` 保证你的命令在包含所有必需依赖项（且锁定在指定版本）的环境中运行。

!!! note

    默认情况下，`uv run` 不会从环境中移除多余的包（即锁文件中不存在的包）。
    有关详细信息，请参阅[多余包的处理](../concepts/projects/sync.md#handling-of-extraneous-packages)。

例如，使用 `flask`：

```console
$ uv add flask
$ uv run -- flask run -p 3000
```

或者，运行一个脚本：

```python title="example.py"
# 需要项目依赖项
import flask

print("hello world")
```

```console
$ uv run example.py
```

或者，你也可以使用 `uv sync` 手动更新环境，然后在执行命令之前激活它：

=== "macOS 和 Linux"

    ```console
    $ uv sync
    $ source .venv/bin/activate
    $ flask run -p 3000
    $ python example.py
    ```

=== "Windows"

    ```pwsh-session
    PS> uv sync
    PS> .venv\Scripts\activate
    PS> flask run -p 3000
    PS> python example.py
    ```

!!! note

    虚拟环境必须处于激活状态才能在不使用 `uv run` 的情况下运行项目中的脚本和命令。
    虚拟环境的激活方式因 Shell 和平台而异。

有关更多详细信息，请参阅项目中[运行命令和脚本](../concepts/projects/run.md)的文档。

## 构建分发包 {#building-distributions}

`uv build` 可用于为项目构建源码分发包和二进制分发包（wheel）。

默认情况下，`uv build` 会构建当前目录中的项目，并将构建产物放在 `dist/` 子目录中：

```console
$ uv build
$ ls dist/
hello-world-0.1.0-py3-none-any.whl
hello-world-0.1.0.tar.gz
```

有关更多详细信息，请参阅[构建项目](../concepts/projects/build.md)的文档。

## 后续步骤 {#next-steps}

要了解更多关于使用 uv 处理项目的信息，请参阅[项目概念](../concepts/projects/index.md)页面和
[命令参考](../reference/cli/init.md)。

或者，继续阅读以了解如何[将 uv 锁文件导出为不同格式](../concepts/projects/export.md)。
