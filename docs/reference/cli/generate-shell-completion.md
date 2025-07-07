---
subtitle: Generate shell completion
---

# 生成 Shell 补全

生成 shell 补全脚本。

```
uv generate-shell-completion [OPTIONS] <SHELL>
```

## Usage

### [`<SHELL>`](#shell_1)

要生成补全脚本的 shell [可选值: bash, elvish, fish, nushell, powershell, zsh]

## Python options

### [`--managed-python`](#-managed-python)

要求使用 uv 管理的 Python 版本 [env: UV_MANAGED_PYTHON=]

### [`--no-managed-python`](#-no-managed-python)

禁用 uv 管理的 Python 版本 [env: UV_NO_MANAGED_PYTHON=]

## Global options

### [`--allow-insecure-host`](#-allow-insecure-host)

允许与主机的不安全连接 [env: UV_INSECURE_HOST=]

### [`--directory`](#-directory)

在运行命令之前切换到给定目录

### [`--project`](#-project)

在给定项目目录中运行命令 [env: UV_PROJECT=]
