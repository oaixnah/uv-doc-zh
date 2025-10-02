---
title: 将 uv 与 Jupyter 结合使用
description: 一份将 uv 与 Jupyter notebook 结合使用的完整指南，用于交互式计算、数据分析和可视化，包括内核管理和虚拟环境集成。
---

# 将 uv 与 Jupyter 结合使用

[Jupyter](https://jupyter.org/) notebook 是一款流行的交互式计算、数据分析和可视化工具。您可以通过几种不同的方式将 Jupyter 与 uv 结合使用，既可以与项目交互，也可以作为独立工具使用。

## 在项目中使用 Jupyter

如果您在[项目](../../concepts/projects/index.md)中工作，您可以通过以下方式启动一个可以访问项目虚拟环境的 Jupyter 服务器：

```console
$ uv run --with jupyter jupyter lab
```

默认情况下，`jupyter lab` 将在[http://localhost:8888/lab](http://localhost:8888/lab) 启动服务器。

在 notebook 中，您可以像在项目中的任何其他文件中一样导入项目的模块。例如，如果您的项目依赖于 `requests`，`import requests` 将从项目的虚拟环境中导入 `requests`。

如果您只希望对项目的虚拟环境进行只读访问，那么就不需要做更多的事情了。但是，如果您需要从 notebook 内部安装其他包，则需要考虑一些额外的细节。

### 创建内核

如果您需要从 notebook 内部安装包，我们建议为您的项目创建一个专用的内核。内核使 Jupyter 服务器能够在一个环境中运行，而各个 notebook 则在它们自己的独立环境中运行。

在 uv 的上下文中，我们可以为一个项目创建一个内核，同时将 Jupyter 本身安装在一个隔离的环境中，就像在 `uv run --with jupyter jupyter lab` 中一样。为项目创建内核可确保 notebook 连接到正确的环境，并且从 notebook 内部安装的任何包都安装到项目的虚拟环境中。

要创建内核，您需要安装 `ipykernel` 作为开发依赖项：

```console
$ uv add --dev ipykernel
```

然后，您可以使用以下命令为 `project` 创建内核：

```console
$ uv run ipython kernel install --user --env VIRTUAL_ENV $(pwd)/.venv --name=project
```

然后，使用以下命令启动服务器：

```console
$ uv run --with jupyter jupyter lab
```

创建 notebook 时，从下拉列表中选择 `project` 内核。然后使用 `!uv add pydantic`将 `pydantic` 添加到项目的依赖项中，或使用 `!uv pip install pydantic` 将 `pydantic`安装到项目的虚拟环境中，而不会将更改持久化到项目的 `pyproject.toml`或 `uv.lock` 文件中。任一命令都将使 `import pydantic` 在 notebook 中生效。

### 在没有内核的情况下安装包

如果您不想创建内核，仍然可以从 notebook 内部安装包。但是，需要考虑一些注意事项。

尽管 `uv run --with jupyter` 在一个隔离的环境中运行，但在 notebook 本身内部，`!uv add` 和相关命令将修改*项目*的环境，即使没有内核。

例如，从 notebook 内部运行 `!uv add pydantic` 会将 `pydantic` 添加到项目的依赖项和虚拟环境中，这样 `import pydantic` 将立即生效，无需进一步配置或重新启动服务器。

但是，由于 Jupyter 服务器是“活动”环境，`!uv pip install` 会将包安装到*Jupyter 的*环境，而不是项目环境。这些依赖项将在 Jupyter 服务器的生命周期内持续存在，但在后续的 `jupyter` 调用中可能会消失。

如果您正在使用依赖 pip 的 notebook（例如，通过 `%pip` 魔法命令），您可以在启动 Jupyter 服务器之前通过运行 `uv venv --seed` 将 pip 包含在项目的虚拟环境中。例如，给定：

```console
$ uv venv --seed
$ uv run --with jupyter jupyter lab
```

后续在 notebook 中调用 `%pip install` 会将包安装到项目的虚拟环境中。但是，这些修改将*不会*反映在项目的 `pyproject.toml` 或 `uv.lock` 文件中。

## 将 Jupyter 作为独立工具使用

如果您需要临时访问 notebook（即，以交互方式运行 Python 代码段），您可以随时使用 `uv tool run jupyter lab` 启动 Jupyter 服务器。这将在一个隔离的环境中运行 Jupyter 服务器。

## 将 Jupyter 与非项目环境结合使用

如果您需要在与[项目](../../concepts/projects/index.md)无关的虚拟环境中运行 Jupyter（例如，没有 `pyproject.toml` 或 `uv.lock`），您可以通过直接将 Jupyter 添加到环境中来实现。例如：

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

这样，`import pydantic` 将在 notebook 中生效，您可以通过 `!uv pip install` 甚至 `!pip install` 安装其他包。

## 从 VS Code 使用 Jupyter

您还可以在 VS Code 等编辑器中与 Jupyter notebook 交互。要将 uv 管理的项目连接到 VS Code 中的 Jupyter notebook，我们建议为项目创建一个内核，如下所示：

```console
# 创建一个项目。
$ uv init project

# 进入项目目录。
$ cd project

# 添加 ipykernel 作为开发依赖项。
$ uv add --dev ipykernel

# 在 VS Code 中打开项目。
$ code .
```

在 VS Code 中打开项目目录后，您可以通过从命令面板中选择“创建：新 Jupyter Notebook”来创建新的 Jupyter notebook。当提示选择内核时，选择“Python 环境”并选择您之前创建的虚拟环境（例如，在 macOS 和 Linux 上为 `.venv/bin/python`，在 Windows 上为 `.venv\Scripts\python`）。

!!! note

    VS Code 要求项目环境中存在 `ipykernel`。如果您不想将 `ipykernel` 添加为开发依赖项，可以使用 `uv pip install ipykernel` 将其直接安装到项目环境中。

如果您需要从 notebook 内部操作项目的环境，您可能需要将 `uv` 添加为显式开发依赖项：

```console
$ uv add --dev uv
```

然后，您可以使用 `!uv add pydantic` 将 `pydantic` 添加到项目的依赖项中，或使用 `!uv pip install pydantic` 将 `pydantic` 安装到项目的虚拟环境中，而无需更新项目的 `pyproject.toml` 或 `uv.lock` 文件。
