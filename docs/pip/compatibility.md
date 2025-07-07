---
subtitle: Compatibility with pip
---

# 与 `pip` 和 `pip-tools` 的兼容性

uv 被设计为 `pip` 和 `pip-tools` 常见工作流的直接替代品。

通俗地说，其目的是让现有的 `pip` 和 `pip-tools` 用户可以切换到 uv，而无需对其打包工作流进行有意义的更改；而且，在大多数情况下，将 `pip install` 换成 `uv pip install` 应该“就能用”。

然而，uv 并_不_打算成为 `pip` 的_精确_克隆，你越是偏离常见的 `pip` 工作流，就越有可能遇到行为上的差异。在某些情况下，这些差异可能是已知且故意的；在其他情况下，它们可能是实现细节的结果；还有一些情况下，它们可能是错误。

本文档概述了 uv 和 `pip` 之间的已知差异，以及其基本原理、解决方法和未来的兼容性意图声明。

## 配置文件和环境变量

uv 不会读取 `pip` 特有的配置文件或环境变量，如 `pip.conf` 或 `PIP_INDEX_URL`。

读取为其他工具准备的配置文件和环境变量有许多缺点：

1.  它要求与目标工具实现逐个错误的兼容，因为用户最终会依赖于格式、解析器等中的错误。
2.  如果目标工具以某种方式_更改_了格式，uv 就会被锁定，必须以等效的方式进行更改。
3.  如果该配置以某种方式进行了版本控制，uv 就需要知道用户期望使用目标工具的_哪个版本_。
4.  它阻止了 uv 引入目标工具中不存在的任何设置或配置，否则 `pip.conf`（或类似文件）将不再能与 `pip` 一起使用。
5.  这可能会导致用户混淆，因为 uv 会读取实际上不影响其行为的设置，而且许多用户可能_不_期望 uv 读取为其他工具准备的配置文件。

相反，uv 支持自己的环境变量，如 `UV_INDEX_URL`。uv 还支持在 `uv.toml` 文件或 `pyproject.toml` 的 `[tool.uv.pip]` 部分中进行持久化配置。更多信息，请参阅[配置文件](../concepts/configuration-files.md)。

## 预发布版本兼容性

默认情况下，uv 在依赖解析期间会在两种情况下接受预发布版本：

1.  如果包是直接依赖项，并且其版本标记包含预发布说明符（例如 `flask>=2.0.0rc1`）。
2.  如果一个包的_所有_已发布版本都是预发布版本。

如果由于传递性预发布版本导致依赖解析失败，uv 将提示用户使用 `--prerelease allow` 重新运行，以允许所有依赖项使用预发布版本。

或者，您可以将传递性依赖项添加到您的 `requirements.in` 文件中，并附带预发布说明符（例如 `flask>=2.0.0rc1`），以选择对该特定依赖项的预发布支持。

