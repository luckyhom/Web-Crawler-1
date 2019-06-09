from urllib.robotparser import RobotFileParser
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

try:
    rp = RobotFileParser()
    rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').spilt('\n'))
    print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
    print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&page=1&type=collections'))
except HTTPError as e:
    print(e.reason)
except URLError as e:
    print(e.reason)
else:
    print('Success!')

# 使用parse()方法执行读取和分析。
