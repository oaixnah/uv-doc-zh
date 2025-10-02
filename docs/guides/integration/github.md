---
title: 在 GitHub Actions 中使用 uv
description:
  在 GitHub Actions 中使用 uv 的指南，包括安装、设置 Python、安装依赖项等。
---

# 在 GitHub Actions 中使用 uv

## 安装

对于在 GitHub Actions 中使用，我们推荐官方的 [`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) action，它会安装 uv，将其添加到 PATH，（可选）持久化缓存等，并支持所有 uv 支持的平台。

要安装最新版本的 uv：

```yaml title="example.yml" hl_lines="11-12"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
```

最佳实践是固定到特定的 uv 版本，例如：

```yaml title="example.yml" hl_lines="14 15"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5
        with:
          # Install a specific version of uv.
          version: "0.8.18"
```

## 设置 Python

可以使用 `python install` 命令安装 Python：

```yaml title="example.yml" hl_lines="14 15"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Set up Python
        run: uv python install
```

这将遵循项目中固定的 Python 版本。

或者，可以使用官方的 GitHub `setup-python` action。这可能会更快，因为 GitHub 会将 Python 版本与运行器一起缓存。

设置
[`python-version-file`](https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#using-the-python-version-file-input)
选项以使用项目中固定的版本：

```yaml title="example.yml" hl_lines="14 15 16 17"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: "Set up Python"
        uses: actions/setup-python@v5
        with:
          python-version-file: ".python-version"
```

或者，指定 `pyproject.toml` 文件以忽略固定版本，并使用与项目的 `requires-python` 约束兼容的最新版本：

```yaml title="example.yml" hl_lines="17"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: "Set up Python"
        uses: actions/setup-python@v5
        with:
          python-version-file: "pyproject.toml"
```

## 多个 Python 版本

当使用矩阵测试多个 Python 版本时，使用 `astral-sh/setup-uv` 设置 Python 版本，这将覆盖 `pyproject.toml` 或 `.python-version` 文件中的 Python 版本规范：

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
      - uses: actions/checkout@v4

      - name: Install uv and set the python version
        uses: astral-sh/setup-uv@v5
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
      - uses: actions/checkout@v4
```

## 同步和运行

安装 uv 和 Python 后，可以使用 `uv sync` 安装项目，并使用 `uv run` 在环境中运行命令：

```yaml title="example.yml" hl_lines="17-22"
name: Example

jobs:
  uv-example:
    name: python
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v5

      - name: Install the project
        run: uv sync --locked --all-extras --dev

      - name: Run tests
        # For example, using `pytest`
        run: uv run pytest tests
```

!!! tip

    [`UV_PROJECT_ENVIRONMENT` 设置](../../concepts/projects/config.md#_9) 可用于安装到系统 Python 环境，而不是创建虚拟环境。

## 缓存

在工作流运行之间存储 uv 的缓存可能会缩短 CI 时间。

[`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) 内置了对持久化缓存的支持：

```yaml title="example.yml"
- name: Enable caching
  uses: astral-sh/setup-uv@v5
  with:
    enable-cache: true
```

您可以配置 action 以在运行器上使用自定义缓存目录：

```yaml title="example.yml"
- name: Define a custom uv cache path
  uses: astral-sh/setup-uv@v5
  with:
    enable-cache: true
    cache-local-path: "/path/to/cache"
```

或在锁文件更改时使其失效：

```yaml title="example.yml"
- name: Define a cache dependency glob
  uses: astral-sh/setup-uv@v5
  with:
    enable-cache: true
    cache-dependency-glob: "uv.lock"
```

或在任何需求文件更改时：

```yaml title="example.yml"
- name: Define a cache dependency glob
  uses: astral-sh/setup-uv@v5
  with:
    enable-cache: true
    cache-dependency-glob: "requirements**.txt"
```

请注意，`astral-sh/setup-uv` 将自动为每个主机架构和平台使用单独的缓存键。

或者，您可以使用 `actions/cache` action 手动管理缓存：

```yaml title="example.yml"
jobs:
  install_job:
    env:
      # Configure a constant location for the uv cache
      UV_CACHE_DIR: /tmp/.uv-cache

    steps:
      # ... setup up Python and uv ...

      - name: Restore uv cache
        uses: actions/cache@v4
        with:
          path: /tmp/.uv-cache
          key: uv-${{ runner.os }}-${{ hashFiles('uv.lock') }}
          restore-keys: |
            uv-${{ runner.os }}-${{ hashFiles('uv.lock') }}
            uv-${{ runner.os }}

      # ... install packages, run tests, etc ...

      - name: Minimize uv cache
        run: uv cache prune --ci
```

`uv cache prune --ci` 命令用于减小缓存大小，并针对 CI 进行了优化。其对性能的影响取决于正在安装的软件包。

!!! tip

    如果使用 `uv pip`，请在缓存键中使用 `requirements.txt` 而不是 `uv.lock`。

!!! note

    [post-job-hook]: https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/running-scripts-before-or-after-a-job

    当使用非临时、自托管的运行器时，默认缓存目录可能会无限增长。在这种情况下，在作业之间共享缓存可能不是最佳选择。相反，应将缓存移动到 GitHub 工作区内，并在作业完成时使用[作业后挂钩][post-job-hook]将其删除。

    ```yaml
    install_job:
      env:
        # Configure a relative location for the uv cache
        UV_CACHE_DIR: ${{ github.workspace }}/.cache/uv
    ```

    使用作业后挂钩需要在自托管运行器上将 `ACTIONS_RUNNER_HOOK_JOB_STARTED` 环境变量设置为清理脚本的路径，如下所示。

    ```sh title="clean-uv-cache.sh"
    #!/usr/bin/env sh
    uv cache clean
    ```

## 使用 `uv pip`

如果使用 `uv pip` 接口而不是 uv 项目接口，uv 默认需要一个虚拟环境。要允许将软件包安装到系统环境中，请在所有 `uv` 调用中使用 `--system` 标志或设置 `UV_SYSTEM_PYTHON` 变量。

`UV_SYSTEM_PYTHON` 变量可以在不同的作用域中定义。

通过在顶层定义它来为整个工作流选择加入：

```yaml title="example.yml"
env:
  UV_SYSTEM_PYTHON: 1

jobs: ...
```

或者，为工作流中的特定作业选择加入：

```yaml title="example.yml"
jobs:
  install_job:
    env:
      UV_SYSTEM_PYTHON: 1
    ...
```

或者，为作业中的特定步骤选择加入：

```yaml title="example.yml"
steps:
  - name: Install requirements
    run: uv pip install -r requirements.txt
    env:
      UV_SYSTEM_PYTHON: 1
```

要再次选择退出，可以在任何 uv 调用中使用 `--no-system` 标志。

## 私有仓库

如果您的项目对私有 GitHub 仓库有[依赖项](../../concepts/projects/dependencies.md#git)，您将需要配置一个[个人访问令牌 (PAT)][PAT] 以允许 uv 获取它们。

在创建具有对私有仓库的读取访问权限的 PAT 后，将其添加为[仓库机密]。

然后，您可以使用 [`gh`](https://cli.github.com/) CLI（默认安装在 GitHub Actions 运行器中）为 Git 配置一个[凭据帮助程序](../../concepts/authentication.md#git_1)，以使用 PAT 查询托管在 `github.com` 上的仓库。

例如，如果您将仓库机密命名为 `MY_PAT`：

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
