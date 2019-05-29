from urllib.robotparser import RobotFileParser

rp = RobotFileParser()  # 首先创建RobotFileParser对象
rp.set_url('http://www.jianshu.com/robots.txt')  # 使用set_url()方法设置robots.txt的链接
#  上面两行可以使用下面代码代替
# rp = RobotFileParser('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))  # 使用can_fetch()方法判断，传入的链接是否可以被抓取
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))

# 运行结果如下

# False
# False

# RobotFileParser 对象的常见方法

# set_url()：用来设置robots.txt 文件的链接
# read()：读取robots.txt 文件的链接
# parse()：用来解析robots.txt，传入的参数是robots.txt 某些行内容，它会按照robots.txt 的语法规则来分卸这些内容。
# can_fetch()：该方法传入两个参数，第一个是User-agent，第二个是要抓取的URL。返回结果是该搜索引擎是否可以抓取这个URL，返回True或False
# mtime()：返回的是上次抓取和分析robots.txt的时间，这对于长时间分析和抓取的搜索爬虫是很有必要的，你可能需要定期检查来抓取最新的robots.txt
# modified()：它同样对长时间分析和抓取的搜索爬虫很有帮助，将当前时间设置为上次抓取和分析robots.txt的时间
