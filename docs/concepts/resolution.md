---
subtitle: Resolution
description: 学习 uv 的解析过程，包括依赖解析和版本解析。了解 uv 如何处理项目的依赖关系，以及如何确保请求的需求得到满足。完整指南帮助您理解 uv 的解析机制。
---

# 解析（Resolution） {#resolution}

解析是将一组需求（requirements）转换为满足这些需求的包版本列表的过程。解析需要递归地搜索包的兼容版本，确保请求的需求得到满足，并且所请求包的需求之间相互兼容。

## 依赖（Dependencies） {#dependencies}

大多数项目和包都有依赖。依赖是当前包正常运行所必需的其他包。包将其依赖定义为 _需求（requirements）_，大致是包名和可接受版本的组合。当前项目定义的依赖称为 _直接依赖（direct dependencies）_。当前项目的每个依赖所添加的依赖称为 _间接依赖（indirect dependencies）_ 或 _传递依赖（transitive dependencies）_。

!!! note

    有关依赖的详细信息，请参阅 Python Packaging 文档中的[依赖说明符页面](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)。

## 基本示例 {#basic-examples}

为了帮助演示解析过程，请考虑以下依赖关系：

<!-- prettier-ignore -->
- 项目依赖 `foo` 和 `bar`。
- `foo` 有一个版本 1.0.0：
    - `foo 1.0.0` 依赖 `lib>=1.0.0`。
- `bar` 有一个版本 1.0.0：
    - `bar 1.0.0` 依赖 `lib>=2.0.0`。
- `lib` 有两个版本，1.0.0 和 2.0.0。两个版本都没有依赖。

在这个示例中，解析器必须找到一组满足项目需求的包版本。由于 `foo` 和 `bar` 都只有一个版本，因此将使用这些版本。解析还必须包含传递依赖，因此必须选择一个 `lib` 的版本。`foo 1.0.0` 允许所有可用的 `lib` 版本，但 `bar 1.0.0` 要求 `lib>=2.0.0`，因此必须使用 `lib 2.0.0`。

在某些解析中，可能存在多个有效解。请考虑以下依赖关系：

<!-- prettier-ignore -->
- 项目依赖 `foo` 和 `bar`。
- `foo` 有两个版本，1.0.0 和 2.0.0：
    - `foo 1.0.0` 没有依赖。
    - `foo 2.0.0` 依赖 `lib==2.0.0`。
- `bar` 有两个版本，1.0.0 和 2.0.0：
    - `bar 1.0.0` 没有依赖。
    - `bar 2.0.0` 依赖 `lib==1.0.0`
- `lib` 有两个版本，1.0.0 和 2.0.0。两个版本都没有依赖。

在这个示例中，必须选择 `foo` 和 `bar` 的某个版本；然而，确定选择哪个版本需要考虑 `foo` 和 `bar` 每个版本的依赖关系。`foo 2.0.0` 和 `bar 2.0.0` 无法一起安装，因为它们对 `lib` 的版本要求存在冲突，因此解析器必须选择 `foo 1.0.0`（搭配 `bar 2.0.0`）或 `bar 1.0.0`（搭配 `foo 2.0.0`）。两者都是有效解，不同的解析算法可能会产生不同的结果。

## 平台标记（Platform Markers） {#platform-markers}

标记（markers）允许为需求附加一个表达式，用于指示该依赖应在何时使用。例如，`bar ; python_version < "3.9"` 表示 `bar` 仅应在 Python 3.8 及更早版本上安装。

标记用于根据当前环境或平台调整包的依赖关系。例如，标记可用于按操作系统、CPU 架构、Python 版本、Python 实现等修改依赖关系。

!!! note

    有关标记的更多详细信息，请参阅 Python Packaging 文档中的[环境标记](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers)部分。

标记对解析很重要，因为它们的值会改变所需的依赖关系。通常，Python 包解析器使用 _当前_ 平台的标记来确定要使用哪些依赖，因为包通常是在当前平台上 _安装_ 的。然而，对于 _锁定（locking）_ 依赖来说，这会带来问题——锁文件只能在与创建锁文件相同平台的开发者那里工作。为了解决这个问题，出现了平台无关的或"通用（universal）"解析器。

