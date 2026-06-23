---
subtitle: Build failures
description: 本文档详细介绍 uv 包管理器中构建失败（build failures）的常见原因与故障排查方法，涵盖如何识别构建失败、确认是否与 uv 特定相关、uv 何时需要构建包，以及命令未找到、头文件/库缺失、模块无法导入、旧版本包构建、构建依赖版本不兼容等常见问题的解决方案，帮助开发者快速定位和修复 Python 包构建过程中的各类错误。
---

# 构建失败故障排查 {#troubleshooting-build-failures}

当没有兼容的 wheel（包的预构建分发版）可用时，uv 需要构建包。构建包可能因多种原因失败，其中一些可能与 uv 本身无关。

## 识别构建失败 {#recognizing-a-build-failure}

以下示例展示了在不受支持的 Python 新版本上尝试安装旧版本 numpy 时产生的构建失败：

```console
$ uv pip install -p 3.13 'numpy<1.20'
Resolved 1 package in 62ms
  × Failed to build `numpy==1.19.5`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel()` failed (exit status: 1)

      [stderr]
      Traceback (most recent call last):
        File "<string>", line 8, in <module>
          from setuptools.build_meta import __legacy__ as backend
        File "/home/konsti/.cache/uv/builds-v0/.tmpi4bgKb/lib/python3.13/site-packages/setuptools/__init__.py", line 9, in <module>
          import distutils.core
      ModuleNotFoundError: No module named 'distutils'

      hint: `distutils` was removed from the standard library in Python 3.12. Consider adding a constraint (like `numpy >1.19.5`) to avoid building a version of `numpy` that depends
      on `distutils`.
```

请注意，错误消息以 "The build backend returned an error" 为前缀。

构建失败信息包含来自构建后端的 `[stderr]`（以及 `[stdout]`，如果存在）。错误日志并非来自 uv 本身。

`╰─▶` 后面的消息是 uv 提供的提示，用于帮助解决常见的构建失败。并非所有构建失败都会提供提示。

## 确认构建失败是否特定于 uv {#confirming-that-a-build-failure-is-specific-to-uv}

构建失败通常与你的系统和构建后端有关。构建失败特定于 uv 的情况很少见。你可以通过尝试使用 pip 复现来确认构建失败是否与 uv 无关：

```console
$ uv venv -p 3.13 --seed
$ source .venv/bin/activate
$ pip install --use-pep517 --no-cache --force-reinstall 'numpy==1.19.5'
Collecting numpy==1.19.5
  Using cached numpy-1.19.5.zip (7.3 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
ERROR: Exception:
Traceback (most recent call last):
  ...
  File "/Users/example/.cache/uv/archive-v0/3783IbOdglemN3ieOULx2/lib/python3.13/site-packages/pip/_vendor/pyproject_hooks/_impl.py", line 321, in _call_hook
    raise BackendUnavailable(data.get('traceback', ''))
pip._vendor.pyproject_hooks._impl.BackendUnavailable: Traceback (most recent call last):
  File "/Users/example/.cache/uv/archive-v0/3783IbOdglemN3ieOULx2/lib/python3.13/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 77, in _build_backend
    obj = import_module(mod_path)
  File "/Users/example/.local/share/uv/python/cpython-3.13.0-macos-aarch64-none/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1310, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1022, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/private/var/folders/6p/k5sd5z7j31b31pq4lhn0l8d80000gn/T/pip-build-env-vdpjme7d/overlay/lib/python3.13/site-packages/setuptools/__init__.py", line 9, in <module>
    import distutils.core
ModuleNotFoundError: No module named 'distutils'
```

!!! important

    `pip install` 调用中应包含 `--use-pep517` 标志，以确保相同的构建隔离行为。uv 默认始终使用[构建隔离](../../pip/compatibility.md#pep-517-build-isolation)。

    我们还建议在复现失败时包含 `--force-reinstall` 和 `--no-cache` 选项。

由于此构建失败在 pip 中也会出现，因此不太可能是 uv 的错误。

如果构建失败可以用其他安装器复现，你应该调查上游（在本例中为 `numpy` 或 `setuptools`），找到避免构建该包的方法，或对系统进行必要的调整以使构建成功。

## uv 为什么需要构建包？ {#why-does-uv-build-a-package}

在生成跨平台锁文件时，uv 需要确定所有包的依赖关系，即使是那些仅在其他平台上安装的包。uv 尝试在解析过程中避免构建包。它会使用该版本的任何可用 wheel，然后尝试在源码分发版中查找静态元数据（主要是包含静态 `project.version`、`project.dependencies` 和 `project.optional-dependencies` 的 pyproject.toml 或 METADATA v2.2+）。只有在所有这些都失败时，它才会构建包。

在安装时，uv 需要为每个包获取当前平台的 wheel。如果索引中没有匹配的 wheel，uv 会尝试构建源码分发版。

你可以在 PyPI 项目的 "Download Files" 下查看存在哪些 wheel，例如 <https://pypi.org/project/numpy/2.1.1.md#files>。文件名为 `...-py3-none-any.whl` 的 wheel 适用于所有平台，其他 wheel 的文件名中包含操作系统和平台信息。在链接的 `numpy` 示例中，你可以看到有针对 Python 3.10 到 3.13 的 macOS、Linux 和 Windows 预构建分发版。

## 常见构建失败 {#common-build-failures}

以下示例展示了常见的构建失败及其解决方法。

### 命令未找到 {#command-is-not-found}

如果构建错误提示缺少某个命令，例如 `gcc`：

<!-- docker run --platform linux/x86_64 -it ghcr.io/astral-sh/uv:python3.10-trixie-slim /bin/bash -c "uv pip install --system pysha3==1.0.2" -->

```hl_lines="17"
× Failed to build `pysha3==1.0.2`
├─▶ The build backend returned an error
╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)

    [stdout]
    running bdist_wheel
    running build
    running build_py
    creating build/lib.linux-x86_64-cpython-310
    copying sha3.py -> build/lib.linux-x86_64-cpython-310
    running build_ext
    building '_pysha3' extension
    creating build/temp.linux-x86_64-cpython-310/Modules/_sha3
    gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DPY_WITH_KECCAK=1 -I/root/.cache/uv/builds-v0/.tmp8V4iEk/include -I/usr/local/include/python3.10 -c
    Modules/_sha3/sha3module.c -o build/temp.linux-x86_64-cpython-310/Modules/_sha3/sha3module.o

    [stderr]
    error: command 'gcc' failed: No such file or directory
