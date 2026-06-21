---
title: 将 uv 与 pre-commit 结合使用
description: 一份关于如何将 uv 与 pre-commit 结合使用的指南，用于自动更新锁定文件、导出需求和编译需求文件。
---

# 在 pre-commit 中使用 uv

官方 pre-commit hook 已发布在 [`astral-sh/uv-pre-commit`](https://github.com/astral-sh/uv-pre-commit)。

要在 pre-commit 中使用 uv，请将以下示例之一添加到 `.pre-commit-config.yaml` 的 `repos` 列表中。

确保即使 `pyproject.toml` 文件发生更改，`uv.lock` 文件也能保持最新：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.11.23
    hooks:
      - id: uv-lock
```

保持 `requirements.txt` 文件与 `uv.lock` 文件同步：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.11.23
    hooks:
      - id: uv-export
```

编译 requirements 文件：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.11.23
    hooks:
      # 编译 requirements
      - id: pip-compile
        args: [requirements.in, -o, requirements.txt]
```

要编译其他 requirements 文件，请修改 `args` 和 `files`：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.11.23
    hooks:
      # 编译 requirements
      - id: pip-compile
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```

要同时对多个文件运行 hook，请添加额外的条目：

```yaml title=".pre-commit-config.yaml"
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv 版本。
    rev: 0.11.23
    hooks:
      # 编译 requirements
      - id: pip-compile
        name: pip-compile requirements.in
        args: [requirements.in, -o, requirements.txt]
      - id: pip-compile
        name: pip-compile requirements-dev.in
        args: [requirements-dev.in, -o, requirements-dev.txt]
        files: ^requirements-dev\.(in|txt)$
```
