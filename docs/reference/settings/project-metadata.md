---
subtitle: Project metadata
description: uv 项目元数据配置参考文档，涵盖 build-constraint-dependencies、conflicts、constraint-dependencies、default-groups、dev-dependencies、environments、exclude-dependencies、index、managed、override-dependencies、package、required-environments、sources、build-backend 及 workspace 等全部项目级设置项的详细说明、默认值、类型和示例用法。
---

# 项目元数据

## [`build-constraint-dependencies`](#build-constraint-dependencies) {: #build-constraint-dependencies }

在解析构建依赖时应用的约束条件。

构建约束用于限制在解析或安装过程中构建包时所选构建依赖的版本。

将某个包纳入约束条件 _不会_ 在构建过程中触发该包的安装；相反，该包必须在项目的构建依赖关系图中的其他位置被请求。

!!! note

    在 `uv lock`、`uv sync` 和 `uv run` 中，uv 只会从工作空间根目录的 `pyproject.toml` 中读取 `build-constraint-dependencies`，并会忽略其他工作空间成员或 `uv.toml` 文件中的任何声明。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
# 确保每当某个包对 setuptools 有构建依赖时，都使用 setuptools v60.0.0。
build-constraint-dependencies = ["setuptools==60.0.0"]
```

---

## [`conflicts`](#conflicts) {: #conflicts }

声明相互冲突（即互斥）的 extras 或依赖组集合。

当两个或多个 extras 具有互不兼容的依赖时，声明冲突非常有用。例如，extra `foo` 可能依赖 `numpy==2.0.0`，而 extra `bar` 依赖 `numpy==2.1.0`。虽然这些依赖相互冲突，但用户可能不会同时激活 `foo` 和 `bar`，因此尽管存在不兼容性，仍然可以为项目生成通用解析方案。

通过显式声明此类冲突，uv 可以为项目生成通用解析方案，同时考虑到某些 extras 和组组合是互斥的。作为交换，如果用户尝试同时激活两个冲突的 extras，安装将会失败。

**默认值**：`[]`

**类型**：`list[list[dict]]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
# 要求 `package[extra1]` 和 `package[extra2]` 在不同的 fork 中解析，
# 以便它们不会相互冲突。
conflicts = [
    [
        { extra = "extra1" },
        { extra = "extra2" },
    ]
]

# 要求依赖组 `group1` 和 `group2` 在不同的 fork 中解析，
# 以便它们不会相互冲突。
conflicts = [
    [
        { group = "group1" },
        { group = "group2" },
    ]
]
```

---

## [`constraint-dependencies`](#constraint-dependencies) {: #constraint-dependencies }

在解析项目依赖时应用的约束条件。

约束用于限制解析过程中所选依赖的版本。

将某个包纳入约束条件 _不会_ 触发该包自身的安装；相反，该包必须在项目的一手依赖或传递依赖中的其他位置被请求。

!!! note
    在 `uv lock`、`uv sync` 和 `uv run` 中，uv 只会从工作空间根目录的 `pyproject.toml` 中读取 `constraint-dependencies`，并会忽略其他工作空间成员或 `uv.toml` 文件中的任何声明。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
# 确保 grpcio 版本始终小于 1.65（如果它被直接或传递依赖请求）。
constraint-dependencies = ["grpcio<1.65"]
```

---

## [`default-groups`](#default-groups) {: #default-groups }

默认安装的 `dependency-groups` 列表。

也可以使用字面值 `"all"` 来默认启用所有组。

**默认值**：`["dev"]`

**类型**：`str | list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
default-groups = ["docs"]
```

---

### [`dependency-groups`](#dependency-groups) {: #dependency-groups }

`dependency-groups` 的附加设置。

目前只能用于为依赖组添加 `requires-python` 约束（通常用于告知 uv 你的开发工具对 Python 版本的要求高于实际项目）。

此设置不能用于定义依赖组，请使用顶层的 `[dependency-groups]` 表来定义。

**默认值**：`[]`

**类型**：`dict`

**示例用法**：

```toml title="pyproject.toml"

[tool.uv.dependency-groups]
my-group = {requires-python = ">=3.12"}
```

---

## [`dev-dependencies`](#dev-dependencies) {: #dev-dependencies }

项目的开发依赖。

开发依赖在 `uv run` 和 `uv sync` 中默认会被安装，但不会出现在项目发布的元数据中。