```

那么你需要使用系统包管理器安装它，例如，要解决上述错误：

```console
$ apt install gcc
```

!!! tip

    使用 uv 管理的 Python 版本时，通常需要安装 `clang` 而不是 `gcc`。

    许多 Linux 发行版提供了一个包含所有常见构建依赖的包。你可以通过安装它来解决大多数构建需求，例如，对于 Debian 或 Ubuntu：

    ```console
    $ apt install build-essential
    ```

### 头文件或库缺失 {#header-or-library-is-missing}

如果构建错误提示缺少头文件或库，例如 `.h` 文件，那么你需要使用系统包管理器安装它。

例如，安装 `pygraphviz` 需要先安装 Graphviz：

<!-- docker run --platform linux/x86_64 -it ghcr.io/astral-sh/uv:python3.12-trixie /bin/bash -c "uv pip install --system 'pygraphviz'" -->

```hl_lines="18-19"
× Failed to build `pygraphviz==1.14`
├─▶ The build backend returned an error
╰─▶ Call to `setuptools.build_meta.build_wheel` failed (exit status: 1)

  [stdout]
  running bdist_wheel
  running build
  running build_py
  ...
  gcc -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O3 -Wall -fPIC -DSWIG_PYTHON_STRICT_BYTE_CHAR -I/root/.cache/uv/builds-v0/.tmpgLYPe0/include -I/usr/local/include/python3.12 -c pygraphviz/graphviz_wrap.c -o
  build/temp.linux-x86_64-cpython-312/pygraphviz/graphviz_wrap.o

  [stderr]
  ...
  pygraphviz/graphviz_wrap.c:9: warning: "SWIG_PYTHON_STRICT_BYTE_CHAR" redefined
      9 | #define SWIG_PYTHON_STRICT_BYTE_CHAR
        |
  <command-line>: note: this is the location of the previous definition
  pygraphviz/graphviz_wrap.c:3023:10: fatal error: graphviz/cgraph.h: No such file or directory
    3023 | #include "graphviz/cgraph.h"
        |          ^~~~~~~~~~~~~~~~~~~
  compilation terminated.
  error: command '/usr/bin/gcc' failed with exit code 1

  hint: This error likely indicates that you need to install a library that provides "graphviz/cgraph.h" for `pygraphviz@1.14`
```

要在 Debian 上解决此错误，你需要安装 `libgraphviz-dev` 包：

```console
$ apt install libgraphviz-dev
```

请注意，仅安装 `graphviz` 包是不够的，还需要安装开发头文件。

!!! tip

    要解决缺少 `Python.h` 的错误，请安装 [`python3-dev` 包](https://packages.debian.org/trixie/python3-dev)。

### 模块缺失或无法导入 {#module-is-missing-or-cannot-be-imported}

如果构建错误提示导入失败，请考虑[禁用构建隔离](../../concepts/projects/config.md#build-isolation)。

例如，某些包假定 `pip` 可用，但未将其声明为构建依赖：

<!-- docker run --platform linux/x86_64 -it ghcr.io/astral-sh/uv:python3.12-trixie-slim /bin/bash -c "uv pip install --system chumpy" -->

```hl_lines="7"
  × Failed to build `chumpy==0.70`
  ├─▶ The build backend returned an error
  ╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)

    [stderr]
    Traceback (most recent call last):
      File "<string>", line 9, in <module>
    ModuleNotFoundError: No module named 'pip'

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "<string>", line 14, in <module>
      File "/root/.cache/uv/builds-v0/.tmpvvHaxI/lib/python3.12/site-packages/setuptools/build_meta.py", line 334, in get_requires_for_build_wheel
        return self._get_build_requires(config_settings, requirements=[])
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/root/.cache/uv/builds-v0/.tmpvvHaxI/lib/python3.12/site-packages/setuptools/build_meta.py", line 304, in _get_build_requires
        self.run_setup()
      File "/root/.cache/uv/builds-v0/.tmpvvHaxI/lib/python3.12/site-packages/setuptools/build_meta.py", line 522, in run_setup
        super().run_setup(setup_script=setup_script)
      File "/root/.cache/uv/builds-v0/.tmpvvHaxI/lib/python3.12/site-packages/setuptools/build_meta.py", line 320, in run_setup
        exec(code, locals())
      File "<string>", line 11, in <module>
    ModuleNotFoundError: No module named 'pip'
