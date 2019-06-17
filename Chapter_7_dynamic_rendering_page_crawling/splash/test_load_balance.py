import requests
from urllib.parse import quote
import re

lua = """
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
    return treat.as_steing(response.body)
end
"""

url = 'http://splash:8050/execute?lua_source=' + quote(lua)  # spalsh 替换为配置nginx的服务器地址
response = requests.get(url, auth=('admin', 'password'))
ip = re.search('(\d+\.\d+\.\d+\.\d+)', response.text).group(1)
print(ip)
# 若运行结果ip会变化且为服务器群的ip即表示负载均衡设置成功。