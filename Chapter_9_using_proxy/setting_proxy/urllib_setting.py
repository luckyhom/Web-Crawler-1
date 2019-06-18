from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '200.111.182.6:443'
proxy_handler = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'http://' + proxy,
})
opener = build_opener(proxy_handler)
try:
    response = opener.open("http://httpbin.org/get")
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)