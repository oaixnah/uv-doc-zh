---
subtitle: Project metadata
---

# 项目元数据

### [`build-constraint-dependencies`](#build-constraint-dependencies) {: #build-constraint-dependencies }

解决构建依赖时应用的约束。

构建约束用于限制在解析或安装期间构建包时选择的构建依赖版本。

将包作为约束包含 _不会_ 在构建期间触发该包的安装；相反，该包必须在项目的构建依赖图中的其他地方被请求。

!!! note

    在 `uv lock`、`uv sync` 和 `uv run` 中，uv 只会从工作空间根目录的 `pyproject.toml` 中读取 `build-constraint-dependencies`，并忽略其他工作空间成员或 `uv.toml` 文件中的任何声明。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
# Ensure that the setuptools v60.0.0 is used whenever a package has a build dependency
# on setuptools.
build-constraint-dependencies = ["setuptools==60.0.0"]
```

---

### [`conflicts`](#conflicts) {: #conflicts }

声明冲突的额外依赖或依赖组集合（即互斥的）。

当两个或多个额外依赖具有相互不兼容的依赖时，声明冲突很有用。例如，额外依赖 `foo` 可能依赖于 `numpy==2.0.0`，而额外依赖 `bar` 依赖于 `numpy==2.1.0`。虽然这些依赖冲突，但用户可能不会同时激活 `foo` 和 `bar`，这使得尽管存在不兼容性，仍可以为项目生成通用解析。

通过明确这些冲突，uv 可以为项目生成通用解析，考虑到某些额外依赖和组的组合是互斥的。作为交换，如果用户尝试激活两个冲突的额外依赖，安装将失败。

**默认值**: `[]`

**类型**: `list[list[dict]]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
# Require that `package[extra1]` and `package[extra2]` are resolved
# in different forks so that they cannot conflict with one another.
conflicts = [
    [
        { extra = "extra1" },
        { extra = "extra2" },
    ]
]

# Require that the dependency groups `group1` and `group2`
# are resolved in different forks so that they cannot conflict
# with one another.
conflicts = [
    [
        { group = "group1" },
        { group = "group2" },
    ]
]
```

---

### [`constraint-dependencies`](#constraint-dependencies) {: #constraint-dependencies }

解析项目依赖时应用的约束。

约束用于限制在解析期间选择的依赖版本。

将包作为约束包含 _不会_ 单独触发该包的安装；相反，该包必须在项目的第一方或传递依赖中的其他地方被请求。

!!! note

    在 `uv lock`、`uv sync` 和 `uv run` 中，uv 只会从工作空间根目录的 `pyproject.toml` 中读取 `constraint-dependencies`，并忽略其他工作空间成员或 `uv.toml` 文件中的任何声明。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
# Ensure that the grpcio version is always less than 1.65, if it's requested by a
# direct or transitive dependency.
constraint-dependencies = ["grpcio<1.65"]
```

---

### [`default-groups`](#default-groups) {: #default-groups }

默认安装的 `dependency-groups` 列表。

也可以是字面量 `"all"` 来默认启用所有组。

**默认值**: `["dev"]`

**类型**: `str | list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
default-groups = ["docs"]
```

---

### [`dependency-groups`](#dependency-groups) {: #dependency-groups }

针对 `dependency-groups` 的附加设置。

目前这只能用于向依赖组添加 `requires-python` 约束（通常用于告知 uv 您的开发工具比实际项目有更高的 Python 要求）。

这不能用于定义依赖组，请使用顶级的 `[dependency-groups]` 表。

**默认值**: `[]`

**类型**: `dict`

**示例用法**:

```toml title="pyproject.toml"

[tool.uv.dependency-groups]
my-group = { requires-python = ">=3.12" }
```

---

### [`dev-dependencies`](#dev-dependencies) {: #dev-dependencies }

项目的开发依赖。

开发依赖将在 `uv run` 和 `uv sync` 中默认安装，但不会出现在项目的发布元数据中。

