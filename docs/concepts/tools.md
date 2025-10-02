---
subtitle: Tools
description: 学习uv管理的工具，包括工具的工作原理、如何安装和运行工具、工具环境和版本管理。完整指南帮助您了解uv的工具管理功能。
---

# 工具

工具是提供命令行界面的 Python 包。

!!! note

    有关使用工具界面的介绍，请参阅[工具指南](../guides/tools.md) — 本文档讨论工具管理的详细信息。

## `uv tool` 界面

uv 包含一个用于与工具交互的专用界面。可以使用 `uv tool run` 调用工具而无需安装，在这种情况下，它们的依赖项会安装在与当前项目隔离的临时虚拟环境中。

因为在不安装工具的情况下运行工具非常普遍，所以为 `uv tool run` 提供了一个 `uvx` 别名 — 这两个命令完全等效。为简洁起见，文档将主要使用 `uvx` 而不是 `uv tool run`。

也可以使用 `uv tool install` 安装工具，在这种情况下，它们的可执行文件[在 `PATH` 上可用](#path) — 仍然使用隔离的虚拟环境，但在命令完成时不会被删除。

## 执行与安装

在大多数情况下，使用 `uvx` 执行工具比安装工具更合适。如果需要让系统上的其他程序可以使用该工具，例如，某个您无法控制的脚本需要该工具，或者您在 Docker 镜像中并希望让用户可以使用该工具，那么安装该工具会很有用。

## 工具环境

使用 `uvx` 运行工具时，虚拟环境存储在 uv 缓存目录中，并被视为一次性的，即，如果运行 `uv cache clean`，该环境将被删除。缓存环境只是为了减少重复调用的开销。如果环境被删除，将自动创建一个新环境。

使用 `uv tool install` 安装工具时，会在 uv 工具目录中创建一个虚拟环境。除非卸载该工具，否则不会删除该环境。如果手动删除该环境，该工具将无法运行。

## 工具版本

除非请求特定版本，否则 `uv tool install` 将安装所请求工具的最新可用版本。`uvx` 将在_首次调用_时使用所请求工具的最新可用版本。之后，`uvx` 将使用工具的缓存版本，除非请求了不同的版本、修剪了缓存或刷新了缓存。

例如，要运行特定版本的 Ruff：

```console
$ uvx ruff@0.6.0 --version
ruff 0.6.0
```

后续调用 `uvx` 将使用最新版本，而不是缓存版本。

```console
$ uvx ruff --version
ruff 0.6.2
```

但是，如果发布了新版本的 Ruff，除非刷新缓存，否则不会使用它。

要请求最新版本的 Ruff 并刷新缓存，请使用 `@latest` 后缀：

```console
$ uvx ruff@latest --version
0.6.2
```

一旦使用 `uv tool install` 安装了工具，`uvx` 将默认使用已安装的版本。

例如，在安装了旧版本的 Ruff 之后：

```console
$ uv tool install ruff==0.5.0
```

`ruff` 和 `uvx ruff` 的版本是相同的：

```console
$ ruff --version
ruff 0.5.0
$ uvx ruff --version
ruff 0.5.0
```

但是，您可以通过显式请求最新版本来忽略已安装的版本，例如：

```console
$ uvx ruff@latest --version
0.6.2
```

或者，通过使用 `--isolated` 标志，这将避免刷新缓存但会忽略已安装的版本：

```console
$ uvx --isolated ruff --version
0.6.2
```

`uv tool install` 也将遵循 `{package}@{version}` 和 `{package}@latest` 说明符，例如：

```console
$ uv tool install ruff@latest
$ uv tool install ruff@0.6.0
```

## 工具目录

默认情况下，uv 工具目录名为 `tools`，位于 uv 应用程序状态目录中，例如 `~/.local/share/uv/tools`。可以使用 `UV_TOOL_DIR` 环境变量自定义该位置。

要显示工具安装目录的路径：

```console
$ uv tool dir
```

工具环境放置在与工具包同名的目录中，例如 `.../tools/<name>`。

!!! important

    工具环境_不_应直接修改。强烈建议不要手动修改工具环境，例如使用 `pip` 操作。

## 升级工具

可以通过 `uv tool upgrade` 升级工具环境，或通过后续的 `uv tool install` 操作完全重新创建。

要升级工具环境中的所有包：

```console
$ uv tool upgrade black
```

要升级工具环境中的单个包：

```console
$ uv tool upgrade black --upgrade-package click
```

工具升级将遵循安装工具时提供的版本约束。例如，`uv tool install black >=23,<24` 后跟 `uv tool upgrade black` 会将 Black 升级到 `>=23,<24` 范围内的最新版本。

要替换版本约束，请使用 `uv tool install` 重新安装工具：

```console
$ uv tool install black>=24
```

同样，工具升级将保留安装工具时提供的设置。例如，`uv tool install black --prerelease allow` 后跟 `uv tool upgrade black` 将保留 `--prerelease allow` 设置。

!!! note

    工具升级将重新安装工具可执行文件，即使它们没有更改。

要在升级期间重新安装包，请使用 `--reinstall` 和 `--reinstall-package` 选项。

要重新安装工具环境中的所有包：

```console
$ uv tool upgrade black --reinstall
```

要重新安装工具环境中的单个包：

```console
$ uv tool upgrade black --reinstall-package click
```

## 包括其他依赖项

可以在工具执行期间包括其他包：

```console
$ uvx --with <extra-package> <tool>
```

并且，在工具安装期间：

```console
$ uv tool install --with <extra-package> <tool-package>
```

可以多次提供 `--with` 选项以包括其他包。

`--with` 选项支持包规范，因此可以请求特定版本：

```console
$ uvx --with <extra-package>==<version> <tool-package>
```

如果请求的版本与工具包的要求冲突，包解析将失败，命令将出错。

## Python 版本

每个工具环境都链接到一个特定的 Python 版本。这使用与其他由 uv 创建的虚拟环境相同的 Python 版本[发现逻辑](./python-versions.md#python_8)，但会忽略非全局 Python 版本请求，如 `.python-version` 文件和 `pyproject.toml` 中的 `requires-python` 值。

可以使用 `--python` 选项请求特定版本。有关更多详细信息，请参阅[Python 版本](./python-versions.md)文档。

如果工具使用的 Python 版本被_卸载_，工具环境将被破坏，工具可能无法使用。

## 工具可执行文件

工具可执行文件包括由 Python 包提供的所有控制台入口点、脚本入口点和二进制脚本。工具可执行文件在 Unix 上被符号链接到 `bin` 目录，在 Windows 上被复制。

### `bin` 目录

可执行文件安装到遵循 XDG 标准的用户 `bin` 目录中，例如 `~/.local/bin`。与 uv 中的其他目录方案不同，XDG 标准在_所有平台_上都使用，尤其包括 Windows 和 macOS — 在这些平台上没有明确的替代位置来放置可执行文件。安装目录由第一个可用的环境变量确定：

- `$UV_TOOL_BIN_DIR`
- `$XDG_BIN_HOME`
- `$XDG_DATA_HOME/../bin`
- `$HOME/.local/bin`

工具包依赖项提供的可执行文件不会被安装。

### `PATH`

`bin` 目录必须在 `PATH` 变量中，以便从 shell 中使用工具可执行文件。如果它不在 `PATH` 中，将显示警告。可以使用 `uv tool update-shell` 命令将 `bin` 目录添加到常见的 shell 配置文件中的 `PATH` 中。

### 覆盖可执行文件

安装工具不会覆盖 `bin` 目录中以前不是由 uv 安装的可执行文件。例如，如果已使用 `pipx` 安装了工具，`uv tool install` 将失败。可以使用 `--force` 标志覆盖此行为。

## 与 `uv run` 的关系

调用 `uv tool run <name>`（或 `uvx <name>`）几乎等同于：

```console
$ uv run --no-project --with <name> -- <name>
```

但是，在使用 uv 的工具界面时，有几个显著的区别：

- 不需要 `--with` 选项 — 所需的包是从命令名称推断出来的。
- 临时环境缓存在专用位置。
- 不需要 `--no-project` 标志 — 工具始终与项目隔离运行。
- 如果已安装工具，`uv tool run` 将使用已安装的版本，但 `uv run` 不会。

如果工具不应与项目隔离，例如在运行 `pytest` 或 `mypy` 时，则应使用 `uv run` 而不是 `uv tool run`。
