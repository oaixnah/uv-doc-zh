---
title: 将 uv 与 Jupyter 结合使用
description: 一份将 uv 与 Jupyter notebook 结合使用的完整指南，用于交互式计算、数据分析和可视化，包括内核管理和虚拟环境集成。
---

# 将 uv 与 Jupyter 结合使用

[Jupyter](https://jupyter.org/) notebook 是一种流行的交互式计算、数据分析和可视化工具。你可以通过几种不同的方式将 Jupyter 与 uv 结合使用，既可以与项目交互，也可以作为独立工具使用。

## 在项目中使用 Jupyter

如果你在一个[项目](../../concepts/projects/index.md)中工作，可以通过以下命令启动一个可访问项目虚拟环境的 Jupyter 服务器：

```console
$ uv run --with jupyter jupyter lab
```

默认情况下，`jupyter lab` 将在
[http://localhost:8888/lab](http://localhost:8888/lab) 启动服务器。

在 notebook 中，你可以像在项目中的任何其他文件一样导入项目的模块。例如，如果你的项目依赖 `requests`，`import requests` 将从项目的虚拟环境中导入 `requests`。

如果你只需要对项目虚拟环境的只读访问权限，那么到此为止就可以了。但是，如果你需要从 notebook 内部安装额外的包，则需要考虑一些额外的细节。

### 创建内核

如果你需要从 notebook 内部安装包，我们建议为你的项目创建一个专用的内核（kernel）。内核使得 Jupyter 服务器可以在一个环境中运行，而各个 notebook 则在各自独立的环境中运行。

在 uv 的上下文中，我们可以在隔离环境中安装 Jupyter 本身的同时为项目创建内核，例如 `uv run --with jupyter jupyter lab`。为项目创建内核可以确保 notebook 连接到正确的环境，并且从 notebook 内部安装的任何包都会被安装到项目的虚拟环境中。

要创建内核，你需要将 `ipykernel` 安装为开发依赖：

```console
$ uv add --dev ipykernel
```

然后，你可以使用以下命令为 `project` 创建内核：

```console
$ uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
```

之后，使用以下命令启动服务器：

```console
$ uv run --with jupyter jupyter lab
```

创建 notebook 时，从下拉菜单中选择 `project` 内核。然后使用 `!uv add pydantic` 将 `pydantic` 添加到项目的依赖中，或者使用 `!uv pip install pydantic` 将 `pydantic` 安装到项目的虚拟环境中，而不将更改持久化到项目的 `pyproject.toml` 或 `uv.lock` 文件中。这两个命令都会使 `import pydantic` 在 notebook 中正常工作。

### 不使用内核安装包

如果你不想创建内核，仍然可以从 notebook 内部安装包。但是，有一些需要注意的事项。

尽管 `uv run --with jupyter` 在隔离环境中运行，但在 notebook 内部，`!uv add` 和相关命令即使没有内核也会修改*项目*的环境。

例如，从 notebook 内部运行 `!uv add pydantic` 会将 `pydantic` 添加到项目的依赖和虚拟环境中，使得 `import pydantic` 立即生效，无需进一步配置或重启服务器。

但是，由于 Jupyter 服务器是"活动"环境，`!uv pip install` 会将包安装到 *Jupyter* 的环境中，而不是项目环境中。这些依赖将在 Jupyter 服务器的生命周期内持续存在，但在后续 `jupyter` 调用中可能会消失。

如果你使用的 notebook 依赖 pip（例如，通过 `%pip` 魔法命令），可以在启动 Jupyter 服务器之前运行 `uv venv --seed` 来将 pip 包含在项目的虚拟环境中。例如：

```console
$ uv venv --seed
$ uv run --with jupyter jupyter lab
```

之后在 notebook 中调用 `%pip install` 会将包安装到项目的虚拟环境中。但是，这些修改*不会*反映在项目的 `pyproject.toml` 或 `uv.lock` 文件中。

## 将 Jupyter 作为独立工具使用

如果你需要临时访问 notebook（即交互式运行 Python 代码片段），你可以随时使用 `uv tool run jupyter lab` 启动 Jupyter 服务器。这将在隔离环境中运行 Jupyter 服务器。

## 在非项目环境中使用 Jupyter

如果你需要在一个不与[项目](../../concepts/projects/index.md)关联的虚拟环境中运行 Jupyter（例如，没有 `pyproject.toml` 或 `uv.lock`），你可以直接将 Jupyter 添加到该环境中。例如：

=== "macOS 和 Linux"

    ```console
    $ uv venv --seed
    $ uv pip install pydantic
    $ uv pip install jupyterlab
    $ .venv/bin/jupyter lab
    ```

=== "Windows"

    ```pwsh-session
    PS> uv venv --seed
    PS> uv pip install pydantic
    PS> uv pip install jupyterlab
    PS> .venv\Scripts\jupyter lab
    ```

此后，`import pydantic` 将在 notebook 中正常工作，你可以通过 `!uv pip install` 甚至 `!pip install` 来安装额外的包。

## 从 VS Code 中使用 Jupyter

你也可以在 VS Code 等编辑器中使用 Jupyter notebook。要将 uv 管理的项目连接到 VS Code 中的 Jupyter notebook，我们建议为项目创建内核，步骤如下：

```console
# 创建一个项目。
$ uv init project

# 进入项目目录。
$ cd project

# 将 ipykernel 添加为开发依赖。
$ uv add --dev ipykernel

# 在 VS Code 中打开项目。
$ code .
```

在 VS Code 中打开项目目录后，你可以通过从命令面板中选择 "Create: New Jupyter Notebook" 来创建新的 Jupyter notebook。当提示选择内核时，选择 "Python Environments" 并选择你之前创建的虚拟环境（例如，macOS 和 Linux 上的 `.venv/bin/python`，或 Windows 上的 `.venv\Scripts\python`）。

!!! note

    VS Code 要求项目环境中存在 `ipykernel`。如果你不想将 `ipykernel` 添加为开发依赖，可以使用 `uv pip install ipykernel` 将其直接安装到项目环境中。

如果你需要从 notebook 内部操作项目环境，可能需要将 `uv` 添加为显式的开发依赖：

```console
$ uv add --dev uv
```

之后，你可以使用 `!uv add pydantic` 将 `pydantic` 添加到项目的依赖中，或者使用 `!uv pip install pydantic` 将 `pydantic` 安装到项目的虚拟环境中，而不更新项目的 `pyproject.toml` 或 `uv.lock` 文件。
