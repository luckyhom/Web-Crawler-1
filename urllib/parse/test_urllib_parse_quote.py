from urllib.parse import quote

keyword = '壁纸'
url = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(url)


# 使用此方法将内容转化为URl编码
# 运行后结果如下

# http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8


