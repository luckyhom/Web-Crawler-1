import requests

r = requests.get('http://www.baidu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)

# 运行结果如下

# <class 'int'> 200
# <class 'requests.structures.CaseInsensitiveDict'> {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip'
# , 'Content-Type': 'text/html', 'Date': 'Wed, 29 May 2019 07:41:37 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:27:56 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': '
# BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
# <class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
# <class 'str'> http://www.baidu.com/
# <class 'list'> []
