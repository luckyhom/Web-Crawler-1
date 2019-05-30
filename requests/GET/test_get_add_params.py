import requests

data = {
    'name': 'germey',
    'age': 22,
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
print(type(r.text))
print(r.json())  # 调用json()方法可以将返回结果是JSON格式的字符串转化为字典，但如果返回结果不是JSON格式，便会出现解析错误，
                 # 抛出json.decoder.JSONDecodeError异常
print(type(r.json()))

# 执行的结果如下

# {
#   "args": {
#     "age": "22",
#     "name": "germey"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.22.0"
#   },
#   "origin": "58.60.1.24, 58.60.1.24",
#   "url": "https://httpbin.org/get?name=germey&age=22"
# }
#
# <class 'str'>
# {'args': {'age': '22', 'name': 'germey'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0'}, 'origin': '58.
# 60.1.24, 58.60.1.24', 'url': 'https://httpbin.org/get?name=germey&age=22'}
# <class 'dict'>

