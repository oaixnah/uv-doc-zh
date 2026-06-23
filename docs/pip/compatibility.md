---
subtitle: Compatibility with pip
description: 本文档详细介绍了 uv 与 pip 和 pip-tools 的兼容性差异，涵盖配置文件、预发布版本、多索引包解析、PEP 517 构建隔离、虚拟环境默认行为、解析策略、字节码编译、严格性规范执行等已知差异，以及相应的解决方法和未来兼容性声明。
---

# 与 `pip` 和 `pip-tools` 的兼容性 {#compatibility-with-pip-and-pip-tools}

uv 被设计为常见 `pip` 和 `pip-tools` 工作流的直接替代品（drop-in replacement）。

粗略来说，其目标是让现有 `pip` 和 `pip-tools` 用户无需对其打包工作流进行重大更改即可切换到 uv；在大多数情况下，将 `pip install` 替换为 `uv pip install` 应该"开箱即用"。

然而，uv _并非_ 旨在成为 `pip` 的_精确_克隆，你越偏离常见的 `pip` 工作流，就越可能遇到行为差异。在某些情况下，这些差异可能是已知且有意的；在其他情况下，它们可能是实现细节导致的结果；还有一些情况则可能是 bug。

本文档概述了 uv 与 `pip` 之间的已知差异，包括原因、解决方法以及未来兼容性意向声明。

## 配置文件和环境变量 {#configuration-files-and-environment-variables}

uv 不会读取特定于 `pip` 的配置文件或环境变量，例如 `pip.conf` 或 `PIP_INDEX_URL`。

读取为其他工具设计的配置文件和环境变量存在若干缺点：

1. 需要与目标工具实现逐 bug 兼容（bug-for-bug compatibility），因为用户最终会依赖格式、解析器等方面的 bug。
2. 如果目标工具以某种方式_更改_了格式，uv 就会被迫以等效方式更改。
3. 如果该配置以某种方式进行了版本控制，uv 就需要知道用户期望使用目标工具的_哪个版本_。
4. 这会阻止 uv 引入目标工具中不存在的任何设置或配置，否则 `pip.conf`（或类似文件）将不再能用于 `pip`。
5. 这可能导致用户困惑，因为 uv 会读取实际上不影响其行为的设置，而许多用户可能_不_期望 uv 读取为其他工具设计的配置文件。

相反，uv 支持自己的环境变量，例如 `UV_INDEX_URL`。uv 还支持在 `uv.toml` 文件或 `pyproject.toml` 的 `[tool.uv.pip]` 部分中进行持久化配置。更多信息请参阅[配置文件](../concepts/configuration-files.md)。

## 预发布版本兼容性 {#pre-release-compatibility}

默认情况下，uv 在两种情况下会在依赖解析期间接受预发布版本（pre-release）：

1. 如果包是直接依赖，且其版本标记包含预发布版本说明符（例如 `flask>=2.0.0rc1`）。
2. 如果包的_所有_已发布版本都是预发布版本。

如果依赖解析因传递预发布版本而失败，uv 会提示用户使用 `--prerelease allow` 重新运行，以允许所有依赖的预发布版本。

或者，你也可以将传递依赖添加到 `requirements.in` 文件中，并附带预发布版本说明符（例如 `flask>=2.0.0rc1`），以选择为该特定依赖启用预发布版本支持。

总而言之，uv 需要预先知道解析器是否应该为给定包接受预发布版本。而 `pip` 则会尊重传递依赖中的预发布标识符，并在没有稳定版本匹配依赖要求时允许传递依赖的预发布版本。

!!! note

    在 pip 26.0 之前，此行为并不一致。

