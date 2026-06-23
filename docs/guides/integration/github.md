---
title: 在 GitHub Actions 中使用 uv
description: 在 GitHub Actions 中使用 uv 的完整指南，涵盖安装配置、Python 版本管理、依赖缓存、私有仓库访问以及发布到 PyPI 等 CI/CD 最佳实践。
---

# 在 GitHub Actions 中使用 uv {#using-uv-in-github-actions}

## 安装 {#installation}

在 GitHub Actions 中使用 uv 时，我们推荐使用官方的
[`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) action，它可以安装 uv、将其添加到
PATH、（可选）持久化缓存等，并支持所有 uv 支持的平台。

安装最新版本的 uv：

```yaml title="example.yml" hl_lines="11 12"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
```

最佳实践是锁定到特定的 uv 版本，例如：

```yaml title="example.yml" hl_lines="14 15"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
        with:
          # 安装特定版本的 uv。
          version: "0.11.23"
```

## 设置 Python {#setting-up-python}

可以使用 `python install` 命令安装 Python：

```yaml title="example.yml" hl_lines="14 15"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0

      - name: Set up Python
        run: uv python install
```

这将遵循项目中锁定的 Python 版本。

或者，也可以使用 GitHub 官方的 `setup-python` action。这种方式可能更快，因为
GitHub 会将 Python 版本与 runner 一起缓存。

设置
[`python-version-file`](https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#using-the-python-version-file-input)
选项以使用项目中锁定的版本：

```yaml title="example.yml" hl_lines="14"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: "Set up Python"
        uses: actions/setup-python@v6
        with:
          python-version-file: ".python-version"

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
```

或者，指定 `pyproject.toml` 文件以忽略锁定版本，使用与项目 `requires-python` 约束兼容的最新版本：

```yaml title="example.yml" hl_lines="14"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: "Set up Python"
        uses: actions/setup-python@v6
        with:
          python-version-file: "pyproject.toml"

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
```

## 多 Python 版本 {#multiple-python-versions}

当使用矩阵（matrix）来测试多个 Python 版本时，通过 `astral-sh/setup-uv` 设置 Python 版本，
这将覆盖 `pyproject.toml` 或 `.python-version` 文件中的 Python 版本规范：

```yaml title="example.yml" hl_lines="17 18"
jobs:
  build:
    name: continuous-integration
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version:
          - "3.10"
          - "3.11"
          - "3.12"

    steps:
      - uses: actions/checkout@v6

      - name: Install uv and set the Python version
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
        with:
          python-version: ${{ matrix.python-version }}
```

如果不使用 `setup-uv` action，可以设置 `UV_PYTHON` 环境变量：

```yaml title="example.yml" hl_lines="12"
jobs:
  build:
    name: continuous-integration
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version:
          - "3.10"
          - "3.11"
          - "3.12"
    env:
      UV_PYTHON: ${{ matrix.python-version }}
    steps:
      - uses: actions/checkout@v6
```

## 同步和运行 {#syncing-and-running}

安装好 uv 和 Python 之后，可以使用 `uv sync` 安装项目，并使用 `uv run` 在环境中运行命令：

```yaml title="example.yml" hl_lines="15 17-22"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v6

      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0

      - name: Install the project
        run: uv sync --locked --all-extras --dev

      - name: Run tests
        # 例如，使用 `pytest`
        run: uv run pytest tests
```

!!! tip

    [`UV_PROJECT_ENVIRONMENT` 设置](../../concepts/projects/config.md#project-environment-path)可
    用于将依赖安装到系统 Python 环境中，而不是创建虚拟环境。

## 缓存 {#caching}

在多次工作流运行之间存储 uv 的缓存可以提高 CI 效率。

[`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) 内置了持久化缓存的支持：

```yaml title="example.yml"
- name: Enable caching
  uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
  with:
    enable-cache: true
```

或者，你也可以使用 `actions/cache` action 手动管理缓存：

```yaml title="example.yml"
jobs:
  install_job:
    env:
      # 为 uv 缓存配置一个固定位置
      UV_CACHE_DIR: /tmp/.uv-cache

    steps:
      # ... 设置 Python 和 uv 的步骤 ...

      - name: Restore uv cache
        uses: actions/cache@v5
        with:
          path: /tmp/.uv-cache
          key: uv-${{ runner.os }}-${{ hashFiles('uv.lock') }}
          restore-keys: |
            uv-${{ runner.os }}-${{ hashFiles('uv.lock') }}
            uv-${{ runner.os }}

      # ... 安装包、运行测试等步骤 ...

      - name: Minimize uv cache
        run: uv cache prune --ci
```

`uv cache prune --ci` 命令用于减小缓存大小，并针对 CI 进行了优化。
其对性能的影响取决于所安装的包。

!!! tip

    如果使用 `uv pip`，请在缓存键中使用 `requirements.txt` 而不是 `uv.lock`。

