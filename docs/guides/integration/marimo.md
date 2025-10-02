---
title: 将 uv 与 marimo 结合使用
description: 一份将 uv 与 marimo notebook 结合使用于交互式计算、脚本执行和数据应用的完整指南。
---

# 将 uv 与 marimo 结合使用

[marimo](https://github.com/marimo-team/marimo) 是一个开源的 Python notebook，它将交互式计算与传统软件的可复现性和可重用性融为一体，让你可以使用 Git进行版本控制、作为脚本运行以及作为应用程序共享。因为 marimo notebook 以纯 Python 脚本的形式存储，所以它们能够与 uv 紧密集成。

你可以随时将 marimo 作为独立工具、自包含脚本、在项目以及非项目环境中使用。

## 将 marimo 作为独立工具使用

为了临时访问 marimo notebook，可以随时在隔离的环境中启动一个 marimo 服务器：

```console
$ uvx marimo edit
```

启动一个特定的 notebook：

```console
$ uvx marimo edit my_notebook.py
```

## 将 marimo 与内联脚本元数据结合使用

因为 marimo notebook 以 Python 脚本的形式存储，它们可以使用内联脚本元数据来封装自己的依赖项，这得益于 uv 对[脚本的支持](../../guides/scripts.md)。例如，要将 `numpy` 作为依赖项添加到你的 notebook 中，请使用以下命令：

```console
$ uv add --script my_notebook.py numpy
```

要交互式地编辑一个包含内联脚本元数据的 notebook，请使用：

```console
$ uvx marimo edit --sandbox my_notebook.py
```

marimo 会自动使用 uv 在一个隔离的虚拟环境中启动你的 notebook，并带上脚本的依赖项。从 marimo UI 安装的包将自动添加到 notebook 的脚本元数据中。

你可以选择将这些 notebook 作为 Python 脚本运行，而无需打开交互式会话：

```console
$ uv run my_notebook.py
```

## 在项目中使用 marimo

如果你在一个[项目](../../concepts/projects/index.md)中工作，你可以通过以下命令启动一个可以访问项目虚拟环境的 marimo notebook（假设 marimo 是一个项目依赖项）：

```console
$ uv run marimo edit my_notebook.py
```

要为你的 notebook 提供额外的包，要么使用 `uv add` 将它们添加到你的项目中，要么使用 marimo 内置的包安装 UI，它会代表你调用 `uv add`。

如果 marimo 不是项目依赖项，你仍然可以使用以下命令运行 notebook：

```console
$ uv run --with marimo marimo edit my_notebook.py
```

这将让您在编辑 notebook 时导入项目的模块。但是，以这种方式运行时通过 marimo 的 UI 安装的包不会添加到您的项目中，并且在后续的 marimo 调用中可能会消失。

## 在非项目环境中使用 marimo

要在与[项目](../../concepts/projects/index.md)无关的虚拟环境中运行 marimo，请直接将 marimo 添加到环境中：

```console
$ uv venv
$ uv pip install numpy
$ uv pip install marimo
$ uv run marimo edit
```

从这里开始，`import numpy` 将在 notebook 中工作，marimo 的 UI 安装程序将代表你使用 `uv pip install` 将包添加到环境中。

## 将 marimo notebook 作为脚本运行

无论你的依赖项是如何管理的（使用内联脚本元数据、在项目中，还是在非项目环境中），你都可以使用以下命令将 marimo notebook 作为脚本运行：

```console
$ uv run my_notebook.py
```

这将以 Python 脚本的形式执行你的 notebook，而不会在浏览器中打开交互式会话。
