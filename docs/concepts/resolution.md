---
subtitle: Resolution
---

# 解析

解析是将一系列需求转换为满足这些需求的软件包版本列表的过程。解析需要递归地搜索兼容的软件包版本，确保请求的需求得到满足，并且所请求软件包的需求是兼容的。

## 依赖

大多数项目和软件包都有依赖。依赖是当前软件包正常工作所必需的其他软件包。一个软件包将其依赖定义为_需求_，大致是一个软件包名称和可接受版本的组合。当前项目定义的依赖称为 _直接依赖_。当前项目的每个依赖所添加的依赖称为 _间接_ 或 _传递依赖_。

!!! note

    有关依赖的详细信息，请参阅 Python 打包文档中的[依赖说明符页面](https://packaging.python.org/en/latest/specifications/dependency-specifiers/)。

## 基本示例

为了帮助演示解析过程，请考虑以下依赖关系：

<!-- prettier-ignore -->
- 项目依赖于 `foo` 和 `bar`。
- `foo` 有一个版本 1.0.0：
    - `foo 1.0.0` 依赖于 `lib>=1.0.0`。
- `bar` 有一个版本 1.0.0：
    - `bar 1.0.0` 依赖于 `lib>=2.0.0`。
- `lib` 有两个版本 1.0.0 和 2.0.0。这两个版本都没有依赖。

在此示例中，解析器必须找到一组满足项目需求的软件包版本。由于 `foo` 和 `bar` 都只有一个版本，因此将使用这些版本。解析还必须包括传递性依赖，因此必须选择一个 `lib` 的版本。`foo 1.0.0` 允许 `lib` 的所有可用版本，但 `bar 1.0.0` 需要 `lib>=2.0.0`，因此必须使用 `lib 2.0.0`。

在某些解析中，可能有多个有效的解决方案。请考虑以下依赖关系：

<!-- prettier-ignore -->
- 项目依赖于 `foo` 和 `bar`。
- `foo` 有两个版本 1.0.0 和 2.0.0：
    - `foo 1.0.0` 没有依赖。
    - `foo 2.0.0` 依赖于 `lib==2.0.0`。
- `bar` 有两个版本 1.0.0 和 2.0.0：
    - `bar 1.0.0` 没有依赖。
    - `bar 2.0.0` 依赖于 `lib==1.0.0`
- `lib` 有两个版本 1.0.0 和 2.0.0。这两个版本都没有依赖。

在此示例中，必须选择 `foo` 和 `bar` 的某个版本；但是，确定哪个版本需要考虑 `foo` 和 `bar` 每个版本的依赖关系。`foo 2.0.0` 和 `bar 2.0.0` 不能一起安装，因为它们在所需的 `lib` 版本上存在冲突，因此解析器必须选择 `foo 1.0.0`（以及 `bar 2.0.0`）或 `bar 1.0.0`（以及 `foo 1.0.0`）。两者都是有效的解决方案，不同的解析算法可能会产生任一结果。

## 平台标记

标记允许将表达式附加到需求上，以指示何时应使用该依赖。例如 `bar ; python_version < "3.9"` 表示 `bar` 只应安装在 Python 3.8 及更早版本上。

标记用于根据当前环境或平台调整软件包的依赖关系。例如，标记可用于按操作系统、CPU 架构、Python 版本、Python 实现等修改依赖关系。

!!! note

    有关标记的更多详细信息，请参阅 Python 打包文档中的[环境标记](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers)部分。

标记对于解析很重要，因为它们的值会更改所需依赖。通常，Python 软件包解析器使用_当前_平台的标记来确定要使用哪些依赖，因为软件包通常是在当前平台上_安装_的。但是，对于_锁定_依赖，这会产生问题——锁定文件仅适用于使用创建锁定文件的同一平台的开发人员。为了解决这个问题，存在平台无关或“通用”解析器。

uv 支持[平台特定解析](#_5)和[通用解析](#_6)解析。

## 平台特定解析

默认情况下，uv 的 pip 接口，即 [`uv pip compile`](../pip/compile.md)，会生成一个平台特定的解析，类似于 `pip-tools`。在 uv 的项目接口中，无法使用平台特定的解析。

uv 还支持使用 `--python-platform` 和 `--python-version` 选项为特定的备用平台和 Python 版本进行解析。例如，如果在 macOS 上使用 Python 3.12，可以使用 `uv pip compile --python-platform linux --python-version 3.10 requirements.in` 来为 Linux 上的 Python 3.10 生成解析。与通用解析不同，在平台特定解析期间，提供的 `--python-version` 是要使用的确切 Python 版本，而不是下限。

!!! note

    Python 的环境标记比简单的 `--python-platform` 参数所能表达的有关当前机器的信息要多得多。例如，macOS 上的 `platform_version` 标记包括内核构建的时间，理论上可以编码在软件包需求中。uv 的解析器会尽力生成一个与在目标 `--python-platform` 上运行的任何机器兼容的解析，这对于大多数用例来说应该足够了，但对于复杂的软件包和平台组合，可能会失去保真度。

## 通用解析

uv 的锁定文件 (`uv.lock`) 是通过通用解析创建的，并且可以跨平台移植。这确保了项目中的每个人的依赖关系都被锁定，无论操作系统、体系结构和 Python 版本如何。uv 锁定文件由[项目](../concepts/projects/index.md)命令（如 `uv lock`、`uv sync` 和 `uv add`）创建和修改。

通用解析也适用于 uv 的 pip 接口，即 [`uv pip compile`](../pip/compile.md)，使用 `--universal` 标志。生成的需求文件将包含标记，以指示每个依赖项与哪个平台相关。

在通用解析期间，如果不同平台需要不同版本，一个包可能会在同一个锁定文件中以不同的版本或 URL 列出多次——标记决定了将使用哪个版本。通用解析通常比平台特定解析更受限制，因为我们需要考虑所有标记的需求。

在通用解析期间，所有必需的包必须与 `pyproject.toml` 中声明的 `requires-python` 的*整个*范围兼容。例如，如果一个项目的 `requires-python` 是 `>=3.8`，如果给定依赖的所有版本都要求 Python 3.9 或更高版本，那么解析将会失败，因为该依赖缺少适用于（例如）Python 3.8 的可用版本，这是项目支持范围的下限。换句话说，项目的 `requires-python` 必须是其所有依赖的 `requires-python` 的子集。

在为给定依赖选择兼容版本时，uv 将（[默认情况下](#_12)）尝试为每个受支持的 Python 版本选择最新的兼容版本。例如，如果一个项目的 `requires-python` 是 `>=3.8`，并且一个依赖的最新版本要求 Python 3.9 或更高版本，而所有支持 Python 3.8 的先前版本，解析器将为运行 Python 3.9 或更高版本的用户选择最新版本，为运行 Python 3.8 的用户选择以前的版本。

在评估依赖的 `requires-python` 范围时，uv 只考虑下限，完全忽略上限。例如，`>=3.8, <4` 被视为 `>=3.8`。尊重 `requires-python` 的上限通常会导致形式上正确但实际上不正确的解析，因为，例如，解析器会回溯到第一个省略上限的已发布版本（请参阅：[`Requires-Python` 上限](https://discuss.python.org/t/requires-python-upper-limits/12663)）。

### 有限的解析环境

默认情况下，通用解析器会尝试为所有平台和 Python 版本进行解析。

如果您的项目仅支持有限的平台或 Python 版本集，您可以通过 `environments` 设置来约束已解析平台的集合，该设置接受一个 [PEP 508 环境标记](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers)列表。换句话说，您可以使用 `environments` 设置来*减少*支持的平台集合。

例如，要将锁定文件限制为 macOS 和 Linux，并避免为 Windows 解析：

```toml title="pyproject.toml"
[tool.uv]
environments = [
    "sys_platform == 'darwin'",
    "sys_platform == 'linux'",
]
```

或者，要避免为其他 Python 实现进行解析：

```toml title="pyproject.toml"
[tool.uv]
environments = [
    "implementation_name == 'cpython'"
]
```

`environments` 设置中的条目必须是不相交的（即，它们不能重叠）。例如，`sys_platform == 'darwin'` 和 `sys_platform == 'linux'` 是不相交的，但 `sys_platform == 'darwin'` 和 `python_version >= '3.9'` 不是，因为两者可能同时为真。

### 所需环境

在 Python 生态系统中，软件包可以作为源代码发行版、构建发行版（wheel）或两者兼而有之发布；但要安装软件包，需要构建发行版。如果软件包缺少构建发行版，或者缺少当前平台或 Python 版本的发行版（构建发行版通常是平台特定的），uv 将尝试从源代码构建软件包，然后安装生成的构建发行版。

一些软件包（如 PyTorch）发布构建发行版，但省略了源代码发行版。此类软件包*仅*可在提供构建发行版的平台上安装。例如，如果一个软件包为 Linux 发布了构建发行版，但没有为 macOS 或 Windows 发布，那么该软件包将*仅*可在 Linux 上安装。

缺少源代码发行版的软件包会给通用解析带来问题，因为通常至少会有一个平台或 Python 版本无法安装该软件包。

默认情况下，uv 要求每个此类软件包至少包含一个与目标 Python 版本兼容的 wheel。`required-environments` 设置可用于确保生成的解析包含特定平台的 wheel，或者在没有此类 wheel 可用时失败。该设置接受一个 [PEP 508 环境标记](https://packaging.python.org/en/latest/specifications/dependency-specifiers/#environment-markers)列表。

`environments` 设置*限制*了 uv 在解析依赖项时将考虑的环境集，而 `required-environments` *扩展*了 uv 在解析依赖项时*必须*支持的平台集。

例如，`environments = ["sys_platform == 'darwin'"]` 会将 uv 限制为仅为 macOS 解析（并忽略 Linux 和 Windows）。另一方面，`required-environments = ["sys_platform == 'darwin'"]` 将*要求*任何没有源代码发行版的软件包都包含一个适用于 macOS 的 wheel 才能安装（如果没有此类 wheel 可用，则会失败）。

在实践中，`required-environments` 对于声明对非最新平台的显式支持很有用，因为这通常需要回溯到这些软件包的最新发布版本之前。例如，为了保证任何仅构建发行版的软件包都包含对 Intel macOS 的支持：

```toml title="pyproject.toml"
[tool.uv]
required-environments = [
    "sys_platform == 'darwin' and platform_machine == 'x86_64'"
]
```

## 依赖偏好

如果存在解析输出文件，即 uv 锁定文件 (`uv.lock`) 或需求输出文件 (`requirements.txt`)，uv 将*偏好*其中列出的依赖版本。同样，如果将软件包安装到虚拟环境中，如果存在已安装的版本，uv 将偏好该版本。这意味着锁定的或已安装的版本不会更改，除非请求了不兼容的版本或使用 `--upgrade` 显式请求升级。

## 解析策略

默认情况下，uv 会尝试使用每个软件包的最新版本。例如，`uv pip install flask>=2.0.0` 将安装 Flask 的最新版本，例如 3.0.0。如果 `flask>=2.0.0` 是项目的依赖项，则只会使用 `flask` 3.0.0。这很重要，例如，因为运行测试不会检查项目是否真的与其声明的 `flask` 2.0.0 的下限兼容。

使用 `--resolution lowest`，uv 将为所有依赖项（直接和间接（传递））安装尽可能低的版本。或者，`--resolution lowest-direct` 将为所有直接依赖项使用最低的兼容版本，而为所有其他依赖项使用最新的兼容版本。uv 将始终为构建依赖项使用最新版本。

例如，给定以下 `requirements.in` 文件：

```python title="requirements.in"
flask>=2.0.0
```

运行 `uv pip compile requirements.in` 将生成以下 `requirements.txt` 文件：

```python title="requirements.txt"
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in
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

但是，`uv pip compile --resolution lowest requirements.in` 将生成：

```python title="requirements.in"
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in --resolution lowest
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

发布库时，建议在持续集成中使用 `--resolution lowest` 或 `--resolution lowest-direct` 单独运行测试，以确保与声明的下限兼容。

## 预发布处理

默认情况下，uv 在依赖解析期间会在两种情况下接受预发布版本：

1. 如果包是直接依赖项，并且其版本说明符包含预发布说明符（例如，`flask>=2.0.0rc1`）。
2. 如果一个包的所有已发布版本都是预发布版本。

如果由于传递性预发布而导致依赖解析失败，uv 将提示使用 `--prerelease allow` 以允许所有依赖项的预发布。

或者，可以将传递性依赖项添加为[约束](#_13)或直接依赖项（即在 `requirements.in` 或 `pyproject.toml` 中），并带有预发布版本说明符（例如，`flask>=2.0.0rc1`），以选择对该特定依赖项的预发布支持。

预发布版本是[众所周知的难以](https://pubgrub-rs-guide.netlify.app/limitations/prerelease_versions)建模的，并且是其他打包工具中错误的常见来源。uv 的预发布处理是*有意*限制的，并且需要用户选择加入预发布以确保正确性。

有关更多详细信息，请参阅[预发布兼容性](../pip/compatibility.md#_2)。

## 多版本解析

在通用解析期间，一个包可能会在同一个锁定文件中以不同的版本或 URL 多次列出，因为不同的平台或 Python 版本可能需要不同的版本。

`--fork-strategy` 设置可用于控制 uv 如何在 (1) 最小化所选版本数量和 (2) 为每个平台选择尽可能新的版本之间进行权衡。前者可以提高跨平台的一致性，而后者可以在可能的情况下使用较新的软件包版本。

默认情况下 (`--fork-strategy requires-python`)，uv 将优化为为每个受支持的 Python 版本选择每个软件包的最新版本，同时最小化跨平台选择的版本数量。

例如，当使用 `>=3.8` 的 Python 需求解析 `numpy` 时，uv 将选择以下版本：

```txt
numpy==1.24.4 ; python_version == "3.8"
numpy==2.0.2 ; python_version == "3.9"
numpy==2.2.0 ; python_version >= "3.10"
```

此解析反映了 NumPy 2.2.0 及更高版本至少需要 Python 3.10，而早期版本与 Python 3.8 和 3.9 兼容。

在 `--fork-strategy fewest` 下，uv 将改为最小化每个软件包选择的版本数量，优先选择与更广泛的受支持 Python 版本或平台兼容的旧版本。

例如，在上述情况下，uv 将为所有 Python 版本选择 `numpy==1.24.4`，而不是为 Python 3.9 升级到 `numpy==2.0.2`，为 Python 3.10 及更高版本升级到 `numpy==2.2.0`。

## 依赖约束

与 pip 类似，uv 支持约束文件 (`--constraint constraints.txt`)，这些文件可以缩小给定软件包的可接受版本范围。约束文件类似于需求文件，但仅作为约束列出并不会导致软件包被包含在解析中。相反，只有当请求的软件包已经作为直接或传递性依赖项被引入时，约束才会生效。约束对于减少传递性依赖项的可用版本范围很有用。它们还可以用于使解析与某个其他已解析版本集保持同步，而不管两者之间有哪些重叠的软件包。

## 依赖覆盖

依赖覆盖允许通过覆盖软件包声明的依赖项来绕过不成功或不理想的解析。当您*知道*某个依赖项与某个软件包的特定版本兼容，尽管元数据另有说明时，覆盖是一种有用的最后手段。

例如，如果一个传递性依赖项声明了 `pydantic>=1.0,<2.0` 的需求，但*确实*可以与 `pydantic>=2.0` 一起使用，用户可以通过在覆盖中包含 `pydantic>=1.0,<3` 来覆盖声明的依赖项，从而允许解析器选择一个较新版本的 `pydantic`。

具体来说，如果 `pydantic>=1.0,<3` 作为覆盖项被包含，uv 将忽略所有在 `pydantic` 上声明的需求，并用覆盖项替换它们。在上面的例子中，`pydantic>=1.0,<2.0` 的需求将被完全忽略，取而代之的是 `pydantic>=1.0,<3`。

虽然约束只能*减少*软件包的可接受版本集，但覆盖可以*扩展*可接受版本集，为错误的版本上限提供了一个“逃生舱口”。与约束一样，覆盖不会添加对软件包的依赖，只有当软件包在直接或传递性依赖中被请求时才会生效。

在 `pyproject.toml` 中，使用 `tool.uv.override-dependencies` 来定义一个覆盖列表。在与 pip 兼容的接口中，可以使用 `--override` 选项来传递与约束文件格式相同的文件。

如果为同一个软件包提供了多个覆盖，则必须使用[标记](#_4)来区分它们。如果一个软件包的依赖项带有标记，在使用覆盖时它会被无条件替换——无论标记的计算结果是真还是假。

## 依赖元数据

在解析过程中，uv 需要解析它遇到的每个包的元数据，以确定其依赖关系。此元数据通常在包索引中作为静态文件提供；但是，对于只提供源分发的包，元数据可能无法预先获得。

在这种情况下，uv 必须构建包以确定其元数据（例如，通过调用 `setup.py`）。这会在解析过程中引入性能损失。此外，它还要求包可以在所有平台上构建，这可能并非总是如此。

例如，您可能有一个只应在 Linux 上构建和安装的包，但在 macOS 或 Windows 上无法成功构建。虽然 uv 可以为此场景构建一个完全有效的锁定文件，但这样做需要构建包，这在非 Linux 平台上会失败。

`tool.uv.dependency-metadata` 表可用于预先为此类依赖项提供静态元数据，从而允许 uv 跳过构建步骤并改用提供的元数据。

例如，要预先为 `chumpy` 提供元数据，请在 `pyproject.toml` 中包含其 `dependency-metadata`：

```toml
[[tool.uv.dependency-metadata]]
name = "chumpy"
version = "0.70"
requires-dist = ["numpy>=1.8.1", "scipy>=0.13.0", "six>=1.11.0"]
```

这些声明旨在用于包未预先声明静态元数据的情况，尽管它们对于需要禁用构建隔离的包也很有用。在这种情况下，预先声明包元数据可能比在解析包之前创建自定义构建环境更容易。

例如，您可以声明 `flash-attn` 的元数据，允许 uv 在不从源代码构建包（这本身需要安装 `torch`）的情况下进行解析：

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

与依赖覆盖类似，`tool.uv.dependency-metadata` 也可用于包的元数据不正确或不完整，或者包在包索引中不可用的情况。虽然依赖覆盖允许全局覆盖包的允许版本，但元数据覆盖允许覆盖*特定包*的声明元数据。

!!! note

    `tool.uv.dependency-metadata` 中的 `version` 字段对于基于注册表的依赖项是可选的（如果省略，uv 将假定元数据适用于该包的所有版本），但对于直接 URL 依赖项（如 Git 依赖项）是*必需*的。

`tool.uv.dependency-metadata` 表中的条目遵循 [元数据 2.3](https://packaging.python.org/en/latest/specifications/core-metadata/) 规范，但 uv 只读取 `name`、`version`、`requires-dist`、`requires-python` 和 `provides-extra`。`version` 字段也被认为是可选的。如果省略，元数据将用于指定包的所有版本。

## 下限

默认情况下，`uv add` 会为依赖项添加下限，并且在使用 uv 管理项目时，如果直接依赖项没有下限，uv 会发出警告。

在“理想情况”下，下限并不重要，但在存在依赖冲突的情况下，它们很重要。例如，考虑一个需要两个包的项目，而这两个包具有冲突的依赖项。解析器需要检查这两个包在约束条件下的所有版本的所有组合——如果所有组合都冲突，则会报告错误，因为依赖项无法满足。如果没有下限，解析器可以（并且通常会）回溯到包的最旧版本。这不仅因为速度慢而有问题，旧版本的包通常无法构建，或者解析器最终可能会选择一个足够旧的版本，它不依赖于冲突的包，但也无法与您的代码一起使用。

在编写库时，下限尤其重要。为您的库所使用的每个依赖项声明最低版本，并验证这些界限是否正确——使用 [`--resolution lowest` 或 `--resolution lowest-direct`](#resolution-strategy) 进行测试，这一点很重要。否则，用户可能会收到一个旧的、不兼容的库依赖项版本，并且库会因意外错误而失败。

## 可复现的解析

uv 支持 `--exclude-newer` 选项，可将解析限制在特定日期之前发布的发行版，从而允许在不考虑新软件包版本的情况下复现安装。日期可以指定为 [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339.html) 时间戳（例如，`2006-12-02T02:07:43Z`）或系统配置时区中的相同格式的本地日期（例如，`2006-12-02`）。

请注意，包索引必须支持 [`PEP 700`](https://peps.python.org/pep-0700/) 中指定的 `upload-time` 字段。如果给定发行版中不存在该字段，则该发行版将被视为不可用。PyPI 为所有包提供 `upload-time`。

为确保可复现性，无法满足的解析消息不会提及由于 `--exclude-newer` 标志而排除了发行版——较新的发行版将被视为不存在。

!!! note

    `--exclude-newer` 选项仅适用于从注册表读取的包（而不是 Git 依赖项等）。此外，在使用 `uv pip` 接口时，除非提供了 `--reinstall` 标志，否则 uv 不会降级以前安装的包，在这种情况下，uv 将执行新的解析。

## 源分发

[PEP 625](https://peps.python.org/pep-0625/) 指定包必须将源分发版作为 gzip tarball (`.tar.gz`) 存档分发。在此规范之前，还允许使用其他存档格式，为了向后兼容，需要支持这些格式。uv 支持读取和提取以下格式的存档：

- gzip tarball (`.tar.gz`, `.tgz`)
- bzip2 tarball (`.tar.bz2`, `.tbz`)
- xz tarball (`.tar.xz`, `.txz`)
- zstd tarball (`.tar.zst`)
- lzip tarball (`.tar.lz`)
- lzma tarball (`.tar.lzma`)
- zip (`.zip`)

## 了解更多

有关解析器内部的更多详细信息，请参阅[解析器参考](../reference/resolver-internals.md)文档。

## 锁文件版本控制

`uv.lock` 文件使用版本化的模式。模式版本包含在锁文件的 `version` 字段中。

任何给定版本的 uv 都可以读取和写入具有相同模式版本的锁文件，但会拒绝具有更高模式版本的锁文件。例如，如果您的 uv 版本支持模式 v1，那么当遇到具有模式 v2 的现有锁文件时，`uv lock` 将会出错。

如果模式更新是向后兼容的，支持模式 v2 的 uv 版本*可能*能够读取具有模式 v1 的锁文件。但是，这并不能保证，如果遇到具有过时模式版本的锁文件，uv 可能会退出并显示错误。

模式版本被视为公共 API 的一部分，因此只在次要版本中作为重大更改进行提升（请参阅[版本控制](../reference/policies/versioning.md)）。因此，可以保证给定次要 uv 版本中的所有 uv 补丁版本都具有完全的锁文件兼容性。换句话说，锁文件只能在次要版本之间被拒绝。
