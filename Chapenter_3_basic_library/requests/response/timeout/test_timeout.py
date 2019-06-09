import requests

r = requests.get('https://www.taobao.com', timeout=1)
print(r.status_code)

# 实际上请求分为两个阶段，即连接（connect）和读取（read）上面设置的timeout将用作连接和读取这两者的timeout的和。如果要分别指定见下。
r = requests.get('https://www.taobao.com', timeout=(5, 11, 30))
# 如果想永久等待可以设置timeout=None，或直接不加参数。