```

要解决此错误，请预安装构建依赖，然后为该包禁用构建隔离：

```console
$ uv pip install pip setuptools
$ uv pip install chumpy --no-build-isolation-package chumpy
```

请注意，你需要安装缺失的包（例如 `pip`）_以及_该包的所有其他构建依赖（例如 `setuptools`）。

### 构建了旧版本的包 {#old-version-of-the-package-is-built}

如果包在解析期间构建失败，且构建失败的版本比你想要使用的版本更旧，请尝试添加带有下限的[约束](../settings/project-metadata.md#constraint-dependencies)（例如 `numpy>=1.17`）。有时，由于算法限制，uv 解析器会尝试使用不合理的旧版本来查找合适的版本，这可以通过使用下限来避免。

例如，在 Python 3.10 上解析以下依赖时，uv 会尝试构建旧版本的 `apache-beam`。

```title="requirements.txt"
dill<0.3.9,>=0.2.2
apache-beam<=2.49.0
```

<!-- docker run --platform linux/x86_64 -it ghcr.io/astral-sh/uv:python3.10-trixie-slim /bin/bash -c "printf 'dill<0.3.9,>=0.2.2\napache-beam<=2.49.0' | uv pip compile -" -->

```hl_lines="1"
× Failed to build `apache-beam==2.0.0`
├─▶ The build backend returned an error
╰─▶ Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit status: 1)

    [stderr]
    ...
```

添加下限约束，例如 `apache-beam<=2.49.0,>2.30.0`，可以解决此构建失败，因为 uv 将避免使用旧版本的 `apache-beam`。

也可以使用 `constraints.txt` 文件或 [`constraint-dependencies`](../settings/project-metadata.md#constraint-dependencies) 设置为间接依赖定义约束。

### 使用了旧版本的构建依赖 {#old-version-of-a-build-dependency-is-used}

如果包因 `uv` 选择了不兼容或过时的构建时依赖版本而构建失败，你可以专门为构建依赖强制设置约束。[`build-constraint-dependencies`](../settings/project-metadata.md#build-constraint-dependencies) 设置（或类似的 `build-constraints.txt` 文件）可用于确保 `uv` 选择合适版本的构建依赖。

例如，[#5551](https://github.com/astral-sh/uv/issues/5551#issuecomment-2256055975) 中描述的问题可以通过指定排除 `setuptools` 版本 `72.0.0` 的构建约束来解决：

```toml title="pyproject.toml"
[tool.uv]
# Prevent setuptools version 72.0.0 from being used as a build dependency.
build-constraint-dependencies = ["setuptools!=72.0.0"]
```

因此，构建约束将确保任何在构建过程中需要 `setuptools` 的包都会避免使用有问题的版本，从而防止由不兼容的构建依赖引起的构建失败。

### 包仅在未使用的平台上需要 {#package-is-only-needed-for-an-unused-platform}

如果锁定因构建来自你不需要支持的平台的包而失败，请考虑[将解析限制](../../concepts/projects/config.md#limited-resolution-environments)在你支持的平台上。

### 包不支持所有 Python 版本 {#package-does-not-support-all-python-versions}

如果你支持大范围的 Python 版本，请考虑使用标记（markers）为旧版 Python 使用旧版本包，为新版 Python 使用新版本包。例如，`numpy` 一次仅支持四个 Python 次要版本，因此要支持更广泛的 Python 版本范围（例如 Python 3.8 到 3.13），需要拆分 `numpy` 的依赖要求：

```
numpy>=1.23; python_version >= "3.10"
numpy<1.23; python_version < "3.10"
```

### 包仅在特定平台上可用 {#package-is-only-usable-on-a-specific-platform}

如果锁定因构建仅在另一个平台上可用的包而失败，你可以[手动提供依赖元数据](../settings/project-metadata.md)以跳过构建。uv 无法验证此信息，因此在使用此覆盖时指定正确的元数据非常重要。
