---
subtitle: Declaring dependencies
---

# 声明依赖项

最佳实践是在静态文件中声明依赖项，而不是通过即席安装来修改环境。一旦定义了依赖项，就可以[锁定](./compile.md)它们以创建一个一致、可复现的环境。

## 使用 `pyproject.toml`

`pyproject.toml` 文件是用于定义项目配置的 Python 标准。

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

每个键定义一个“extra”，可以使用 `--extra` 和 `--all-extras` 标志或 `package[<extra>]` 语法进行安装。有关更多详细信息，请参阅[安装包](./packages.md#_2)的文档。

有关 `pyproject.toml` 的入门详情，请参阅官方[`pyproject.toml` 指南](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)。

## 使用 `requirements.in`

使用轻量级的 `requirements.txt` 格式来声明项目的依赖项也很常见。每个需求都在其自己的行上定义。通常，此文件被称为 `requirements.in`，以区别于用于锁定依赖项的 `requirements.txt`。

在 `requirements.in` 文件中定义依赖项：

```python title="requirements.in"
httpx
ruff>=0.3.0
```

此格式不支持可选依赖项组。
