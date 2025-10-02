---
subtitle: Caching
description: 学习如何使用uv缓存Python项目的依赖项，包括依赖缓存的工作原理、缓存策略和配置选项。完整指南帮助您优化构建时间和减少网络流量。
---

## 依赖缓存

uv 使用积极的缓存策略来避免重新下载（和重新构建）在先前运行中已经访问过的依赖项。

uv 缓存语义的具体细节因依赖项的性质而异：

- **对于注册表依赖项**（例如从 PyPI 下载的依赖项），uv 会遵循 HTTP 缓存头。
- **对于直接的 URL 依赖项**，uv 会遵循 HTTP 缓存头，并根据 URL 本身进行缓存。
- **对于 Git 依赖项**，uv 根据完全解析的 Git 提交哈希进行缓存。因此，`uv pip compile` 在写入已解析的依赖集时，会将 Git 依赖项固定到特定的提交哈希。
- **对于本地依赖项**，uv 根据源归档（即本地的 `.whl` 或 `.tar.gz` 文件）的最后修改时间进行缓存。对于目录，uv 根据 `pyproject.toml`、`setup.py` 或 `setup.cfg` 文件的最后修改时间进行缓存。

如果您遇到缓存问题，uv 提供了一些解决方法：

- 要强制 uv 为所有依赖项重新验证缓存数据，请向任何命令传递 `--refresh`（例如，`uv sync --refresh` 或 `uv pip install --refresh ...`）。
- 要强制 uv 为特定依赖项重新验证缓存数据，请向任何命令传递 `--refresh-package`（例如，`uv sync --refresh-package flask` 或 `uv pip install --refresh-package flask ...`）。
- 要强制 uv 忽略现有的已安装版本，请向任何安装命令传递 `--reinstall`（例如，`uv sync --reinstall` 或 `uv pip install --reinstall ...`）。

作为一种特殊情况，uv 将始终重新构建并重新安装在命令行上明确传递的任何本地目录依赖项（例如，`uv pip install .`）。

## 动态元数据

默认情况下，只有当目录根目录中的 `pyproject.toml`、`setup.py` 或 `setup.cfg` 文件发生更改，或者添加或删除了 `src` 目录时，uv 才会重新构建和重新安装本地目录依赖项（例如，可编辑安装）。这是一种启发式方法，在某些情况下，可能导致重新安装的次数少于预期。

