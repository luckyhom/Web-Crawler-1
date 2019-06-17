import http.cookiejar
import urllib.request

cookie = http.cookiejar.CookieJar()  # 创建一个CookieJar对象
handler = urllib.request.HTTPCookieProcessor(cookie)  # 利用HTTPCookieProcessor和CoolkieJar对象创建一个handler
opener = urllib.request.build_opener(handler)  # 利用build_opener()和handler构建出一个Opener。
response = opener.open('http://www.baidu.com')  # 执行Opener对象的open()方法即可。
for item in cookie:
    print(item.name+"="+item.value)
