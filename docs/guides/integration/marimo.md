---
title: 将 uv 与 marimo 结合使用
description: 一份将 uv 与 marimo notebook 结合使用于交互式计算、脚本执行和数据应用的完整指南。
---

# 将 uv 与 marimo 结合使用

[marimo](https://github.com/marimo-team/marimo) 是一个开源 Python notebook，它将交互式计算与传统软件的可复现性和可复用性融为一体，让你能够使用 Git 进行版本控制、作为脚本运行以及作为应用分享。由于 marimo notebook 以纯 Python 脚本的形式存储，因此能够与 uv 紧密集成。

你可以轻松地将 marimo 作为独立工具、自包含脚本、在项目中以及在非项目环境中使用。

## 将 marimo 作为独立工具使用

如需临时访问 marimo notebook，你可以随时在隔离环境中启动 marimo 服务器：

```console
$ uvx marimo edit
```

启动特定的 notebook：

```console
$ uvx marimo edit my_notebook.py
```

## 将 marimo 与内联脚本元数据结合使用

由于 marimo notebook 以 Python 脚本的形式存储，它们可以通过 uv 的[脚本支持](../../guides/scripts.md)使用内联脚本元数据来封装自身的依赖项。例如，要将 `numpy` 添加为 notebook 的依赖项，请使用以下命令：

```console
$ uv add --script my_notebook.py numpy
```

要以交互方式编辑包含内联脚本元数据的 notebook，请使用：

```console
$ uvx marimo edit --sandbox my_notebook.py
```

marimo 将自动使用 uv 在包含脚本依赖项的隔离虚拟环境中启动你的 notebook。从 marimo 用户界面安装的包将自动添加到 notebook 的脚本元数据中。

你也可以选择将这些 notebook 作为 Python 脚本运行，而无需打开交互式会话：

```console
$ uv run my_notebook.py
```

## 在项目中使用 marimo

如果你在[项目](../../concepts/projects/index.md)中工作，可以通过以下命令启动一个能够访问项目虚拟环境的 marimo notebook（假设 marimo 是项目依赖项）：

```console
$ uv run marimo edit my_notebook.py
```

要使其他包在你的 notebook 中可用，可以使用 `uv add` 将它们添加到你的项目中，或者使用 marimo 内置的包安装用户界面，它会代表你调用 `uv add`。

如果 marimo 不是项目依赖项，你仍然可以使用以下命令运行 notebook：

```console
$ uv run --with marimo marimo edit my_notebook.py
```

这将允许你在编辑 notebook 时导入项目中的模块。但是，以这种方式运行时通过 marimo 用户界面安装的包不会被添加到你的项目中，并且在后续 marimo 调用中可能会丢失。

## 在非项目环境中使用 marimo

要在与[项目](../../concepts/projects/index.md)无关的虚拟环境中运行 marimo，请直接将 marimo 添加到环境中：

```console
$ uv venv
$ uv pip install numpy
$ uv pip install marimo
$ uv run marimo edit
```

此后，`import numpy` 将在 notebook 中正常工作，并且 marimo 的用户界面安装器将代表你使用 `uv pip install` 将包添加到环境中。

## 将 marimo notebook 作为脚本运行

无论你的依赖项是如何管理的（通过内联脚本元数据、在项目中或在非项目环境中），你都可以使用以下命令将 marimo notebook 作为脚本运行：

```console
$ uv run my_notebook.py
```

这会将你的 notebook 作为 Python 脚本执行，而无需在浏览器中打开交互式会话。
