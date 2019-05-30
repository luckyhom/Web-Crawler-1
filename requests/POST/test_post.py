import requests

data = {'name': 'germey', 'age': 22}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)

# 运行结果如下

# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "age": "22",
#     "name": "germey"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Length": "18",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0"
#   },
#   "json": null,
#   "origin": "58.60.1.24, 58.60.1.24",
#   "url": "https://httpbin.org/post"
# }
# form部分就是提交的数据