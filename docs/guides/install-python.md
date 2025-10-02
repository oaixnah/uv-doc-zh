---
title: 安装和管理 Python
subtitle: Installing Python
description: 一份使用 uv 安装 Python 的指南，内容包括请求特定版本、自动安装、查看已安装版本等。
---

# 安装和管理 Python

如果你的系统上已经安装了 Python，uv 将无需配置即可[检测并使用](#python_4)它。但是，uv 也可以安装和管理 Python 版本。uv 会根据需要[自动安装](#python_3)缺失的 Python 版本——你无需为了开始使用而预先安装 Python。

## 入门

要安装最新的 Python 版本：

```console
$ uv python install
```

!!! note

    Python 官方不发布可分发的二进制文件。因此，uv 使用来自 Astral [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) 项目的发行版。更多详情请参阅 [Python 发行版](../concepts/python-versions.md#uv-python_1)文档。

一旦安装了 Python，`uv` 命令将自动使用它。

!!! important

    当 uv 安装 Python 后，它不会在全局范围内可用（即通过 `python` 命令）。
    此功能的支持尚处于_预览_阶段。详情请参阅[安装 Python 可执行文件](../concepts/python-versions.md#python_3)。

    你仍然可以使用[`uv run`](../guides/scripts.md#python_1) 或 [创建并激活虚拟环境](../pip/environments.md)来直接使用 `python`。

## 安装特定版本

要安装特定的 Python 版本：

```console
$ uv python install 3.12
```

要安装多个 Python 版本：

```console
$ uv python install 3.11 3.12
```

要安装替代的 Python 实现，例如 PyPy：

```console
$ uv python install pypy@3.10
```

更多详情请参阅 [`python install`](../concepts/python-versions.md#python_2) 文档。

## 重新安装 Python

要重新安装由 uv 管理的 Python 版本，请使用 `--reinstall`，例如：

```console
$ uv python install --reinstall
```

这将重新安装所有先前安装的 Python 版本。Python 发行版在不断改进，因此即使 Python 版本没有改变，重新安装也可能解决一些错误。

## 查看 Python 安装

要查看可用和已安装的 Python 版本：

```console
$ uv python list
```

更多详情请参阅 [`python list`](../concepts/python-versions.md#python_6) 文档。

## 自动下载 Python

使用 uv 无需显式安装 Python。默认情况下，当需要时，uv 会自动下载 Python 版本。例如，如果未安装 Python 3.12，以下命令将下载它：

```console
$ uvx python@3.12 -c "print('hello world')"
```

即使没有请求特定的 Python 版本，uv 也会按需下载最新版本。例如，如果你的系统上没有 Python 版本，以下命令将在创建新虚拟环境之前安装 Python：

```console
$ uv venv
```

!!! tip

    如果你想更好地控制 Python 的下载时机，可以[轻松禁用自动下载](../concepts/python-versions.md#python_10)。

<!-- TODO(zanieb): Restore when Python shim management is added
Note that when an automatic Python installation occurs, the `python` command will not be added to the shell. Use `uv python install-shim` to ensure the `python` shim is installed.
-->

## 使用现有的 Python 版本

如果你的系统上存在 Python 安装，uv 将会使用它们。此行为无需配置：如果系统 Python 满足命令调用的要求，uv 将使用它。详情请参阅 [Python 发现](../concepts/python-versions.md#python_8)文档。

要强制 uv 使用系统 Python，请提供 `--no-managed-python` 标志。更多详情请参阅 [Python 版本偏好](../concepts/python-versions.md#python_11)文档。

## 升级 Python 版本

!!! important

    升级 Python 补丁版本的功能尚处于_预览_阶段。这意味着其行为是实验性的，可能会发生变化。

要将 Python 版本升级到最新的受支持补丁版本：

```console
$ uv python upgrade 3.12
```

要升级所有由 uv 管理的 Python 版本：

```console
$ uv python upgrade
```

更多详情请参阅 [`python upgrade`](../concepts/python-versions.md#python_4) 文档。

## 后续步骤

要了解有关 `uv python` 的更多信息，请参阅 [Python 版本](../concepts/python-versions.md)页面和[命令参考](../reference/cli/python.md)。

或者，继续阅读以了解如何[运行脚本](./scripts.md)和使用 uv 调用 Python。
