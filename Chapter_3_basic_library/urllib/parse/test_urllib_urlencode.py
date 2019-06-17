from urllib.parse import urlencode
# urlencod() 常用于构造GET请求参数，将一个字典序列化为GET请求参数。

params = {
    'name': 'germey',
    'age': 22,
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

# 运行结果为

# http://www.baidu.com?name=germey&age=22