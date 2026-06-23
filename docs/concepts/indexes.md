---
subtitle: Package indexes
description: 本文详细介绍 uv 的包索引配置，涵盖自定义索引定义、将包固定到特定索引、跨多个索引的搜索策略（包括 first-index、unsafe-first-match、unsafe-best-match）、认证方式（环境变量、URL 嵌入、netrc/keyring 凭证提供者）、缓存控制标头自定义、扁平索引支持，以及与 pip 兼容的 --index-url 和 --extra-index-url 选项。
---

# 包索引 {#package-indexes}

默认情况下，uv 使用 [Python Package Index (PyPI)](https://pypi.org) 进行依赖解析和包安装。然而，uv 可以通过 `[[tool.uv.index]]` 配置选项（以及对应的命令行选项 `--index`）配置为使用其他包索引，包括私有索引。

## 定义索引 {#defining-an-index}

要在解析依赖时包含额外的索引，请在 `pyproject.toml` 中添加 `[[tool.uv.index]]` 条目：

```toml
[[tool.uv.index]]
# Optional name for the index.
name = "pytorch"
# Required URL for the index.
url = "https://download.pytorch.org/whl/cpu"
```

索引按定义的顺序确定优先级，即配置文件中列出的第一个索引在解析依赖时优先被查询，而通过命令行提供的索引优先于配置文件中的索引。

默认情况下，uv 将 Python Package Index (PyPI) 作为"默认"索引，即当其他索引上找不到包时使用的索引。要从索引列表中排除 PyPI，请在另一个索引条目上设置 `default = true`（或使用 `--default-index` 命令行选项）：

```toml
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
default = true
```

默认索引始终被视为最低优先级，无论其在索引列表中的位置如何。

索引名称只能包含字母数字字符、破折号、下划线和句点，并且必须是有效的 ASCII 字符。

在命令行上（使用 `--index` 或 `--default-index`）或通过环境变量（`UV_INDEX` 或 `UV_DEFAULT_INDEX`）提供索引时，名称是可选的，但可以使用 `<name>=<url>` 语法包含，如下所示：

```shell
# On the command line.
$ uv lock --index pytorch=https://download.pytorch.org/whl/cpu
# Via an environment variable.
$ UV_INDEX=pytorch=https://download.pytorch.org/whl/cpu uv lock
```

## 将包固定到索引 {#pinning-a-package-to-an-index}

可以通过在包的 `tool.uv.sources` 条目中指定索引来将包固定到特定索引。例如，要确保 `torch` _始终_ 从 `pytorch` 索引安装，请将以下内容添加到 `pyproject.toml`：

```toml
[tool.uv.sources]
torch = { index = "pytorch" }

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
```

类似地，要根据平台从不同的索引拉取包，可以提供按环境标记（environment markers）区分的源列表：

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

可以将索引标记为 `explicit = true`，以防止包从该索引安装，除非显式固定到该索引。例如，要确保 `torch` 从 `pytorch` 索引安装，但所有其他包从 PyPI 安装，请将以下内容添加到 `pyproject.toml`：

```toml
[tool.uv.sources]
torch = { index = "pytorch" }

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

通过 `tool.uv.sources` 引用的命名索引必须在项目的 `pyproject.toml` 文件中定义；通过命令行、环境变量或用户级配置提供的索引将不会被识别。

如果索引同时标记为 `default = true` 和 `explicit = true`，它将被视为显式索引（即只能通过 `tool.uv.sources` 使用），同时也会移除 PyPI 作为默认索引。

## 跨多个索引搜索 {#searching-across-multiple-indexes}

默认情况下，uv 会在第一个包含给定包的索引处停止搜索，并将解析范围限制在该第一个索引上存在的版本（`first-index`）。

例如，如果通过 `[[tool.uv.index]]` 指定了内部索引，uv 的行为是：如果某个包存在于该内部索引上，它将 _始终_ 从该内部索引安装，而不会从 PyPI 安装。其目的是防止"依赖混淆"（dependency confusion）攻击，即攻击者在 PyPI 上发布一个与内部包同名的恶意包，从而导致安装恶意包而不是内部包。例如，参见 2022 年 12 月的 [`torchtriton` 攻击](https://pytorch.org/blog/compromised-nightly-dependency/)。

要选择其他索引行为，请使用 `--index-strategy` 命令行选项或 `UV_INDEX_STRATEGY` 环境变量，支持以下值：

- `first-index`（默认）：跨所有索引搜索每个包，将候选版本限制在包含该包的第一个索引中存在的版本。
- `unsafe-first-match`：跨所有索引搜索每个包，但优先选择第一个有兼容版本的索引，即使其他索引上有更新的版本。
- `unsafe-best-match`：跨所有索引搜索每个包，并从组合的候选版本集中选择最佳版本。

虽然 `unsafe-best-match` 最接近 pip 的行为，但它使用户面临"依赖混淆"攻击的风险。

## 认证 {#authentication}

大多数私有包索引需要认证才能访问包，通常通过用户名和密码（或访问令牌）。

!!! tip

    有关与特定私有索引提供者进行认证的专用指南，请参阅：
    [Azure Artifacts](../guides/integration/azure.md)、
    [Google Artifact Registry](../guides/integration/google.md)、
    [AWS CodeArtifact](../guides/integration/aws.md) 和
    [JFrog Artifactory](../guides/integration/jfrog.md)。

### 直接提供凭证 {#providing-credentials-directly}

凭证可以直接通过环境变量提供，或嵌入到 URL 中。

例如，假设有一个名为 `internal-proxy` 的索引，需要用户名（`public`）和密码（`koala`），请在 `pyproject.toml` 中定义该索引（不带凭证）：

```toml
[[tool.uv.index]]
name = "internal-proxy"
url = "https://example.com/simple"
```

然后，您可以设置 `UV_INDEX_INTERNAL_PROXY_USERNAME` 和 `UV_INDEX_INTERNAL_PROXY_PASSWORD` 环境变量，其中 `INTERNAL_PROXY` 是索引名称的大写形式，非字母数字字符替换为下划线：

```sh
export UV_INDEX_INTERNAL_PROXY_USERNAME=public
export UV_INDEX_INTERNAL_PROXY_PASSWORD=koala
```

通过环境变量提供凭证，可以避免在明文 `pyproject.toml` 文件中存储敏感信息。

或者，凭证可以直接嵌入到索引定义中：

```toml
[[tool.uv.index]]
name = "internal"
url = "https://public:koala@pypi-proxy.corp.dev/simple"
```

出于安全目的，凭证 _永远不会_ 存储在 `uv.lock` 文件中；因此，uv 在安装时 _必须_ 能够访问经过认证的 URL。

### 使用凭证提供者 {#using-credential-providers}

除了直接提供凭证外，uv 还支持从 netrc 和 keyring 中发现凭证。有关设置特定凭证提供者的详细信息，请参阅 [HTTP 认证](./authentication/http.md) 文档。

默认情况下，uv 会在查询凭证提供者之前尝试未认证的请求。如果请求失败，uv 将搜索凭证。如果找到凭证，将尝试认证请求。

!!! note

    如果设置了用户名，uv 将先搜索凭证，然后再进行未认证的请求。

某些索引（例如 GitLab）会将未认证的请求转发到公共索引（如 PyPI），这意味着 uv 不会搜索凭证。可以使用 `authenticate` 设置按索引更改此行为。例如，要始终搜索凭证：

```toml hl_lines="4"
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
authenticate = "always"
```

当 `authenticate` 设置为 `always` 时，uv 将主动搜索凭证，并在找不到凭证时报错。

### 跨索引搜索时忽略错误代码 {#ignoring-error-codes-when-searching-across-indexes}

使用 [first-index 策略](#searching-across-multiple-indexes) 时，如果遇到 HTTP 401 未授权（Unauthorized）或 HTTP 403 禁止（Forbidden）状态码，uv 将停止跨索引搜索。唯一的例外是，uv 在搜索 `pytorch` 索引时会忽略 403 错误（因为该索引在包不存在时返回 403）。

要配置索引忽略哪些错误代码，请使用 `ignored-error-codes` 设置。例如，为私有索引忽略 403（但不忽略 401）：

```toml
[[tool.uv.index]]
name = "private-index"
url = "https://private-index.com/simple"
authenticate = "always"
ignore-error-codes = [403]
```

当遇到 `404 Not Found` 时，uv 将始终继续跨索引搜索，此行为不可覆盖。

### 禁用认证 {#disabling-authentication}

为防止凭证泄露，可以为索引禁用认证：

```toml hl_lines="4"
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
authenticate = "never"
```

当 `authenticate` 设置为 `never` 时，uv 将永远不会搜索给定索引的凭证，并且如果直接提供了凭证将会报错。

### 自定义缓存控制标头 {#customizing-cache-control-headers}

默认情况下，uv 会遵循索引提供的缓存控制标头。例如，PyPI 提供包元数据时附带 `max-age=600` 标头，从而允许 uv 缓存包元数据 10 分钟；而提供 wheel 和源码分发包（source distributions）时附带 `max-age=365000000, immutable` 标头，从而允许 uv 无限期缓存构建产物。

要覆盖索引的缓存控制标头，请使用 `cache-control` 设置：

```toml
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
cache-control = { api = "max-age=600", files = "max-age=365000000, immutable" }
```

`cache-control` 设置接受一个具有两个可选键的对象：

- `api`：控制 Simple API 请求（包元数据）的缓存。
- `files`：控制构建产物下载（wheel 和源码分发包）的缓存。

这些键的值是遵循 [HTTP Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) 语法的字符串。例如，要强制 uv 始终重新验证包元数据，请设置 `api = "no-cache"`：

```toml
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
cache-control = { api = "no-cache" }
```

此设置最常用于覆盖私有索引的默认缓存控制标头，这些索引通常会（无意中）禁用缓存。我们通常建议遵循 PyPI 的缓存标头方法，即设置 `api = "max-age=600"` 和 `files = "max-age=365000000, immutable"`。

### 为索引配置 `exclude-newer` {#configuring-exclude-newer-for-an-index}

如果使用 [`exclude-newer`](./resolution.md#reproducible-resolutions)，可以为特定索引配置不同的截止时间：

```toml
[[tool.uv.index]]
name = "internal"
url = "https://internal.example.com/simple"
exclude-newer = "7 days"
```

索引特定的值仅影响从该索引提供的包。包特定的 `exclude-newer-package` 覆盖仍然优先。

如果索引不提供 `upload-time` 元数据，可以完全禁用该索引的截止时间：

```toml
[[tool.uv.index]]
name = "internal"
url = "https://internal.example.com/simple"
exclude-newer = false
```

## "扁平"索引 {#flat-indexes}

默认情况下，`[[tool.uv.index]]` 条目被假定为实现 [PEP 503](https://peps.python.org/pep-0503/) Simple Repository API 的 PyPI 风格注册表。然而，uv 也支持"扁平"（flat）索引，即包含扁平列表的 wheel 和源码分发包的本地目录或 HTML 页面。在 pip 中，此类索引使用 `--find-links` 选项指定。

要在 `pyproject.toml` 中定义扁平索引，请使用 `format = "flat"` 选项：

```toml
[[tool.uv.index]]
name = "example"
url = "/path/to/directory"
format = "flat"
```

扁平索引支持与 Simple Repository API 索引相同的功能集（例如 `explicit = true`）；您也可以使用 `tool.uv.sources` 将包固定到扁平索引。

## `--index-url` 和 `--extra-index-url` {#index-url-and-extra-index-url}

除了 `[[tool.uv.index]]` 配置选项外，uv 还兼容支持 pip 风格的 `--index-url` 和 `--extra-index-url` 命令行选项，其中 `--index-url` 定义默认索引，`--extra-index-url` 定义额外的索引。

这些选项可以与 `[[tool.uv.index]]` 配置选项结合使用，并遵循相同的优先级规则：

- 默认索引始终被视为最低优先级，无论是通过旧的 `--index-url` 参数、推荐的 `--default-index` 参数，还是带有 `default = true` 的 `[[tool.uv.index]]` 条目定义。
- 索引按定义的顺序被查询，无论是通过旧的 `--extra-index-url` 参数、推荐的 `--index` 参数，还是 `[[tool.uv.index]]` 条目。

实际上，`--index-url` 和 `--extra-index-url` 可以被视为未命名的 `[[tool.uv.index]]` 条目，前者启用了 `default = true`。在此上下文中，`--index-url` 映射到 `--default-index`，`--extra-index-url` 映射到 `--index`。