总之，uv 需要预先知道解析器是否应接受给定包的预发布版本。而 `pip` _可能_会尊重传递性依赖项中的预发布标识符，具体取决于解析器遇到相关说明符的顺序 ([#1641](https://github.com/astral-sh/uv/issues/1641#issuecomment-1981402429))。

预发布版本是[众所周知的难以建模](https://pubgrub-rs-guide.netlify.app/limitations/prerelease_versions)，并且是打包工具中错误的常见来源。即使是被视为参考实现的 `pip`，在预发布处理方面也存在许多悬而未决的问题 ([#12469](https://github.com/pypa/pip/issues/12469), [#12470](https://github.com/pypa/pip/issues/12470), [#40505](https://discuss.python.org/t/handling-of-pre-releases-when-backtracking/40505/20) 等)。uv 的预发布处理是_有意_限制的，并_有意_要求用户选择加入预发布，以确保正确性。

未来，uv _可能_会支持传递性依赖项中的预发布标识符。然而，这很可能取决于 Python 打包规范的演变。现有的 PEP [不涵盖“依赖解析”](https://discuss.python.org/t/handling-of-pre-releases-when-backtracking/40505/17)，而是专注于_单个_版本说明符的行为。因此，在更广泛的打包生态系统中，关于预发布的正确和预期行为存在悬而未决的问题。

## 存在于多个索引上的包

在 uv 和 `pip` 中，用户都可以指定多个包索引来搜索给定包的可用版本。然而，uv 和 `pip` 在处理存在于多个索引上的包时有所不同。

例如，假设一家公司在私有索引上发布了一个内部版本的 `requests`（`--extra-index-url`），但同时也允许默认从 PyPI 安装包。在这种情况下，私有的 `requests` 将与 PyPI 上的公共 [`requests`](https://pypi.org/project/requests/) 冲突。

当 uv 在多个索引中搜索一个包时，它会按顺序迭代索引（优先于默认索引的 `--extra-index-url`），并在找到匹配项后立即停止搜索。这意味着如果一个包存在于多个索引上，uv 会将其候选版本限制在包含该包的第一个索引中存在的版本。

而 `pip` 会合并所有索引中的候选版本，并从合并后的集合中选择最佳版本，但它对搜索索引的顺序[不做任何保证](https://github.com/pypa/pip/issues/5045#issuecomment-369521345)，并期望包在名称和版本上是唯一的，即使跨索引也是如此。

uv 的行为是，如果一个包存在于内部索引上，它应该总是从内部索引安装，而绝不从 PyPI 安装。其目的是防止“依赖混淆”攻击，即攻击者在 PyPI 上发布一个与内部包同名的恶意包，从而导致安装恶意包而不是内部包。例如，可以参考 2022 年 12 月的[`torchtriton` 攻击](https://pytorch.org/blog/compromised-nightly-dependency/)。

从 v0.1.39 开始，用户可以通过 `--index-strategy` 命令行选项或 `UV_INDEX_STRATEGY` 环境变量选择加入 `pip` 风格的多索引行为，该变量支持以下值：

- `first-index` (默认): 在所有索引中搜索每个包，将候选版本限制在包含该包的第一个索引中存在的版本，优先于默认索引 URL 的 `--extra-index-url` 索引。
- `unsafe-first-match`: 在所有索引中搜索每个包，但优先选择具有兼容版本的第一个索引，即使其他索引上有更新的版本。
- `unsafe-best-match`: 在所有索引中搜索每个包，并从候选版本的合并集合中选择最佳版本。

虽然 `unsafe-best-match` 最接近 `pip` 的行为，但它使用户面临“依赖混淆”攻击的风险。

uv 还支持将包固定到专用索引（请参阅：[_索引_](../concepts/indexes.md#_3)），以便给定的包_总是_从特定索引安装。

## PEP 517 构建隔离

uv 默认使用 [PEP 517](https://peps.python.org/pep-0517/) 构建隔离（类似于 `pip install --use-pep517`），遵循 `pypa/build` 并预期 `pip` 将来会默认使用 PEP 517 构建 ([pypa/pip#9175](https://github.com/pypa/pip/issues/9175))。

如果由于缺少构建时依赖项而导致包安装失败，请尝试使用该包的较新版本；如果问题仍然存在，请考虑向包维护者提交问题，请求他们更新打包设置以声明正确的 PEP 517 构建时依赖项。

作为一种应急方法，您可以预先安装包的构建依赖项，然后使用 `--no-build-isolation` 运行 `uv pip install`，如下所示：

```shell
uv pip install wheel && uv pip install --no-build-isolation biopython==1.77
```

有关已知在 PEP 517 构建隔离下失败的包列表，请参阅 [#2252](https://github.com/astral-sh/uv/issues/2252)。

## 传递性 URL 依赖

虽然 uv 对 URL 依赖项（例如 `ruff @ https://...`）提供了一流的支持，但它在处理_传递性_ URL 依赖项方面与 pip 有两点不同。

首先，uv 假设非 URL 依赖项不会在解析中引入 URL 依赖项。换句话说，它假设从注册表获取的依赖项本身不依赖于 URL。如果非 URL 依赖项_确实_引入了 URL 依赖项，uv 将在解析期间拒绝该 URL 依赖项。（请注意，PyPI 不允许已发布的包依赖于 URL 依赖项；其他注册表可能更宽松。）

其次，如果使用直接 URL 依赖项定义了约束（`--constraint`）或覆盖（`--override`），并且被约束的包本身具有直接 URL 依赖项，则 uv _可能_会在解析期间拒绝该传递性直接 URL 依赖项，如果该 URL 在输入需求集中的其他地方没有被引用。

如果 uv 拒绝了传递性 URL 依赖项，最好的做法是在相关的 `pyproject.toml` 或 `requirement.in` 文件中将 URL 依赖项作为直接依赖项提供，因为上述约束不适用于直接依赖项。

## 默认使用虚拟环境

`uv pip install` 和 `uv pip sync` 默认设计为与虚拟环境一起工作。

具体来说，uv 将始终将包安装到当前活动的虚拟环境中，或者在当前目录或任何父目录中搜索名为 `.venv` 的虚拟环境（即使它未被激活）。

这与 `pip` 不同，后者在没有活动虚拟环境的情况下会将包安装到全局环境中，并且不会搜索非活动的虚拟环境。

在 uv 中，您可以通过 `--python /path/to/python` 选项提供 Python 可执行文件的路径来安装到非虚拟环境中，或者通过 `--system` 标志，该标志会像 `pip` 一样安装到 `PATH` 上找到的第一个 Python 解释器中。

换句话说，uv 颠倒了默认设置，要求明确选择安装到系统 Python 中，这可能导致损坏和其他复杂情况，并且只应在有限的情况下进行。

更多信息，请参阅[“使用任意 Python 环境”](./environments.md#python_1)。

## 解析策略

对于给定的依赖说明符集，通常没有单一的“正确”包集可供安装。相反，有许多满足说明符的有效包集。

`pip` 和 uv 都不对将要安装的包的_确切_集合做出任何保证；只保证解析将是一致的、确定性的，并符合说明符。因此，在某些情况下，`pip` 和 uv 会产生不同的解析结果；然而，两种解析结果_应该_都是同样有效的。

例如，考虑：

```python title="requirements.in"
starlette
fastapi
```

在撰写本文时，最新的 `starlette` 版本是 `0.37.2`，最新的 `fastapi` 版本是 `0.110.0`。然而，`fastapi==0.110.0` 也依赖于 `starlette`，并引入了一个上限：`starlette>=0.36.3,<0.37.0`。

如果解析器优先考虑包含最新版本的 `starlette`，它将需要使用一个排除了 `starlette` 上限的旧版本 `fastapi`。实际上，这需要回退到 `fastapi==0.1.17`：

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

或者，如果解析器优先考虑包含最新版本的 `fastapi`，它将需要使用一个满足上限的旧版本 `starlette`。实际上，这需要回退到 `starlette==0.36.3`：

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

当 uv 的解析结果与 `pip` 的不同且不理想时，这通常表明说明符过于宽松，用户应考虑收紧它们。例如，在 `starlette` 和 `fastapi` 的情况下，用户可以要求 `fastapi>=0.110.0`。

## `pip check`

目前，`uv pip check` 将显示以下诊断信息：

-   一个包没有 `METADATA` 文件，或者 `METADATA` 文件无法解析。
-   一个包的 `Requires-Python` 与正在运行的解释器的 Python 版本不匹配。
-   一个包依赖于一个未安装的包。
-   一个包依赖于一个已安装但版本不兼容的包。
-   虚拟环境中安装了多个版本的包。

在某些情况下，`uv pip check` 会显示 `pip check` 不会显示的诊断信息，反之亦然。例如，与 `uv pip check` 不同，`pip check` 在当前环境中安装了多个版本的包时_不会_发出警告。

## `--user` 和 `user` 安装方案

uv 不支持 `--user` 标志，该标志根据 `user` 安装方案安装包。相反，我们建议使用虚拟环境来隔离包安装。

此外，如果 pip 检测到用户对目标目录没有写权限，它将回退到 `user` 安装方案，就像在某些系统上安装到系统 Python 中时一样。uv 不实现任何此类回退。

更多信息，请参阅 [#2077](https://github.com/astral-sh/uv/issues/2077)。

## `--only-binary` 强制执行

`--only-binary` 参数用于将安装限制为预构建的二进制发行版。当提供 `--only-binary :all:` 时，pip 和 uv 都会拒绝从 PyPI 和其他注册表构建源发行版。

然而，当依赖项作为直接 URL 提供时（例如 `uv pip install https://...`），pip _不_强制执行 `--only-binary`，并将为所有此类包构建源发行版。

而 uv _确实_对直接 URL 依赖项强制执行 `--only-binary`，但有一个例外：给定 `uv pip install https://... --only-binary flask`，如果 uv 无法提前推断包名，它_将_在给定 URL 处构建源发行版，因为在这种情况下，uv 无法在不构建其元数据的情况下确定该包是否“被允许”。

pip 和 uv 都允许即使在提供 `--only-binary` 的情况下构建和安装可编辑的需求。例如，`uv pip install -e . --only-binary :all:` 是允许的。

## `--no-binary` 强制执行

`--no-binary` 参数用于将安装限制为源发行版。当提供 `--no-binary` 时，uv 将拒绝安装预构建的二进制发行版，但_将_重用本地缓存中已存在的任何二进制发行版。

此外，与 pip 相反，当提供 `--no-binary` 时，uv 的解析器仍将从预构建的二进制发行版中读取元数据。

## `manylinux_compatible` 强制执行

[PEP 600](https://peps.python.org/pep-0600/#package-installers) 描述了一种机制，Python 发行商可以通过在 `_manylinux` 标准库模块上定义 `manylinux_compatible` 函数来选择退出 `manylinux` 兼容性。

uv 尊重 `manylinux_compatible`，但仅针对当前的 glibc 版本进行测试，并全局应用 `manylinux_compatible` 的返回值。

换句话说，如果 `manylinux_compatible` 返回 `True`，uv 将视系统为 `manylinux` 兼容；如果返回 `False`，uv 将视系统为 `manylinux` 不兼容，而不会为每个 glibc 版本调用 `manylinux_compatible`。

这种方法不是规范的完整实现，但与常见的 blanket `manylinux_compatible` 实现兼容，例如 [`no-manylinux`](https://pypi.org/project/no-manylinux/)：

```python
from __future__ import annotations
manylinux1_compatible = False
manylinux2010_compatible = False
manylinux2014_compatible = False


def manylinux_compatible(*_, **__):  # PEP 600
    return False
```

## 字节码编译

与 `pip` 不同，uv 在安装期间默认不将 `.py` 文件编译为 `.pyc` 文件（即，uv 不创建或填充 `__pycache__` 目录）。要在安装期间启用字节码编译，请将 `--compile-bytecode` 标志传递给 `uv pip install` 或 `uv pip sync`，或将 `UV_COMPILE_BYTECODE` 环境变量设置为 `1`。

跳过字节码编译在某些工作流中可能是不希望的；例如，我们建议在 [Docker 构建](../guides/integration/docker.md) 中启用字节码编译以提高启动时间（以增加构建时间为代价）。

由于字节码编译会抑制 Python 解释器发出的各种警告，在极少数情况下，当运行使用 uv 安装的 Python 代码时，您可能会看到 `SyntaxWarning` 或 `DeprecationWarning` 消息，而使用 `pip` 时则不会出现。这些是有效的警告，但通常被字节码编译过程隐藏，可以忽略、在上游修复，或通过在 uv 中启用字节码编译来类似地抑制。

## 严格性和规范强制执行

uv 倾向于比 `pip` 更严格，并且通常会拒绝 `pip` 会安装的包。例如，uv 会拒绝带有无效 URL 片段的 HTML 索引（请参阅：[PEP 503](https://peps.python.org/pep-0503/)），而 `pip` 会忽略此类片段。

在某些情况下，uv 会为已知存在特定规范合规性问题的流行包实现宽松的行为。

如果 uv 由于规范违规而拒绝了 `pip` 会安装的包，最好的做法是首先尝试安装该包的较新版本；如果失败，则向包维护者报告问题。

## `pip` 命令行选项和子命令

uv 不支持 `pip` 的完整命令行选项和子命令集，尽管它确实支持一个很大的子集。

缺失的选项和子命令根据用户需求和实现复杂性进行优先级排序，并且通常在单个问题中进行跟踪。例如：

- [`--trusted-host`](https://github.com/astral-sh/uv/issues/1339)
- [`--user`](https://github.com/astral-sh/uv/issues/2077)

如果您遇到缺失的选项或子命令，请搜索问题跟踪器以查看是否已报告，如果没有，请考虑开设一个新问题。欢迎对任何现有问题进行投票以表达您的兴趣。

## 注册表身份验证

uv 不支持 `pip` 的 `--keyring-provider` 的 `auto` 或 `import` 选项。目前，仅支持 `subprocess` 选项。

与 `pip` 不同，uv 默认不启用密钥环身份验证。

与 `pip` 不同，uv 不会等到请求返回 HTTP 401 后才搜索身份验证。uv 会将身份验证附加到所有具有可用凭据的主机的请求中。

## `egg` 支持

uv 不支持在 `pip` 中被认为是遗留或已弃用的功能。例如，uv 不支持 `.egg` 风格的发行版。

然而，uv 对 (1) `.egg-info` 风格的发行版（偶尔在 Docker 镜像和 Conda 环境中找到）和 (2) 遗留的可编辑 `.egg-link` 风格的发行版有部分支持。

具体来说，uv 不支持安装新的 `.egg-info` 或 `.egg-link` 风格的发行版，但在解析期间会尊重任何此类现有发行版，使用 `uv pip list` 和 `uv pip freeze` 列出它们，并使用 `uv pip uninstall` 卸载它们。
