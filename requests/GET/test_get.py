import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

# 运行结果如下

# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0"
#   },
#   "origin": "58.60.1.24, 58.60.1.24",
#   "url": "https://httpbin.org/get"
# }
