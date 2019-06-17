import requests

response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# 使用本地证书作为客户端证书，这可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组。
print(response.status_code)