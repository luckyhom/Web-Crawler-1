from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunparse(data))