不再推荐使用此字段。相反，请使用 `dependency-groups.dev` 字段，这是声明开发依赖的标准化方式。`tool.uv.dev-dependencies` 和 `dependency-groups.dev` 的内容会合并以确定 `dev` 依赖组的最终要求。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
dev-dependencies = ["ruff==0.5.0"]
```

---

### [`environments`](#environments) {: #environments }

解析依赖时支持的环境列表。

默认情况下，uv 在 `uv lock` 操作期间会为所有可能的环境进行解析。但是，您可以限制支持的环境集合以提高性能并避免解决方案空间中不可满足的分支。

当使用 `--universal` 标志调用 `uv pip compile` 时，这些环境也会被遵守。

**默认值**: `[]`

**类型**: `str | list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
# Resolve for macOS, but not for Linux or Windows.
environments = ["sys_platform == 'darwin'"]
```

---

### [`index`](#index) {: #index }

解析依赖时使用的索引。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单仓库 API）的仓库，或按相同格式布局的本地目录。

索引按定义顺序考虑，因此第一个定义的索引具有最高优先级。此外，此设置提供的索引比通过 [`index_url`](#index-url) 或 [`extra_index_url`](#extra-index-url) 指定的任何索引具有更高的优先级。除非指定了替代的[索引策略](#index-strategy)，否则 uv 只会考虑包含给定包的第一个索引。

如果索引标记为 `explicit = true`，它将专门用于通过 `[tool.uv.sources]` 明确选择它的依赖，如下所示：

```toml
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu121"
explicit = true

[tool.uv.sources]
torch = { index = "pytorch" }
```

如果索引标记为 `default = true`，它将被移动到优先级列表的末尾，从而在解析包时获得最低优先级。此外，将索引标记为默认将禁用 PyPI 默认索引。

**默认值**: `[]`

**类型**: `dict`

**示例用法**:

```toml title="pyproject.toml"

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu121"
```

---

### [`managed`](#managed) {: #managed }

项目是否由 uv 管理。如果为 `false`，当调用 `uv run` 时，uv 将忽略该项目。

**默认值**: `true`

**类型**: `bool`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
managed = false
```

---

### [`override-dependencies`](#override-dependencies) {: #override-dependencies }

解析项目依赖时应用的覆盖。

覆盖用于强制选择包的特定版本，无论任何其他包请求的版本如何，也无论选择该版本是否通常构成无效解析。

虽然约束是 _累加的_，即它们与组成包的要求相结合，但覆盖是 _绝对的_，即它们完全替换任何组成包的要求。

将包作为覆盖包含 _不会_ 单独触发该包的安装；相反，该包必须在项目的第一方或传递依赖中的其他地方被请求。

!!! note

    在 `uv lock`、`uv sync` 和 `uv run` 中，uv 只会从工作空间根目录的 `pyproject.toml` 中读取 `override-dependencies`，并忽略其他工作空间成员或 `uv.toml` 文件中的任何声明。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
# Always install Werkzeug 2.3.0, regardless of whether transitive dependencies request
# a different version.
override-dependencies = ["werkzeug==2.3.0"]
```

---

### [`package`](#package) {: #package }

项目是否应被视为 Python 包，或非包（"虚拟"）项目。

包会以可编辑模式构建并安装到虚拟环境中，因此需要构建后端，而虚拟项目 _不会_ 被构建或安装；相反，只有它们的依赖会包含在虚拟环境中。

创建包需要在 `pyproject.toml` 中存在 `build-system`，并且项目遵循符合构建后端期望的结构（例如，`src` 布局）。

**默认值**: `true`

**类型**: `bool`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
package = false
```

---

### [`required-environments`](#required-environments) {: #required-environments }

对于缺少源分发的包，所需平台的列表。

当包没有源分发时，其可用性将限制在其构建分发（wheels）支持的平台上。例如，如果包只为 Linux 发布 wheels，那么它将无法在 macOS 或 Windows 上安装。

默认情况下，uv 要求每个包至少包含一个与指定 Python 版本兼容的 wheel。`required-environments` 设置可用于确保生成的解析包含特定平台的 wheels，或者如果没有此类 wheels 可用则失败。

