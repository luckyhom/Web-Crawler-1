from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743',
})  # 构建ProxyHandler 对象的参数是一个字典，键名是协议类型，键值是代理链接，可以添加多个代理
opener = build_opener(proxy_handler)  # 利用build_opener() 和ProxyHandler对象构造一个Opener，之后发送请求即可。
try:
    response = opener.open("https://www.baidu.com")
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
