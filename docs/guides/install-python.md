---
title: 安装和管理 Python
subtitle: Installing Python
description: 一份使用 uv 安装和管理 Python 版本的全面指南，涵盖安装最新版本、指定版本、多版本管理、PyPy 等替代实现、自动下载机制、使用系统已有 Python、升级版本以及查看已安装版本等内容。
---

# 安装 Python {#installing-python}

如果系统上已经安装了 Python，uv 将无需配置即可[检测并使用](#using-existing-python-versions)它。不过，uv 也可以自行安装和管理 Python 版本。uv 会按需[自动安装](#automatic-python-downloads)缺失的 Python 版本——你无需提前安装 Python 即可开始使用。

## 快速入门 {#getting-started}

安装最新的 Python 版本：

```console
$ uv python install
```

!!! note

    Python 官方不发布可分发的二进制文件。因此，uv 使用 Astral 的 [`python-build-standalone`](https://github.com/astral-sh/python-build-standalone) 项目提供的发行版。更多详情请参阅 [Python 发行版](../concepts/python-versions.md#managed-python-distributions)文档。

Python 安装完成后，`uv` 命令会自动使用它。uv 还会将安装的版本添加到你的 `PATH` 中：

```console
$ python3.13
```

默认情况下，uv 仅安装_带版本号_的可执行文件。要安装 `python` 和 `python3` 可执行文件，请使用实验性的 `--default` 选项：

```console
$ uv python install --default
```

!!! tip

    更多详情请参阅[安装 Python 可执行文件](../concepts/python-versions.md#installing-python-executables)文档。

## 安装特定版本 {#installing-a-specific-version}

安装特定版本的 Python：

```console
$ uv python install 3.12
```

安装多个 Python 版本：

```console
$ uv python install 3.11 3.12
```

安装替代的 Python 实现，例如 PyPy：

```console
$ uv python install pypy@3.10
```

更多详情请参阅 [`python install`](../concepts/python-versions.md#installing-a-python-version) 文档。

## 重新安装 Python {#reinstalling-python}

要重新安装 uv 管理的 Python 版本，请使用 `--reinstall`，例如：

```console
$ uv python install --reinstall
```

这将重新安装所有之前已安装的 Python 版本。Python 发行版在持续改进，因此即使 Python 版本没有变化，重新安装也可能解决一些错误。

## 查看 Python 安装情况 {#viewing-python-installations}

查看可用和已安装的 Python 版本：

```console
$ uv python list
```

更多详情请参阅 [`python list`](../concepts/python-versions.md#viewing-available-python-versions) 文档。

## 自动下载 Python {#automatic-python-downloads}

使用 uv 时无需显式安装 Python。默认情况下，uv 会在需要时自动下载 Python 版本。例如，以下命令会在 Python 3.12 未安装时自动下载它：

```console
$ uvx python@3.12 -c "print('hello world')"
```

即使没有指定特定的 Python 版本，uv 也会按需下载最新版本。例如，如果系统上没有任何 Python 版本，以下命令会在创建新的虚拟环境之前先安装 Python：

```console
$ uv venv
```

!!! tip

    如果你希望更好地控制 Python 的下载时机，可以[轻松禁用自动下载](../concepts/python-versions.md#disabling-automatic-python-downloads)功能。

<!-- TODO(zanieb): Restore when Python shim management is added
Note that when an automatic Python installation occurs, the `python` command will not be added to the shell. Use `uv python install-shim` to ensure the `python` shim is installed.
-->

## 使用已有的 Python 版本 {#using-existing-python-versions}

如果系统上已有 Python 安装，uv 会直接使用它们。此行为无需任何配置：只要系统 Python 满足命令调用的要求，uv 就会使用它。详情请参阅 [Python 发现机制](../concepts/python-versions.md#discovery-of-python-versions)文档。

要强制 uv 使用系统 Python，请使用 `--no-managed-python` 标志。更多详情请参阅 [Python 版本偏好](../concepts/python-versions.md#requiring-or-disabling-managed-python-versions)文档。

## 升级 Python 版本 {#upgrading-python-versions}

!!! important

    升级 Python 补丁版本的功能处于_预览_阶段。这意味着该行为是实验性的，可能会发生变化。

将某个 Python 版本升级到最新的补丁版本：

```console
$ uv python upgrade 3.12
```

升级所有 uv 管理的 Python 版本：

```console
$ uv python upgrade
```

更多详情请参阅 [`python upgrade`](../concepts/python-versions.md#upgrading-python-versions) 文档。

## 下一步 {#next-steps}

要了解更多关于 `uv python` 的信息，请参阅 [Python 版本概念](../concepts/python-versions.md)页面和[命令参考](../reference/cli/python.md)。

或者，继续阅读以了解如何使用 uv [运行脚本](./scripts.md)和调用 Python。
