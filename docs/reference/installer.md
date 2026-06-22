---
subtitle: Installer
description: 本文档介绍 uv 安装程序的配置选项，包括如何更改安装路径、禁用 Shell 配置文件的自动修改、在 CI 等临时环境中进行非托管安装，以及如何向安装脚本传递自定义选项。
---

# 安装程序

## 更改安装路径

默认情况下，uv 安装到用户的[可执行文件目录](./storage.md#executable-directory)中。

要更改安装路径，请使用 `UV_INSTALL_DIR`：

=== "macOS and Linux"

    ```console
    $ curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/custom/path" sh
    ```

=== "Windows"

    ```pwsh-session
    PS> powershell -ExecutionPolicy ByPass -c {$env:UV_INSTALL_DIR = "C:\Custom\Path";irm https://astral.sh/uv/install.ps1 | iex}
    ```

!!! note

    更改安装路径仅影响 uv 二进制文件的安装位置。uv 仍会将其数据（缓存、Python 安装、工具等）存储在默认位置。有关这些位置及其自定义方式的详细信息，请参阅[存储参考](./storage.md)。

## 禁用 Shell 配置修改

安装程序可能还会更新你的 Shell 配置文件，以确保 uv 二进制文件在你的 `PATH` 中。要禁用此行为，请使用 `UV_NO_MODIFY_PATH`。例如：

```console
$ curl -LsSf https://astral.sh/uv/install.sh | env UV_NO_MODIFY_PATH=1 sh
```

如果使用 `UV_NO_MODIFY_PATH` 安装，后续操作（如 `uv self update`）将不会修改你的 Shell 配置文件。

## 非托管安装

在 CI 等临时环境中，使用 `UV_UNMANAGED_INSTALL` 将 uv 安装到指定路径，同时阻止安装程序修改 Shell 配置文件或环境变量：

```console
$ curl -LsSf https://astral.sh/uv/install.sh | env UV_UNMANAGED_INSTALL="/custom/path" sh
```

使用 `UV_UNMANAGED_INSTALL` 也会禁用自更新（通过 `uv self update`）。

## 向安装脚本传递选项

推荐使用环境变量，因为它们在各个平台上保持一致。不过，选项也可以直接传递给安装脚本。例如，要查看可用选项：

```console
$ curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --help
```
