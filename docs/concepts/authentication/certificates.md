---
subtitle: TLS certificates
description: 本文档介绍 uv 包管理器中 TLS 证书的配置方式，包括 TLS 后端（rustls + aws-lc-rs）、支持 X.509 签名算法、系统证书与内置 Mozilla 根证书的切换、自定义 CA 证书（通过 SSL_CERT_FILE/SSL_CERT_DIR 环境变量）、客户端证书认证（mTLS），以及通过 allow-insecure-host 配置选项允许自签名证书或不安全主机连接的安全注意事项。
---

# TLS 证书

uv 使用 TLS 与包索引及其他 HTTPS 服务器进行安全通信。TLS 证书用于验证这些服务器的身份，确保连接不会被拦截。

## TLS 后端

uv 使用 [`rustls`](https://github.com/rustls/rustls)（一个用 Rust 编写的内存安全 TLS 实现），并以 [`aws-lc-rs`](https://github.com/aws/aws-lc-rs) 作为加密提供者。

uv 支持以下 X.509 证书签名算法：

- ECDSA（P-256、P-384、P-521）配合 SHA-256、SHA-384 或 SHA-512
- Ed25519
- RSA PKCS#1 v1.5（2048–8192 位）配合 SHA-256、SHA-384 或 SHA-512
- RSA-PSS（2048–8192 位）配合 SHA-256、SHA-384 或 SHA-512

## 系统证书

默认情况下，uv 使用内置的 Mozilla 根证书进行 TLS 验证。在某些情况下，你可能希望改用平台的原生证书存储——例如，当你依赖系统证书存储中包含的企业信任根（如用于强制代理）时。

要使用系统证书，可以传递 [`--system-certs`](../../reference/cli.md#uv) 标志，将 [`UV_SYSTEM_CERTS`](../../reference/environment.md#uv_system_certs) 环境变量设置为 `true`，或在 `uv.toml` 中设置 [`system-certs = true`](../../reference/settings.md#system-certs)。

使用系统证书时，证书验证由 [`rustls-platform-verifier`](https://github.com/rustls/rustls-platform-verifier) 执行，该库将验证操作委托给操作系统的证书验证器。

## 自定义证书

要使用自定义 CA 证书，可以将 [`SSL_CERT_FILE`](../../reference/environment.md#ssl_cert_file) 环境变量设置为 PEM 编码的证书包路径（例如 `certs.pem`、`ca-bundle.crt`），或将 [`SSL_CERT_DIR`](../../reference/environment.md#ssl_cert_dir) 设置为一个或多个包含 PEM 编码证书文件的目录。支持多个条目，使用平台特定的分隔符分隔（Unix 上为 `:`，Windows 上为 `;`）。

证书通常以 `.pem`、`.crt` 或 `.cer` 扩展名存储，但 uv 会尝试从提供的 `SSL_CERT_DIR` 中的任何常规文件中读取证书。

无法解析为 PEM 证书的文件将被忽略。uv 会解析符号链接，并忽略悬空符号链接。

不支持 DER 编码的文件。

设置这些环境变量后，将**完全覆盖**默认的证书来源——只有提供的证书才会被信任。

`SSL_CERT_FILE` 可以指向单个证书或包含多个证书的证书包。`SSL_CERT_DIR` 可以包含多个目录条目；uv 将从每个目录中加载所有有效证书。

如果需要客户端证书认证（mTLS），请将 [`SSL_CLIENT_CERT`](../../reference/environment.md#ssl_client_cert) 环境变量设置为一个 PEM 格式文件的路径，该文件包含证书及其后的私钥。

## 不安全主机

如果你使用的环境需要信任自签名证书或以其他方式禁用证书验证，可以通过 [`allow-insecure-host`](../../reference/settings.md#allow-insecure-host) 配置选项指示 uv 允许与指定主机建立不安全连接。例如，在 `pyproject.toml` 中添加以下内容将允许与 `example.com` 建立不安全连接：

```toml
[tool.uv]
allow-insecure-host = ["example.com"]
```

`allow-insecure-host` 接受主机名（如 `localhost`）或主机名-端口对（如 `localhost:8080`），并且仅适用于 HTTPS 连接，因为 HTTP 连接本身就是不安全的。

请谨慎使用 `allow-insecure-host`，仅在受信任的环境中使用，因为缺少证书验证可能会使你面临安全风险。