虽然 `environments` 设置 _限制_ 了 uv 在解析依赖时会考虑的环境集合，但 `required-environments` _扩展_ 了 uv 在解析依赖时 _必须_ 支持的平台集合。

例如，`environments = ["sys_platform == 'darwin'"]` 会将 uv 限制为仅为 macOS 求解（并忽略 Linux 和 Windows）。另一方面，`required-environments = ["sys_platform == 'darwin'"]` 会 _要求_ 任何没有源分发的包必须包含 macOS 的 wheel 才能安装。

**默认值**: `[]`

**类型**: `str | list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv]
# Require that the package is available for macOS ARM and x86 (Intel).
required-environments = [
    "sys_platform == 'darwin' and platform_machine == 'arm64'",
    "sys_platform == 'darwin' and platform_machine == 'x86_64'",
]
```

---

### [`sources`](#sources) {: #sources }

解析依赖时使用的源。

`tool.uv.sources` 通过在开发期间合并的附加源来丰富依赖元数据。依赖源可以是 Git 仓库、URL、本地路径或替代注册表。

更多信息请参见[依赖](../concepts/projects/dependencies.md)。

**默认值**: `{}`

**类型**: `dict`

**示例用法**:

```toml title="pyproject.toml"

[tool.uv.sources]
httpx = { git = "https://github.com/encode/httpx", tag = "0.27.0" }
pytest = { url = "https://files.pythonhosted.org/packages/6b/77/7440a06a8ead44c7757a64362dd22df5760f9b12dc5f11b6188cd2fc27a0/pytest-8.3.3-py3-none-any.whl" }
pydantic = { path = "/path/to/pydantic", editable = true }
```

---

### [`build-backend`](#build-backend) {: #build-backend }

uv 构建后端（`uv_build`）的设置。

请注意，这些设置仅在使用 `uv_build` 后端时适用，其他构建后端（如 hatchling）有自己的配置。

所有接受 glob 的选项都使用来自 [PEP 639](https://packaging.python.org/en/latest/specifications/glob-patterns/) 的可移植 glob 模式。

#### [`data`](#build-backend_data) {: #build-backend_data }

<span id="data"></span>

wheels 的数据包含。

每个条目都是一个目录，其内容被复制到 wheel 中的匹配目录 `<name>-<version>.data/(purelib|platlib|headers|scripts|data)`。安装时，此数据会移动到其目标位置，如 <https://docs.python.org/3.12/library/sysconfig.html#installation-paths> 中定义。通常，小数据文件通过将它们放在 Python 模块中而不是使用数据包含来包含。

- `scripts`：安装到可执行文件目录，Unix 上为 `<venv>/bin`，Windows 上为 `<venv>\Scripts`。当激活虚拟环境或使用 `uv run` 时，此目录会添加到 `PATH`，因此此数据类型可用于安装附加二进制文件。对于 Python 入口点，请考虑使用 `project.scripts`。
- `data`：安装到虚拟环境根目录。

  警告：这可能会覆盖现有文件！

- `headers`：安装到包含目录。以此包作为构建要求构建 Python 包的编译器使用包含目录来查找附加头文件。
- `purelib` 和 `platlib`：安装到 `site-packages` 目录。不建议使用这两个选项。

**默认值**: `{}`

**类型**: `dict[str, str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.build-backend]
data = { "headers": "include/headers", "scripts": "bin" }
```

---

#### [`default-excludes`](#build-backend_default-excludes) {: #build-backend_default-excludes }

<span id="default-excludes"></span>

如果设置为 `false`，则不应用默认排除。

默认排除：`__pycache__`、`*.pyc` 和 `*.pyo`。

**默认值**: `true`

**类型**: `bool`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.build-backend]
default-excludes = false
```

---

#### [`module-name`](#build-backend_module-name) {: #build-backend_module-name }

<span id="module-name"></span>

在 `module-root` 内的模块目录名称。

默认模块名称是包名称，其中点和破折号替换为下划线。

包名称需要是有效的 Python 标识符，目录需要包含 `__init__.py`。例外是存根包，其名称以 `-stubs` 结尾，词干是模块名称，并包含 `__init__.pyi` 文件。

对于具有单个模块的命名空间包，路径可以是点分的，例如 `foo.bar` 或 `foo-stubs.bar`。

请注意，使用此选项存在创建两个具有不同名称但相同模块名称的包的风险。一起安装此类包会导致未指定的行为，通常会出现损坏的文件或目录树。

**默认值**: `None`

**类型**: `str`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-name = "sklearn"
```

