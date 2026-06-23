---
title: 使用工具
subtitle: Using tools
description: 本文介绍如何使用 uv 运行和管理 Python 工具，涵盖 uvx 一次性调用、安装工具、升级工具、请求特定版本与 extras、从不同来源安装、以及旧版 Windows 脚本支持等完整指南。
---

# 使用工具 {#using-tools}

许多 Python 包提供了可作为工具使用的应用程序。uv 为便捷调用和安装工具提供了专门支持。

## 运行工具 {#running-tools}

`uvx` 命令可以在不安装工具的情况下调用它。

例如，运行 `ruff`：

```console
$ uvx ruff
```

!!! note

    这与以下命令完全等价：

    ```console
    $ uv tool run ruff
    ```

    `uvx` 是为了方便而提供的别名。

可以在工具名称后传入参数：

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

使用 `uvx` 时，工具会被安装到临时的隔离环境中。

!!! note

    如果你在[_项目_](../concepts/projects/index.md)中运行工具，且该工具要求你的项目已安装（例如使用 `pytest` 或 `mypy` 时），你需要使用 [`uv run`](./projects.md#running-commands) 而不是 `uvx`。否则，工具将在与你的项目隔离的虚拟环境中运行。

    如果你的项目采用扁平结构（例如不使用 `src` 目录存放模块），则项目本身不需要安装，使用 `uvx` 即可。在这种情况下，只有当你希望在项目的依赖中锁定工具版本时，使用 `uv run` 才有优势。

## 包名与命令名不同的情况 {#commands-with-different-package-names}

当调用 `uvx ruff` 时，uv 会安装提供 `ruff` 命令的 `ruff` 包。但有时包名和命令名并不相同。

可以使用 `--from` 选项从特定包中调用命令，例如 `httpie` 提供的 `http` 命令：

```console
$ uvx --from httpie http
```

## 请求特定版本 {#requesting-specific-versions}

要运行特定版本的工具，使用 `command@<version>` 语法：

```console
$ uvx ruff@0.3.0 check
```

要运行最新版本的工具，使用 `command@latest`：

```console
$ uvx ruff@latest check
```

`--from` 选项也可以用于指定包版本，如上所示：

```console
$ uvx --from 'ruff==0.3.0' ruff check
```

或者限制版本范围：

```console
$ uvx --from 'ruff>0.2.0,<0.3.0' ruff check
```

请注意，`@` 语法只能用于精确版本。

## 请求 extras {#requesting-extras}

`--from` 选项可用于运行带有 extras 的工具：

```console
$ uvx --from 'mypy[faster-cache,reports]' mypy --xml-report mypy_report
```

也可以与版本选择结合使用：

```console
$ uvx --from 'mypy[faster-cache,reports]==1.13.0' mypy --xml-report mypy_report
```

## 请求不同来源 {#requesting-different-sources}

`--from` 选项也可用于从替代来源安装。

例如，从 git 拉取：

```console
$ uvx --from git+https://github.com/httpie/cli httpie
```

你也可以从特定命名分支拉取最新提交：

```console
$ uvx --from git+https://github.com/httpie/cli@master httpie
```

或者拉取特定标签：

```console
$ uvx --from git+https://github.com/httpie/cli@3.2.4 httpie
```

甚至拉取特定提交：

```console
$ uvx --from git+https://github.com/httpie/cli@2843b87 httpie
```

或者启用 [Git LFS](https://git-lfs.com) 支持：

```console
$ uvx --lfs --from git+https://github.com/astral-sh/lfs-cowsay lfs-cowsay
```

## 带插件的命令 {#commands-with-plugins}

可以包含额外的依赖，例如在运行 `mkdocs` 时包含 `mkdocs-material`：

```console
$ uvx --with mkdocs-material mkdocs --help
```

## 安装工具 {#installing-tools}

如果某个工具使用频繁，将其安装到持久化环境并添加到 `PATH` 中会比反复调用 `uvx` 更有用。

!!! tip

    `uvx` 是 `uv tool run` 的便捷别名。所有其他与工具交互的命令都需要使用完整的 `uv tool` 前缀。

安装 `ruff`：

```console
$ uv tool install ruff
```

当工具被安装后，其可执行文件会被放置在 `PATH` 中的 `bin` 目录下，这样无需 uv 即可运行该工具。如果它不在 `PATH` 中，会显示警告，可以使用 `uv tool update-shell` 将其添加到 `PATH`。

安装 `ruff` 后，它应该可以直接使用：

```console
$ ruff --version
```

与 `uv pip install` 不同，安装工具不会使其模块在当前环境中可用。例如，以下命令将会失败：

```console
$ python -c "import ruff"
```

这种隔离对于减少工具、脚本和项目之间依赖的交互和冲突非常重要。

与 `uvx` 不同，`uv tool install` 作用于_包_，会安装该工具提供的所有可执行文件。

例如，以下命令将安装 `http`、`https` 和 `httpie` 可执行文件：

```console
$ uv tool install httpie
```

此外，无需 `--from` 即可包含包版本：

```console
$ uv tool install 'httpie>0.1.0'
```

同样，也适用于包来源：

```console
$ uv tool install git+https://github.com/httpie/cli
```

或带有 [Git LFS](https://git-lfs.com) 的包来源：

```console
$ uv tool install --lfs git+https://github.com/astral-sh/lfs-cowsay
```

与 `uvx` 一样，安装时可以包含额外的包：

```console
$ uv tool install mkdocs --with mkdocs-material
```

可以使用 `--with-executables-from` 标志在同一工具环境中一起安装多个相关的可执行文件。例如，以下命令将安装 `ansible` 的可执行文件，以及 `ansible-core` 和 `ansible-lint` 提供的可执行文件：

```console
$ uv tool install --with-executables-from ansible-core,ansible-lint ansible
```

## 升级工具 {#upgrading-tools}

要升级工具，使用 `uv tool upgrade`：

```console
$ uv tool upgrade ruff
```

工具升级会遵循安装工具时指定的版本约束。例如，先执行 `uv tool install ruff >=0.3,<0.4`，再执行 `uv tool upgrade ruff`，会将 Ruff 升级到 `>=0.3,<0.4` 范围内的最新版本。

要替换版本约束，可以使用 `uv tool install` 重新安装工具：

```console
$ uv tool install ruff>=0.4
```

要升级所有工具：

```console
$ uv tool upgrade --all
```

## 请求 Python 版本 {#requesting-python-versions}

默认情况下，uv 在运行、安装或升级工具时会使用默认的 Python 解释器（它找到的第一个）。你可以使用 `--python` 选项指定要使用的 Python 解释器。

例如，在运行工具时请求特定 Python 版本：

```console
$ uvx --python 3.10 ruff
```

或者在安装工具时：

```console
$ uv tool install --python 3.10 ruff
```

或者在升级工具时：

```console
$ uv tool upgrade --python 3.10 ruff
```

有关请求 Python 版本的更多详细信息，请参阅 [Python 版本](../concepts/python-versions.md#requesting-a-version)概念页面。

## 旧版 Windows 脚本 {#legacy-windows-scripts}

工具也支持运行[旧版 setuptools 脚本](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#scripts)。安装后，这些脚本可通过 `$(uv tool dir)\<tool-name>\Scripts` 访问。

目前仅支持 `.ps1`、`.cmd` 和 `.bat` 扩展名的旧版脚本。

例如，下面是一个运行命令提示符脚本的示例。

```console
$ uv tool run --from nuitka==2.6.7 nuitka.cmd --version
```

此外，你不需要指定扩展名。`uvx` 会自动按照 `.ps1`、`.cmd`、`.bat` 的执行顺序为你查找对应文件。

```console
$ uv tool run --from nuitka==2.6.7 nuitka --version
```

## 下一步 {#next-steps}

要了解更多关于使用 uv 管理工具的信息，请参阅[工具概念](../concepts/tools.md)页面和[命令参考](../reference/cli/tool.md)。

或者，继续阅读以了解如何[处理项目](./projects.md)。