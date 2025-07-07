---
title: 使用备用包索引
description:
  一份关于如何通过 uv 使用备用包索引的指南，包括 Azure Artifacts、Google Artifact Registry、AWS CodeArtifact 等。
---

# 使用备用包索引

虽然 uv 默认使用官方的 Python 包索引 (PyPI)，但它也支持[备用包索引](../../concepts/indexes.md)。大多数备用索引需要各种形式的身份验证，这需要一些初始设置。

!!! important

    如果使用 pip 接口，请阅读关于在 uv 中[使用多个索引](../../pip/compatibility.md#packages-that-exist-on-multiple-indexes)的文档 — 默认行为与 pip 不同，以防止依赖混淆攻击，但这意味着 uv 可能无法像您预期的那样找到包的版本。

## Azure Artifacts

uv 可以从 [Azure Artifacts](https://learn.microsoft.com/en-us/azure/devops/artifacts/start-using-azure-artifacts?view=azure-devops&tabs=nuget%2Cnugetserver) 安装包，可以使用[个人访问令牌](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows) (PAT)，也可以使用 [`keyring`](https://github.com/jaraco/keyring) 包。

要使用 Azure Artifacts，请将索引添加到您的项目中：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
```

### 使用 Azure 访问令牌进行身份验证

如果有可用的个人访问令牌 (PAT)（例如，Azure pipeline 中的 [`$(System.AccessToken)`](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml#systemaccesstoken)），则可以通过“基本”HTTP 身份验证方案提供凭据。在 URL 的密码字段中包含 PAT。用户名也必须包含，但可以是任何字符串。

例如，将令牌存储在 `$AZURE_ARTIFACTS_TOKEN` 环境变量中，为索引设置凭据：

```bash
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=dummy
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AZURE_ARTIFACTS_TOKEN"
```

!!! note

    `PRIVATE_REGISTRY` 应与您在 `pyproject.toml` 中定义的索引名称匹配。

### 使用 `keyring` 和 `artifacts-keyring` 进行身份验证

您还可以使用带有 [`artifacts-keyring` 插件](https://github.com/Microsoft/artifacts-keyring)的 [`keyring`](https://github.com/jaraco/keyring) 包向 Artifacts 进行身份验证。因为这两个包是向 Azure Artifacts 进行身份验证所必需的，所以它们必须从 Artifacts 以外的源预先安装。

`artifacts-keyring` 插件包装了 [Azure Artifacts Credential Provider 工具](https://github.com/microsoft/artifacts-credprovider)。凭据提供程序支持几种不同的身份验证模式，包括交互式登录 — 有关配置信息，请参阅[该工具的文档](https://github.com/microsoft/artifacts-credprovider)。

uv 仅支持在[子进程模式](../../reference/settings.md#keyring-provider)下使用 `keyring` 包。`keyring` 可执行文件必须在 `PATH` 中，即全局安装或在活动环境中安装。`keyring` CLI 需要 URL 中的用户名，并且必须是 `VssSessionToken`。

```bash
# 从公共 PyPI 预安装 keyring 和 Artifacts 插件
uv tool install keyring --with artifacts-keyring

# 启用 keyring 身份验证
export UV_KEYRING_PROVIDER=subprocess

# 为索引设置用户名
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=VssSessionToken
```

!!! note

    可以使用 [`tool.uv.keyring-provider`](../../reference/settings.md#keyring-provider) 设置在您的 `uv.toml` 或 `pyproject.toml` 中启用 keyring。

    同样，索引的用户名可以直接添加到索引 URL 中。

### 将包发布到 Azure Artifacts

如果您还想将自己的包发布到 Azure Artifacts，可以使用 `uv publish`，如[构建和发布指南](../package.md)中所述。

首先，为您要发布包的索引添加一个 `publish-url`。例如：

```toml title="pyproject.toml" hl_lines="4"
[[tool.uv.index]]
name = "private-registry"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
publish-url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/"
```

然后，配置凭据（如果不使用 keyring）：

```console
$ export UV_PUBLISH_USERNAME=dummy
$ export UV_PUBLISH_PASSWORD="$AZURE_ARTIFACTS_TOKEN"
```

并发布包：

```console
$ uv publish --index private-registry
```

要在不将 `publish-url` 添加到项目的情况下使用 `uv publish`，您可以设置 `UV_PUBLISH_URL`：

```console
$ export UV_PUBLISH_URL=https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/upload/
$ uv publish
```

请注意，此方法不是首选方法，因为 uv 无法在上传构件之前检查包是否已发布。

## Google Artifact Registry

uv 可以从 [Google Artifact Registry](https://cloud.google.com/artifact-registry/docs) 安装包，可以使用访问令牌，也可以使用 [`keyring`](https://github.com/jaraco/keyring) 包。

!!! note

    本指南假定已安装并验证了 [`gcloud`](https://cloud.google.com/sdk/gcloud) CLI。

要使用 Google Artifact Registry，请将索引添加到您的项目中：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/simple/"
```

### 使用 Google 访问令牌进行身份验证

可以通过“基本”HTTP 身份验证方案提供凭据。在 URL 的密码字段中包含访问令牌。用户名必须是 `oauth2accesstoken`，否则身份验证将失败。

使用 `gcloud` 生成令牌：

```bash
export ARTIFACT_REGISTRY_TOKEN=$(
    gcloud auth application-default print-access-token
)
```

!!! note

    您可能需要传递额外的参数才能正确生成令牌（如 `--project`），这是一个基本示例。

然后为索引设置凭据：

```bash
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=oauth2accesstoken
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$ARTIFACT_REGISTRY_TOKEN"
```

!!! note

    `PRIVATE_REGISTRY` 应与您在 `pyproject.toml` 中定义的索引名称匹配。

### 使用 `keyring` 和 `keyrings.google-artifactregistry-auth` 进行身份验证

您还可以使用带有 [`keyrings.google-artifactregistry-auth` 插件](https://github.com/GoogleCloudPlatform/artifact-registry-python-tools)的 [`keyring`](https://github.com/jaraco/keyring) 包向 Artifact Registry 进行身份验证。因为这两个包是向 Artifact Registry 进行身份验证所必需的，所以它们必须从 Artifact Registry 以外的源预先安装。

`keyrings.google-artifactregistry-auth` 插件包装 [gcloud CLI](https://cloud.google.com/sdk/gcloud) 以生成短期访问令牌，将它们安全地存储在系统密钥环中，并在它们过期时刷新它们。

uv 仅支持在[子进程模式](../../reference/settings.md#keyring-provider)下使用 `keyring` 包。`keyring` 可执行文件必须在 `PATH` 中，即全局安装或在活动环境中安装。`keyring` CLI 需要 URL 中的用户名，并且必须是 `oauth2accesstoken`。

```bash
# 从公共 PyPI 预安装 keyring 和 Artifact Registry 插件
uv tool install keyring --with keyrings.google-artifactregistry-auth

# 启用 keyring 身份验证
export UV_KEYRING_PROVIDER=subprocess

# 为索引设置用户名
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=oauth2accesstoken
```

!!! note

    可以使用 [`tool.uv.keyring-provider`](../../reference/settings.md#keyring-provider) 设置在您的 `uv.toml` 或 `pyproject.toml` 中启用 keyring。

    同样，索引的用户名可以直接添加到索引 URL 中。

### 将包发布到 Google Artifact Registry

如果您还想将自己的包发布到 Google Artifact Registry，可以使用 `uv publish`，如[构建和发布指南](../package.md)中所述。

首先，为您要发布包的索引添加一个 `publish-url`。例如：

```toml title="pyproject.toml" hl_lines="4"
[[tool.uv.index]]
name = "private-registry"
url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/simple/"
publish-url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/"
```

然后，配置凭据（如果不使用 keyring）：

```console
$ export UV_PUBLISH_USERNAME=oauth2accesstoken
$ export UV_PUBLISH_PASSWORD="$ARTIFACT_REGISTRY_TOKEN"
```

并发布包：

```console
$ uv publish --index private-registry
```

要在不将 `publish-url` 添加到项目的情况下使用 `uv publish`，您可以设置 `UV_PUBLISH_URL`：

```console
$ export UV_PUBLISH_URL=https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/
$ uv publish
```

请注意，此方法不是首选方法，因为 uv 无法在上传构件之前检查包是否已发布。

## AWS CodeArtifact

uv 可以从 [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/using-python.html) 安装包，可以使用访问令牌，也可以使用 [`keyring`](https://github.com/jaraco/keyring) 包。

!!! note

    本指南假定已安装并验证了 [`awscli`](https://aws.amazon.com/cli/)。

可以这样声明索引：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"
```

### 使用 AWS 访问令牌进行身份验证

可以通过“基本”HTTP 身份验证方案提供凭据。在 URL 的密码字段中包含访问令牌。用户名必须是 `aws`，否则身份验证将失败。

使用 `awscli` 生成令牌：

```bash
export AWS_CODEARTIFACT_TOKEN="$(
    aws codeartifact get-authorization-token \
    --domain <DOMAIN> \
    --domain-owner <ACCOUNT_ID> \
    --query authorizationToken \
    --output text
)"
```

!!! note

    您可能需要传递额外的参数才能正确生成令牌（如 `--region`），这是一个基本示例。

然后为索引设置凭据：

```bash
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=aws
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$AWS_CODEARTIFACT_TOKEN"
```

!!! note

    `PRIVATE_REGISTRY` 应与您在 `pyproject.toml` 中定义的索引名称匹配。

### 使用 `keyring` 和 `keyrings.codeartifact` 进行身份验证

您还可以使用带有 [`keyrings.codeartifact` 插件](https://github.com/jmkeyes/keyrings.codeartifact)的 [`keyring`](https://github.com/jaraco/keyring) 包向 Artifact Registry 进行身份验证。因为这两个包是向 Artifact Registry 进行身份验证所必需的，所以它们必须从 Artifact Registry 以外的源预先安装。

`keyrings.codeartifact` 插件包装 [boto3](https://pypi.org/project/boto3/) 以生成短期访问令牌，将它们安全地存储在系统密钥环中，并在它们过期时刷新它们。

uv 仅支持在[子进程模式](../../reference/settings.md#keyring-provider)下使用 `keyring` 包。`keyring` 可执行文件必须在 `PATH` 中，即全局安装或在活动环境中安装。`keyring` CLI 需要 URL 中的用户名，并且必须是 `aws`。

```bash
# 从公共 PyPI 预安装 keyring 和 AWS CodeArtifact 插件
uv tool install keyring --with keyrings.codeartifact

# 启用 keyring 身份验证
export UV_KEYRING_PROVIDER=subprocess

# 为索引设置用户名
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=aws
```

!!! note

    可以使用 [`tool.uv.keyring-provider`](../../reference/settings.md#keyring-provider) 设置在您的 `uv.toml` 或 `pyproject.toml` 中启用 keyring。

    同样，索引的用户名可以直接添加到索引 URL 中。

### 将包发布到 AWS CodeArtifact

如果您还想将自己的包发布到 AWS CodeArtifact，可以使用 `uv publish`，如[构建和发布指南](../package.md)中所述。

首先，为您要发布包的索引添加一个 `publish-url`。例如：

```toml title="pyproject.toml" hl_lines="4"
[[tool.uv.index]]
name = "private-registry"
url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/simple/"
publish-url = "https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/"
```

然后，配置凭据（如果不使用 keyring）：

```console
$ export UV_PUBLISH_USERNAME=aws
$ export UV_PUBLISH_PASSWORD="$AWS_CODEARTIFACT_TOKEN"
```

并发布包：

```console
$ uv publish --index private-registry
```

要在不将 `publish-url` 添加到项目的情况下使用 `uv publish`，您可以设置 `UV_PUBLISH_URL`：

```console
$ export UV_PUBLISH_URL=https://<DOMAIN>-<ACCOUNT_ID>.d.codeartifact.<REGION>.amazonaws.com/pypi/<REPOSITORY>/
$ uv publish
```

请注意，此方法不是首选方法，因为 uv 无法在上传构件之前检查包是否已发布。

## JFrog Artifactory

uv 可以从 JFrog Artifactory 安装包，可以使用用户名和密码，也可以使用 JWT 令牌。

要使用它，请将索引添加到您的项目中：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://<organization>.jfrog.io/artifactory/api/pypi/<repository>/simple"
```

### 使用用户名和密码进行身份验证

```console
$ export UV_INDEX_PRIVATE_REGISTRY_USERNAME="<username>"
$ export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="<password>"
```

### 使用 JWT 令牌进行身份验证

```console
$ export UV_INDEX_PRIVATE_REGISTRY_USERNAME=""
$ export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$JFROG_JWT_TOKEN"
```

!!! note

    将环境变量名称中的 `PRIVATE_REGISTRY` 替换为您在 `pyproject.toml` 中定义的实际索引名称。

### 将包发布到 JFrog Artifactory

为您的索引定义添加一个 `publish-url`：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://<organization>.jfrog.io/artifactory/api/pypi/<repository>/simple"
publish-url = "https://<organization>.jfrog.io/artifactory/api/pypi/<repository>"
```

!!! important

    如果您将 `--token "$JFROG_TOKEN"` 或 `UV_PUBLISH_TOKEN` 与 JFrog 一起使用，您将收到 401 未授权错误，因为 JFrog 需要一个空用户名，但当使用 `--token` 时，uv 会将 `__token__` 作为用户名传递。

要进行身份验证，请将您的令牌作为密码传递，并将用户名设置为空字符串：

```console
$ uv publish --index <index_name> -u "" -p "$JFROG_TOKEN"
```

或者，您可以设置环境变量：

```console
$ export UV_PUBLISH_USERNAME=""
$ export UV_PUBLISH_PASSWORD="$JFROG_TOKEN"
$ uv publish --index private-registry
```

!!! note

    发布环境变量（`UV_PUBLISH_USERNAME` 和 `UV_PUBLISH_PASSWORD`）不包括索引名称。
