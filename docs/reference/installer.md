---
subtitle: Installer
description: 了解 uv 项目的安装程序。
---

# 安装程序

## 更改安装路径

默认情况下，uv 安装在 `~/.local/bin`。如果设置了 `XDG_BIN_HOME`，则会使用该路径。
同样，如果设置了 `XDG_DATA_HOME`，目标目录将被推断为 `XDG_DATA_HOME/../bin`。

要更改安装路径，请使用 `UV_INSTALL_DIR`：

=== "macOS 和 Linux"

    ```console
    $ curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/custom/path" sh
    ```

=== "Windows"

    ```pwsh-session
    PS> powershell -ExecutionPolicy ByPass -c {$env:UV_INSTALL_DIR = "C:\Custom\Path";irm https://astral.sh/uv/install.ps1 | iex}
    ```

## 禁用 shell 修改

安装程序可能还会更新您的 shell 配置文件，以确保 uv 二进制文件在您的 `PATH` 中。要禁用此行为，请使用 `INSTALLER_NO_MODIFY_PATH`。例如：

```console
$ curl -LsSf https://astral.sh/uv/install.sh | env INSTALLER_NO_MODIFY_PATH=1 sh
```

如果使用 `INSTALLER_NO_MODIFY_PATH` 安装，后续操作（如 `uv self update`）将不会修改您的 shell 配置文件。

## 非托管安装

在 CI 等临时环境中，使用 `UV_UNMANAGED_INSTALL` 将 uv 安装到特定路径，同时防止安装程序修改 shell 配置文件或环境变量：

```console
$ curl -LsSf https://astral.sh/uv/install.sh | env UV_UNMANAGED_INSTALL="/custom/path" sh
```

使用 `UV_UNMANAGED_INSTALL` 也会禁用自我更新（通过 `uv self update`）。

## 向安装脚本传递选项

建议使用环境变量，因为它们在各平台上是一致的。但是，也可以直接向安装脚本传递选项。例如，要查看可用选项：

```console
$ curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --help
```
