---
subtitle: Locking and syncing
description: 学习如何使用uv锁定和同步Python项目的依赖项，包括自动锁定与同步、检查锁文件是否是最新、创建锁文件和升级锁定的包版本。完整指南帮助您确保项目环境始终是最新的。
---

# 锁定与同步

锁定（Locking）是将项目依赖解析到 [锁文件（lockfile）](./layout.md#_3) 的过程。

同步（Syncing）是从锁文件中安装一部分包到 [项目环境](./layout.md#_2) 的过程。

## 自动锁定与同步

在 uv 中，锁定和同步是_自动_的。例如，当使用 `uv run` 时，项目会在调用所请求的命令之前被锁定和同步。这确保了项目环境始终是最新的。同样，读取锁文件的命令，如 `uv tree`，也会在运行前自动更新它。

要禁用自动锁定，请使用 `--locked` 选项：

```console
$ uv run --locked ...
```

如果锁文件不是最新的，uv 将引发错误而不是更新锁文件。

要在不检查锁文件是否为最新的情况下使用它，请使用 `--frozen` 选项：

```console
$ uv run --frozen ...
```

同样，要在不检查环境是否为最新的情况下运行命令，请使用 `--no-sync` 选项：

```console
$ uv run --no-sync ...
```

## 检查锁文件是否是最新

在考虑锁文件是否是最新时，uv 会检查它是否与项目元数据匹配。
例如，如果您向 `pyproject.toml` 添加一个依赖项，锁文件将被视为过时。同样，如果您更改依赖项的版本约束，使得锁定的版本被排除，锁文件也将被视为过时。但是，如果您更改版本约束，使得现有的锁定版本仍然被包含在内，锁文件仍将被视为最新。

您可以通过向 `uv lock` 传递 `--check` 标志来检查锁文件是否是最新：

```console
$ uv lock --check
```

这等同于其他命令的 `--locked` 标志。

!!! important

    当新版本的包发布时，uv 不会将锁文件视为过时——如果您想升级依赖项，需要明确更新锁文件。有关详细信息，请参阅[升级锁定的包版本](#_10)的文档。

## 创建锁文件

虽然锁文件是[自动](#_2)创建的，但也可以使用 `uv lock` 显式创建或更新锁文件：

```console
$ uv lock
```

## 同步环境

虽然环境是[自动](#_2)同步的，但也可以使用 `uv sync` 显式同步：

```console
$ uv sync
```

手动同步环境对于确保您的编辑器具有正确版本的依赖项特别有用。

### 可编辑安装

当环境同步时，uv 会将项目（以及其他工作区成员）作为_可编辑_包安装，这样更改反映在环境中就不需要重新同步。

要选择退出此行为，请使用 `--no-editable` 选项。

!!! note

    如果项目没有定义构建系统，它将不会被安装。
    有关详细信息，请参阅[构建系统](./config.md#_6)文档。

### 保留无关的包

同步默认是“精确的”，这意味着它将删除锁文件中不存在的任何包。

要保留无关的包，请使用 `--inexact` 选项：

```console
$ uv sync --inexact
```

### 同步可选依赖项

uv 从 `[project.optional-dependencies]` 表中读取可选依赖项。这些通常被称为“extras”。

uv 默认不同步 extras。使用 `--extra` 选项来包含一个 extra。

```console
$ uv sync --extra foo
```

要快速启用所有 extras，请使用 `--all-extras` 选项。

有关如何管理可选依赖项的详细信息，请参阅[可选依赖项](./dependencies.md#_16)文档。

### 同步开发依赖项

uv 从 `[dependency-groups]` 表中读取开发依赖项（如 [PEP 735](https://peps.python.org/pep-0735/) 中所定义）。

`dev` 组是特殊情况，默认情况下会同步。有关更改默认值的详细信息，请参阅[默认组](./dependencies.md#_19)文档。

`--no-dev` 标志可用于排除 `dev` 组。

`--only-dev` 标志可用于安装 `dev` 组，而_不_安装项目及其依赖项。

可以使用 `--all-groups`、`--no-default-groups`、`--group <name>`、`--only-group <name>` 和 `--no-group <name>` 选项来包含或排除其他组。`--only-group` 的语义与 `--only-dev` 相同，项目将不被包括在内。但是，`--only-group` 也会排除默认组。

组排除总是优先于包含，因此给定命令：

```
$ uv sync --no-group foo --group foo
```

`foo` 组将不会被安装。

有关如何管理开发依赖项的详细信息，请参阅[开发依赖项](./dependencies.md#_17)文档。

## 升级锁定的包版本

对于现有的 `uv.lock` 文件，uv 在运行 `uv sync` 和 `uv lock` 时会偏好先前锁定的包版本。只有当项目的依赖约束排除了先前锁定的版本时，包版本才会更改。

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

在所有情况下，升级都受限于项目的依赖约束。例如，如果项目为包定义了上限版本，则升级不会超过该版本。

!!! note

    uv 对 Git 依赖项应用类似的逻辑。例如，如果一个 Git 依赖项引用 `main` 分支，uv 在现有的 `uv.lock` 文件中会偏好锁定的提交 SHA，而不是 `main` 分支上的最新提交，除非使用了 `--upgrade` 或 `--upgrade-package` 标志。

这些标志也可以提供给 `uv sync` 或 `uv run`，以更新锁文件_和_环境。

## 导出锁文件

如果您需要将 uv 与其他工具或工作流集成，您可以使用 `uv export --format requirements-txt` 将 `uv.lock` 导出为 `requirements.txt` 格式。然后，生成的 `requirements.txt` 文件可以通过 `uv pip install` 或其他工具（如 `pip`）进行安装。

通常，我们建议不要同时使用 `uv.lock` 和 `requirements.txt` 文件。如果您发现自己正在导出 `uv.lock` 文件，请考虑开一个 issue 来讨论您的用例。

## 部分安装

有时，分多步执行安装会很有帮助，例如，为了在构建 Docker 镜像时实现最佳的层缓存。`uv sync` 为此有几个标志。

- `--no-install-project`: 不安装当前项目
- `--no-install-workspace`: 不安装任何工作区成员，包括根项目
- `--no-install-package <NO_INSTALL_PACKAGE>`: 不安装给定的包

当使用这些选项时，目标的所有依赖项仍然会被安装。例如，`--no-install-project` 将省略_项目_，但不会省略其任何依赖项。

如果使用不当，这些标志可能会导致环境损坏，因为一个包可能会缺少其依赖项。
