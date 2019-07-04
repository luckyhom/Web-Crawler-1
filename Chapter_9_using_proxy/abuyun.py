import requests


url = 'http://httpbin.org/get'

# 代理服务器
proxy_host = 'http-pro.abuyun.com'
proxy_port = '9010'

# 代理隧道验证信息
proxy_user = 'HT313253Q488J11P'
proxy_pass = 'C883FE2DD76C948C'

proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'port': proxy_port,
    'user': proxy_user,
    'pass': proxy_pass,
}
proxies = {
    'http': proxy_meta,
    'https': proxy_meta,
}
response = requests.get(url, proxies=proxies)
print(response.status_code)
print(response.text)
