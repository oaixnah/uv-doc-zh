---
subtitle: Caching
description: 全面介绍 uv 的缓存机制：涵盖依赖缓存语义（仓库/URL/Git/本地/扁平索引）、动态元数据缓存键配置（tool.uv.cache-keys）、缓存安全性（线程安全与 append-only 设计）、缓存清除命令（uv cache clean/prune）、CI 环境缓存策略（uv cache prune --ci）、缓存目录优先级以及缓存版本管理（桶版本化与兼容性）。
---

# 缓存 {#caching}

## 依赖缓存 {#dependency-caching}

uv 采用激进的缓存策略，以避免重复下载（和重新构建）在之前运行中已经访问过的依赖项。

uv 的缓存语义根据依赖项的性质而有所不同：

- **对于仓库（registry）依赖项**（例如从 PyPI 下载的依赖项），uv 遵循 HTTP 缓存头（caching headers）。
- **对于直接 URL 依赖项**，uv 遵循 HTTP 缓存头，并且还基于 URL 本身进行缓存。
- **对于 Git 依赖项**，uv 基于完全解析的 Git 提交哈希（commit hash）进行缓存。因此，`uv pip compile` 在写入已解析的依赖项集合时，会将 Git 依赖项锁定到特定的提交哈希。
- **对于本地依赖项**，uv 基于源归档文件（即本地 `.whl` 或 `.tar.gz` 文件）的最后修改时间进行缓存。对于目录，uv 基于 `pyproject.toml`、`setup.py` 或 `setup.cfg` 文件的最后修改时间进行缓存。
- **对于扁平索引（flat indexes）**（即 `--find-links` 位置），uv 假定索引内容是不可变的，按文件名缓存每个文件。因此，用新内容替换同名文件（例如，将重新构建的 wheel 放入 `--find-links` 目录中）不会在缓存刷新之前被检测到。

如果你遇到缓存问题，uv 提供了以下几种应急（escape hatch）方案：

- 要完全清除缓存，请运行 `uv cache clean`。要清除特定包的缓存，请运行 `uv cache clean <package-name>`。例如，`uv cache clean ruff` 将清除 `ruff` 包的缓存。
- 要强制 uv 重新验证所有依赖项的缓存数据，请向任何命令传递 `--refresh` 参数（例如，`uv sync --refresh` 或 `uv pip install --refresh ...`）。
- 要强制 uv 重新验证特定依赖项的缓存数据，请向任何命令传递 `--refresh-package` 参数（例如，`uv sync --refresh-package ruff` 或 `uv pip install --refresh-package ruff ...`）。
- 要强制 uv 忽略已安装的版本，请向任何安装命令传递 `--reinstall` 参数（例如，`uv sync --reinstall` 或 `uv pip install --reinstall ...`）。（建议先运行 `uv cache clean <package-name>`，以确保在重新安装之前清除缓存。）

作为一种特殊情况，uv 将始终重新构建和重新安装通过命令行显式传递的任何本地目录依赖项（例如，`uv pip install .`）。

## 动态元数据 {#dynamic-metadata}

默认情况下，uv _仅_在目录根目录中的 `pyproject.toml`、`setup.py` 或 `setup.cfg` 文件发生更改，或者 `src` 目录被添加或移除时，才会重新构建和重新安装本地目录依赖项（例如，可编辑安装（editables））。这是一种启发式方法，在某些情况下可能导致重新安装的次数少于预期。

要将附加信息纳入给定包的缓存键（cache key）中，你可以在 [`tool.uv.cache-keys`](https://docs.astral.sh/uv/reference/settings/#cache-keys) 下添加缓存键条目，该设置涵盖了文件路径和 Git 提交哈希。设置 [`tool.uv.cache-keys`](https://docs.astral.sh/uv/reference/settings/#cache-keys) 将替换默认值，因此任何必要的文件（如 `pyproject.toml`）仍应包含在用户定义的缓存键中。

例如，如果一个项目在 `pyproject.toml` 中指定了依赖项，但使用 [`setuptools-scm`](https://pypi.org/project/setuptools-scm/) 来管理其版本，因此应在提交哈希或依赖项发生更改时重新构建，你可以在项目的 `pyproject.toml` 中添加以下内容：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { git = { commit = true } }]
```

如果你的动态元数据包含了来自 Git 标签集的信息，你可以扩展缓存键以包含标签：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { git = { commit = true, tags = true } }]
```

同样，如果一个项目从 `requirements.txt` 读取依赖项来填充其依赖项，你可以在项目的 `pyproject.toml` 中添加以下内容：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { file = "requirements.txt" }]
```

`file` 键支持 glob 模式，遵循 [`glob`](https://docs.rs/glob/0.3.1/glob/struct.Pattern.html) crate 的语法。例如，要在项目目录或其任何子目录中的 `.toml` 文件被修改时使缓存失效，请使用以下配置：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "**/*.toml" }]
```

!!! note

    使用 glob 模式可能会带来性能开销，因为 uv 可能需要遍历文件系统来确定是否有任何文件发生了更改。而这又可能需要遍历大型或深度嵌套的目录。

同样，如果项目依赖于某个环境变量，你可以在项目的 `pyproject.toml` 中添加以下内容，以便在环境变量更改时使缓存失效：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { env = "MY_ENV_VAR" }]
```

最后，要在特定目录（如 `src`）被创建或移除时使项目失效，请在项目的 `pyproject.toml` 中添加以下内容：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { dir = "src" }]
```

