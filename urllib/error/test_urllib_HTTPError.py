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

# 运行结果如下

# Not Found
# 404
# Server: nginx/1.10.3 (Ubuntu)
# Date: Wed, 29 May 2019 02:14:05 GMT
# Content-Type: text/html; charset=UTF-8
# Transfer-Encoding: chunked
# Connection: close
# Vary: Cookie
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Cache-Control: no-cache, must-revalidate, max-age=0
# Link: <https://cuiqingcai.com/wp-json/>; rel="https://api.w.org/"
#
#
# Not Found
# 404
# Server: nginx/1.10.3 (Ubuntu)
# Date: Wed, 29 May 2019 02:14:05 GMT
# Content-Type: text/html; charset=UTF-8
# Transfer-Encoding: chunked
# Connection: close
# Vary: Cookie
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Cache-Control: no-cache, must-revalidate, max-age=0
# Link: <https://cuiqingcai.com/wp-json/>; rel="https://api.w.org/"