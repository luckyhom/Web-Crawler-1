from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)

# 运行结果如下

# Not Found

