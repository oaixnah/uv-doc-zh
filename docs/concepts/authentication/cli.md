---
subtitle: The auth CLI
description: 本文档介绍 uv auth 命令行工具的使用方法，涵盖服务的登录、登出、凭证查看、与 Bazel 等外部工具的凭证助手协议集成，以及凭证存储后端的配置。
---

# `uv auth` 命令行

uv 提供了一个高层级接口，用于存储和检索服务凭证（credentials）。

## 登录服务

要添加服务的凭证，请使用 `uv auth login` 命令：

```console
$ uv auth login example.com
```

此命令会提示输入凭证。

凭证也可以通过 `--username` 和 `--password` 选项提供，或者对于使用 `__token__` 或任意用户名的服务，可以使用 `--token` 选项。

!!! note

    我们建议通过 stdin 提供密钥。使用 `-` 表示该值应从 stdin 读取，例如，对于 `--password`：

    ```console
    $ echo 'my-password' | uv auth login example.com --password -
    ```

    `--token` 也可以使用相同的模式。

添加凭证后，uv 会在需要从给定服务获取内容的打包操作中使用它们。目前仅支持 HTTPS Basic 认证（HTTPS Basic authentication）。凭证尚不会用于 Git 请求。

!!! note

    凭证不会被验证，即错误的凭证不会导致失败。

## 登出服务

要移除凭证，请使用 `uv auth logout` 命令：

```console
$ uv auth logout example.com
```

!!! note

    凭证不会在远程服务器上失效，即它们只会从本地存储中移除，而不会被标记为不可用。

## 显示服务的凭证

要显示为给定 URL 存储的凭证，请使用 `uv auth token` 命令：

```console
$ uv auth token example.com
```

如果登录时使用了用户名，则也需要提供用户名，例如：

```console
$ uv auth token --username foo example.com
```

## 与外部工具一起使用凭证

`uv auth helper` 允许支持凭证助手（credential helpers）的工具从 uv 请求 HTTP 凭证。目前，uv 支持
[Bazel 凭证助手协议](https://github.com/bazelbuild/proposals/blob/main/designs/2022-06-07-bazel-credential-helpers.md)。

此命令旨在由外部工具调用。它从 stdin 读取 JSON 请求，并将 JSON 响应写入 stdout。当匹配的凭证可用时，响应会包含 `Authorization` 头：

```console
$ echo '{"uri": "https://example.com/path"}' | uv --preview-features auth-helper auth helper --protocol=bazel get
{"headers":{"Authorization":["Basic ..."]}}
```

如果未找到凭证，uv 将返回空的头信息集合：

```json
{ "headers": {} }
```

!!! note

    `uv auth helper` 是实验性功能。使用 `--preview-features auth-helper` 或 `UV_PREVIEW_FEATURES=auth-helper` 来禁用警告。

[Bazel 集成指南](../../guides/integration/bazel.md) 说明了如何将此命令与 Bazel 一起使用。

## 配置存储后端

凭证会持久化到 uv 的[凭证存储](./http.md#the-uv-credentials-store)中。

默认情况下，凭证会写入明文文件。可以通过设置 `UV_PREVIEW_FEATURES=native-auth` 来启用加密的系统原生存储后端。