!!! note

    [post-job-hook]: https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/running-scripts-before-or-after-a-job

    当使用非临时性的自托管 runner 时，默认缓存目录可能会无限增长。
    在这种情况下，在作业之间共享缓存可能不是最优选择。相反，可以将缓存
    移到 GitHub Workspace 内部，并使用
    [Post Job Hook][post-job-hook] 在作业完成后将其删除。

    ```yaml
    install_job:
      env:
        # 为 uv 缓存配置一个相对路径
        UV_CACHE_DIR: ${{ github.workspace }}/.cache/uv
    ```

    使用 post job hook 需要在自托管 runner 上将 `ACTIONS_RUNNER_HOOK_JOB_STARTED` 环境
    变量设置为清理脚本的路径，例如下面所示的脚本。

    ```sh title="clean-uv-cache.sh"
    #!/usr/bin/env sh
    uv cache clean
    ```

## 使用 `uv pip` {#using-uv-pip}

如果使用 `uv pip` 接口而非 uv 项目接口，uv 默认需要一个虚拟环境。
要允许将包安装到系统环境中，可以在所有 `uv` 调用中使用 `--system` 标志，或设置 `UV_SYSTEM_PYTHON` 变量。

`UV_SYSTEM_PYTHON` 变量可以在不同作用域中定义。

在顶层定义以对整个工作流生效：

```yaml title="example.yml"
env:
  UV_SYSTEM_PYTHON: 1

jobs: ...
```

或者，针对工作流中的特定作业：

```yaml title="example.yml"
jobs:
  install_job:
    env:
      UV_SYSTEM_PYTHON: 1
    ...
```

或者，针对作业中的特定步骤：

```yaml title="example.yml"
steps:
  - name: Install requirements
    run: uv pip install -r requirements.txt
    env:
      UV_SYSTEM_PYTHON: 1
```

要重新退出系统模式，可以在任何 uv 调用中使用 `--no-system` 标志。

## 私有仓库 {#private-repos}

如果你的项目[依赖](../../concepts/projects/dependencies.md#git)私有 GitHub 仓库，
你需要配置一个[个人访问令牌（personal access token，PAT）][PAT]以允许 uv 获取它们。

创建具有私有仓库读取权限的 PAT 后，将其添加为[仓库密钥（repository secret）][repository secret]。

然后，你可以使用 [`gh`](https://cli.github.com/) CLI（默认安装在 GitHub Actions
runner 中）来配置
[Git 凭据助手（credential helper）](../../concepts/authentication/git.md#git-credential-helpers)，以便对 `github.com` 上托管的仓库使用 PAT 进行查询。

例如，如果你将仓库密钥命名为 `MY_PAT`：

```yaml title="example.yml"
steps:
  - name: Register the personal access token
    run: echo "${{ secrets.MY_PAT }}" | gh auth login --with-token
  - name: Configure the Git credential helper
    run: gh auth setup-git
```

[PAT]:
  https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
[repository secret]:
  https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository

## 发布到 PyPI {#publishing-to-pypi}

可以使用 uv 从 GitHub Actions 构建并将你的包发布到 PyPI。我们在
[astral-sh/trusted-publishing-examples](https://github.com/astral-sh/trusted-publishing-examples)
中提供了一个独立示例。该工作流使用[可信发布（trusted publishing）](https://docs.pypi.org/trusted-publishers/)，因此无需配置任何凭据。

在示例工作流中，我们使用一个脚本来测试源分发包（source distribution）和 wheel 是否都能正常工作，以及是否遗漏了任何文件。此步骤为推荐步骤，但并非必须。

首先，向你的项目添加一个发布工作流：

```yaml title=".github/workflows/release.yml"
name: "Publish release to PyPI"

on:
  push:
    tags:
      # 在任何以 `v` 开头的标签上发布，例如 v0.1.0
      - v*

jobs:
  run:
    runs-on: ubuntu-latest
    environment:
      name: pypi
    permissions:
      id-token: write
      contents: read
    steps:
      - name: Checkout
        uses: actions/checkout@v6
      - name: Install uv
        uses: astral-sh/setup-uv@08807647e7069bb48b6ef5acd8ec9567f424441b # v8.1.0
      - name: Install Python 3.13
        run: uv python install 3.13
      - name: Build
        run: uv build
      # 检查基本功能是否正常，以及是否遗漏了关键文件
      - name: Smoke test (wheel)
        run: uv run --isolated --no-project --with dist/*.whl tests/smoke_test.py
      - name: Smoke test (source distribution)
        run: uv run --isolated --no-project --with dist/*.tar.gz tests/smoke_test.py
      - name: Publish
        run: uv publish
```

然后，在 GitHub 仓库的 "Settings" -> "Environments" 下创建工作流中定义的环境。

![GitHub 设置对话框，显示如何在 "Settings" -> "Environments" 下添加 "pypi" 环境](../../assets/github-add-environment.png)

在 PyPI 项目的 "Publishing" 设置中添加一个[可信发布者（trusted publisher）](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)。
确保所有字段与你的 GitHub 配置匹配。

![PyPI 项目发布设置对话框，显示如何为可信发布者配置设置所有字段](../../assets/pypi-add-trusted-publisher.png)

保存后：

![PyPI 项目发布设置对话框，显示已配置的可信发布设置](../../assets/pypi-with-trusted-publisher.png)

最后，创建一个发布标签并推送。确保它以 `v` 开头以匹配工作流中的模式。

```console
$ git tag -a v0.1.0 -m v0.1.0
$ git push --tags
```
