---
subtitle: Tools
description: 学习uv管理的工具，包括工具的工作原理、如何安装和运行工具、工具环境和版本管理。完整指南帮助您了解uv的工具管理功能。
---

# 工具 {#tools}

工具（Tools）是提供命令行接口的 Python 包。

!!! note

    有关工具接口的入门介绍，请参阅[工具指南](../guides/tools.md) —— 本文档讨论工具管理的详细信息。

## `uv tool` 接口 {#the-uv-tool-interface}

uv 包含一个专门用于与工具交互的接口。工具可以通过 `uv tool run` 直接调用而无需安装，在这种情况下，它们的依赖项会被安装到一个与当前项目隔离的临时虚拟环境中。

由于不安装而直接运行工具非常常见，因此为 `uv tool run` 提供了 `uvx` 别名 —— 这两个命令完全等价。为简洁起见，文档中通常会使用 `uvx` 而非 `uv tool run`。

工具也可以通过 `uv tool install` 安装，在这种情况下，它们的可执行文件将[在 `PATH` 上可用](#tool-executables) —— 仍然使用隔离的虚拟环境，但命令完成后不会被移除。

## 执行 vs 安装 {#execution-vs-installation}

在大多数情况下，使用 `uvx` 执行工具比安装工具更合适。安装工具在你需要让系统上的其他程序也能使用该工具时很有用，例如，某个不受你控制的脚本需要该工具，或者你在 Docker 镜像中并希望让用户可以使用该工具。

## 工具环境 {#tool-environments}

使用 `uvx` 运行工具时，虚拟环境存储在 uv 缓存目录中，并被视为可丢弃的，也就是说，如果你运行 `uv cache clean`，该环境将被删除。环境仅被缓存以减少重复调用的开销。如果环境被移除，将自动创建新的环境。

使用 `uv tool install` 安装工具时，虚拟环境会在 [uv 工具目录](../reference/storage.md#tools) 中创建。除非卸载工具，否则该环境不会被移除。如果手动删除该环境，工具将无法运行。

!!! important

    工具环境 _不_ 应该被直接修改。强烈建议永远不要手动修改工具环境，例如通过 `pip` 操作。

## 工具版本 {#tool-versions}

除非请求特定版本，否则 `uv tool install` 将安装所请求工具的最新可用版本。`uvx` 在 _首次调用时_ 将使用所请求工具的最新可用版本。之后，`uvx` 将使用缓存的工具版本，除非请求了不同版本、缓存被清理或缓存被刷新。

例如，运行特定版本的 Ruff：

```console
$ uvx ruff@0.6.0 --version
ruff 0.6.0
```

后续调用 `uvx` 将使用最新版本，而非缓存版本。

```console
$ uvx ruff --version
ruff 0.6.2
```

但是，如果 Ruff 发布了新版本，除非刷新缓存，否则不会使用新版本。

要请求最新版本的 Ruff 并刷新缓存，请使用 `@latest` 后缀：

```console
$ uvx ruff@latest --version
0.6.2
```

一旦使用 `uv tool install` 安装了工具，`uvx` 将默认使用已安装的版本。

例如，安装了旧版本的 Ruff 后：

```console
$ uv tool install ruff==0.5.0
```

`ruff` 和 `uvx ruff` 的版本相同：

```console
$ ruff --version
ruff 0.5.0
$ uvx ruff --version
ruff 0.5.0
```

但是，你可以通过显式请求最新版本来忽略已安装的版本，例如：

```console
$ uvx ruff@latest --version
0.6.2
```

或者，使用 `--isolated` 标志，这将避免刷新缓存但忽略已安装的版本：

```console
$ uvx --isolated ruff --version
0.6.2
```

`uv tool install` 同样支持 `{package}@{version}` 和 `{package}@latest` 指定符，例如：

```console
$ uv tool install ruff@latest
$ uv tool install ruff@0.6.0
```

## 升级工具 {#upgrading-tools}

工具环境可以通过 `uv tool upgrade` 升级，或通过后续的 `uv tool install` 操作完全重建。

升级工具环境中的所有包：

```console
$ uv tool upgrade black
```

升级工具环境中的单个包：

```console
$ uv tool upgrade black --upgrade-package click
```

工具升级将遵循安装工具时提供的版本约束。例如，`uv tool install black >=23,<24` 之后再执行 `uv tool upgrade black` 会将 Black 升级到 `>=23,<24` 范围内的最新版本。

要替换版本约束，请使用 `uv tool install` 重新安装工具：

```console
$ uv tool install black>=24
```

同样，工具升级将保留安装工具时提供的设置。例如，`uv tool install black --prerelease allow` 之后再执行 `uv tool upgrade black` 将保留 `--prerelease allow` 设置。

!!! note

    工具升级将重新安装工具可执行文件，即使它们没有更改。

要在升级期间重新安装包，请使用 `--reinstall` 和 `--reinstall-package` 选项。

重新安装工具环境中的所有包：

```console
$ uv tool upgrade black --reinstall
```

重新安装工具环境中的单个包：

```console
$ uv tool upgrade black --reinstall-package click
```

## 包含额外的依赖项 {#including-additional-dependencies}

可以在工具执行期间包含额外的包：

```console
$ uvx --with <extra-package> <tool>
```

以及在工具安装期间：

```console
$ uv tool install --with <extra-package> <tool-package>
```

`--with` 选项可以多次提供以包含多个额外包。

`--with` 选项支持包规格说明，因此可以请求特定版本：

```console
$ uvx --with <extra-package>==<version> <tool-package>
```

`-w` 简写可以替代 `--with` 选项：

```console
$ uvx -w <extra-package> <tool-package>
```

如果请求的版本与工具包的要求冲突，包解析将失败，命令会报错。

## 从额外包安装可执行文件 {#installing-executables-from-additional-packages}

安装工具时，你可能希望将额外包中的可执行文件包含在同一个工具环境中。当你有一些相关的工具需要协同工作，或者想要安装共享依赖项的多个可执行文件时，这非常有用。

`--with-executables-from` 选项允许你指定额外的包，其可执行文件应与主工具一起安装：

```console
$ uv tool install --with-executables-from <package1>,<package2> <tool-package>
```

例如，安装 Ansible 以及来自 `ansible-core` 和 `ansible-lint` 的可执行文件：

```console
$ uv tool install --with-executables-from ansible-core,ansible-lint ansible
```

这会将 `ansible`、`ansible-core` 和 `ansible-lint` 包中的所有可执行文件安装到同一个工具环境中，使它们都可在 `PATH` 上使用。

`--with-executables-from` 选项可以与其他安装选项结合使用：

```console
$ uv tool install --with-executables-from ansible-core --with mkdocs-material ansible
```

请注意，`--with-executables-from` 与 `--with` 的区别在于：

- `--with` 将额外包作为依赖项包含，但不安装其可执行文件
- `--with-executables-from` 既将包作为依赖项包含，也安装其可执行文件

## Python 版本 {#python-versions}

每个工具环境都关联到一个特定的 Python 版本。这使用与 uv 创建的其他虚拟环境相同的 Python 版本[发现逻辑](./python-versions.md#discovery-of-python-versions)，但会忽略非全局的 Python 版本请求，如 `.python-version` 文件和 `pyproject.toml` 中的 `requires-python` 值。

`--python` 选项可用于请求特定版本。有关更多详细信息，请参阅 [Python 版本](./python-versions.md) 文档。

如果工具使用的 Python 版本被 _卸载_，工具环境将被破坏，工具可能无法使用。

## 工具可执行文件 {#tool-executables}

工具可执行文件包括 Python 包提供的所有控制台入口点（console entry points）、脚本入口点（script entry points）和二进制脚本（binary scripts）。在 Unix 上，工具可执行文件通过符号链接（symlink）链接到[可执行文件目录](../reference/storage.md#tool-executables)，在 Windows 上则复制到该目录。

!!! note

    工具包的依赖项提供的可执行文件不会被安装。

[可执行文件目录](../reference/storage.md#executable-directory)必须在 `PATH` 变量中，工具可执行文件才能在 shell 中使用。如果不在 `PATH` 中，将显示警告。`uv tool update-shell` 命令可用于将可执行文件目录添加到常见 shell 配置文件的 `PATH` 中。

### 覆盖可执行文件 {#overwriting-executables}

安装工具不会覆盖可执行文件目录中之前并非由 uv 安装的可执行文件。例如，如果使用 `pipx` 安装了某个工具，`uv tool install` 将失败。可以使用 `--force` 标志来覆盖此行为。

## 与 `uv run` 的关系 {#relationship-to-uv-run}

调用 `uv tool run <name>`（或 `uvx <name>`）几乎等价于：

```console
$ uv run --no-project --with <name> -- <name>
```

但是，使用 uv 的工具接口时有一些显著差异：

- 不需要 `--with` 选项 —— 所需的包从命令名称推断。
- 临时环境缓存在专用位置。
- 不需要 `--no-project` 标志 —— 工具始终在项目隔离的情况下运行。
- 如果工具已安装，`uv tool run` 将使用已安装的版本，但 `uv run` 不会。

如果工具不应与项目隔离，例如运行 `pytest` 或 `mypy` 时，则应使用 `uv run` 而不是 `uv tool run`。