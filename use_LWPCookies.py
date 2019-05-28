import http.cookiejar
import urllib.request

cookie = http.cookiejar.LWPCookieJar()  # 构造一个LWPCookieJar对象
cookie.load('cookies_LWPCookies.txt', ignore_discard=True, ignore_expires=True)  # LWPCookieJar对象从txt文件中读取cookies
handler = urllib.request.HTTPCookieProcessor(cookie)  # 使用LWPCookieJar对象和HTTPCookieProcessor创建一个hanlder
opener = urllib.request.build_opener(handler)  # 使用build_opener()方法和hanlder创建一个opener
response = opener.open('http://www.baidu.com')  # 使用opener打开url即可
print(response.read().decode('utf-8'))
