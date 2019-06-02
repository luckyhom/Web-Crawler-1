from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)
# 得到所有li 节点
result_li = html.xpath('//li')
print(result_li)
print(result_li[0])
# 得到子节点a
result_a = html.xpath('//li/a')
print(result_a)
print(result_a[0])