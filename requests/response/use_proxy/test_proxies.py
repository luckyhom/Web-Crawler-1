import requests

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

requests.get('https://www.taobao.com', proxies=proxies)

# 此处的proxies只是示例，真正使用时需要使用有效的代理