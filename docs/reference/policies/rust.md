# Rust 支持

编译 uv 所需的最低支持 Rust 版本（Minimum Supported Rust Version）列在 `Cargo.toml` 中 `[workspace.package]` 部分的 `rust-version` 键中。该版本可能在任意版本（次版本或补丁版本）中发生变化。它将永远不会高于 N-2 的 Rust 版本，其中 N 是最新稳定版本。例如，如果最新稳定 Rust 版本为 1.85，则 uv 的最低支持 Rust 版本最多为 1.83。

此信息仅适用于从源码构建 uv 的用户。从 Python 包索引（Python package index）安装 uv 通常会安装预编译的二进制文件，无需进行 Rust 编译。
