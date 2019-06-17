from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://127.0.0.1'

p = HTTPPasswordMgrWithDefaultRealm()  # 实例化HTTPPasswordMgrWithDefaultRealm对象
p.add_password(None, url, username, password)  # 为HTTPPasswordMgrWithDefaultRealm对象添加url、用户名和密码，建立一个处理验证的hanler
auth_handler = HTTPBasicAuthHandler(p) # 使用HTTPPasswordMgrWithDfaultRealm对象实例化HTTPBasicAuthHandler对象
opener = build_opener(auth_handler)  # 使用build_opener()方法利用HTTPBasicAuthHandler对象构建一个opener,这个Opener对象在发送请求时就相当于已经验证成功了

try:
    result = opener.open(url)  # 利用Opener的open()方法打开链接就可以完成验证，返回的结果就是验证后的页面源码内容
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
