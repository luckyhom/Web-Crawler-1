import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('https://www.baidu.com', timeout=0.01)  # 设定一个超时的异常
except urllib.error.URLError as e:
    print(type(e.reason))  # reason 属性返回的不一定是字符串，在这里是socket.timeout 类
    if isinstance(e.reason, socket.timeout):  # 判断e.reason的类型。
        print('TIME OUT')