---

#### [`module-root`](#build-backend_module-root) {: #build-backend_module-root }

<span id="module-root"></span>

包含模块目录的目录。

常见值是 `src`（src 布局，默认）或空路径（平面布局）。

**默认值**: `"src"`

**类型**: `str`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-root = ""
```

---

#### [`namespace`](#build-backend_namespace) {: #build-backend_namespace }

<span id="namespace"></span>

构建命名空间包。

构建 PEP 420 隐式命名空间包，允许多个根 `__init__.py`。

当命名空间包包含多个根 `__init__.py` 时使用此选项，对于具有单个根 `__init__.py` 的命名空间包，请使用点分的 `module-name`。

为了比较点分的 `module-name` 和 `namespace = true`，下面的第一个示例可以用 `module-name = "cloud.database"` 表示：有一个根 `__init__.py` `database`。在第二个示例中，我们有三个根（`cloud.database`、`cloud.database_pro`、`billing.modules.database_pro`），因此需要 `namespace = true`。

```text
src
└── cloud
    └── database
        ├── __init__.py
        ├── query_builder
        │   └── __init__.py
        └── sql
            ├── parser.py
            └── __init__.py
```

```text
src
├── cloud
│   ├── database
│   │   ├── __init__.py
│   │   ├── query_builder
│   │   │   └── __init__.py
│   │   └── sql
│   │       ├── __init__.py
│   │       └── parser.py
│   └── database_pro
│       ├── __init__.py
│       └── query_builder.py
└── billing
    └── modules
        └── database_pro
            ├── __init__.py
            └── sql.py
```

**默认值**: `false`

**类型**: `bool`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.build-backend]
namespace = true
```

---

#### [`source-exclude`](#build-backend_source-exclude) {: #build-backend_source-exclude }

<span id="source-exclude"></span>

从源分发中排除文件和目录的 Glob 表达式。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.build-backend]
source-exclude = ["*.bin"]
```

---

#### [`source-include`](#build-backend_source-include) {: #build-backend_source-include }

<span id="source-include"></span>

在源分发中额外包含文件和目录的 Glob 表达式。

`pyproject.toml` 和模块目录的内容始终包含在内。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.build-backend]
source-include = ["tests/**"]
```

---

#### [`wheel-exclude`](#build-backend_wheel-exclude) {: #build-backend_wheel-exclude }

<span id="wheel-exclude"></span>

从 wheel 中排除文件和目录的 Glob 表达式。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.build-backend]
wheel-exclude = ["*.bin"]
```

---

### `workspace`

#### [`exclude`](#workspace_exclude) {: #workspace_exclude }

<span id="exclude"></span>

要排除为工作空间成员的包。如果包同时匹配 `members` 和 `exclude`，它将被排除。

支持 glob 和显式路径。

有关 glob 语法的更多信息，请参阅 [`glob` 文档](https://docs.rs/glob/latest/glob/struct.Pattern.html)。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.workspace]
exclude = ["member1", "path/to/member2", "libs/*"]
```

---

#### [`members`](#workspace_members) {: #workspace_members }

<span id="members"></span>

要包含为工作空间成员的包。

支持 glob 和显式路径。

有关 glob 语法的更多信息，请参阅 [`glob` 文档](https://docs.rs/glob/latest/glob/struct.Pattern.html)。

**默认值**: `[]`

**类型**: `list[str]`

**示例用法**:

```toml title="pyproject.toml"
[tool.uv.workspace]
members = ["member1", "path/to/member2", "libs/*"]
```

---

