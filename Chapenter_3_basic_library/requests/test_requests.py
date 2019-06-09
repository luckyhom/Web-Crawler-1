import requests

r = requests.get('https://www.baidu.com')  # 得到一个Response 对象
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(type(r.cookies))
print(r.cookies)  # r.cookies是一个RequestsCookieJar对象

# 其他类型的请求的实现
# r = requests.post('http://httpbin.org/post')
# r = requests.put('http://httpbin.org/put')
# r = requests.delete('http://httpbin.org/delete')
# r = requests.head('http://httpbin.org/get')
# r = requests.options('http://httpbin.org/get')