不再推荐使用此字段。建议改用 `dependency-groups.dev` 字段，这是声明开发依赖的标准方式。`tool.uv.dev-dependencies` 和 `dependency-groups.dev` 的内容会被合并，以确定 `dev` 依赖组的最终需求。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
dev-dependencies = ["ruff==0.5.0"]
```

---

## [`environments`](#environments) {: #environments }

用于解析依赖的受支持环境列表。

默认情况下，uv 在 `uv lock` 操作期间会为所有可能的环境进行解析。但是，你可以限制受支持环境的集合，以提高性能并避免解决方案空间中出现不可满足的分支。

当使用 `--universal` 标志调用 `uv pip compile` 时，这些环境也会被遵循。

**默认值**：`[]`

**类型**：`str | list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
# 仅为 macOS 解析，不为 Linux 或 Windows 解析。
environments = ["sys_platform == 'darwin'"]
```

---

## [`exclude-dependencies`](#exclude-dependencies) {: #exclude-dependencies }

在解析项目依赖时要排除的依赖。

排除项用于阻止某个包在解析过程中被选中，无论它是否被任何其他包请求。当某个包被排除时，它将完全从依赖列表中省略。

将某个包纳入排除项将阻止其被安装，即使它被传递依赖请求也是如此。这对于移除可选依赖或处理依赖损坏的包非常有用。

!!! note

    在 `uv lock`、`uv sync` 和 `uv run` 中，uv 只会从工作空间根目录的 `pyproject.toml` 中读取 `exclude-dependencies`，并会忽略其他工作空间成员或 `uv.toml` 文件中的任何声明。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
# 排除 Werkzeug 的安装，即使传递依赖请求它。
exclude-dependencies = ["werkzeug"]
```

---

## [`index`](#index) {: #index }

解析依赖时使用的索引源。