uv 同时支持[平台特定解析](#platform-specific-resolution)和[通用解析](#universal-resolution)。

## 平台特定解析（Platform-specific Resolution） {#platform-specific-resolution}

默认情况下，uv 的 pip 接口，即 [`uv pip compile`](../pip/compile.md)，会生成平台特定的解析结果，与 `pip-tools` 类似。在 uv 的项目接口中无法使用平台特定解析。

uv 还支持通过 `--python-platform` 和 `--python-version` 选项为特定的、替代的平台和 Python 版本进行解析。例如，如果在 macOS 上使用 Python 3.12，可以使用 `uv pip compile --python-platform linux --python-version 3.10 requirements.in` 来为 Linux 上的 Python 3.10 生成解析结果。与通用解析不同，在平台特定解析期间，提供的 `--python-version` 是要使用的确切 Python 版本，而不是下限。

!!! note

    Python 的环境标记暴露了关于当前机器的远比简单的 `--python-platform` 参数所能表达的更多信息。例如，macOS 上的 `platform_version` 标记包含内核构建的时间，这（理论上）可以被编码在包需求中。uv 的解析器会尽力生成与目标 `--python-platform` 上运行的任何机器兼容的解析结果，这对于大多数用例来说应该足够了，但对于复杂的包和平台组合可能会丢失一些精度。

## 通用解析（Universal Resolution） {#universal-resolution}

uv 的锁文件（`uv.lock`）是通过通用解析创建的，可跨平台移植。这确保了无论操作系统、架构和 Python 版本如何，依赖关系都被锁定给项目中的所有协作者。uv 锁文件由[项目](../concepts/projects/index.md)命令（如 `uv lock`、`uv sync` 和 `uv add`）创建和修改。

通用解析也可在 uv 的 pip 接口中使用，即 [`uv pip compile`](../pip/compile.md)，通过 `--universal` 标志启用。生成的 requirements 文件将包含标记，以指示每个依赖适用于哪个平台。

在通用解析期间，如果不同平台需要不同版本，一个包可能会以不同版本或 URL 多次列出——标记决定将使用哪个版本。通用解析通常比平台特定解析受到更多约束，因为我们需要考虑所有标记的需求。

在通用解析期间，所有必需的包必须与 `pyproject.toml` 中声明的 `requires-python` 的 _整个_ 范围兼容。例如，如果项目的 `requires-python` 是 `>=3.8`，而某个依赖的所有版本都要求 Python 3.9 或更高版本，则解析将失败，因为该依赖缺少适用于（例如）Python 3.8（项目支持范围的下限）的可用版本。换句话说，项目的 `requires-python` 必须是其所有依赖的 `requires-python` 的子集。

为给定依赖选择兼容版本时，uv 将（[默认情况下](#multi-version-resolution)）尝试为每个受支持的 Python 版本选择最新的兼容版本。例如，如果项目的 `requires-python` 是 `>=3.8`，而某个依赖的最新版本要求 Python 3.9 或更高版本，而所有先前版本都支持 Python 3.8，则解析器将为运行 Python 3.9 或更高版本的用户选择最新版本，为运行 Python 3.8 的用户选择先前版本。

在评估依赖的 `requires-python` 范围时，uv 仅考虑下限，完全忽略上限。例如，`>=3.8, <4` 被视为 `>=3.8`。遵循 `requires-python` 的上限通常会导致形式上正确但实际不正确的解析，因为解析器会回溯到第一个省略上限的已发布版本（参见：[`Requires-Python` 上限](https://discuss.python.org/t/requires-python-upper-limits/12663)）。

## 限定解析环境（Limited Resolution Environments） {#limited-resolution-environments}

默认情况下，通用解析器会尝试为所有平台和 Python 版本求解。

如果您的项目仅支持有限的平台或 Python 版本集合，可以通过 `environments` 设置来约束求解的平台集合，该设置接受 [PEP 508 环境标记](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers)列表。换句话说，您可以使用 `environments` 设置来 _缩减_ 支持的平台集合。

例如，要将锁文件约束为 macOS 和 Linux，并避免为 Windows 求解：

```toml title="pyproject.toml"
[tool.uv]
environments = [
    "sys_platform == 'darwin'",
    "sys_platform == 'linux'",
]
```

或者，避免为替代的 Python 实现求解：

```toml title="pyproject.toml"
[tool.uv]
environments = [
    "implementation_name == 'cpython'"
]
```

`environments` 设置中的条目必须是互斥的（即它们不能重叠）。例如，`sys_platform == 'darwin'` 和 `sys_platform == 'linux'` 是互斥的，但 `sys_platform == 'darwin'` 和 `python_version >= '3.9'` 不是，因为两者可能同时为真。

## 必需环境（Required Environments） {#required-environments}

在 Python 生态系统中，包可以以源码分发（source distributions）、构建分发（wheels）或两者兼有的形式发布；但要安装包，需要构建分发。如果包缺少构建分发，或者缺少适用于当前平台或 Python 版本的构建分发（构建分发通常是平台特定的），uv 将尝试从源码构建包，然后安装生成的构建分发。

某些包（如 PyTorch）发布了构建分发，但省略了源码分发。此类包 _仅_ 可在有构建分发的平台上安装。例如，如果某个包发布了适用于 Linux 的构建分发，但没有适用于 macOS 或 Windows 的，则该包 _仅_ 可在 Linux 上安装。

缺少源码分发的包会给通用解析带来问题，因为通常至少会有一个平台或 Python 版本无法安装该包。

默认情况下，uv 要求每个此类包至少包含一个与目标 Python 版本兼容的 wheel。`required-environments` 设置可用于确保生成的解析结果包含特定平台的 wheel，或在没有此类 wheel 可用时失败。该设置接受 [PEP 508 环境标记](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers)列表。

`environments` 设置 _限制_ 了 uv 在解析依赖时将考虑的环境集合，而 `required-environments` 则 _扩展_ 了 uv 在解析依赖时 _必须_ 支持的平台集合。

例如，`environments = ["sys_platform == 'darwin'"]` 会将 uv 限制为仅为 macOS 求解（忽略 Linux 和 Windows）。另一方面，`required-environments = ["sys_platform == 'darwin'"]` 将 _要求_ 任何没有源码分发的包必须包含 macOS 的 wheel 才能安装（如果没有此类 wheel 可用则会失败）。

在实践中，`required-environments` 对于声明对非最新平台的显式支持非常有用，因为这通常需要回溯到这些包的最新发布版本之前。例如，要保证任何仅构建分发的包包含对 Intel macOS 的支持：

```toml title="pyproject.toml"
[tool.uv]
required-environments = [
    "sys_platform == 'darwin' and platform_machine == 'x86_64'"
]
```

## 常见标记值（Common Marker Values） {#common-marker-values}

`environments` 和 `required-environments` 设置接受 [PEP 508 环境标记](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers)。这些标记的值源自 Python 运行时（例如 [`sys.platform`](https://docs.python.org/3/library/sys.html#sys.platform)、[`platform.machine()`](https://docs.python.org/3/library/platform.html#platform.machine)、[`platform.system()`](https://docs.python.org/3/library/platform.html#platform.system) 和 [`os.name`](https://docs.python.org/3/library/os.html#os.name)）。

为便于快速参考，各平台最常见的标记值如下：

| 标记（Marker）              | Linux       | macOS      | Windows     |
| --------------------------- | ----------- | ---------- | ----------- |
| `sys_platform`              | `'linux'`   | `'darwin'` | `'win32'`   |
| `platform_system`           | `'Linux'`   | `'Darwin'` | `'Windows'` |
| `platform_machine`（x86-64） | `'x86_64'`  | `'x86_64'` | `'AMD64'`   |
| `platform_machine`（ARM64）  | `'aarch64'` | `'arm64'`  | `'ARM64'`   |
| `os_name`                   | `'posix'`   | `'posix'`  | `'nt'`      |

!!! note

    在 Windows 上，即使在 64 位系统上，`sys_platform` 也始终是 `'win32'`。

您可以通过运行以下命令检查当前平台的值：

```console
$ uvx python -c "import sysconfig; print(sysconfig.get_config_vars())"
```

## 依赖偏好（Dependency Preferences） {#dependency-preferences}

如果解析输出文件存在，即 uv 锁文件（`uv.lock`）或 requirements 输出文件（`requirements.txt`），uv 将 _偏好_ 其中列出的依赖版本。类似地，如果将包安装到虚拟环境中，uv 将偏好已安装的版本（如果存在）。这意味着锁定或已安装的版本不会更改，除非请求了不兼容的版本或通过 `--upgrade` 显式请求升级。

## 解析策略（Resolution Strategy） {#resolution-strategy}

默认情况下，uv 尝试使用每个包的最新版本。例如，`uv pip install flask>=2.0.0` 将安装 Flask 的最新版本，例如 3.0.0。如果 `flask>=2.0.0` 是项目的依赖，则只会使用 `flask` 3.0.0。这一点很重要，例如，因为运行测试不会检查项目是否实际与其声明的 `flask` 2.0.0 下限兼容。

使用 `--resolution lowest`，uv 将为所有依赖（直接和间接/传递依赖）安装尽可能最低的版本。或者，`--resolution lowest-direct` 将为所有直接依赖使用最低兼容版本，同时为所有其他依赖使用最新兼容版本。uv 将始终为构建依赖使用最新版本。

例如，给定以下 `requirements.in` 文件：

```python title="requirements.in"
flask>=2.0.0
```

运行 `uv pip compile requirements.in -o requirements.txt` 将生成以下 `requirements.txt` 文件：

```python title="requirements.txt"
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in -o requirements.txt
blinker==1.7.0
    # via flask
click==8.1.7
    # via flask
flask==3.0.0
itsdangerous==2.1.2
    # via flask
jinja2==3.1.2
    # via flask
markupsafe==2.1.3
    # via
    #   jinja2
    #   werkzeug
werkzeug==3.0.1
    # via flask
```

然而，`uv pip compile --resolution lowest requirements.in -o requirements.txt` 将生成：

```python title="requirements.txt"
# This file was autogenerated by uv via the following command:
#    uv pip compile --resolution lowest requirements.in -o requirements.txt
click==7.1.2
    # via flask
flask==2.0.0
itsdangerous==2.0.0
    # via flask
jinja2==3.0.0
    # via flask
markupsafe==2.0.0
    # via jinja2
werkzeug==2.0.0
    # via flask
```

发布库时，建议在持续集成中分别使用 `--resolution lowest` 或 `--resolution lowest-direct` 运行测试，以确保与声明的下限兼容。

## 预发布版本处理（Pre-release Handling） {#pre-release-handling}

默认情况下，uv 在两种情况下会在依赖解析期间接受预发布版本：

1. 如果包是直接依赖，且其版本说明符包含预发布版本说明符（例如 `flask>=2.0.0rc1`）。
1. 如果包 _所有_ 已发布的版本都是预发布版本。

如果依赖解析因传递预发布版本而失败，uv 将提示使用 `--prerelease allow` 来允许所有依赖的预发布版本。

或者，可以将传递依赖添加为[约束](#dependency-constraints)或直接依赖（即在 `requirements.in` 或 `pyproject.toml` 中），并附带预发布版本说明符（例如 `flask>=2.0.0rc1`），以选择为该特定依赖启用预发布版本支持。

预发布版本是[出了名的难以建模](https://pubgrub-rs-guide.netlify.app/limitations/prerelease_versions)，并且是其他打包工具中常见的错误来源。uv 的预发布版本处理是 _有意_ 限制的，需要用户主动选择启用预发布版本以确保正确性。

更多详情，请参见[预发布版本兼容性](../pip/compatibility.md#pre-release-compatibility)。

## 多版本解析（Multi-version Resolution） {#multi-version-resolution}

在通用解析期间，一个包可能会在同一锁文件中以不同版本或 URL 多次列出，因为不同平台或 Python 版本可能需要不同的版本。

`--fork-strategy` 设置可用于控制 uv 如何在 (1) 最小化所选版本数量和 (2) 为每个平台选择尽可能最新的版本之间进行权衡。前者导致跨平台更大的一致性，而后者导致在可能的情况下使用更新的包版本。

默认情况下（`--fork-strategy requires-python`），uv 将优化为每个受支持的 Python 版本选择每个包的最新版本，同时最小化跨平台的所选版本数量。

例如，当使用 Python 要求 `>=3.8` 解析 `numpy` 时，uv 将选择以下版本：

```txt
numpy==1.24.4 ; python_version == "3.8"
numpy==2.0.2 ; python_version == "3.9"
numpy==2.2.0 ; python_version >= "3.10"
```

此解析反映了 NumPy 2.2.0 及更高版本至少需要 Python 3.10，而较早版本与 Python 3.8 和 3.9 兼容。

在 `--fork-strategy fewest` 下，uv 将改为最小化每个包的所选版本数量，偏好与更广泛的受支持 Python 版本或平台兼容的较旧版本。

例如，在上述场景中，uv 将为所有 Python 版本选择 `numpy==1.24.4`，而不是为 Python 3.9 升级到 `numpy==2.0.2` 和为 Python 3.10 及更高版本升级到 `numpy==2.2.0`。

## 依赖约束（Dependency Constraints） {#dependency-constraints}

与 pip 类似，uv 支持约束文件（`--constraint constraints.txt`），用于缩小给定包的可接受版本集合。约束文件类似于 requirements 文件，但仅作为约束列出不会导致包被包含到解析中。相反，约束仅在请求的包已作为直接或传递依赖被引入时才生效。约束对于缩小传递依赖的可用版本范围非常有用。它们也可用于保持解析结果与某组其他已解析版本同步，无论两者之间有哪些包重叠。

## 依赖覆盖（Dependency Overrides） {#dependency-overrides}

依赖覆盖允许通过覆盖包的声明依赖来绕过不成功或不理想的解析结果。覆盖是一种有用的最后手段，适用于您 _知道_ 某个依赖与某个包的特定版本兼容，尽管元数据表明不兼容的情况。

例如，如果传递依赖声明了需求 `pydantic>=1.0,<2.0`，但 _确实_ 可以与 `pydantic>=2.0` 一起工作，用户可以通过在覆盖中包含 `pydantic>=1.0,<3` 来覆盖声明的依赖，从而允许解析器选择更新版本的 `pydantic`。

具体来说，如果 `pydantic>=1.0,<3` 被包含为覆盖，uv 将忽略所有对 `pydantic` 的声明需求，用覆盖替换它们。在上面的示例中，`pydantic>=1.0,<2.0` 需求将被完全忽略，取而代之的是 `pydantic>=1.0,<3`。

约束只能 _缩小_ 包的可接受版本集合，而覆盖可以 _扩大_ 可接受版本集合，为错误的上限版本边界提供了逃生通道。与约束一样，覆盖不会添加对包的依赖，仅在包作为直接或传递依赖被请求时才生效。

在 `pyproject.toml` 中，使用 `tool.uv.override-dependencies` 来定义覆盖列表。在 pip 兼容接口中，可以使用 `--override` 选项来传递与约束文件格式相同的文件。

如果为同一个包提供了多个覆盖，必须使用[标记](#platform-markers)来区分它们。如果包有一个带标记的依赖，在使用覆盖时它会被无条件替换——标记是否评估为 true 或 false 并不重要。

## 依赖元数据（Dependency Metadata） {#dependency-metadata}

在解析期间，uv 需要解析它遇到的每个包的元数据，以确定其依赖关系。此元数据通常作为包索引中的静态文件可用；然而，对于仅提供源码分发的包，元数据可能无法预先获取。

在这种情况下，uv 必须构建包以确定其元数据（例如，通过调用 `setup.py`）。这可能会在解析期间引入性能损失。此外，它还要求包能够在所有平台上构建，而这可能并不成立。

例如，您可能有一个只应在 Linux 上构建和安装的包，但在 macOS 或 Windows 上无法成功构建。虽然 uv 可以为此场景构建一个完全有效的锁文件，但这样做需要构建该包，而这在非 Linux 平台上会失败。

`tool.uv.dependency-metadata` 表可用于为此类依赖预先提供静态元数据，从而允许 uv 跳过构建步骤并使用提供的元数据。

例如，要为 `chumpy` 预先提供元数据，请在其 `pyproject.toml` 中包含 `dependency-metadata`：

```toml
[[tool.uv.dependency-metadata]]
name = "chumpy"
version = "0.70"
requires-dist = ["numpy>=1.8.1", "scipy>=0.13.0", "six>=1.11.0"]
```

这些声明适用于包 _没有_ 预先声明静态元数据的情况，尽管它们对于需要[禁用构建隔离](./projects/config.md#build-isolation)的包也很有用。在这种情况下，预先声明包元数据可能比在解析包之前创建自定义构建环境更容易。

例如，过去版本的 `flash-attn` 没有声明静态元数据。通过预先声明 `flash-attn` 的元数据，uv 可以解析 `flash-attn` 而无需从源码构建包（这本身需要安装 `torch`）：

```toml
[project]
name = "project"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = ["flash-attn"]

[tool.uv.sources]
flash-attn = { git = "https://github.com/Dao-AILab/flash-attention", tag = "v2.6.3" }

[[tool.uv.dependency-metadata]]
name = "flash-attn"
version = "2.6.3"
requires-dist = ["torch", "einops"]
```

与依赖覆盖类似，`tool.uv.dependency-metadata` 也可用于包的元数据不正确或不完整的情况，或者当包在包索引中不可用时。依赖覆盖允许全局覆盖包的允许版本，而元数据覆盖允许覆盖 _特定包_ 的声明元数据。

!!! note

    `tool.uv.dependency-metadata` 中的 `version` 字段对于基于注册表的依赖是可选的（省略时，uv 将假定元数据适用于包的所有版本），但对于直接 URL 依赖（如 Git 依赖）是 _必需的_。

`tool.uv.dependency-metadata` 表中的条目遵循 [Metadata 2.3](https://packaging.python.org/en/latest/specifications/core-metadata/) 规范，不过 uv 仅读取 `name`、`version`、`requires-dist`、`requires-python` 和 `provides-extra`。`version` 字段也被视为可选的。如果省略，元数据将用于指定包的所有版本。

## 冲突依赖（Conflicting Dependencies） {#conflicting-dependencies}

uv 要求项目声明的所有依赖彼此兼容，并在创建锁文件时一起解析所有依赖。这包括项目依赖、可选依赖（"extras"）和依赖组（开发依赖）。

如果在一个 extra 中声明的依赖与另一个 extra 中的依赖不兼容，uv 将无法解析项目需求并报错。例如，考虑两组相互冲突的可选依赖：

```toml title="pyproject.toml"
[project.optional-dependencies]
extra1 = ["numpy==2.1.2"]
extra2 = ["numpy==2.0.0"]
```

如果您使用上述依赖运行 `uv lock`，解析将失败：

```console
$ uv lock
  x No solution found when resolving dependencies:
  `-> Because myproject[extra2] depends on numpy==2.0.0 and myproject[extra1] depends on numpy==2.1.2, we can conclude that myproject[extra1] and
      myproject[extra2] are incompatible.
      And because your project requires myproject[extra1] and myproject[extra2], we can conclude that your projects's requirements are unsatisfiable.
```

为了解决这个问题，uv 支持显式声明冲突。如果您指定 `extra1` 和 `extra2` 是冲突的，uv 将分别解析它们。在 `tool.uv` 部分中指定冲突：

```toml title="pyproject.toml"
[tool.uv]
conflicts = [
    [
      { extra = "extra1" },
      { extra = "extra2" },
    ],
]
```

现在，运行 `uv lock` 将成功。但是，您不能同时安装 `extra1` 和 `extra2`：

```console
$ uv sync --extra extra1 --extra extra2
Resolved 3 packages in 14ms
error: extra `extra1`, extra `extra2` are incompatible with the declared conflicts: {`myproject[extra1]`, `myproject[extra2]`}
```

发生此错误是因为同时安装 `extra1` 和 `extra2` 会导致将两个不同版本的包安装到同一环境中。

上述处理冲突可选依赖的策略也适用于依赖组：

```toml title="pyproject.toml"
[dependency-groups]
group1 = ["numpy==2.1.2"]
group2 = ["numpy==2.0.0"]

[tool.uv]
conflicts = [
    [
      { group = "group1" },
      { group = "group2" },
    ],
]
```

与冲突 extras 的唯一区别是，您需要使用 `group` 键而不是 `extra`。

当使用包含多个项目的工作空间（workspace）时，同样的限制适用——uv 要求所有工作空间成员彼此兼容。类似地，可以跨工作空间成员声明冲突。

例如，考虑以下工作空间：

```toml title="member1/pyproject.toml"
[project]
name = "member1"

[project.optional-dependencies]
extra1 = ["numpy==2.1.2"]
```

```toml title="member2/pyproject.toml"
[project]
name = "member2"

[project.optional-dependencies]
extra2 = ["numpy==2.0.0"]
```

要声明这些不同工作空间成员中 extras 之间的冲突，请使用 `package` 键：

```toml title="pyproject.toml"
[tool.uv]
conflicts = [
    [
      { package = "member1", extra = "extra1" },
      { package = "member2", extra = "extra2" },
    ],
]
```

一个工作空间成员的项目依赖（即 `project.dependencies`）也可能与另一个成员的 extra 冲突，例如：

```toml title="member1/pyproject.toml"
[project]
name = "member1"
dependencies = ["numpy==2.1.2"]
```

```toml title="member2/pyproject.toml"
[project]
name = "member2"

[project.optional-dependencies]
extra2 = ["numpy==2.0.0"]
```

此冲突也可以使用 `package` 键声明：

```toml title="pyproject.toml"
[tool.uv]
conflicts = [
    [
      { package = "member1" },
      { package = "member2", extra = "extra2" },
    ],
]
```

类似地，某些工作空间成员可能具有冲突的项目依赖：

```toml title="member1/pyproject.toml"
[project]
name = "member1"
dependencies = ["numpy==2.1.2"]
```

```toml title="member2/pyproject.toml"
[project]
name = "member2"
dependencies = ["numpy==2.0.0"]
```

此冲突也可以使用 `package` 键声明：

```toml title="pyproject.toml"
[tool.uv]
conflicts = [
    [
      { package = "member1" },
      { package = "member2" },
    ],
]
```

这些工作空间成员将无法一起安装，例如，工作空间根目录不能定义：

```toml title="pyproject.toml"
[project]
name = "root"
dependencies = ["member1", "member2"]
```

## 下限（Lower Bounds） {#lower-bounds}

默认情况下，`uv add` 会为依赖添加下限，并且在使用 uv 管理项目时，如果直接依赖没有下限，uv 会发出警告。

下限在"正常路径"中并不关键，但它们对于存在依赖冲突的情况很重要。例如，考虑一个需要两个包的项目，而这些包具有冲突的依赖关系。解析器需要检查两个包在约束范围内的所有版本组合——如果所有组合都冲突，则会报告错误，因为依赖关系无法满足。如果没有下限，解析器可以（而且通常会）回溯到包的最旧版本。这不仅因为速度慢而成为问题，旧版本的包通常无法构建，或者解析器最终可能选择一个足够旧的版本，它既不依赖冲突的包，也无法与您的代码一起工作。

下限在编写库时尤其关键。声明库所依赖的每个依赖的最低版本，并验证这些下限是否正确非常重要——使用 [`--resolution lowest` 或 `--resolution lowest-direct`](#resolution-strategy) 进行测试。否则，用户可能会收到库依赖的旧的不兼容版本，库将因意外错误而失败。

## 可复现解析（Reproducible Resolutions） {#reproducible-resolutions}

uv 支持 `--exclude-newer` 选项，将解析限制在特定日期之前上传的发行版，从而无论新包发布如何，都能复现安装。该日期与每个单独发行版制品的上传时间（即每个文件上传到包索引的时间）进行比较，而不是包版本的发布日期。日期可以指定为 [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) 时间戳（例如 `2006-12-02T02:07:43Z`）或系统配置时区中相同格式的本地日期（例如 `2006-12-02`）。

!!! important

    包索引必须支持 [`PEP 700`](https://peps.python.org/pep-0700/) 中指定的 `upload-time` 字段。如果给定发行版不存在该字段，则该发行版将被视为不可用，除非通过 `--exclude-newer-package <package>=false` 选择退出该包，或者索引配置了其自身的 `exclude-newer` 值，或者通过 `[[tool.uv.index]] exclude-newer = false` 选择退出该索引。PyPI 为所有包提供了 `upload-time`。

为了确保可复现性，无法满足的解析消息不会提及由于 `--exclude-newer` 标志而排除了发行版——更新的发行版将被视为不存在。

!!! note

    `--exclude-newer` 选项仅适用于从注册表读取的包（而不是例如 Git 依赖）。此外，在使用 `uv pip` 接口时，uv 不会降级先前安装的包，除非提供了 `--reinstall` 标志，在这种情况下 uv 将执行新的解析。

此选项也支持在 `pyproject.toml` 中使用，例如：

```pyproject.toml
[tool.uv]
exclude-newer = "2006-12-02T02:07:43Z"
```

在持久化配置中指定时，不允许使用本地日期时间。

也可以为特定包指定值，例如 `--exclude-newer-package setuptools=2006-12-02`，或：

```pyproject.toml
[tool.uv]
exclude-newer-package = { setuptools = "2006-12-02T02:07:43Z" }
```

包选项也接受 `<package>=false` 来选择退出该包的限制，例如 `--exclude-newer-package setuptools=false`，或：

```pyproject.toml
[tool.uv]
exclude-newer-package = { setuptools = false }
```

这对于临时使用更新版本的包或允许从不发布上传时间的索引解析包非常有用。

包特定的值将优先于全局和索引特定的值。

同样，单个索引可以覆盖全局截止时间：

```pyproject.toml
[tool.uv]
exclude-newer = "2006-12-02T02:07:43Z"

[[tool.uv.index]]
name = "internal"
url = "https://internal.example.com/simple"
exclude-newer = "7 days"
```

或者为该索引完全禁用它：

```pyproject.toml
[[tool.uv.index]]
name = "internal"
url = "https://internal.example.com/simple"
exclude-newer = false
```

这对于不发布 `upload-time` 的私有索引很有用，或者用于在保留全局行为的同时对特定索引应用不同的可复现性窗口。

## 依赖冷却期（Dependency Cooldowns） {#dependency-cooldowns}

uv 还支持依赖"冷却期"，在此期间解析将忽略比指定时长更新的包。这是通过延迟包更新直到社区有机会审查新版本包来提高安全态势的好方法。

此功能通过 [`exclude-newer` 选项](#reproducible-resolutions)提供，并共享相同的语义。

通过指定持续时间而不是绝对值来定义依赖冷却期。可以使用"友好"持续时间（例如 `24 hours`、`1 week`、`30 days`）或 ISO 8601 持续时间（例如 `PT24H`、`P7D`、`P30D`）。

!!! note

    持续时间不遵循本地时区的语义，始终解析为固定的秒数，假设一天为 24 小时（例如，DST 转换被忽略）。不允许使用日历单位（如月和年），因为它们本质上是不一致的长度。

当使用持续时间进行解析时，时间戳是相对于当前时间计算的。当使用 `uv.lock` 文件时，时间戳包含在锁文件中。uv 不会在当前时间变化时更新锁文件，而是会在执行新解析时更新时间戳，例如当使用 `--upgrade` 或 `--refresh` 时。

此选项也支持在 `pyproject.toml` 中使用，例如：

```pyproject.toml
[tool.uv]
exclude-newer = "1 week"
```

也可以为特定包指定值，例如 `--exclude-newer-package "setuptools=30 days"`，或：

```pyproject.toml
[tool.uv]
exclude-newer = "1 week"
exclude-newer-package = { setuptools = "30 days" }
```

## 源码分发（Source Distribution） {#source-distribution}

[PEP 625](https://peps.python.org/pep-0625/) 规定包必须以 gzip tarball（`.tar.gz`）归档格式分发源码分发。在此规范之前，也允许其他归档格式，为了向后兼容，需要支持这些格式。uv 支持读取和提取以下格式的归档：

- gzip tarball（`.tar.gz`、`.tgz`）
- bzip2 tarball（`.tar.bz2`、`.tbz`）
- xz tarball（`.tar.xz`、`.txz`）
- zstd tarball（`.tar.zst`）
- lzip tarball（`.tar.lz`）
- lzma tarball（`.tar.lzma`）
- zip（`.zip`）

!!! important

    强烈建议不要使用 `.tar.gz` 以外的源码分发扩展名，因为这些扩展名在 Python 打包生态系统中并未得到广泛或一致的支持。

!!! warning "已弃用"

    对 `.tar.gz` 以外源码分发扩展名的支持已弃用，将在 uv 的未来版本中移除。

## 锁文件版本控制（Lockfile Versioning） {#lockfile-versioning}

`uv.lock` 文件使用版本化的模式（schema）。模式版本包含在锁文件的 `version` 字段中。

任何给定版本的 uv 可以读取和写入具有相同模式版本的锁文件，但会拒绝具有更高模式版本的锁文件。例如，如果您的 uv 版本支持模式 v1，`uv lock` 在遇到具有模式 v2 的现有锁文件时将报错。

支持模式 v2 的 uv 版本 _可能_ 能够读取具有模式 v1 的锁文件，如果模式更新是向后兼容的。但是，这并不保证，uv 在遇到具有过时模式版本的锁文件时可能会退出并报错。

模式版本被视为公共 API 的一部分，因此仅在小版本（minor releases）中作为破坏性变更进行提升（参见[版本控制](../reference/policies/versioning.md)）。因此，给定 uv 小版本中的所有 uv 补丁版本（patch versions）都保证具有完全的锁文件兼容性。换句话说，锁文件可能仅在跨小版本时被拒绝。

锁文件的 `revision` 字段用于跟踪锁文件的向后兼容更改。例如，向发行版添加新字段。对 `revision` 的更改不会导致旧版本 uv 报错。

## 了解更多 {#learn-more}

有关解析器内部机制的更多详细信息，请参阅[解析器参考](../reference/internals/resolver.md)文档。