---
title: Azure Artifacts
description: 使用 uv 与 Azure Artifacts 安装和发布 Python 包。
---

# Azure Artifacts

uv 可以从 [Azure Artifacts](https://learn.microsoft.com/en-us/azure/devops/artifacts/start-using-azure-artifacts?view=azure-devops&tabs=nuget%2Cnugetserver) 安装包，方式有两种：使用[个人访问令牌 (Personal Access Token, PAT)](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows)，或者使用 [`keyring`](https://github.com/jaraco/keyring) 包。

要使用 Azure Artifacts，请将索引添加到你的项目中：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
```

## 使用 Azure 访问令牌进行身份验证

如果有可用的个人访问令牌 (PAT)（例如 [Azure 流水线中的 `$(System.AccessToken)`](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml#systemaccesstoken)），可以通过 "Basic" HTTP 认证方案提供凭据。将 PAT 包含在 URL 的密码字段中。用户名也必须包含，但可以是任意字符串。

例如，假设令牌存储在 `$AZURE_ARTIFACTS_TOKEN` 环境变量中，可以通过以下方式为索引设置凭据：

```bash
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=dummy
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AZURE_ARTIFACTS_TOKEN"
```

!!! note

    `PRIVATE_REGISTRY` 应与你在 `pyproject.toml` 中定义的索引名称一致。

## 使用 `keyring` 和 `artifacts-keyring` 进行身份验证

你还可以使用 [`keyring`](https://github.com/jaraco/keyring) 包及其 [`artifacts-keyring` 插件](https://github.com/Microsoft/artifacts-keyring) 对 Artifacts 进行身份验证。由于这两个包是向 Azure Artifacts 进行身份验证所必需的，因此必须从 Artifacts 以外的源预先安装。

`artifacts-keyring` 插件封装了 [Azure Artifacts Credential Provider 工具](https://github.com/microsoft/artifacts-credprovider)。该凭据提供程序支持多种不同的身份验证模式，包括交互式登录——有关配置信息，请参阅[该工具的文档](https://github.com/microsoft/artifacts-credprovider)。

uv 仅支持在[子进程模式](../../reference/settings.md#keyring-provider)下使用 `keyring` 包。`keyring` 可执行文件必须在 `PATH` 中，即全局安装或在当前激活的环境中安装。`keyring` CLI 要求 URL 中包含用户名，且用户名必须为 `VssSessionToken`。

```bash
# 从公共 PyPI 预安装 keyring 和 Artifacts 插件
uv tool install keyring --with artifacts-keyring

# 启用 keyring 身份验证
export UV_KEYRING_PROVIDER=subprocess

# 设置索引的用户名
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=VssSessionToken
```

!!! note

    [`tool.uv.keyring-provider`](../../reference/settings.md#keyring-provider) 设置可用于在 `uv.toml` 或 `pyproject.toml` 中启用 keyring。

    同样，索引的用户名也可以直接添加到索引 URL 中。

## 发布包

如果你还想将自己的包发布到 Azure Artifacts，可以按照[构建和发布指南](../package.md)中的说明使用 `uv publish`。

首先，为你想要发布包的索引添加 `publish-url`。例如：

```toml title="pyproject.toml" hl_lines="4"
[[tool.uv.index]]
name = "private-registry"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
publish-url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/"
```

然后，配置凭据（如果不使用 keyring）：

```bash
export UV_PUBLISH_USERNAME=dummy
export UV_PUBLISH_PASSWORD="$AZURE_ARTIFACTS_TOKEN"
```

接着发布包：

```bash
uv publish --index private-registry
```

要在不将 `publish-url` 添加到项目中的情况下使用 `uv publish`，可以设置 `UV_PUBLISH_URL`：

```bash
export UV_PUBLISH_URL=https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/
uv publish
```

请注意，此方法不太推荐，因为 uv 无法在上传构件之前检查包是否已经发布。
