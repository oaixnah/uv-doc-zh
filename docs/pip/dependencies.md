---
subtitle: Declaring dependencies
description: 本文档介绍如何在 uv 项目中声明依赖项，涵盖使用 pyproject.toml 文件定义项目依赖和可选依赖（extra），以及使用轻量级 requirements.in 文件声明依赖的两种方式。
---

# 声明依赖项

最佳实践是在静态文件中声明依赖项，而不是通过临时安装来修改环境。一旦依赖项被定义，就可以对其进行[锁定](./compile.md)，以创建一致、可复现的环境。

## 使用 `pyproject.toml`

`pyproject.toml` 文件是定义项目配置的 Python 标准。

在 `pyproject.toml` 文件中定义项目依赖项：

```toml title="pyproject.toml"
[project]
dependencies = [
  "httpx",
  "ruff>=0.3.0"
]
```

在 `pyproject.toml` 文件中定义可选依赖项：

```toml title="pyproject.toml"
[project.optional-dependencies]
cli = [
  "rich",
  "click",
]
```

每个键定义了一个"extra"（可选扩展），可以使用 `--extra` 和 `--all-extras` 标志或 `package[<extra>]` 语法来安装。有关更多详细信息，请参阅[安装软件包](./packages.md#installing-packages-from-files)的文档。

有关 `pyproject.toml` 入门的更多详细信息，请参阅官方 [`pyproject.toml` 指南](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)。

## 使用 `requirements.in`

使用轻量级的 [requirements 文件格式](https://pip.pypa.io/en/stable/reference/requirements-file-format/)来声明项目的依赖项也很常见。每个依赖项单独一行定义。通常，这个文件被称为 `requirements.in`，以区别于用于锁定依赖项的 `requirements.txt`。

在 `requirements.in` 文件中定义依赖项：

```python title="requirements.in"
httpx
ruff>=0.3.0
```

此格式不支持可选依赖项分组。
