import requests
from requests.packages import urllib3

urllib3.disable_warning()  # 用于忽略警告
response = requests.get('http://www.12306.cn', verify=False)
print(response.status_code)