请注意，`dir` 键仅跟踪目录本身的更改，而不跟踪目录内部的任意更改。

作为一种应急方案，如果项目使用了 `dynamic` 元数据，而这些元数据无法被 `tool.uv.cache-keys` 覆盖，你可以通过将项目添加到 `tool.uv.reinstall-package` 列表中来指示 uv _始终_重新构建和重新安装它：

```toml title="pyproject.toml"
[tool.uv]
reinstall-package = ["my-package"]
```

这将强制 uv 在每次运行时重新构建和重新安装 `my-package`，无论该包的 `pyproject.toml`、`setup.py` 或 `setup.cfg` 文件是否发生了更改。

## 缓存安全性 {#cache-safety}

同时运行多个 uv 命令是安全的，即使它们针对同一个虚拟环境也是如此。uv 的缓存被设计为线程安全的（thread-safe）且仅追加（append-only）的，因此对多个并发的读取者和写入者具有鲁棒性。uv 在安装时会对目标虚拟环境应用基于文件的锁，以避免跨进程的并发修改。

请注意，直接修改缓存（例如，删除文件或目录）_永远_是不安全的。

## 清除缓存 {#clearing-the-cache}

uv 提供了几种不同的机制来从缓存中移除条目：

- `uv cache clean` 从缓存目录中移除_所有_缓存条目，将其完全清空。
- `uv cache clean ruff` 移除 `ruff` 包的所有缓存条目，适用于使单个或有限数量包的缓存失效。
- `uv cache prune` 移除所有_未使用_的缓存条目。例如，缓存目录可能包含在之前 uv 版本中创建的、不再需要且可以安全移除的条目。`uv cache prune` 可以定期运行，以保持缓存目录的整洁。

uv 会在其他 uv 命令运行时阻止缓存修改操作。默认情况下，这些 `uv cache` 命令有 5 分钟的超时等待时间，等待其他 uv 进程终止以避免死锁。此超时时间可以通过 [`UV_LOCK_TIMEOUT`](../reference/environment.md#uv_lock_timeout) 进行更改。在已知没有其他 uv 进程正在读取或写入缓存的情况下，可以使用 `--force` 忽略锁。

## 持续集成中的缓存 {#caching-in-continuous-integration}

在持续集成环境（如 GitHub Actions 或 GitLab CI）中，通常会缓存包安装产物（artifacts），以加速后续运行。

默认情况下，uv 会缓存从源码构建的 wheel 以及直接下载的预构建 wheel，以实现高性能的包安装。

然而，在持续集成环境中，持久化预构建 wheel 可能并不理想。使用 uv 时，事实证明，从缓存中_省略_预构建 wheel（改为每次运行时从仓库重新下载）通常更快。另一方面，缓存从源码构建的 wheel 往往是值得的，因为 wheel 构建过程可能很昂贵，尤其是对于扩展模块（extension modules）。

为了支持这种缓存策略，uv 提供了 `uv cache prune --ci` 命令，该命令会从缓存中移除所有预构建 wheel 和未解压的源码分发包（source distributions），但保留所有从源码构建的 wheel。我们建议在持续集成作业结束时运行 `uv cache prune --ci`，以确保最大程度的缓存效率。有关示例，请参阅 [GitHub 集成指南](../guides/integration/github.md#caching)。

## 缓存目录 {#cache-directory}

uv 按以下顺序确定缓存目录：

1. 如果请求了 `--no-cache`，则使用临时缓存目录。
2. 通过 `--cache-dir`、`UV_CACHE_DIR` 或 [`tool.uv.cache-dir`](../reference/settings.md#cache-dir) 指定的特定缓存目录。
3. 系统适当的缓存目录，例如，在 Unix 上为 `$XDG_CACHE_HOME/uv` 或 `$HOME/.cache/uv`，在 Windows 上为 `%LOCALAPPDATA%\uv\cache`。

!!! note

    uv _始终_需要一个缓存目录。当请求 `--no-cache` 时，uv 仍会使用临时缓存来在该单次调用中共享数据。

    在大多数情况下，应使用 `--refresh` 而不是 `--no-cache`——因为它会为后续操作更新缓存，但不会从缓存中读取。

为了性能，缓存目录应位于与 uv 所操作的 Python 环境相同的文件系统上。否则，uv 将无法将文件从缓存链接（link）到环境中，而需要回退到缓慢的复制操作。

## 缓存版本管理 {#cache-versioning}

uv 缓存由多个桶（bucket）组成（例如，wheel 桶、源码分发包桶、Git 仓库桶等）。每个桶都有版本控制，因此如果某个 uv 版本包含对缓存格式的破坏性更改，uv 将不会尝试读取或写入不兼容的缓存桶。

例如，uv 0.4.13 包含了对核心元数据桶的破坏性更改。因此，桶版本从 v12 提升到了 v13。在同一个缓存版本内，更改保证同时具有向前和向后兼容性。

由于缓存格式的更改伴随着缓存版本的更改，多个版本的 uv 可以安全地读取和写入同一个缓存目录。但是，如果缓存版本在某个 uv 版本对之间发生了更改，那么这些版本可能无法共享相同的底层缓存条目。

例如，对 uv 0.4.12 和 uv 0.4.13 使用单个共享缓存是安全的，尽管由于缓存版本的更改，缓存本身可能在核心元数据桶中包含重复的条目。