预发布版本[众所周知地难以建模](https://pubgrub-rs-guide.netlify.app/limitations/prerelease_versions)，并且是打包工具中常见的 bug 来源。uv 的预发布版本处理是_有意_受限的，并且_有意_要求用户主动选择加入预发布版本，以确保正确性。

未来，uv _可能_会支持传递依赖中的预发布标识符。然而，这很可能取决于 Python 打包规范的演进。现有的 PEP [并未涵盖"依赖解析"](https://discuss.python.org/t/handling-of-pre-releases-when-backtracking/40505/17)，而是专注于_单个_版本说明符的行为。

## 存在于多个索引上的包 {#packages-that-exist-on-multiple-indexes}

在 uv 和 `pip` 中，用户都可以指定多个包索引来搜索给定包的可用版本。然而，uv 和 `pip` 在处理存在于多个索引上的包时有所不同。

例如，假设一家公司在私有索引（`--extra-index-url`）上发布了内部版本的 `requests`，但也允许默认从 PyPI 安装包。在这种情况下，私有的 `requests` 将与 PyPI 上的公共 [`requests`](https://pypi.org/project/requests/) 发生冲突。

当 uv 在多个索引中搜索包时，它会按顺序遍历索引（优先使用 `--extra-index-url` 而非默认索引），并在找到匹配项后立即停止搜索。这意味着如果包存在于多个索引上，uv 会将其候选版本限制为第一个包含该包的索引中的版本。

而 `pip` 会合并所有索引的候选版本，并从合并后的集合中选择最佳版本，尽管它对[搜索索引的顺序不做任何保证](https://github.com/pypa/pip/issues/5045#issuecomment-369521345)，并期望包在名称和版本上唯一，即使跨索引也是如此。

uv 的行为是这样的：如果包存在于内部索引上，它应该始终从内部索引安装，而绝不会从 PyPI 安装。其目的是防止"依赖混淆"（dependency confusion）攻击，即攻击者在 PyPI 上发布与内部包同名的恶意包，从而导致安装恶意包而非内部包。例如，参见 2022 年 12 月的[`torchtriton` 攻击事件](https://pytorch.org/blog/compromised-nightly-dependency/)。

从 v0.1.39 开始，用户可以通过 `--index-strategy` 命令行选项或 `UV_INDEX_STRATEGY` 环境变量选择加入 `pip` 风格的多索引行为，支持以下值：

- `first-index`（默认）：在所有索引中搜索每个包，将候选版本限制为第一个包含该包的索引中的版本，优先使用 `--extra-index-url` 索引而非默认索引 URL。
- `unsafe-first-match`：在所有索引中搜索每个包，但优先选择第一个具有兼容版本的索引，即使其他索引上有更新的版本。
- `unsafe-best-match`：在所有索引中搜索每个包，并从合并的候选版本集合中选择最佳版本。

虽然 `unsafe-best-match` 最接近 `pip` 的行为，但它会使用户面临"依赖混淆"攻击的风险。

uv 还支持将包固定到专用索引（参见：[_索引_](../concepts/indexes.md#pinning-a-package-to-an-index)），使得给定包_始终_从特定索引安装。

## PEP 517 构建隔离 {#pep-517-build-isolation}

uv 默认使用 [PEP 517](https://peps.python.org/pep-0517/) 构建隔离（类似于 `pip install --use-pep517`），遵循 `pypa/build` 的做法，并预期 `pip` 未来会默认使用 PEP 517 构建（[pypa/pip#9175](https://github.com/pypa/pip/issues/9175)）。

如果包因缺少构建时依赖而安装失败，请尝试使用较新版本的包；如果问题持续存在，请考虑向包维护者提交 issue，请求他们更新打包设置以声明正确的 PEP 517 构建时依赖。

作为一种应急方案，你可以预装包的构建依赖，然后使用 `--no-build-isolation` 运行 `uv pip install`，例如：

```shell
uv pip install wheel && uv pip install --no-build-isolation biopython==1.77
```

有关已知在 PEP 517 构建隔离下失败的包列表，请参阅 [#2252](https://github.com/astral-sh/uv/issues/2252)。

## 传递式 URL 依赖 {#transitive-url-dependencies}

虽然 uv 包含对 URL 依赖（例如 `ruff @ https://...`）的一流支持，但在处理_传递式_ URL 依赖时与 pip 有两个不同之处。

首先，uv 假设非 URL 依赖不会将 URL 依赖引入解析过程。换句话说，它假设从注册中心获取的依赖本身不依赖于 URL。如果非 URL 依赖_确实_引入了 URL 依赖，uv 将在解析过程中拒绝该 URL 依赖。（请注意，PyPI 不允许已发布的包依赖 URL 依赖；其他注册中心可能更宽松。）

其次，如果使用直接 URL 依赖定义约束（`--constraint`）或覆盖（`--override`），并且被约束的包有自己的直接 URL 依赖，uv _可能_会在解析过程中拒绝该传递式直接 URL 依赖，前提是该 URL 未在输入需求集合的其他地方被引用。

如果 uv 拒绝了传递式 URL 依赖，最佳做法是将该 URL 依赖作为直接依赖提供在相关的 `pyproject.toml` 或 `requirement.in` 文件中，因为上述约束不适用于直接依赖。

## 默认使用虚拟环境 {#virtual-environments-by-default}

`uv pip install` 和 `uv pip sync` 默认设计为与虚拟环境配合使用。

具体来说，uv 始终将包安装到当前激活的虚拟环境中，或者搜索当前目录或任何父目录中名为 `.venv` 的虚拟环境（即使它未被激活）。

这与 `pip` 不同，`pip` 在没有激活虚拟环境时会安装到全局环境中，并且不会搜索未激活的虚拟环境。

在 uv 中，你可以通过 `--python /path/to/python` 选项提供 Python 可执行文件的路径，或通过 `--system` 标志安装到非虚拟环境中，`--system` 标志会安装到 `PATH` 中找到的第一个 Python 解释器中，类似于 `pip`。

换句话说，uv 颠倒了默认行为，需要明确选择加入才能安装到系统 Python 中，这可能导致损坏和其他复杂问题，应仅在有限情况下使用。

更多信息请参阅["使用任意 Python 环境"](./environments.md#using-arbitrary-python-environments)。

## 解析策略 {#resolution-strategy}

对于给定的一组依赖说明符，通常不存在单一的"正确"包集合可供安装。相反，存在许多满足说明符的有效包集合。

`pip` 和 uv 都不保证安装的包集合_精确_一致；只保证解析结果是一致的、确定性的，并且符合说明符的要求。因此，在某些情况下，`pip` 和 uv 会产生不同的解析结果；然而，两种解析结果_应该_都是同等有效的。

例如，考虑以下情形：

```python title="requirements.in"
starlette
fastapi
```

在撰写本文时，最新的 `starlette` 版本是 `0.37.2`，最新的 `fastapi` 版本是 `0.110.0`。然而，`fastapi==0.110.0` 也依赖 `starlette`，并引入了上限：`starlette>=0.36.3,<0.37.0`。

如果解析器优先包含最新版本的 `starlette`，则需要使用排除了 `starlette` 上限的旧版本 `fastapi`。在实践中，这需要回退到 `fastapi==0.1.17`：

```python title="requirements.txt"
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in
annotated-types==0.6.0
    # via pydantic
anyio==4.3.0
    # via starlette
fastapi==0.1.17
idna==3.6
    # via anyio
pydantic==2.6.3
    # via fastapi
pydantic-core==2.16.3
    # via pydantic
sniffio==1.3.1
    # via anyio
starlette==0.37.2
    # via fastapi
typing-extensions==4.10.0
    # via
    #   pydantic
    #   pydantic-core
```

或者，如果解析器优先包含最新版本的 `fastapi`，则需要使用满足上限的旧版本 `starlette`。在实践中，这需要回退到 `starlette==0.36.3`：

```python title="requirements.txt"
# This file was autogenerated by uv via the following command:
#    uv pip compile requirements.in
annotated-types==0.6.0
    # via pydantic
anyio==4.3.0
    # via starlette
fastapi==0.110.0
idna==3.6
    # via anyio
pydantic==2.6.3
    # via fastapi
pydantic-core==2.16.3
    # via pydantic
sniffio==1.3.1
    # via anyio
starlette==0.36.3
    # via fastapi
typing-extensions==4.10.0
    # via
    #   fastapi
    #   pydantic
    #   pydantic-core
```

当 uv 的解析结果与 `pip` 存在不理想的差异时，通常表明说明符过于宽松，用户应考虑收紧它们。例如，在 `starlette` 和 `fastapi` 的例子中，用户可以要求 `fastapi>=0.110.0`。

## `pip check` {#pip-check}

目前，`uv pip check` 会报告以下诊断信息：

- 包没有 `METADATA` 文件，或 `METADATA` 文件无法解析。
- 包的 `Requires-Python` 与运行中解释器的 Python 版本不匹配。
- 包依赖了未安装的包。
- 包依赖了已安装但版本不兼容的包。
- 虚拟环境中安装了多个版本的同一个包。

在某些情况下，`uv pip check` 会报告 `pip check` 不会报告的诊断信息，反之亦然。例如，与 `uv pip check` 不同，`pip check` _不会_在当前环境中安装了多个版本的同一个包时发出警告。

## `--user` 和 `user` 安装方案 {#user-and-the-user-install-scheme}

uv 不支持 `--user` 标志，该标志基于 `user` 安装方案安装包。我们建议使用虚拟环境来隔离包的安装。

此外，当 pip 检测到用户没有目标目录的写入权限时（例如在某些系统上安装到系统 Python 中时），会回退到 `user` 安装方案。uv 不会实现任何此类回退。

更多信息请参阅 [#2077](https://github.com/astral-sh/uv/issues/2077)。

## `--only-binary` 强制执行 {#only-binary-enforcement}

`--only-binary` 参数用于将安装限制为预编译的二进制发行版。当提供 `--only-binary :all:` 时，pip 和 uv 都会拒绝从 PyPI 和其他注册中心构建源代码发行版。

然而，当依赖以直接 URL 形式提供时（例如 `uv pip install https://...`），pip _不会_强制执行 `--only-binary`，并且会为此类所有包构建源代码发行版。

而 uv _会_对直接 URL 依赖强制执行 `--only-binary`，但有一个例外：对于 `uv pip install https://... --only-binary flask`，如果 uv 无法提前推断包名，它_会_构建给定 URL 的源代码发行版，因为在这种情况下，uv 无法在不构建其元数据的情况下确定该包是否被"允许"。

pip 和 uv 都允许在提供 `--only-binary` 时构建和安装可编辑（editable）需求。例如，`uv pip install -e . --only-binary :all:` 是允许的。

## `--no-binary` 强制执行 {#no-binary-enforcement}

`--no-binary` 参数用于将安装限制为源代码发行版。当提供 `--no-binary` 时，uv 会拒绝安装预编译的二进制发行版，但_会_重用本地缓存中已存在的任何二进制发行版。

此外，与 pip 不同，当提供 `--no-binary` 时，uv 的解析器仍会从预编译的二进制发行版中读取元数据。

## `manylinux_compatible` 强制执行 {#manylinux_compatible-enforcement}

[PEP 600](https://peps.python.org/pep-0600/#package-installers) 描述了一种机制，Python 发行商可以通过在 `_manylinux` 标准库模块上定义 `manylinux_compatible` 函数来选择退出 `manylinux` 兼容性。

uv 尊重 `manylinux_compatible`，但仅针对当前 glibc 版本进行测试，并全局应用 `manylinux_compatible` 的返回值。

换句话说，如果 `manylinux_compatible` 返回 `True`，uv 会将系统视为 `manylinux` 兼容；如果返回 `False`，uv 会将系统视为 `manylinux` 不兼容，而不会为每个 glibc 版本调用 `manylinux_compatible`。

这种方法并非规范的完整实现，但与常见的通用 `manylinux_compatible` 实现兼容，例如 [`no-manylinux`](https://pypi.org/project/no-manylinux/)：

```python
from __future__ import annotations
manylinux1_compatible = False
manylinux2010_compatible = False
manylinux2014_compatible = False


def manylinux_compatible(*_, **__):  # PEP 600
    return False
```

## 字节码编译 {#bytecode-compilation}

与 `pip` 不同，uv 默认在安装期间不会将 `.py` 文件编译为 `.pyc` 文件（即，uv 不会创建或填充 `__pycache__` 目录）。要在安装期间启用字节码编译，请将 `--compile-bytecode` 标志传递给 `uv pip install` 或 `uv pip sync`，或将 `UV_COMPILE_BYTECODE` 环境变量设置为 `1`。

跳过字节码编译在某些工作流中可能是不理想的；例如，我们建议在 [Docker 构建](../guides/integration/docker.md)中启用字节码编译，以缩短启动时间（代价是增加构建时间）。

由于字节码编译会抑制 Python 解释器发出的各种警告，在极少数情况下，你可能会在运行使用 uv 安装的 Python 代码时看到 `SyntaxWarning` 或 `DeprecationWarning` 消息，而这些消息在使用 `pip` 时不会出现。这些是有效的警告，但通常被字节码编译过程隐藏，可以选择忽略、在上游修复，或通过在 uv 中启用字节码编译来同样抑制。

## 严格性和规范执行 {#strictness-and-spec-enforcement}

uv 往往比 `pip` 更严格，通常会拒绝 `pip` 会安装的包。例如，uv 拒绝 URL 片段无效的 HTML 索引（参见：[PEP 503](https://peps.python.org/pep-0503/)），而 `pip` 会忽略此类片段。

在某些情况下，uv 会对已知存在特定规范合规问题的流行包实施宽松行为。

如果 uv 因规范违规而拒绝了 `pip` 会安装的包，最佳做法是首先尝试安装较新版本的包；如果失败，则向包维护者报告该问题。

## `pip` 命令行选项和子命令 {#pip-command-line-options-and-subcommands}

uv 不支持 `pip` 的完整命令行选项和子命令集，尽管它确实支持其中很大一部分。

缺失的选项和子命令根据用户需求和实现复杂度进行优先级排序，通常会在单独的 issue 中跟踪。例如：

- [`--trusted-host`](https://github.com/astral-sh/uv/issues/1339)
- [`--user`](https://github.com/astral-sh/uv/issues/2077)

如果你遇到缺失的选项或子命令，请搜索 issue 跟踪器以查看是否已被报告，如果没有，请考虑提交新的 issue。欢迎对现有 issue 点赞以表达你的关注。

## 注册中心认证 {#registry-authentication}

uv 不支持 `pip` 的 `--keyring-provider` 的 `auto` 或 `import` 选项。目前仅支持 `subprocess` 选项。

与 `pip` 不同，uv 默认不启用 keyring 认证。

与 `pip` 不同，uv 不会等待请求返回 HTTP 401 后才搜索认证信息。uv 会为所有有可用凭据的主机的请求附加认证信息。

## `egg` 支持 {#egg-support}

uv 不支持 `pip` 中被视为遗留或已弃用的功能。例如，uv 不支持 `.egg` 风格的发行版。

然而，uv 对以下内容有部分支持：(1) `.egg-info` 风格的发行版（偶尔出现在 Docker 镜像和 Conda 环境中）和 (2) 遗留的可编辑 `.egg-link` 风格发行版。

具体来说，uv 不支持安装新的 `.egg-info` 或 `.egg-link` 风格的发行版，但在解析期间会尊重任何此类现有发行版，使用 `uv pip list` 和 `uv pip freeze` 列出它们，并使用 `uv pip uninstall` 卸载它们。

## 构建约束 {#build-constraints}

当通过 `--constraint`（或 `UV_CONSTRAINT`）提供约束时，uv _不会_在解析构建依赖时应用这些约束（即构建源代码发行版时）。相反，构建约束应通过专用的 `--build-constraint`（或 `UV_BUILD_CONSTRAINT`）设置来提供。

而 pip 在通过 `PIP_CONSTRAINT` 指定时会将约束应用于构建依赖，但在通过命令行 `--constraint` 提供时则不会。

例如，要确保使用 `setuptools 60.0.0` 来构建任何构建依赖中包含 `setuptools` 的包，请使用 `--build-constraint`，而不是 `--constraint`。

## `pip compile` 默认值 {#pip-compile-defaults}

`pip compile` 和 `pip-tools` 的默认行为之间存在一些微小但值得注意的差异。

默认情况下，uv 不会将编译后的需求写入输出文件。相反，uv 要求用户通过 `-o` 或 `--output-file` 选项明确指定输出文件。

默认情况下，uv 在输出编译后的需求时会去除 extras（附加功能）。换句话说，uv 默认使用 `--strip-extras`，而 `pip-compile` 默认使用 `--no-strip-extras`。`pip-compile` 计划在下一个主要版本（v8.0.0）中更改此默认值，届时两个工具都将默认使用 `--strip-extras`。要在 uv 中保留 extras，请将 `--no-strip-extras` 标志传递给 `uv pip compile`。

默认情况下，uv 不会将任何索引 URL 写入输出文件，而 `pip-compile` 会输出任何与默认值（PyPI）不匹配的 `--index-url` 或 `--extra-index-url`。要在输出文件中包含索引 URL，请将 `--emit-index-url` 标志传递给 `uv pip compile`。与 `pip-compile` 不同，uv 在传递 `--emit-index-url` 时会包含所有索引 URL，包括默认索引 URL。

## `requires-python` 上限 {#requires-python-upper-bounds}

在评估依赖的 `requires-python` 范围时，uv 只考虑下限，完全忽略上限。例如，`>=3.8, <4` 被视为 `>=3.8`。尊重 `requires-python` 的上限通常会导致形式上正确但实际不正确的解析结果，因为解析器会回退到第一个省略了上限的已发布版本（参见：[`Requires-Python` 上限](https://discuss.python.org/t/requires-python-upper-limits/12663)）。

## `requires-python` 说明符 {#requires-python-specifiers}

在根据 `requires-python` 说明符评估 Python 版本时，uv 会将候选版本截断为主要、次要和补丁组件，忽略（例如）预发布和后发布标识符。

例如，声明 `requires-python: >=3.13` 的项目将接受 Python 3.13.0b1。虽然 3.13.0b1 严格来说不大于 3.13，但省略预发布标识符后，它确实大于 3.13。

虽然这并不严格符合 [PEP 440](https://peps.python.org/pep-0440/)，但它_与_ [pip](https://github.com/pypa/pip/blob/24.1.1/src/pip/_internal/resolution/resolvelib/candidates.py#L540) 一致。

## 包优先级 {#package-priority}

给定一组需求，通常存在多种可能的解决方案，解析器必须在它们之间做出选择。uv 的解析器和 pip 的解析器具有不同的包优先级集合。虽然两个解析器都使用用户提供的顺序作为优先级之一，但 pip 具有 uv 所没有的额外[优先级](https://pip.pypa.io/en/stable/topics/more-dependency-resolution/#the-resolver-algorithm)。因此，uv 比 pip 更容易受到用户顺序变化的影响。

例如，`uv pip install foo bar` 优先考虑 `foo` 的较新版本而非 `bar`，可能导致与 `uv pip install bar foo` 不同的解析结果。同样，此行为也适用于 `uv pip compile` 输入文件中需求的排序。

## Wheel 文件名和元数据验证 {#wheel-filename-and-metadata-validation}

默认情况下，uv 会拒绝文件名与文件内 wheel 元数据不一致的 wheel。例如，一个名为 `foo-1.0.0-py3-none-any.whl` 的 wheel，其元数据指示版本为 `1.0.1`，将被 uv 拒绝，但被 pip 接受。

要强制 uv 接受此类 wheel，请在环境中设置 `UV_SKIP_WHEEL_FILENAME_CHECK=1`。

## 包名规范化 {#package-name-normalization}

默认情况下，uv 将包名规范化为其 [PEP 503 兼容形式](https://packaging.python.org/en/latest/specifications/name-normalization/#name-normalization)，并在所有输出上下文中使用这些规范化名称。这与 pip 不同，pip 倾向于保留注册中心上发布的逐字包名。

例如，`uv pip list` 显示规范化的包名（例如 `docstring-parser`），而 `pip list` 显示非规范化的包名（例如 `docstring_parser`）：

```shell
(venv) $ diff --side-by-side  <(pip list) <(uv pip list)
Package          Version					Package          Version
---------------- -------					---------------- -------
docstring_parser 0.16					      |	docstring-parser 0.16
jaraco.classes   3.4.0					      |	jaraco-classes   3.4.0
more-itertools   10.7.0				    		more-itertools   10.7.0
pip              25.1					    	pip              25.1
PyMuPDFb         1.24.10				      |	pymupdfb         1.24.10
PyPDF2           3.0.1					      |	pypdf2           3.0.1
```