接受符合 [PEP 503](https://peps.python.org/pep-0503/)（简单仓库 API）的仓库，或按相同格式组织的本地目录。

索引按定义顺序依次考虑，最先定义的索引具有最高优先级。此外，此设置提供的索引优先级高于通过 [`index_url`](configuration.md/#index-url) 或 [`extra_index_url`](configuration.md/#extra-index-url) 指定的任何索引。uv 只会考虑包含给定包的第一个索引，除非指定了替代的[索引策略](configuration.md/#index-strategy)。

如果某个索引标记为 `explicit = true`，它将专门用于通过 `[tool.uv.sources]` 显式选择它的依赖，例如：

```toml
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu130"
explicit = true

[tool.uv.sources]
torch = { index = "pytorch" }
```

如果某个索引标记为 `default = true`，它将被移至优先级列表的末尾，从而在解析包时获得最低优先级。此外，将索引标记为默认会禁用 PyPI 默认索引。

**默认值**：`[]`

**类型**：`dict`

**示例用法**：

```toml title="pyproject.toml"

[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cu130"
```

---

## [`managed`](#managed) {: #managed }

项目是否由 uv 管理。如果为 `false`，uv 在调用 `uv run` 时将忽略该项目。

**默认值**：`true`

**类型**：`bool`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
managed = false
```

---

## [`override-dependencies`](#override-dependencies) {: #override-dependencies }

在解析项目依赖时应用的覆盖项。

覆盖项用于强制选择特定版本的包，无论任何其他包请求的版本是什么，也无论选择该版本通常是否构成无效的解析方案。

约束是 _叠加性_ 的，即它们与组成包的需求合并，而覆盖项是 _绝对性_ 的，即它们完全替换任何组成包的需求。

将某个包纳入覆盖项 _不会_ 触发该包自身的安装；相反，该包必须在项目的一手依赖或传递依赖中的其他位置被请求。

!!! note

    在 `uv lock`、`uv sync` 和 `uv run` 中，uv 只会从工作空间根目录的 `pyproject.toml` 中读取 `override-dependencies`，并会忽略其他工作空间成员或 `uv.toml` 文件中的任何声明。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
# 始终安装 Werkzeug 2.3.0，无论传递依赖是否请求了不同的版本。
override-dependencies = ["werkzeug==2.3.0"]
```

---

## [`package`](#package) {: #package }

项目是否应被视为 Python 包，还是非包（"虚拟"）项目。

包会被构建并以可编辑模式安装到虚拟环境中，因此需要一个构建后端；而虚拟项目 _不会_ 被构建或安装，只有其依赖会被包含在虚拟环境中。

创建包要求在 `pyproject.toml` 中存在 `build-system`，并且项目遵循符合构建后端预期的结构（例如 `src` 布局）。

**默认值**：`true`

**类型**：`bool`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
package = false
```

---

## [`required-environments`](#required-environments) {: #required-environments }

对于缺少源代码分发包的包，声明必需的平台列表。

当某个包没有源代码分发包时，其可用性将仅限于其构建分发包（wheel）所支持的平台。例如，如果某个包仅为 Linux 发布 wheel，那么它将无法在 macOS 或 Windows 上安装。

默认情况下，uv 要求每个包至少包含一个与指定 Python 版本兼容的 wheel。`required-environments` 设置可用于确保最终的解析结果包含特定平台的 wheel，或者在无法获取此类 wheel 时使解析失败。

`environments` 设置 _限制_ 了 uv 在解析依赖时会考虑的环境集合，而 `required-environments` _扩展_ 了 uv 在解析依赖时 _必须_ 支持的平台集合。

例如，`environments = ["sys_platform == 'darwin'"]` 会将 uv 限制为仅针对 macOS 进行解析（忽略 Linux 和 Windows）。而 `required-environments = ["sys_platform == 'darwin'"]` 则会 _要求_ 任何没有源代码分发包的包必须包含 macOS 的 wheel 才能被安装。

**默认值**：`[]`

**类型**：`str | list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv]
# 要求包在以下平台上可用：
required-environments = [
    # macOS on Apple Silicon (ARM)
    "sys_platform == 'darwin' and platform_machine == 'arm64'",
    # Linux on x86_64 (Intel/AMD)
    "sys_platform == 'linux' and platform_machine == 'x86_64'",
    # Windows on x86_64 (Intel/AMD)
    "sys_platform == 'win32' and platform_machine == 'AMD64'",
]
```

---

## [`sources`](#sources) {: #sources }

解析依赖时使用的源。

`tool.uv.sources` 通过附加源来丰富依赖元数据，在开发过程中纳入使用。依赖源可以是 Git 仓库、URL、本地路径或替代注册表。

更多信息请参阅[依赖](../../concepts/projects/dependencies.md)。

**默认值**：`{}`

**类型**：`dict`

**示例用法**：

```toml title="pyproject.toml"

[tool.uv.sources]
httpx = { git = "https://github.com/encode/httpx", tag = "0.27.0" }
pytest = { url = "https://files.pythonhosted.org/packages/6b/77/7440a06a8ead44c7757a64362dd22df5760f9b12dc5f11b6188cd2fc27a0/pytest-8.3.3-py3-none-any.whl" }
pydantic = { path = "/path/to/pydantic", editable = true }
```

---

## `build-backend`

uv 构建后端（`uv_build`）的设置。

请注意，这些设置仅在使用 `uv_build` 后端时适用，其他构建后端（如 hatchling）有自己的配置。

所有接受 glob 模式的选项均使用 [PEP 639](https://packaging.python.org/en/latest/specifications/glob-patterns/) 中的可移植 glob 模式。

### [`data`](#build-backend_data) {: #build-backend_data }
<span id="data"></span>

wheel 的数据包含项。

每个条目都是一个目录，其内容会被复制到 wheel 中 `<name>-<version>.data/(purelib|platlib|headers|scripts|data)` 下的对应目录。安装时，这些数据会被移动到其目标位置，如 <https://docs.python.org/3.12/library/sysconfig.html#installation-paths> 所定义。通常，小型数据文件应放置在 Python 模块中，而不是使用数据包含项。

- `scripts`：安装到可执行文件目录，Unix 上为 `<venv>/bin`，Windows 上为 `<venv>\Scripts`。激活虚拟环境或使用 `uv run` 时，此目录会被添加到 `PATH`，因此此数据类型可用于安装额外的二进制文件。对于 Python 入口点，建议改用 `project.scripts`。
- `data`：安装到虚拟环境根目录之上。

    警告：这可能会覆盖现有文件！

- `headers`：安装到 include 目录。将本包作为构建依赖的编译器会使用 include 目录来查找额外的头文件。
- `purelib` 和 `platlib`：安装到 `site-packages` 目录。不建议使用这两个选项。

**默认值**：`{}`

**类型**：`dict[str, str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.build-backend]
data = { headers = "include/headers", scripts = "bin" }
```

---

### [`default-excludes`](#build-backend_default-excludes) {: #build-backend_default-excludes }
<span id="default-excludes"></span>

如果设置为 `false`，则不应用默认排除项。

默认排除项：`__pycache__`、`*.pyc` 和 `*.pyo`。

**默认值**：`true`

**类型**：`bool`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.build-backend]
default-excludes = false
```

---

### [`module-name`](#build-backend_module-name) {: #build-backend_module-name }
<span id="module-name"></span>

`module-root` 内部模块目录的名称。

默认模块名称是将包名中的点和短横线替换为下划线后的结果。

包名需要是有效的 Python 标识符，且目录需要包含 `__init__.py`。例外情况是 stubs 包，其名称以 `-stubs` 结尾，词干为模块名，并包含 `__init__.pyi` 文件。

对于单模块的命名空间包，路径可以使用点号分隔，例如 `foo.bar` 或 `foo-stubs.bar`。

对于多模块的命名空间包，路径可以是列表形式，例如 `["foo", "bar"]`。我们建议每个包只使用一个模块，将多个包拆分为工作空间。

请注意，使用此选项存在创建两个名称不同但模块名相同的包的风险。将此类包一起安装会导致未定义的行为，通常会导致文件或目录树损坏。

**默认值**：`None`

**类型**：`str | list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-name = "sklearn"
```

---

### [`module-root`](#build-backend_module-root) {: #build-backend_module-root }
<span id="module-root"></span>

包含模块目录的目录。

常见值为 `src`（src 布局，默认值）或空路径（扁平布局）。

**默认值**：`"src"`

**类型**：`str`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.build-backend]
module-root = ""
```

---

### [`namespace`](#build-backend_namespace) {: #build-backend_namespace }
<span id="namespace"></span>

构建命名空间包。

构建 PEP 420 隐式命名空间包，允许存在多个根 `__init__.py`。

当命名空间包包含多个根 `__init__.py` 时使用此选项，对于只有一个根 `__init__.py` 的命名空间包，请改用点号分隔的 `module-name`。

对比点号分隔的 `module-name` 和 `namespace = true`，下面的第一个示例可以用 `module-name = "cloud.database"` 表示：只有一个根 `__init__.py`，即 `database`。在第二个示例中，有三个根（`cloud.database`、`cloud.database_pro`、`billing.modules.database_pro`），因此需要 `namespace = true`。

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

**默认值**：`false`

**类型**：`bool`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.build-backend]
namespace = true
```

