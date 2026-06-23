---
title: Google Artifact Registry
description: 使用 uv 与 Google Artifact Registry 集成，用于安装和发布 Python 包。
---

# Google Artifact Registry

uv 可以从
[Google Artifact Registry](https://cloud.google.com/artifact-registry/docs) 安装包，方式包括使用访问令牌（access token），或使用 [`keyring`](https://github.com/jaraco/keyring) 包。

!!! note

    本指南假设 [`gcloud`](https://cloud.google.com/sdk/gcloud) CLI 已安装并完成身份验证。

要使用 Google Artifact Registry，请将索引添加到你的项目中：

```toml title="pyproject.toml"
[[tool.uv.index]]
name = "private-registry"
url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/simple/"
```

## 使用 Google 访问令牌进行身份验证

凭据可以通过 "Basic" HTTP 身份验证方案提供。将访问令牌包含在 URL 的密码字段中。用户名必须为 `oauth2accesstoken`，否则身份验证将失败。

使用 `gcloud` 生成令牌：

```bash
export ARTIFACT_REGISTRY_TOKEN=$(
    gcloud auth application-default print-access-token
)
```

!!! note

    你可能需要传递额外的参数来正确生成令牌（例如 `--project`），以上仅为基本示例。

然后为索引设置凭据：

```bash
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=oauth2accesstoken
export UV_INDEX_PRIVATE_REGISTRY_PASSWORD="$ARTIFACT_REGISTRY_TOKEN"
```

!!! note

    `PRIVATE_REGISTRY` 应与你在 `pyproject.toml` 中定义的索引名称相匹配。

## 使用 `keyring` 和 `keyrings.google-artifactregistry-auth` 进行身份验证

你还可以使用 [`keyring`](https://github.com/jaraco/keyring) 包搭配 [`keyrings.google-artifactregistry-auth` 插件](https://github.com/GoogleCloudPlatform/artifact-registry-python-tools)来对 Artifact Registry 进行身份验证。由于这两个包是进行 Artifact Registry 身份验证所必需的，它们必须从 Artifact Registry 以外的源预先安装。

`keyrings.google-artifactregistry-auth` 插件封装了 [gcloud CLI](https://cloud.google.com/sdk/gcloud)，用于生成短期访问令牌，将其安全地存储在系统密钥环（keyring）中，并在过期时自动刷新。

uv 仅支持在[子进程模式](../../reference/settings/configuration.md#keyring-provider) 下使用 `keyring` 包。`keyring` 可执行文件必须在 `PATH` 中，即需全局安装或安装在当前激活的环境中。`keyring` CLI 要求 URL 中包含用户名，且必须为 `oauth2accesstoken`。

```bash
# 从公共 PyPI 预安装 keyring 和 Artifact Registry 插件
uv tool install keyring --with keyrings.google-artifactregistry-auth

# 启用 keyring 身份验证
export UV_KEYRING_PROVIDER=subprocess

# 设置索引的用户名
export UV_INDEX_PRIVATE_REGISTRY_USERNAME=oauth2accesstoken
```

!!! note

    [`tool.uv.keyring-provider`](../../reference/settings/configuration.md#keyring-provider) 设置可用于在 `uv.toml` 或 `pyproject.toml` 中启用 keyring。

    同样，索引的用户名也可以直接添加到索引 URL 中。

## 发布包

如果你还想将自己的包发布到 Google Artifact Registry，可以使用 `uv publish`，如[构建与发布指南](../package.md)中所述。

首先，为你要发布包的索引添加 `publish-url`。例如：

```toml title="pyproject.toml" hl_lines="4"
[[tool.uv.index]]
name = "private-registry"
url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/simple/"
publish-url = "https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/"
```

然后，配置凭据（如果不使用 keyring）：

```bash
export UV_PUBLISH_USERNAME=oauth2accesstoken
export UV_PUBLISH_PASSWORD="$ARTIFACT_REGISTRY_TOKEN"
```

并发布包：

```bash
uv publish --index private-registry
```

要在不向项目添加 `publish-url` 的情况下使用 `uv publish`，你可以设置 `UV_PUBLISH_URL`：

```bash
export UV_PUBLISH_URL=https://<REGION>-python.pkg.dev/<PROJECT>/<REPOSITORY>/
uv publish
```

请注意，此方法不是首选方式，因为在上传制品之前，uv 无法检查包是否已发布。
