---
subtitle: Package indexes
description: 学习uv支持的包索引，包括默认索引和自定义索引。了解如何配置uv以使用不同的包索引，以及uv如何处理索引优先级。完整指南帮助您自定义uv的包索引行为。
---

# 包索引

默认情况下，uv 使用 [Python 软件包索引 (PyPI)](https://pypi.org) 进行依赖解析和软件包安装。但是，uv 可以配置为使用其他软件包索引，包括私有索引，通过 `[[tool.uv.index]]` 配置选项（以及类似功能的命令行选项 `--index`）。

## 定义索引

要在解析依赖项时包含一个额外的索引，请将 `[[tool.uv.index]]` 条目添加到您的 `pyproject.toml` 中：

```toml
[[tool.uv.index]]
# 索引的可选名称。
name = "pytorch"
# 索引的必需 URL。
url = "https://download.pytorch.org/whl/cpu"
```

索引按其定义顺序进行优先级排序，因此配置文件中列出的第一个索引是解析依赖项时首先查询的索引，而通过命令行提供的索引优先于配置文件中的索引。

默认情况下，uv 将 Python 软件包索引 (PyPI) 作为“默认”索引，即在任何其他索引上都找不到软件包时使用的索引。要从索引列表中排除 PyPI，请在另一个索引条目上设置 `default = true`（或使用 `--default-index` 命令行选项）：

```toml
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
default = true
```

无论其在索引列表中的位置如何，默认索引始终被视为最低优先级。

索引名称只能包含字母数字字符、破折号、下划线和句点，并且必须是有效的 ASCII。

在命令行（使用 `--index` 或 `--default-index`）或通过环境变量（`UV_INDEX` 或 `UV_DEFAULT_INDEX`）提供索引时，名称是可选的，但可以使用 `<name>=<url>` 语法包含，如下所示：

```shell
# 在命令行上。
$ uv lock --index pytorch=https://download.pytorch.org/whl/cpu
# 通过环境变量。
$ UV_INDEX=pytorch=https://download.pytorch.org/whl/cpu uv lock
```

## 将软件包固定到索引

通过在其 `tool.uv.sources` 条目中指定索引，可以将软件包固定到特定索引。例如，要确保 `torch` _总是_ 从 `pytorch` 索引安装，请将以下内容添加到您的 `pyproject.toml` 中：

```toml
[tool.uv.sources]
torch = { index = "pytorch" }

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
```

同样，要根据平台从不同的索引中拉取，您可以提供一个由环境标记区分的源列表：

```toml title="pyproject.toml"
[project]
dependencies = ["torch"]

[tool.uv.sources]
torch = [
  { index = "pytorch-cu118", marker = "sys_platform == 'darwin'"},
  { index = "pytorch-cu124", marker = "sys_platform != 'darwin'"},
]

[[tool.uv.index]]
name = "pytorch-cu118"
url = "https://download.pytorch.org/whl/cu118"

[[tool.uv.index]]
name = "pytorch-cu124"
url = "https://download.pytorch.org/whl/cu124"
```

一个索引可以被标记为 `explicit = true`，以防止软件包从该索引安装，除非明确固定到它。例如，要确保 `torch` 从 `pytorch` 索引安装，但所有其他软件包都从 PyPI 安装，请将以下内容添加到您的 `pyproject.toml` 中：

```toml
[tool.uv.sources]
torch = { index = "pytorch" }

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

通过 `tool.uv.sources` 引用的命名索引必须在项目的 `pyproject.toml` 文件中定义；通过命令行、环境变量或用户级配置提供的索引将不会被识别。

如果一个索引同时被标记为 `default = true` 和 `explicit = true`，它将被视为一个显式索引（即，只能通过 `tool.uv.sources` 使用），同时也会移除 PyPI 作为默认索引。

## 跨多个索引搜索

默认情况下，uv 将在找到给定软件包的第一个索引处停止，并将解析限制为该第一个索引中存在的内容（`first-index`）。

例如，如果通过 `[[tool.uv.index]]` 指定了一个内部索引，uv 的行为是，如果一个软件包存在于该内部索引上，它将 _总是_ 从该内部索引安装，而绝不会从 PyPI 安装。其目的是防止“依赖混淆”攻击，即攻击者在 PyPI 上发布一个与内部软件包同名的恶意软件包，从而导致恶意软件包被安装而不是内部软件包。例如，请参阅 2022 年 12 月的 [`torchtriton` 攻击](https://pytorch.org/blog/compromised-nightly-dependency/)。

要选择备用索引行为，请使用 `--index-strategy` 命令行选项或 `UV_INDEX_STRATEGY` 环境变量，它支持以下值：

- `first-index` (默认): 在所有索引中搜索每个软件包，将候选版本限制为包含该软件包的第一个索引中存在的版本。
- `unsafe-first-match`: 在所有索引中搜索每个软件包，但优先选择具有兼容版本的第一个索引，即使其他索引上有更新的版本。
- `unsafe-best-match`: 在所有索引中搜索每个软件包，并从候选版本的组合集中选择最佳版本。

虽然 `unsafe-best-match` 最接近 pip 的行为，但它使用户面临“依赖混淆”攻击的风险。

## 身份验证

大多数私有软件包索引需要身份验证才能访问软件包，通常通过用户名和密码（或访问令牌）。

!!! tip

    有关使用特定私有索引提供程序（例如，来自 AWS、Azure 或 GCP）进行身份验证的详细信息，请参阅[备用索引指南](../guides/integration/alternative-indexes.md)。

### 直接提供凭据

凭据可以通过环境变量直接提供，也可以嵌入到 URL 中。

例如，给定一个名为 `internal-proxy` 的索引，需要用户名 (`public`) 和密码 (`koala`)，请在您的 `pyproject.toml` 中定义该索引（不带凭据）：

```toml
[[tool.uv.index]]
name = "internal-proxy"
url = "https://example.com/simple"
```

然后，您可以设置 `UV_INDEX_INTERNAL_PROXY_USERNAME` 和 `UV_INDEX_INTERNAL_PROXY_PASSWORD` 环境变量，其中 `INTERNAL_PROXY` 是索引名称的大写版本，非字母数字字符替换为下划线：

```sh
export UV_INDEX_INTERNAL_PROXY_USERNAME=public
export UV_INDEX_INTERNAL_PROXY_PASSWORD=koala
```

通过环境变量提供凭据，可以避免在纯文本 `pyproject.toml` 文件中存储敏感信息。

或者，凭据可以直接嵌入到索引定义中：

```toml
[[tool.uv.index]]
name = "internal"
url = "https://public:koala@pypi-proxy.corp.dev/simple"
```

出于安全目的，凭据 _永远不会_ 存储在 `uv.lock` 文件中；因此，uv _必须_ 在安装时有权访问经过身份验证的 URL。

### 使用凭据提供程序

除了直接提供凭据外，uv 还支持从 netrc 和 keyring 中发现凭据。有关设置特定凭据提供程序的详细信息，请参阅 [HTTP 身份验证](./authentication.md#http) 文档。

默认情况下，uv 会在查询提供程序之前尝试未经身份验证的请求。如果请求失败，uv 将搜索凭据。如果找到凭据，将尝试经过身份验证的请求。

!!! note

    如果设置了用户名，uv 将在发出未经身份验证的请求之前搜索凭据。

某些索引（例如 GitLab）会将未经身份验证的请求转发到公共索引，如 PyPI — 这意味着 uv 将不会搜索凭据。可以使用 `authenticate` 设置按索引更改此行为。例如，要始终搜索凭据：

```toml hl_lines="4"
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
authenticate = "always"
```

当 `authenticate` 设置为 `always` 时，uv 将急切地搜索凭据，如果找不到凭据则会出错。

### 跨索引搜索时忽略错误代码

使用 [first-index 策略](#_4)时，如果遇到 HTTP 401 Unauthorized 或 HTTP 403 Forbidden 状态代码，uv 将停止跨索引搜索。唯一的例外是，在搜索 `pytorch` 索引时，uv 将忽略 403s（因为当软件包不存在时，此索引返回 403）。

要配置为索引忽略哪些错误代码，请使用 `ignored-error-codes` 设置。例如，要为私有索引忽略 403s（但不忽略 401s）：

```toml
[[tool.uv.index]]
name = "private-index"
url = "https://private-index.com/simple"
authenticate = "always"
ignore-error-codes = [403]
```

uv 在遇到 `404 Not Found` 时将始终继续跨索引搜索。这不能被覆盖。

### 禁用身份验证

为防止泄露凭据，可以为索引禁用身份验证：

```toml hl_lines="4"
[[tool.uv.index]]
name = "example"
url = "https://example.com/simple"
authenticate = "never"
```

当 `authenticate` 设置为 `never` 时，uv 将永远不会为给定索引搜索凭据，如果直接提供凭据则会出错。

## “扁平”索引

默认情况下，`[[tool.uv.index]]` 条目被假定为实现 [PEP 503](https://peps.python.org/pep-0503/) 简单存储库 API 的 PyPI 样式注册表。但是，uv 还支持“扁平”索引，这些索引是包含 wheels 和源分发包的扁平列表的本地目录或 HTML 页面。在 pip 中，此类索引使用 `--find-links` 选项指定。

要在您的 `pyproject.toml` 中定义一个扁平索引，请使用 `format = "flat"` 选项：

```toml
[[tool.uv.index]]
name = "example"
url = "/path/to/directory"
format = "flat"
```

扁平索引支持与简单存储库 API 索引相同的功能集（例如，`explicit = true`）；您还可以使用 `tool.uv.sources` 将软件包固定到扁平索引。

## `--index-url` 和 `--extra-index-url`

除了 `[[tool.uv.index]]` 配置选项外，uv 还支持 pip 风格的 `--index-url` 和 `--extra-index-url` 命令行选项以实现兼容性，其中 `--index-url` 定义默认索引，`--extra-index-url` 定义附加索引。

这些选项可以与 `[[tool.uv.index]]` 配置选项结合使用，并遵循相同的优先级规则：

- 默认索引始终被视为最低优先级，无论是通过旧版 `--index-url` 参数、推荐的 `--default-index` 参数还是带有 `default = true` 的 `[[tool.uv.index]]` 条目定义。
- 索引按其定义顺序进行查询，无论是通过旧版 `--extra-index-url` 参数、推荐的 `--index` 参数还是 `[[tool.uv.index]]` 条目。

实际上，`--index-url` 和 `--extra-index-url` 可以被认为是未命名的 `[[tool.uv.index]]` 条目，前者启用了 `default = true`。在这种情况下，`--index-url` 映射到 `--default-index`，`--extra-index-url` 映射到 `--index`。
