---
subtitle: Managing packages
description: 一份关于 uv 管理 Python 包的指南，包括安装、升级、卸载、检查包等。
---

# 管理包

## 安装包

要将包（例如 Flask）安装到虚拟环境中：

```console
$ uv pip install flask
```

要安装启用了可选依赖项的包（例如，带有 “dotenv” 附加功能的 Flask）：

```console
$ uv pip install "flask[dotenv]"
```

要安装多个包（例如 Flask 和 Ruff）：

```console
$ uv pip install flask ruff
```

要安装带约束的包（例如 Ruff v0.2.0 或更高版本）：

```console
$ uv pip install 'ruff>=0.2.0'
```

要安装特定版本的包（例如 Ruff v0.3.0）：

```console
$ uv pip install 'ruff==0.3.0'
```

要从磁盘安装包：

```console
$ uv pip install "ruff @ ./projects/ruff"
```

要从 GitHub 安装包：

```console
$ uv pip install "git+https://github.com/astral-sh/ruff"
```

要从 GitHub 安装特定引用的包：

```console
$ # 安装一个标签
$ uv pip install "git+https://github.com/astral-sh/ruff@v0.2.0"

$ # 安装一个提交
$ uv pip install "git+https://github.com/astral-sh/ruff@1fadefa67b26508cc59cf38e6130bde2243c929d"

$ # 安装一个分支
$ uv pip install "git+https://github.com/astral-sh/ruff@main"
```

有关从私有仓库安装的信息，请参阅 [Git 身份验证](../concepts/authentication.md#git) 文档。

## 可编辑包

可编辑包的源代码更改无需重新安装即可生效。

要将当前项目安装为可编辑包：

```console
$ uv pip install -e .
```

要将另一个目录中的项目安装为可编辑包：

```console
$ uv pip install -e "ruff @ ./project/ruff"
```

## 从文件安装包

可以从标准文件格式一次性安装多个包。

从 `requirements.txt` 文件安装：

```console
$ uv pip install -r requirements.txt
```

有关 `requirements.txt` 文件的更多信息，请参阅 [`uv pip compile`](./compile.md) 文档。

从 `pyproject.toml` 文件安装：

```console
$ uv pip install -r pyproject.toml
```

从启用了可选依赖项的 `pyproject.toml` 文件安装（例如，“foo” 附加功能）：

```console
$ uv pip install -r pyproject.toml --extra foo
```

从启用了所有可选依赖项的 `pyproject.toml` 文件安装：

```console
$ uv pip install -r pyproject.toml --all-extras
```

要在当前项目目录的 `pyproject.toml` 中安装依赖组（例如 `foo` 组）：

```console
$ uv pip install --group foo
```

要指定从中获取组的项目目录：

```console
$ uv pip install --project some/path/ --group foo --group bar
```

或者，您可以为每个组指定一个 `pyproject.toml` 的路径：

```console
$ uv pip install --group some/path/pyproject.toml:foo --group other/pyproject.toml:bar
```

!!! note

    与 pip 一样，`--group` 标志不适用于通过 `-r` 或 `-e` 等标志指定的其他源。
    例如，`uv pip install -r some/path/pyproject.toml --group foo` 从 `./pyproject.toml` 而不是 `some/path/pyproject.toml` 中获取 `foo`。

## 卸载包

要卸载包（例如 Flask）：

```console
$ uv pip uninstall flask
```

要卸载多个包（例如 Flask 和 Ruff）：

```console
$ uv pip uninstall flask ruff
```
