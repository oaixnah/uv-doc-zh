---
title: 将 uv 与 pre-commit 结合使用
description: 一份关于如何将 uv 与 pre-commit 结合使用的指南，用于自动更新锁定文件、导出需求和编译需求文件。
---

# 在 pre-commit 中使用 uv

官方 pre-commit钩子见 [`astral-sh/uv-pre-commit`](https://github.com/astral-sh/uv-pre-commit)。

要将 uv 与 pre-commit 结合使用，请将以下示例之一添加到 `.pre-commit-config.yaml` 的 `repos` 列表中。

为确保即使 `pyproject.toml` 文件已更改，`uv.lock` 文件也是最新的：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.7.19
    hooks:
      - id: uv-lock
```

要使 `requirements.txt` 文件与 `uv.lock` 文件保持同步：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.7.19
    hooks:
      - id: uv-export
```

编译需求文件：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.7.19
    hooks:
      # 编译需求
      - id: pip-compile
        args: [requirements.in, -o, requirements.txt]
```

要编译其他需求文件，请修改 `args` 和 `files`：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.7.19
    hooks:
      # 编译需求
      - id: pip-compile
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```

要同时在多个文件上运行钩子，请添加其他条目：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.7.19
    hooks:
      # 编译需求
      - id: pip-compile
        name: pip-compile requirements.in
        args: [requirements.in, -o, requirements.txt]
      - id: pip-compile
        name: pip-compile requirements-dev.in
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```
