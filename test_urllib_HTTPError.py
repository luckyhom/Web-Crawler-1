from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')

# 另一种写法，先捕获HTTPError，在捕获URLError。因为HTTPError是URLError的子类。

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:  # 先捕获HTTPError
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:  # 再尝试不捕获URLError
    print(e.reason)
else:  # 使用else处理正常的逻辑
    print('Request Successfully')
