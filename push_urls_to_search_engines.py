"""
将站点 sitemap 中的 URL 推送到各大搜索引擎（Bing、Google），
主动通知搜索引擎爬虫来抓取和索引页面。
"""
import json
import logging
import os
import xml.etree.ElementTree as ET

import requests
from google.auth.transport.requests import Request
from google.oauth2 import service_account

# 初始化日志记录器，用于跟踪推送状态和排查问题
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_urls_from_website_file() -> list[str]:
    """从本地 sitemap.xml 中提取所有待推送的 URL 列表"""
    try:
        # 解析 sitemap.xml 文件
        tree = ET.parse('sitemap.xml')
        root = tree.getroot()
        # sitemap 标准命名空间
        ns = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        # 提取所有 <url><loc> 中的链接地址
        return list(loc.text for loc in root.findall('sitemap:url/sitemap:loc', ns) if loc.text)
    except FileNotFoundError:
        logger.error("sitemap.xml not found")
        return []


def to_bing_now(urls: list[str]):
    """
    通过 Microsoft Bing IndexNow API 主动推送 URL 给 Bing 搜索引擎。
    IndexNow 是一个通用的搜索引擎通知协议，Bing 和 Yandex 都支持。
    """
    if BING_NOW_API_KEY := os.getenv('BING_NOW_API_KEY'):
        # 向 IndexNow 端点发送 POST 请求，批量提交 URL
        resp = requests.post(
            'https://api.indexnow.org/IndexNow',
            headers={'Content-Type': 'application/json'},
            json={
                "host": "uv.oaix.tech",
                "key": BING_NOW_API_KEY,
                "keyLocation": f"https://uv.oaix.tech/{BING_NOW_API_KEY}.txt",
                "urlList": urls
            }
        )
        logger.info(f"Status: {resp.status_code}, Text: {resp.text}")
    else:
        logger.error("BING_NOW_API_KEY is not set")


def to_google_console(urls: list[str]):
    """
    通过 Google Indexing API 主动推送 URL 给 Google 搜索引擎。
    使用 Google 服务账号进行 OAuth 2.0 认证，逐条提交 URL 更新通知。
    """
    if GOOGLE_SERVICE_ACCOUNT_JSON := os.getenv('GOOGLE_SERVICE_ACCOUNT_JSON'):
        # Google Indexing API 的权限范围和端点
        scopes = ["https://www.googleapis.com/auth/indexing"]
        endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"

        # 从环境变量中的服务账号 JSON 加载凭证
        credentials = service_account.Credentials.from_service_account_info(
            json.loads(GOOGLE_SERVICE_ACCOUNT_JSON), scopes=scopes
        )

        # 创建带认证的 HTTP 会话
        authed_session = requests.Session()

        # 通过服务账号凭证获取 access token
        request = Request()
        credentials.refresh(request)

        # 在会话头部添加 Bearer token 认证信息
        authed_session.headers.update({
            'Authorization': f'Bearer {credentials.token}',
            'Content-Type': 'application/json'
        })

        # 逐条向 Google Indexing API 提交 URL 更新通知
        for url in urls:
            content = {
                "url": url,
                "type": "URL_UPDATED"
            }

            response = authed_session.post(endpoint, json=content)
            logger.info(f"Status: {response.status_code}, Text: {response.text}")
            if response.status_code == 200:
                logger.info(f"Successfully submitted: {url}")
            else:
                logger.error(f"Failed to submit {url}: {response.text}")
    else:
        logger.error("GOOGLE_SERVICE_ACCOUNT_JSON not set")


if __name__ == '__main__':
    # 从 sitemap 中提取所有 URL，然后分别推送到 Bing 和 Google
    if sitemap_urls := get_urls_from_website_file():
        to_bing_now(sitemap_urls)
        to_google_console(sitemap_urls)
