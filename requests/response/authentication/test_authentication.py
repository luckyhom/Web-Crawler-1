import requests
from requests.auth import HTTPBasicAuth

r = requests.get('htttp://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# 上面一行代码可以简写为下面这一行
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)  # 用户名和密码正确，请求就会自动认证成功，会返回200状态码；如果认证失败，则返回401状态码
