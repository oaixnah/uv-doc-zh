---
subtitle: Preview features
description: uv 预览功能（preview features）详解：介绍如何通过 --preview 标志、UV_PREVIEW 环境变量或 uv.toml 配置文件启用/禁用 uv 的选择性预览功能，涵盖 json-output、pylock、format、malware-check 等全部可用预览特性的说明与使用指南。
---

# 预览功能

uv 包含选择性启用的预览功能，旨在收集社区反馈，并在向所有用户开放之前，确保这些变更确实能带来净收益。

## 启用预览功能

要启用所有预览功能，请使用 `--preview` 标志：

```console
$ uv run --preview ...
```

或者，设置 `UV_PREVIEW` 环境变量：

```console
$ UV_PREVIEW=1 uv run ...
```

要启用特定的预览功能，请使用 `--preview-features` 标志：

```console
$ uv run --preview-features foo ...
```

`--preview-features` 标志可以重复使用以启用多个功能：

```console
$ uv run --preview-features foo --preview-features bar ...
```

或者，功能可以以逗号分隔列表的形式提供：

```console
$ uv run --preview-features foo,bar ...
```

`UV_PREVIEW_FEATURES` 环境变量也可以类似地使用，例如：

```console
$ UV_PREVIEW_FEATURES=foo,bar uv run ...
```

预览功能也可以在 `uv.toml` 中启用，或者在 `pyproject.toml` 和 PEP 723 元数据中的 `[tool.uv]` 下启用：

```toml
preview-features = ["foo", "bar"]
```

设置 `preview-features = true` 可以启用所有预览功能。

部分预览功能在配置文件加载之前就已生效，因此无法通过配置文件启用。

为了向后兼容性，启用不存在的预览功能会发出警告，但不会报错，无论来自何种配置来源。

## 使用预览功能

通常，如果行为变更是由某种用户交互触发的，则无需更改任何预览设置即可使用预览功能。例如，当 `pylock.toml` 支持处于预览阶段时，你可以直接使用 `uv pip install` 配合 `pylock.toml` 文件，而无需额外配置，因为指定 `pylock.toml` 文件本身就表明你希望使用该功能。不过，系统会显示一条警告，提示该功能处于预览阶段。启用该预览功能可以消除此警告。

## 可用的预览功能

以下预览功能目前可用：

- `add-bounds`：允许配置 [`uv add` 的默认边界](../reference/settings.md#add-bounds)。
- `json-output`：允许在各种 uv 命令中使用 `--output-format json`。
- `package-conflicts`：允许在包级别定义工作区冲突。
- `pylock`：允许从 `pylock.toml` 文件安装。
- `python-install-default`：允许[安装 `python` 和 `python3` 可执行文件](./python-versions.md#installing-python-executables)。
- `format`：允许使用 `uv format`。
- `index-exclude-newer`：允许在已配置的包索引上设置 `exclude-newer`。
- `azure-endpoint`：允许使用 Azure 凭据对 Azure Blob Storage 端点的请求进行签名。
- `native-auth`：允许将凭据存储在[系统原生位置](../concepts/authentication/http.md#the-uv-credentials-store)。
- `auth-helper`：允许将 `uv auth helper` 用作外部工具的凭据辅助工具。
- `workspace-metadata`：允许使用 `uv workspace metadata`。
- `workspace-dir`：允许使用 `uv workspace dir`。
- `workspace-list`：允许使用 `uv workspace list`。
- `target-workspace-discovery`：使用包含本地 `uv run` 目标的目录（而非当前工作目录）作为项目和工作区发现的起点。此功能在配置加载之前就已生效。
- `project-directory-must-exist`：拒绝无效的 `--project` 路径，而不是发出警告并继续执行。除 `uv init` 外，该路径必须已作为目录存在或指向一个 `pyproject.toml` 文件。此功能在配置加载之前就已生效。
- `malware-check`：允许 `uv sync` 及其他命令在安装包之前通过 [OSV](https://osv.dev) 检查恶意软件。

## 禁用预览功能

`--no-preview` 选项可用于禁用预览功能。
