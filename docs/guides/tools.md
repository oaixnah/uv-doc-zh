---
title: 使用工具
subtitle: Using tools
description: 一份关于使用 uv 运行作为 Python 包发布的工具的指南，包括使用 uvx 进行一次性调用、请求特定工具版本、安装工具、升级工具等。
---

# 使用工具

许多 Python 包提供可作为工具使用的应用程序。uv 对轻松调用和安装工具提供了专门的支持。

## 运行工具

`uvx` 命令可以在不安装工具的情况下调用它。

例如，要运行 `ruff`：

```console
$ uvx ruff
```

!!! note

    这完全等同于：

    ```console
    $ uv tool run ruff
    ```

    为方便起见，提供了 `uvx` 作为别名。

参数可以在工具名称后提供：

```console
$ uvx pycowsay hello from uv

  -------------
< hello from uv >
  -------------
   \   ^__^
    \  (oo)\_______
       (__)\       )\/\
           ||----w |
           ||     ||

```

使用 `uvx` 时，工具会安装到临时的、隔离的环境中。

!!! note

    如果您在[项目](../concepts/projects/index.md)中运行工具，并且该工具要求安装您的项目（例如，使用 `pytest` 或 `mypy` 时），您应该使用 [`uv run`](../reference/cli/run.md) 而不是 `uvx`。否则，该工具将在与您的项目隔离的虚拟环境中运行。

    如果您的项目结构是扁平的，例如，没有使用 `src` 目录来存放模块，那么项目本身就不需要安装，使用 `uvx` 就可以了。在这种情况下，只有当您想在项目的依赖项中固定工具的版本时，使用 `uv run` 才是有益的。

## 命令与包名不同

当调用 `uvx ruff` 时，uv 会安装提供 `ruff` 命令的 `ruff` 包。但是，有时包名和命令名会不同。

`--from` 选项可用于从特定包调用命令，例如，由 `httpie` 提供的 `http`：

```console
$ uvx --from httpie http
```

## 请求特定版本

要运行特定版本的工具，请使用 `command@<version>`：

```console
$ uvx ruff@0.3.0 check
```

要运行最新版本的工具，请使用 `command@latest`：

```console
$ uvx ruff@latest check
```

如上所述，`--from` 选项也可用于指定包版本：

```console
$ uvx --from 'ruff==0.3.0' ruff check
```

或者，要限制版本范围：

```console
$ uvx --from 'ruff>0.2.0,<0.3.0' ruff check
```

请注意，`@` 语法只能用于精确版本。

## 请求额外内容

`--from` 选项可用于运行带有附加功能的工具：

```console
$ uvx --from 'mypy[faster-cache,reports]' mypy --xml-report mypy_report
```

这也可以与版本选择结合使用：

```console
$ uvx --from 'mypy[faster-cache,reports]==1.13.0' mypy --xml-report mypy_report
```

## 请求不同来源

`--from` 选项也可用于从其他来源安装。

例如，从 git 拉取：

```console
$ uvx --from git+https://github.com/httpie/cli httpie
```

您还可以从特定的命名分支拉取最新的提交：

```console
$ uvx --from git+https://github.com/httpie/cli@master httpie
```

或者拉取特定的标签：

```console
$ uvx --from git+https://github.com/httpie/cli@3.2.4 httpie
```

甚至可以拉取特定的提交：

```console
$ uvx --from git+https://github.com/httpie/cli@2843b87 httpie
```

## 带插件的命令

可以包含额外的依赖项，例如，在运行 `mkdocs` 时包含 `mkdocs-material`：

```console
$ uvx --with mkdocs-material mkdocs --help
```

## 安装工具

如果一个工具经常使用，最好将其安装到持久环境中并添加到 `PATH`，而不是重复调用 `uvx`。

!!! tip

    `uvx` 是 `uv tool run` 的一个方便的别名。所有其他与工具交互的命令都需要完整的 `uv tool` 前缀。

要安装 `ruff`：

```console
$ uv tool install ruff
```

安装工具后，其可执行文件会放在 `PATH` 中的 `bin` 目录中，这样就可以在没有 uv 的情况下运行该工具。如果它不在 `PATH` 中，将会显示警告，并且可以使用 `uv tool update-shell` 将其添加到 `PATH`。

安装 `ruff` 后，它应该是可用的：

```console
$ ruff --version
```

与 `uv pip install` 不同，安装工具不会使其模块在当前环境中可用。例如，以下命令将失败：

```console
$ python -c "import ruff"
```

这种隔离对于减少工具、脚本和项目的依赖项之间的交互和冲突非常重要。

与 `uvx` 不同，`uv tool install` 操作的是一个_包_，并将安装该工具提供的所有可执行文件。

例如，以下命令将安装 `http`、`https` 和 `httpie` 可执行文件：

```console
$ uv tool install httpie
```

此外，可以不使用 `--from` 来包含包版本：

```console
$ uv tool install 'httpie>0.1.0'
```

同样，对于包来源也是如此：

```console
$ uv tool install git+https://github.com/httpie/cli
```

与 `uvx` 一样，安装可以包含额外的包：

```console
$ uv tool install mkdocs --with mkdocs-material
```

## 升级工具

要升级工具，请使用 `uv tool upgrade`：

```console
$ uv tool upgrade ruff
```

工具升级将遵循安装工具时提供的版本约束。例如，`uv tool install 'ruff>=0.3,<0.4'` 后跟 `uv tool upgrade ruff` 会将 Ruff 升级到 `>=0.3,<0.4` 范围内的最新版本。

要替换版本约束，请使用 `uv tool install` 重新安装工具：

```console
$ uv tool install 'ruff>=0.4'
```

要升级所有工具：

```console
$ uv tool upgrade --all
```

## 请求 Python 版本

默认情况下，uv 在运行、安装或升级工具时会使用您的默认 Python 解释器（它找到的第一个）。您可以使用 `--python` 选项指定要使用的 Python 解释器。

例如，在运行工具时请求特定的 Python 版本：

```console
$ uvx --python 3.10 ruff
```

或者，在安装工具时：

```console
$ uv tool install --python 3.10 ruff
```

或者，在升级工具时：

```console
$ uv tool upgrade --python 3.10 ruff
```

有关请求 Python 版本的更多详细信息，请参阅[Python 版本](../concepts/python-versions.md#_1)概念页面。

## 旧版 Windows 脚本

工具还支持运行[旧版 setuptools 脚本](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#scripts)。这些脚本在安装后可通过 `$(uv tool dir)\<tool-name>\Scripts` 获得。

目前仅支持扩展名为 `.ps1`、`.cmd` 和 `.bat` 的旧版脚本。

例如，下面是运行命令提示符脚本的示例。

```console
$ uv tool run --from nuitka==2.6.7 nuitka.cmd --version
```

此外，您不需要指定扩展名。`uvx` 会自动按执行顺序为您查找以 `.ps1`、`.cmd` 和 `.bat` 结尾的文件。

```console
$ uv tool run --from nuitka==2.6.7 nuitka --version
```

## 后续步骤

要了解有关使用 uv 管理工具的更多信息，请参阅[工具概念](../concepts/tools.md)页面和[命令参考](../reference/cli/index.md)。

或者，继续阅读以了解如何[处理项目](./projects.md)。
