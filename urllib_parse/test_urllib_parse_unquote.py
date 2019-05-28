from urllib.parse import unquote

url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))

# unquote()可对其进行URL解码
# 运行结果为
# https://www.baidu.com/s?wd=壁纸
