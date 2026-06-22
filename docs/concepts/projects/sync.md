---
subtitle: Locking and syncing
description: 学习如何使用uv锁定和同步Python项目的依赖项，包括自动锁定与同步、检查锁文件是否是最新、创建锁文件和升级锁定的包版本。完整指南帮助您确保项目环境始终是最新的。
---

# 锁定与同步

锁定（Locking）是将项目的依赖项解析为[锁文件（lockfile）](./layout.md#the-lockfile)的过程。同步（Syncing）是将锁文件中的一部分包安装到[项目环境](./layout.md#the-project-environment)中的过程。

## 自动锁定与同步

锁定和同步在 uv 中是_自动_进行的。例如，当使用 `uv run` 时，项目会在调用所请求的命令之前被锁定和同步。这确保了项目环境始终是最新的。类似地，读取锁文件的命令（如 `uv tree`）也会在运行前自动更新锁文件。

要禁用自动锁定，请使用 `--locked` 选项：

```console
$ uv run --locked ...
```

如果锁文件不是最新的，uv 将抛出错误而不是更新锁文件。

要在不检查锁文件是否最新的情况下使用锁文件，请使用 `--frozen` 选项：

```console
$ uv run --frozen ...
```

类似地，要在不检查环境是否最新的情况下运行命令，请使用 `--no-sync` 选项：

```console
$ uv run --no-sync ...
```

## 检查锁文件

在判断锁文件是否最新时，uv 会检查其是否与项目元数据匹配。例如，如果你向 `pyproject.toml` 添加了一个依赖项，锁文件将被视为已过期。类似地，如果你更改了某个依赖项的版本约束，使得已锁定的版本被排除在外，锁文件也将被视为已过期。但是，如果你更改版本约束后，已锁定的版本仍然被包含在内，则锁文件仍被视为最新。

你可以通过向 `uv lock` 传递 `--check` 标志来检查锁文件是否最新：

```console
$ uv lock --check
```

这等同于其他命令中的 `--locked` 标志。

!!! important

    当包的新版本发布时，uv 不会将锁文件视为已过期——如果你想升级依赖项，需要显式更新锁文件。有关详细信息，请参阅[升级锁定的包版本](#upgrading-locked-package-versions)文档。

## 创建锁文件

虽然锁文件是[自动创建](#automatic-lock-and-sync)的，但也可以使用 `uv lock` 显式创建或更新锁文件：

```console
$ uv lock
```

## 同步环境

虽然环境是[自动同步](#automatic-lock-and-sync)的，但也可以使用 `uv sync` 显式同步：

```console
$ uv sync
```

手动同步环境对于确保你的编辑器拥有正确版本的依赖项特别有用。

### 可编辑安装

当环境被同步时，uv 会将项目（以及其他工作空间成员）安装为_可编辑_包，这样对源代码的更改无需重新同步即可反映在环境中。

要退出此行为，请使用 `--no-editable` 选项。

!!! note

    如果项目未定义构建系统，则不会安装该项目。有关详细信息，请参阅[构建系统](./config.md#build-systems)文档。

### 处理多余包

`uv sync` 默认执行"精确"同步，这意味着它会移除锁文件中不存在的任何包。

要保留多余包，请使用 `--inexact` 标志：

```console
$ uv sync --inexact
```

相比之下，`uv run` 默认使用"非精确"同步，确保所有必需的包都已安装，但不会移除多余包。要在 `uv run` 中启用精确同步，请使用 `--exact` 标志：

```console
$ uv run --exact ...
```

### 同步可选依赖项

uv 从 `[project.optional-dependencies]` 表中读取可选依赖项。这些通常被称为"额外依赖项（extras）"。

uv 默认不会同步额外依赖项。使用 `--extra` 选项来包含一个额外依赖项。

```console
$ uv sync --extra foo
```

要快速启用所有额外依赖项，请使用 `--all-extras` 选项。

有关如何管理可选依赖项的详细信息，请参阅[可选依赖项](./dependencies.md#optional-dependencies)文档。

### 同步开发依赖项

uv 从 `[dependency-groups]` 表中读取开发依赖项（如 [PEP 735](https://peps.python.org/pep-0735/) 所定义）。

`dev` 组是特殊处理的，默认会被同步。有关更改默认值的详细信息，请参阅[默认组](./dependencies.md#default-groups)文档。

`--no-dev` 标志可用于排除 `dev` 组。

`--only-dev` 标志可用于安装 `dev` 组，而_不包含_项目及其依赖项。

可以使用 `--all-groups`、`--no-default-groups`、`--group <name>`、`--only-group <name>` 和 `--no-group <name>` 选项来包含或排除其他组。`--only-group` 的语义与 `--only-dev` 相同，即不会包含项目本身。但是，`--only-group` 也会排除默认组。

组排除始终优先于组包含，因此对于以下命令：

```
$ uv sync --no-group foo --group foo
```

`foo` 组将不会被安装。

有关如何管理开发依赖项的详细信息，请参阅[开发依赖项](./dependencies.md#development-dependencies)文档。

## 升级锁定的包版本

在使用已有的 `uv.lock` 文件时，运行 `uv sync` 和 `uv lock` 时 uv 会优先使用之前锁定的包版本。只有当项目的依赖项约束排除了之前锁定的版本时，包版本才会发生变化。

要升级所有包：

```console
$ uv lock --upgrade
```

要将单个包升级到最新版本，同时保留所有其他包的锁定版本：

```console
$ uv lock --upgrade-package <package>
```

要将单个包升级到特定版本：

```console
$ uv lock --upgrade-package <package>==<version>
```

在所有情况下，升级都受限于项目的依赖项约束。例如，如果项目为某个包定义了上限版本，那么升级不会超过该版本。

!!! note

    uv 对 Git 依赖项也应用类似的逻辑。例如，如果某个 Git 依赖项引用了 `main` 分支，uv 将优先使用已有 `uv.lock` 文件中锁定的提交 SHA，而不是 `main` 分支上的最新提交，除非使用了 `--upgrade` 或 `--upgrade-package` 标志。

这些标志也可以提供给 `uv sync` 或 `uv run`，以同时更新锁文件_和_环境。

## 导出锁文件

如果你需要将 uv 与其他工具或工作流集成，可以将 `uv.lock` 导出为不同格式，包括 `requirements.txt`、`pylock.toml`（PEP 751）和 CycloneDX SBOM。

```console
$ uv export --format requirements.txt
$ uv export --format pylock.toml
$ uv export --format cyclonedx1.5
```

有关所有导出格式及其用例的全面文档，请参阅[导出指南](./export.md)。

## 部分安装

有时分多步执行安装会很有帮助，例如，在构建 Docker 镜像时为了优化层缓存。`uv sync` 有几个用于此目的的标志。

- `--no-install-project`：不安装当前项目
- `--no-install-workspace`：不安装任何工作空间成员，包括根项目
- `--no-install-package <NO_INSTALL_PACKAGE>`：不安装指定的包

使用这些选项时，目标的所有依赖项仍然会被安装。例如，`--no-install-project` 会省略_项目_本身，但不会省略其任何依赖项。

如果使用不当，这些标志可能导致环境损坏，因为某个包可能会缺少其依赖项。

## 恶意软件检查

!!! important

    同步时进行恶意软件检查目前处于[预览阶段](../preview.md)，在稳定之前可能会发生变化。

在同步过程中，uv 可以通过对照 [OSV](https://osv.dev) 对锁文件进行轻量级扫描，以检查已知的恶意软件。OSV 引用了 OpenSSF 的[恶意软件包数据库](https://github.com/ossf/malicious-packages)中的 MAL 安全公告。

如果锁定的依赖项匹配到恶意软件安全公告，同步将被终止。

要启用恶意软件检查，请在环境中设置 `UV_MALWARE_CHECK=1`。
