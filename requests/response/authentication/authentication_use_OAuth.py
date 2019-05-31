# requests 还提供了其他认证方式，如OAuth 认证，不过此时需要安装oauth报，安装命令如下：
# pip install requests_oauthlib
# 实现身份验证如下

import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/acount/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth)