---

### [`source-exclude`](#build-backend_source-exclude) {: #build-backend_source-exclude }
<span id="source-exclude"></span>

从源代码分发包中排除哪些文件和目录的 glob 表达式。

这些排除项也会应用于 wheel，以确保从源代码树构建的 wheel 与从源代码分发包构建的 wheel 保持一致。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.build-backend]
source-exclude = ["*.bin"]
```

---

### [`source-include`](#build-backend_source-include) {: #build-backend_source-include }
<span id="source-include"></span>

从源代码分发包中额外包含哪些文件和目录的 glob 表达式。

`pyproject.toml` 和模块目录的内容始终会被包含。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.build-backend]
source-include = ["tests/**"]
```

---

### [`wheel-exclude`](#build-backend_wheel-exclude) {: #build-backend_wheel-exclude }
<span id="wheel-exclude"></span>

从 wheel 中排除哪些文件和目录的 glob 表达式。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.build-backend]
wheel-exclude = ["*.bin"]
```

---

## `workspace`

### [`exclude`](#workspace_exclude) {: #workspace_exclude }
<span id="exclude"></span>

要排除在工作空间成员之外的包。如果某个包同时匹配 `members` 和 `exclude`，则会被排除。

支持 glob 模式和显式路径。

有关 glob 语法的更多信息，请参阅 [`glob` 文档](https://docs.rs/glob/latest/glob/struct.Pattern.html)。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.workspace]
exclude = ["member1", "path/to/member2", "libs/*"]
```

---

### [`members`](#workspace_members) {: #workspace_members }
<span id="members"></span>

要包含为工作空间成员的包。

支持 glob 模式和显式路径。

有关 glob 语法的更多信息，请参阅 [`glob` 文档](https://docs.rs/glob/latest/glob/struct.Pattern.html)。

**默认值**：`[]`

**类型**：`list[str]`

**示例用法**：

```toml title="pyproject.toml"
[tool.uv.workspace]
members = ["member1", "path/to/member2", "libs/*"]
```
