---
title: 结合 uv 使用 PyTorch
description:
  一份结合 uv 使用 PyTorch 的指南，内容包括安装 PyTorch、配置跨平台和跨加速器的构建等。
---

# 结合 uv 使用 PyTorch

[PyTorch](https://pytorch.org/) 生态系统是深度学习研究和开发的热门选择。你可以使用 uv 来管理 PyTorch 项目和 PyTorch 在不同 Python 版本和环境中的依赖，甚至可以控制加速器的选择（例如，仅 CPU vs. CUDA）。

!!! note

    本指南中概述的某些功能需要 uv 0.5.3 或更高版本。我们建议在配置 PyTorch 之前进行升级。

## 安装 PyTorch

从打包的角度来看，PyTorch 有一些不寻常的特点：

- 许多 PyTorch wheel 托管在一个专用的索引上，而不是 Python 包索引（PyPI）。因此，安装 PyTorch 通常需要配置项目以使用 PyTorch 索引。
- PyTorch 为每个加速器（例如，仅 CPU、CUDA）生成不同的构建。由于在发布或安装时没有指定这些加速器的标准化机制，PyTorch 将它们编码在本地版本说明符中。因此，PyTorch 版本通常看起来像 `2.5.1+cpu`、`2.5.1+cu121` 等。
- 不同加速器的构建发布到不同的索引。例如，`+cpu` 构建发布在 https://download.pytorch.org/whl/cpu，而 `+cu121` 构建发布在 https://download.pytorch.org/whl/cu121。

因此，所需的打包配置将根据你需要支持的平台和要启用的加速器而有所不同。

首先，考虑以下（默认）配置，该配置将通过运行 `uv init --python 3.12` 然后运行 `uv add torch torchvision` 生成。

在这种情况下，PyTorch 将从 PyPI 安装，PyPI 托管了适用于 Windows 和 macOS 的仅 CPU 的 wheel，以及适用于 Linux 的 GPU 加速 wheel（目标为 CUDA 12.6）：

```toml
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "torch>=2.7.0",
  "torchvision>=0.22.0",
]
```

!!! tip "支持的 Python 版本"

    在撰写本文时，PyTorch 尚未发布适用于 Python 3.14 的 wheel；因此，`requires-python = ">=3.14"` 的项目可能会解析失败。请参阅[兼容性矩阵](https://github.com/pytorch/pytorch/blob/main/RELEASE.md#release-compatibility-matrix)。

对于希望在 Windows 和 macOS 上使用 CPU 构建，在 Linux 上使用启用 CUDA 的构建的项目来说，这是一个有效的配置。但是，如果你需要支持不同的平台或加速器，则需要相应地配置项目。

## 使用 PyTorch 索引

在某些情况下，你可能希望在所有平台上使用特定的 PyTorch 变体。例如，你可能也想在 Linux 上使用仅 CPU 的构建。

在这种情况下，第一步是将相关的 PyTorch 索引添加到你的 `pyproject.toml` 中：

=== "CPU-only"

    ```toml
    [[tool.uv.index]]
    name = "pytorch-cpu"
    url = "https://download.pytorch.org/whl/cpu"
    explicit = true
    ```

=== "CUDA 11.8"

    ```toml
    [[tool.uv.index]]
    name = "pytorch-cu118"
    url = "https://download.pytorch.org/whl/cu118"
    explicit = true
    ```

=== "CUDA 12.6"

    ```toml
    [[tool.uv.index]]
    name = "pytorch-cu126"
    url = "https://download.pytorch.org/whl/cu126"
    explicit = true
    ```

=== "CUDA 12.8"

    ```toml
    [[tool.uv.index]]
    name = "pytorch-cu128"
    url = "https://download.pytorch.org/whl/cu128"
    explicit = true
    ```

=== "ROCm6"

    ```toml
    [[tool.uv.index]]
    name = "pytorch-rocm"
    url = "https://download.pytorch.org/whl/rocm6.3"
    explicit = true
    ```

=== "Intel GPUs"

    ```toml
    [[tool.uv.index]]
    name = "pytorch-xpu"
    url = "https://download.pytorch.org/whl/xpu"
    explicit = true
    ```

我们建议使用 `explicit = true` 来确保该索引*仅*用于 `torch`、`torchvision` 和其他与 PyTorch 相关的包，而不是像 `jinja2` 这样的通用依赖项，后者应继续从默认索引（PyPI）获取。

接下来，更新 `pyproject.toml` 以将 `torch` 和 `torchvision` 指向所需的索引：

=== "CPU-only"

    ```toml
    [tool.uv.sources]
    torch = [
      { index = "pytorch-cpu" },
    ]
    torchvision = [
      { index = "pytorch-cpu" },
    ]
    ```

=== "CUDA 11.8"

    PyTorch 不会为 macOS 发布 CUDA 构建。因此，我们使用 `sys_platform` 来指示 uv 在 Linux 和 Windows 上使用 PyTorch 索引，但在 macOS 上回退到 PyPI：

    ```toml
    [tool.uv.sources]
    torch = [
      { index = "pytorch-cu118", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    torchvision = [
      { index = "pytorch-cu118", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    ```

=== "CUDA 12.6"

    PyTorch 不会为 macOS 发布 CUDA 构建。因此，我们使用 `sys_platform` 来指示 uv 将 PyTorch 索引限制在 Linux 和 Windows 上，在 macOS 上回退到 PyPI：

    ```toml
    [tool.uv.sources]
    torch = [
      { index = "pytorch-cu126", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    torchvision = [
      { index = "pytorch-cu126", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    ```

=== "CUDA 12.8"

    PyTorch 不会为 macOS 发布 CUDA 构建。因此，我们使用 `sys_platform` 来指示 uv 将 PyTorch 索引限制在 Linux 和 Windows 上，在 macOS 上回退到 PyPI：

    ```toml
    [tool.uv.sources]
    torch = [
      { index = "pytorch-cu128", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    torchvision = [
      { index = "pytorch-cu128", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    ```

=== "ROCm6"

    PyTorch 不会为 macOS 或 Windows 发布 ROCm6 构建。因此，我们使用 `sys_platform` 来指示 uv 将 PyTorch 索引限制在 Linux 上，在 macOS 和 Windows 上回退到 PyPI：

    ```toml
    [tool.uv.sources]
    torch = [
      { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },
    ]
    torchvision = [
      { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },
    ]
    # ROCm6 支持依赖于 `pytorch-triton-rocm`，它也应该从 PyTorch 索引安装
    #（并包含在 `project.dependencies` 中）。
    pytorch-triton-rocm = [
      { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },
    ]
    ```

=== "Intel GPUs"

    PyTorch 不会为 macOS 发布 Intel GPU 构建。因此，我们使用 `sys_platform` 来指示 uv 将 PyTorch 索引限制在 Linux 和 Windows 上，在 macOS 上回退到 PyPI：

    ```toml
    [tool.uv.sources]
    torch = [
      { index = "pytorch-xpu", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    torchvision = [
      { index = "pytorch-xpu", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    # Intel GPU 支持依赖于 `pytorch-triton-xpu`，它也应该从 PyTorch 索引安装
    #（并包含在 `project.dependencies` 中）。
    pytorch-triton-xpu = [
      { index = "pytorch-xpu", marker = "sys_platform == 'linux' or sys_platform == 'win32'" },
    ]
    ```

作为一个完整的示例，以下项目将在所有平台上使用 PyTorch 的仅 CPU 构建：

```toml
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.12.0"
dependencies = [
  "torch>=2.7.0",
  "torchvision>=0.22.0",
]

[tool.uv.sources]
torch = [
    { index = "pytorch-cpu" },
]
torchvision = [
    { index = "pytorch-cpu" },
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

## 使用环境标记配置加速器

在某些情况下，你可能希望在一个环境（例如，macOS 和 Windows）中使用仅 CPU 的构建，而在另一个环境（例如，Linux）中使用启用 CUDA 的构建。

使用 `tool.uv.sources`，你可以使用环境标记为每个平台指定所需的索引。例如，以下配置将在 Linux 上使用 PyTorch 的启用 CUDA 的构建，并在所有其他平台（例如，macOS 和 Windows）上使用仅 CPU 的构建：

```toml
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.12.0"
dependencies = [
  "torch>=2.7.0",
  "torchvision>=0.22.0",
]

[tool.uv.sources]
torch = [
  { index = "pytorch-cpu", marker = "sys_platform != 'linux'" },
  { index = "pytorch-cu128", marker = "sys_platform == 'linux'" },
]
torchvision = [
  { index = "pytorch-cpu", marker = "sys_platform != 'linux'" },
  { index = "pytorch-cu128", marker = "sys_platform == 'linux'" },
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[[tool.uv.index]]
name = "pytorch-cu128"
url = "https://download.pytorch.org/whl/cu128"
explicit = true
```

同样，以下配置将在 Linux 上使用 PyTorch 的 AMD GPU 构建，并在 Windows 和 macOS 上使用仅 CPU 的构建（通过回退到 PyPI）：

```toml
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.12.0"
dependencies = [
  "torch>=2.7.0",
  "torchvision>=0.22.0",
  "pytorch-triton-rocm>=3.3.0 ; sys_platform == 'linux'",
]

[tool.uv.sources]
torch = [
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },
]
torchvision = [
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },
]
pytorch-triton-rocm = [
  { index = "pytorch-rocm", marker = "sys_platform == 'linux'" },
]

[[tool.uv.index]]
name = "pytorch-rocm"
url = "https://download.pytorch.org/whl/rocm6.3"
explicit = true
```

或者，对于 Intel GPU 构建：

```toml
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.12.0"
dependencies = [
  "torch>=2.7.0",
  "torchvision>=0.22.0",
  "pytorch-triton-xpu>=3.3.0 ; sys_platform == 'win32' or sys_platform == 'linux'",
]

[tool.uv.sources]
torch = [
  { index = "pytorch-xpu", marker = "sys_platform == 'win32' or sys_platform == 'linux'" },
]
torchvision = [
  { index = "pytorch-xpu", marker = "sys_platform == 'win32' or sys_platform == 'linux'" },
]
pytorch-triton-xpu = [
  { index = "pytorch-xpu", marker = "sys_platform == 'win32' or sys_platform == 'linux'" },
]

[[tool.uv.index]]
name = "pytorch-xpu"
url = "https://download.pytorch.org/whl/xpu"
explicit = true
```

## 使用可选依赖项配置加速器

在某些情况下，你可能希望在某些情况下使用仅 CPU 的构建，而在其他情况下使用启用 CUDA 的构建，并通过用户提供的 extra（例如，`uv sync --extra cpu` vs. `uv sync --extra cu128`）来切换选择。

使用 `tool.uv.sources`，你可以使用 extra 标记为每个启用的 extra 指定所需的索引。例如，以下配置将为 `uv sync --extra cpu` 使用 PyTorch 的仅 CPU 构建，为 `uv sync --extra cu128` 使用启用 CUDA 的构建：

```toml
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.12.0"
dependencies = []

[project.optional-dependencies]
cpu = [
  "torch>=2.7.0",
  "torchvision>=0.22.0",
]
cu128 = [
  "torch>=2.7.0",
  "torchvision>=0.22.0",
]

[tool.uv]
conflicts = [
  [
    { extra = "cpu" },
    { extra = "cu128" },
  ],
]

[tool.uv.sources]
torch = [
  { index = "pytorch-cpu", extra = "cpu" },
  { index = "pytorch-cu128", extra = "cu128" },
]
torchvision = [
  { index = "pytorch-cpu", extra = "cpu" },
  { index = "pytorch-cu128", extra = "cu128" },
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[[tool.uv.index]]
name = "pytorch-cu128"
url = "https://download.pytorch.org/whl/cu128"
explicit = true
```

!!! note

    由于在 macOS 上没有 GPU 加速的构建，因此在启用 `cu128` extra 时，上述配置将无法在 macOS 上安装。

## `uv pip` 接口

虽然以上示例主要关注 uv 的项目接口（`uv lock`、`uv sync`、`uv run` 等），但也可以通过 `uv pip` 接口安装 PyTorch。

PyTorch 本身提供了一个[专用接口](https://pytorch.org/get-started/locally/)来确定针对给定目标配置运行的适当 pip 命令。例如，你可以在 Linux 上安装稳定的、仅 CPU 的 PyTorch：

```shell
$ pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

要将相同的工作流程与 uv 一起使用，请将 `pip3` 替换为 `uv pip`：

```shell
$ uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

## 自动后端选择

uv 支持通过 `--torch-backend=auto` 命令行参数（或 `UV_TORCH_BACKEND=auto` 环境变量）自动选择适当的 PyTorch 索引，如下所示：

```shell
$ # 使用命令行参数。
$ uv pip install torch --torch-backend=auto

$ # 使用环境变量。
$ UV_TORCH_BACKEND=auto uv pip install torch
```

启用后，uv 将查询已安装的 CUDA 驱动程序和 AMD GPU 版本，然后为所有相关包（例如，`torch`、`torchvision` 等）使用最兼容的 PyTorch 索引。如果未找到此类 GPU，uv 将回退到仅 CPU 的索引。uv 将继续遵守 PyTorch 生态系统之外的任何包的现有索引配置。

你还可以使用 `--torch-backend=cu126`（或 `UV_TORCH_BACKEND=cu126`）选择特定的后端（例如，CUDA 12.6）：

```shell
$ # 使用命令行参数。
$ uv pip install torch torchvision --torch-backend=cu126

$ # 使用环境变量。
$ UV_TORCH_BACKEND=cu126 uv pip install torch torchvision
```

目前，`--torch-backend` 仅在 `uv pip` 接口中可用。
