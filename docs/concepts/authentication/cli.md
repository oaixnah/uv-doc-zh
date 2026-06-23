---
subtitle: The auth CLI
description: 本文档详细介绍 uv auth CLI 命令行工具的使用方法，涵盖服务的登录（uv auth login）与登出（uv auth logout）、凭证查看（uv auth token）、通过 Bazel 凭证助手协议与外部工具共用凭证（uv auth helper），以及凭证存储后端的配置。
---

# `uv auth` CLI {#the-uv-auth-cli}

uv 提供了用于存储和检索服务凭证的高级接口。

## 登录服务 {#logging-in-to-a-service}

要为服务添加凭证，请使用 `uv auth login` 命令：

```console
$ uv auth login example.com
```

这将提示输入凭证。

凭证也可以通过 `--username` 和 `--password` 选项提供，对于使用 `__token__` 或任意用户名的服务，还可以使用 `--token` 选项。

!!! note

    我们建议通过 stdin 提供密钥。使用 `-` 表示该值应从 stdin 读取，例如对于 `--password`：

    ```console
    $ echo 'my-password' | uv auth login example.com --password -
    ```

    同样的模式也可用于 `--token`。

凭证添加后，uv 将在需要从给定服务获取内容的打包操作中使用它们。目前仅支持 HTTPS Basic 认证。凭证尚不用于 Git 请求。

!!! note

    凭证不会进行验证，即错误的凭证不会导致失败。

## 登出服务 {#logging-out-of-a-service}

要移除凭证，请使用 `uv auth logout` 命令：

```console
$ uv auth logout example.com
```

!!! note

    凭证不会在远程服务器上失效，即它们只会从本地存储中移除，不会使其变得不可用。

## 查看服务的凭证 {#showing-credentials-for-a-service}

要查看为给定 URL 存储的凭证，请使用 `uv auth token` 命令：

```console
$ uv auth token example.com
```

如果登录时使用了用户名，则也需要提供用户名，例如：

```console
$ uv auth token --username foo example.com
```

## 与外部工具共用凭证 {#using-credentials-with-external-tools}

`uv auth helper` 允许支持凭证助手的工具从 uv 请求 HTTP 凭证。目前，uv 支持
[Bazel 凭证助手协议](https://github.com/bazelbuild/proposals/blob/main/designs/2022-06-07-bazel-credential-helpers.md)。

该命令旨在由外部工具调用。它从 stdin 读取 JSON 请求，并将 JSON 响应写入 stdout。当存在匹配的凭证时，响应中包含 `Authorization` 头：

```console
$ echo '{"uri": "https://example.com/path"}' | uv --preview-features auth-helper auth helper --protocol=bazel get
{"headers":{"Authorization":["Basic ..."]}}
```

如果未找到凭证，uv 将返回空的头信息集合：

```json
{ "headers": {} }
```

!!! note

    `uv auth helper` 是实验性功能。使用 `--preview-features auth-helper` 或
    `UV_PREVIEW_FEATURES=auth-helper` 来禁用警告。

[Bazel 集成指南](../../guides/integration/bazel.md)介绍了如何将此命令与 Bazel 配合使用。

## 配置存储后端 {#configuring-the-storage-backend}

凭证会持久化存储到 uv 的[凭证存储](./http.md#the-uv-credentials-store)中。

默认情况下，凭证写入明文文件。可以通过 `UV_PREVIEW_FEATURES=native-auth` 启用加密的系统原生存储后端。
