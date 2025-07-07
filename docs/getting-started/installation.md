---
subtitle: Installation
---

# 安装 uv

## 安装方法

使用我们的独立安装程序或您选择的包管理器来安装 uv。

### 独立安装程序

uv 提供了一个独立的安装程序来下载和安装 uv：

=== "macOS 和 Linux"

    使用 `curl` 下载脚本并用 `sh` 执行：

    ```console
    $ curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

    如果您的系统没有 `curl`，您可以使用 `wget`：

    ```console
    $ wget -qO- https://astral.sh/uv/install.sh | sh
    ```

    通过在 URL 中包含版本号来请求特定版本：

    ```console
    $ curl -LsSf https://astral.sh/uv/0.7.19/install.sh | sh
    ```

=== "Windows"

    使用 `irm` 下载脚本并用 `iex` 执行：

    ```pwsh-session
    PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

    更改[执行策略](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4#powershell-execution-policies)允许从互联网运行脚本。

    通过在 URL 中包含版本号来请求特定版本：

    ```pwsh-session
    PS> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.7.19/install.ps1 | iex"
    ```

!!! tip

    安装脚本可以在使用前进行检查：

    === "macOS 和 Linux"

        ```console
        $ curl -LsSf https://astral.sh/uv/install.sh | less
        ```

    === "Windows"

        ```pwsh-session
        PS> powershell -c "irm https://astral.sh/uv/install.ps1 | more"
        ```

    或者，安装程序或二进制文件可以直接从 [GitHub](#github-releases) 下载。

有关自定义 uv 安装的详细信息，请参阅[安装程序](../reference/installer.md)的参考文档。

### PyPI

为方便起见，uv 已发布到 [PyPI](https://pypi.org/project/uv/)。

如果从 PyPI 安装，我们建议将 uv 安装到隔离的环境中，例如，使用 `pipx`：

```console
$ pipx install uv
```

但是，也可以使用 `pip`：

```console
$ pip install uv
```

!!! note

    uv 为许多平台提供了预构建的发行版 (wheels)；如果给定平台没有可用的 wheel，uv 将从源代码构建，这需要 Rust 工具链。有关从源代码构建 uv 的详细信息，请参阅[贡献设置指南](https://github.com/astral-sh/uv/blob/main/CONTRIBUTING.md#setup)。

### Cargo

uv 可通过 Cargo 获得，但必须从 Git 构建而不是 [crates.io](https://crates.io)，因为它依赖于未发布的 crate。

```console
$ cargo install --git https://github.com/astral-sh/uv uv
```

### Homebrew

uv 在核心 Homebrew 包中可用。

```console
$ brew install uv
```

### WinGet

uv 可通过 [WinGet](https://winstall.app/apps/astral-sh.uv) 获得。

```console
$ winget install --id=astral-sh.uv  -e
```

### Scoop

uv 可通过 [Scoop](https://scoop.sh/#/apps?q=uv) 获得。

```console
$ scoop install main/uv
```

### Docker

uv 在 [`ghcr.io/astral-sh/uv`](https://github.com/astral-sh/uv/pkgs/container/uv) 提供了一个 Docker 镜像。

有关更多详细信息，请参阅我们的[在 Docker 中使用 uv](../guides/integration/docker.md) 指南。

### GitHub Releases

uv 发行版工件可以直接从 [GitHub Releases](https://github.com/astral-sh/uv/releases) 下载。

每个发行版页面都包含所有支持平台的二进制文件，以及通过 `github.com` 而不是 `astral.sh` 使用独立安装程序的说明。

## 升级 uv

当通过独立安装程序安装 uv 时，它可以按需自行更新：

```console
$ uv self update
```

!!! tip

    更新 uv 将重新运行安装程序，并可能修改您的 shell 配置文件。要禁用此行为，请设置 `INSTALLER_NO_MODIFY_PATH=1`。

当使用其他安装方法时，自更新被禁用。请改用包管理器的升级方法。例如，使用 `pip`：

```console
$ pip install --upgrade uv
```

## Shell 自动补全

!!! tip

    您可以运行 `echo $SHELL` 来帮助您确定您的 shell。

要为 uv 命令启用 shell 自动补全，请运行以下命令之一：

=== "Bash"

    ```bash
    echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc
    ```

=== "Zsh"

    ```bash
    echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
    ```

=== "fish"

    ```bash
    echo 'uv generate-shell-completion fish | source' > ~/.config/fish/completions/uv.fish
    ```

=== "Elvish"

    ```bash
    echo 'eval (uv generate-shell-completion elvish | slurp)' >> ~/.elvish/rc.elv
    ```

=== "PowerShell / pwsh"

    ```powershell
    if (!(Test-Path -Path $PROFILE)) {
      New-Item -ItemType File -Path $PROFILE -Force
    }
    Add-Content -Path $PROFILE -Value '(& uv generate-shell-completion powershell) | Out-String | Invoke-Expression'
    ```

要为 uvx 命令启用 shell 自动补全，请运行以下命令之一：

=== "Bash"

    ```bash
    echo 'eval "$(uvx --generate-shell-completion bash)"' >> ~/.bashrc
    ```

=== "Zsh"

    ```bash
    echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
    ```

=== "fish"

    ```bash
    echo 'uvx --generate-shell-completion fish | source' > ~/.config/fish/completions/uvx.fish
    ```

=== "Elvish"

    ```bash
    echo 'eval (uvx --generate-shell-completion elvish | slurp)' >> ~/.elvish/rc.elv
    ```

=== "PowerShell / pwsh"

    ```powershell
    if (!(Test-Path -Path $PROFILE)) {
      New-Item -ItemType File -Path $PROFILE -Force
    }
    Add-Content -Path $PROFILE -Value '(& uvx --generate-shell-completion powershell) | Out-String | Invoke-Expression'
    ```

然后重新启动 shell 或加载 shell 配置文件。

## 卸载

如果您需要从系统中删除 uv，请按照以下步骤操作：

1.  清理存储的数据（可选）：

    ```console
    $ uv cache clean
    $ rm -r "$(uv python dir)"
    $ rm -r "$(uv tool dir)"
    ```

    !!! tip

        在删除二进制文件之前，您可能需要删除 uv 存储的任何数据。

2.  删除 uv 和 uvx 二进制文件：

    === "macOS 和 Linux"

        ```console
        $ rm ~/.local/bin/uv ~/.local/bin/uvx
        ```

    === "Windows"

        ```pwsh-session
        PS> rm $HOME\.local\bin\uv.exe
        PS> rm $HOME\.local\bin\uvx.exe
        ```

    !!! note

        在 0.5.0 之前，uv 安装在 `~/.cargo/bin` 中。可以从那里删除二进制文件以进行卸载。从旧版本升级不会自动从 `~/.cargo/bin` 中删除二进制文件。

## 后续步骤

请参阅[第一步](./first-steps.md)或直接跳转到[使用指南](../guides/index.md)以开始使用 uv。
