---
subtitle: Package indexes
description: 学习uv支持的包索引，包括默认索引和自定义索引。了解如何配置uv以使用不同的包索引，以及uv如何处理索引优先级。完整指南帮助您自定义uv的包索引行为。
---

# 包索引

默认情况下，uv 使用 [Python 包索引 (PyPI)](https://pypi.org) 进行依赖解析和包安装。不过，uv 也可以配置为使用其他包索引（包括私有索引），通过 `[[tool.uv.index]]` 配置选项（以及对应的命令行选项 `--index`）来实现。

## 定义索引

要在解析依赖时添加额外的索引，请在 `pyproject.toml` 中添加一个 `[[tool.uv.index]]` 条目：

```toml
[[tool.uv.index]]
# 索引的可选名称。
name = "pytorch"
# 索引的必需 URL。
url = "https://download.pytorch.org/whl/cpu"
```

索引按照定义顺序确定优先级，即配置文件中列出的第一个索引在解析依赖时会被最先查询，而通过命令行提供的索引优先级高于配置文件中的索引。

默认情况下，uv 将 Python 包索引 (PyPI) 作为"默认"索引，即当在其他索引上找不到某个包时使用的索引。要从索引列表中排除 PyPI，请在另一个索引条目上设置 `default = true`（或使用 `--default-index` 命令行选项）：

```toml
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
default = true
```

无论默认索引在索引列表中的位置如何，它始终被视为最低优先级。

索引名称只能包含字母数字字符、连字符、下划线和句点，并且必须是有效的 ASCII 字符。

在命令行（通过 `--index` 或 `--default-index`）或环境变量（`UV_INDEX` 或 `UV_DEFAULT_INDEX`）中提供索引时，名称是可选的，但可以使用 `<name>=<url>` 语法包含名称，例如：

```shell
# 在命令行中。
$ uv lock --index pytorch=https://download.pytorch.org/whl/cpu
# 通过环境变量。
$ UV_INDEX=pytorch=https://download.pytorch.org/whl/cpu uv lock
```

## 将包锁定到指定索引

可以通过在包的 `tool.uv.sources` 条目中指定索引，将包锁定到特定索引。例如，要确保 `torch` _始终_ 从 `pytorch` 索引安装，请在 `pyproject.toml` 中添加以下内容：

```toml
[tool.uv.sources]
torch = { index = "pytorch" }

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
```

类似地，要根据平台从不同的索引拉取，可以通过环境标记（environment markers）提供按不同条件区分的源列表：

```toml title="pyproject.toml"
[project]
dependencies = ["torch"]

[tool.uv.sources]
torch = [
  { index = "pytorch-cpu", marker = "sys_platform == 'darwin'"},
  { index = "pytorch-cu130", marker = "sys_platform != 'darwin'"},
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"

[[tool.uv.index]]
name = "pytorch-cu130"
url = "https://download.pytorch.org/whl/cu130"
```

索引可以标记为 `explicit = true`，以防止包从该索引安装，除非显式地锁定到该索引。例如，要确保 `torch` 从 `pytorch` 索引安装，但所有其他包都从 PyPI 安装，请在 `pyproject.toml` 中添加以下内容：

```toml
[tool.uv.sources]
torch = { index = "pytorch" }

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

通过 `tool.uv.sources` 引用的已命名索引必须在项目的 `pyproject.toml` 文件中定义；通过命令行、环境变量或用户级配置提供的索引将不会被识别。

如果一个索引同时标记为 `default = true` 和 `explicit = true`，它将被视为显式索引（即只能通过 `tool.uv.sources` 使用），同时也会移除 PyPI 作为默认索引。

## 跨多个索引搜索 {#searching-across-multiple-indexes}

默认情况下，uv 会在找到给定包的第一个索引处停止，并将解析范围限制为该第一个索引上存在的版本（`first-index` 策略）。

例如，如果通过 `[[tool.uv.index]]` 指定了一个内部索引，uv 的行为是：如果某个包在该内部索引上存在，它将 _始终_ 从该内部索引安装，而绝不会从 PyPI 安装。这样做的目的是防止"依赖混淆"（dependency confusion）攻击——攻击者在 PyPI 上发布一个与内部包同名的恶意包，从而导致安装恶意包而非内部包。参见 2022 年 12 月的 [`torchtriton` 攻击事件](https://pytorch.org/blog/compromised-nightly-dependency/)。

要选择其他索引行为，可以使用 `--index-strategy` 命令行选项或 `UV_INDEX_STRATEGY` 环境变量，支持以下值：

- `first-index`（默认）：在所有索引中搜索每个包，但将候选版本限制为包含该包的第一个索引中存在的版本。
- `unsafe-first-match`：在所有索引中搜索每个包，但优先选择第一个有兼容版本的索引，即使其他索引上有更新的版本。
- `unsafe-best-match`：在所有索引中搜索每个包，并从合并的候选版本集合中选择最佳版本。

虽然 `unsafe-best-match` 最接近 pip 的行为，但它使用户面临"依赖混淆"攻击的风险。

## 身份验证

大多数私有包索引需要身份验证才能访问包，通常通过用户名和密码（或访问令牌）进行。

!!! tip

    请参阅针对特定私有索引提供者进行身份验证的专用指南：
    [Azure Artifacts](../guides/integration/azure.md)、
    [Google Artifact Registry](../guides/integration/google.md)、
    [AWS CodeArtifact](../guides/integration/aws.md) 和
    [JFrog Artifactory](../guides/integration/jfrog.md)。

### 直接提供凭证

凭证可以直接通过环境变量提供，或嵌入在 URL 中。

例如，假设有一个名为 `internal-proxy` 的索引，需要用户名（`public`）和密码（`koala`），在 `pyproject.toml` 中定义该索引（不含凭证）：

```toml
[[tool.uv.index]]
name = "internal-proxy"
url = "https://example.com/simple"
```

然后，你可以设置 `UV_INDEX_INTERNAL_PROXY_USERNAME` 和 `UV_INDEX_INTERNAL_PROXY_PASSWORD` 环境变量，其中 `INTERNAL_PROXY` 是索引名称的大写形式，非字母数字字符替换为下划线：

```sh
export UV_INDEX_INTERNAL_PROXY_USERNAME=public
export UV_INDEX_INTERNAL_PROXY_PASSWORD=koala
```

通过环境变量提供凭证，可以避免将敏感信息存储在明文的 `pyproject.toml` 文件中。

或者，凭证可以直接嵌入在索引定义中：

```toml
[[tool.uv.index]]
name = "internal"
url = "https://public:koala@pypi-proxy.corp.dev/simple"
```

出于安全考虑，凭证 _绝不会_ 存储在 `uv.lock` 文件中；因此，uv _必须_ 在安装时能够访问经过身份验证的 URL。

### 使用凭证提供者

除了直接提供凭证外，uv 还支持从 netrc 和 keyring 中发现凭证。有关设置特定凭证提供者的详细信息，请参阅 [HTTP 身份验证](./authentication/http.md) 文档。

默认情况下，uv 会在查询提供者之前先尝试未经验证的请求。如果请求失败，uv 将搜索凭证。如果找到凭证，将尝试经过身份验证的请求。

!!! note

    如果设置了用户名，uv 将在发出未经验证的请求之前搜索凭证。

某些索引（如 GitLab）会将未经验证的请求转发到公共索引（如 PyPI）——这意味着 uv 不会搜索凭证。可以通过 `authenticate` 设置按索引更改此行为。例如，要始终搜索凭证：

```toml hl_lines="4"
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
authenticate = "always"
```

当 `authenticate` 设置为 `always` 时，uv 将立即搜索凭证，如果找不到凭证则报错。

### 跨索引搜索时忽略错误代码

使用 [首个索引策略](#searching-across-multiple-indexes) 时，如果遇到 HTTP 401 未授权或 HTTP 403 禁止访问状态码，uv 将停止跨索引搜索。唯一的例外是，uv 在搜索 `pytorch` 索引时会忽略 403（因为该索引在包不存在时返回 403）。

要配置索引忽略哪些错误代码，可以使用 `ignored-error-codes` 设置。例如，对私有索引忽略 403（但不忽略 401）：

```toml
[[tool.uv.index]]
name = "private-index"
url = "https://private-index.com/simple"
authenticate = "always"
ignore-error-codes = [403]
```

当遇到 `404 未找到` 时，uv 将始终继续跨索引搜索。此行为无法覆盖。

### 禁用身份验证

为防止凭证泄露，可以为索引禁用身份验证：

```toml hl_lines="4"
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
authenticate = "never"
```

当 `authenticate` 设置为 `never` 时，uv 将永远不会为该索引搜索凭证，并且如果直接提供了凭证则会报错。

### 自定义缓存控制头

默认情况下，uv 会遵循索引提供的缓存控制头（cache control headers）。例如，PyPI 提供包元数据时带有 `max-age=600` 头，允许 uv 缓存包元数据 10 分钟；而提供 wheels 和源码分发版时带有 `max-age=365000000, immutable` 头，允许 uv 无限期缓存工件。

要覆盖索引的缓存控制头，可以使用 `cache-control` 设置：

```toml
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
cache-control = { api = "max-age=600", files = "max-age=365000000, immutable" }
```

`cache-control` 设置接受一个包含两个可选键的对象：

- `api`：控制 Simple API 请求（包元数据）的缓存。
- `files`：控制工件下载（wheels 和源码分发版）的缓存。

这些键的值是遵循 [HTTP Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) 语法的字符串。例如，要强制 uv 始终重新验证包元数据，可以设置 `api = "no-cache"`：

```toml
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
cache-control = { api = "no-cache" }
```

此设置最常用于覆盖私有索引的默认缓存控制头，这些私有索引通常会（往往是无意地）禁用缓存。我们通常建议遵循 PyPI 的缓存头策略，即设置 `api = "max-age=600"` 和 `files = "max-age=365000000, immutable"`。

### 为索引配置 `exclude-newer`

如果你正在使用 [`exclude-newer`](./resolution.md#reproducible-resolutions)，可以为特定索引配置不同的截止时间：

```toml
[[tool.uv.index]]
name = "internal"
url = "https://internal.example.com/simple"
exclude-newer = "7 days"
```

索引特定的值仅影响从该索引提供的包。包特定的 `exclude-newer-package` 覆盖仍具有更高的优先级。

如果索引不提供 `upload-time` 元数据，你可以完全禁用该索引的截止时间：

```toml
[[tool.uv.index]]
name = "internal"
url = "https://internal.example.com/simple"
exclude-newer = false
```

## "扁平"索引

默认情况下，`[[tool.uv.index]]` 条目被假定为实现 [PEP 503](https://peps.python.org/pep-0503/) Simple Repository API 的 PyPI 风格注册中心。然而，uv 也支持"扁平"索引，即包含 wheels 和源码分发版扁平列表的本地目录或 HTML 页面。在 pip 中，此类索引通过 `--find-links` 选项指定。

要在 `pyproject.toml` 中定义扁平索引，请使用 `format = "flat"` 选项：

```toml
[[tool.uv.index]]
name = "example"
url = "/path/to/directory"
format = "flat"
```

扁平索引与 Simple Repository API 索引支持相同的功能集（例如 `explicit = true`）；你也可以使用 `tool.uv.sources` 将包锁定到扁平索引。

## `--index-url` 和 `--extra-index-url`

除了 `[[tool.uv.index]]` 配置选项外，uv 还支持 pip 风格的 `--index-url` 和 `--extra-index-url` 命令行选项以实现兼容性，其中 `--index-url` 定义默认索引，`--extra-index-url` 定义额外的索引。

这些选项可以与 `[[tool.uv.index]]` 配置选项结合使用，并遵循相同的优先级规则：

- 默认索引始终被视为最低优先级，无论它是通过旧的 `--index-url` 参数、推荐的 `--default-index` 参数，还是带有 `default = true` 的 `[[tool.uv.index]]` 条目定义的。
- 索引按照定义的顺序被查询，无论是通过旧的 `--extra-index-url` 参数、推荐的 `--index` 参数，还是 `[[tool.uv.index]]` 条目。

实际上，`--index-url` 和 `--extra-index-url` 可以被视为未命名的 `[[tool.uv.index]]` 条目，前者启用了 `default = true`。在此上下文中，`--index-url` 映射到 `--default-index`，`--extra-index-url` 映射到 `--index`。
