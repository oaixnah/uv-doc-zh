---
subtitle: Managing packages
description: uv 管理 Python 包的完整指南，涵盖使用 uv pip 安装、卸载、可编辑安装以及从 requirements.txt 和 pyproject.toml 等文件批量安装包的操作方法。
---

# 管理包 {#managing-packages}

## 安装包 {#installing-a-package}

将包安装到虚拟环境中，例如 Flask：

```console
$ uv pip install flask
```

安装带有可选依赖的包，例如带有 "dotenv" extra 的 Flask：

```console
$ uv pip install "flask[dotenv]"
```

安装多个包，例如 Flask 和 Ruff：

```console
$ uv pip install flask ruff
```

安装带有约束条件的包，例如 Ruff v0.2.0 或更高版本：

```console
$ uv pip install 'ruff>=0.2.0'
```

安装指定版本的包，例如 Ruff v0.3.0：

```console
$ uv pip install 'ruff==0.3.0'
```

从磁盘安装包：

```console
$ uv pip install "ruff @ ./projects/ruff"
```

从 GitHub 安装包：

```console
$ uv pip install "git+https://github.com/astral-sh/ruff"
```

从 GitHub 安装特定引用位置的包：

```console
$ # 安装一个标签
$ uv pip install "git+https://github.com/astral-sh/ruff@v0.2.0"

$ # 安装一个提交
$ uv pip install "git+https://github.com/astral-sh/ruff@1fadefa67b26508cc59cf38e6130bde2243c929d"

$ # 安装一个分支
$ uv pip install "git+https://github.com/astral-sh/ruff@main"
```

从私有仓库安装的说明，请参阅 [Git 认证](../concepts/authentication/git.md) 文档。

## 可编辑包 {#editable-packages}

可编辑包不需要重新安装即可使其源代码的更改生效。

将当前项目安装为可编辑包：

```console
$ uv pip install -e .
```

将另一个目录中的项目安装为可编辑包：

```console
$ uv pip install -e "ruff @ ./project/ruff"
```

## 从文件安装包 {#installing-packages-from-files}

可以通过标准文件格式一次性安装多个包。

从 `requirements.txt` 文件安装：

```console
$ uv pip install -r requirements.txt
```

有关 `requirements.txt` 文件的更多信息，请参阅 [`uv pip compile`](./compile.md) 文档。

从 `pyproject.toml` 文件安装：

```console
$ uv pip install -r pyproject.toml
```

从 `pyproject.toml` 文件安装并启用可选依赖，例如 "foo" extra：

```console
$ uv pip install -r pyproject.toml --extra foo
```

从 `pyproject.toml` 文件安装并启用所有可选依赖：

```console
$ uv pip install -r pyproject.toml --all-extras
```

安装当前项目目录中 `pyproject.toml` 的依赖组（dependency groups），例如 `foo` 组：

```console
$ uv pip install --group foo
```

指定应从哪个项目目录获取依赖组：

```console
$ uv pip install --project some/path/ --group foo --group bar
```

或者，你可以为每个组指定一个 `pyproject.toml` 的路径：

```console
$ uv pip install --group some/path/pyproject.toml:foo --group other/pyproject.toml:bar
```

!!! note

    与 pip 一样，`--group` 标志不适用于通过 `-r` 或 `-e` 等标志指定的其他源。例如，`uv pip install -r some/path/pyproject.toml --group foo` 会从 `./pyproject.toml` 获取 `foo`，而**不是**从 `some/path/pyproject.toml`。

## 卸载包 {#uninstalling-a-package}

卸载包，例如 Flask：

```console
$ uv pip uninstall flask
```

卸载多个包，例如 Flask 和 Ruff：

```console
$ uv pip uninstall flask ruff
```