要将附加信息合并到给定包的缓存键中，您可以在 [`tool.uv.cache-keys`](../reference/settings/configuration.md#cache-keys) 下添加缓存键条目，该条目涵盖文件路径和 Git 提交哈希。设置 [`tool.uv.cache-keys`](../reference/settings/configuration.md#cache-keys) 将替换默认值，因此任何必要的文件（如 `pyproject.toml`）仍应包含在用户定义的缓存键中。

例如，如果一个项目在 `pyproject.toml` 中指定了依赖项，但使用 [`setuptools-scm`](https://pypi.org/project/setuptools-scm/) 来管理其版本，因此每当提交哈希或依赖项发生更改时都应重新构建，您可以将以下内容添加到项目的 `pyproject.toml` 中：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { git = { commit = true } }]
```

如果您的动态元数据包含来自 Git 标签集的信息，您可以扩展缓存键以包含这些标签：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { git = { commit = true, tags = true } }]
```

同样，如果一个项目从 `requirements.txt` 读取以填充其依赖项，您可以将以下内容添加到项目的 `pyproject.toml` 中：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { file = "requirements.txt" }]
```

`file` 键支持通配符（glob），遵循 [`glob`](https://docs.rs/glob/0.3.1/glob/struct.Pattern.html) crate 的语法。例如，要在项目目录或其任何子目录中的 `.toml` 文件被修改时使缓存失效，请使用以下内容：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "**/*.toml" }]
```

!!! note

    使用通配符的成本可能很高，因为 uv 可能需要遍历文件系统以确定是否有任何文件已更改。
    这反过来可能需要遍历大型或深度嵌套的目录。

同样，如果项目依赖于环境变量，您可以将以下内容添加到项目的 `pyproject.toml` 中，以便在环境变量更改时使缓存失效：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { env = "MY_ENV_VAR" }]
```

最后，要在创建或删除特定目录（如 `src`）时使项目失效，请将以下内容添加到项目的 `pyproject.toml` 中：

```toml title="pyproject.toml"
[tool.uv]
cache-keys = [{ file = "pyproject.toml" }, { dir = "src" }]
```

请注意，`dir` 键只会跟踪目录本身的更改，而不会跟踪目录内的任意更改。

作为一种解决方法，如果项目使用的 `dynamic` 元数据未被 `tool.uv.cache-keys` 覆盖，您可以通过将项目添加到 `tool.uv.reinstall-package` 列表来指示 uv _始终_ 重新构建和重新安装它：

```toml title="pyproject.toml"
[tool.uv]
reinstall-package = ["my-package"]
```

这将强制 uv 在每次运行时重新构建和重新安装 `my-package`，无论该包的 `pyproject.toml`、`setup.py` 或 `setup.cfg` 文件是否已更改。

## 缓存安全

可以安全地同时运行多个 uv 命令，即使是针对同一个虚拟环境。uv 的缓存设计为线程安全和仅附加，因此对多个并发的读取者和写入者是健壮的。uv 在安装时对目标虚拟环境应用基于文件的锁，以避免跨进程的并发修改。

请注意，在其他 uv 命令运行时修改 uv 缓存（例如，`uv cache clean`）是 _不_ 安全的，并且 _永远不要_ 直接修改缓存（例如，通过删除文件或目录）。

## 清理缓存

uv 提供了几种从缓存中删除条目的机制：

- `uv cache clean` 从缓存目录中删除 _所有_ 缓存条目，将其完全清除。
- `uv cache clean ruff` 删除 `ruff` 包的所有缓存条目，这对于使单个或有限的一组包的缓存失效很有用。
- `uv cache prune` 删除所有 _未使用_ 的缓存条目。例如，缓存目录可能包含在以前的 uv 版本中创建的条目，这些条目不再需要，可以安全地删除。`uv cache prune` 可以定期安全运行，以保持缓存目录的清洁。

## 在持续集成中缓存

在持续集成环境（如 GitHub Actions 或 GitLab CI）中缓存包安装工件以加快后续运行是很常见的。

默认情况下，uv 会缓存它从源代码构建的 wheel 和它直接下载的预构建 wheel，以实现高性能的包安装。

然而，在持续集成环境中，持久化预构建的 wheel 可能并不可取。对于 uv 来说，事实证明，从缓存中 _省略_ 预构建的 wheel（而是在每次运行时从注册表重新下载它们）通常更快。另一方面，缓存从源代码构建的 wheel 往往是值得的，因为 wheel 构建过程可能很昂贵，特别是对于扩展模块。

为了支持这种缓存策略，uv 提供了一个 `uv cache prune --ci` 命令，该命令从缓存中删除所有预构建的 wheel 和解压的源代码分发，但保留任何从源代码构建的 wheel。我们建议在持续集成作业结束时运行 `uv cache prune --ci`，以确保最大的缓存效率。有关示例，请参阅 [GitHub 集成指南](../guides/integration/github.md#_3)。

## 缓存目录

uv 按以下顺序确定缓存目录：

1.  如果请求了 `--no-cache`，则为临时缓存目录。
2.  通过 `--cache-dir`、`UV_CACHE_DIR` 或 [`tool.uv.cache-dir`](../reference/settings/configuration.md#cache-dir) 指定的特定缓存目录。
3.  系统适当的缓存目录，例如，在 Unix 上为 `$XDG_CACHE_HOME/uv` 或 `$HOME/.cache/uv`，在 Windows 上为 `%LOCALAPPDATA%\uv\cache`。

!!! note

    uv _始终_ 需要一个缓存目录。当请求 `--no-cache` 时，uv 仍将使用临时缓存来在该单次调用中共享数据。

    在大多数情况下，应使用 `--refresh` 而不是 `--no-cache` — 因为它会为后续操作更新缓存，但不会从缓存中读取。

为了性能，缓存目录与 uv 正在操作的 Python 环境位于同一文件系统上非常重要。否则，uv 将无法将文件从缓存链接到环境中，而需要回退到缓慢的复制操作。

## 缓存版本控制

uv 缓存由多个存储桶（例如，用于 wheel 的存储桶、用于源代码分发的存储桶、用于 Git 存储库的存储桶等）组成。每个存储桶都有版本，因此如果某个版本包含对缓存格式的重大更改，uv 将不会尝试从不兼容的缓存存储桶中读取或写入。

例如，uv 0.4.13 包含了对核心元数据存储桶的重大更改。因此，存储桶版本从 v12 增加到 v13。在缓存版本内，更改保证是向前和向后兼容的。

由于缓存格式的更改伴随着缓存版本的更改，因此多个版本的 uv 可以安全地读取和写入同一个缓存目录。但是，如果给定的一对 uv 版本之间的缓存版本发生了更改，那么这些版本可能无法共享相同的基础缓存条目。

例如，为 uv 0.4.12 和 uv 0.4.13 使用单个共享缓存是安全的，尽管由于缓存版本的更改，缓存本身可能在核心元数据存储桶中包含重复的条目。
