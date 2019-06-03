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

# 获得父节点
result_f = html.xpath('//a[@href="link4.html"]/../@class')
print(result_f)  # 获取的目标li 节点的class

# 同时也可以通过parent:: 来获得父节点
result_p = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result_p)

# 还可以通过@ 进行属性过滤
result_attribute = html.xpath('//li[@class="item-0"]')
print(result_attribute)

# 获取节点中的文本
result_text = html.xpath('//li[@class="item-0"]//a//text()')
print(result_text)

# 使用另一种方法（即使用//）选取
result_text_1 = html.xpath('//li[@class="item-0"]//text()')
print(result_text_1)

# 节点属性获取（匹配需要用[]括起来属性，获取不需要括号
result_node_attribute = html.xpath('//li/a/@href')
print(result_node_attribute)

# 属性多值匹配，需要使用contains() 函数
muti_attribute_html = '''
<li class="li li-first"><a href="link.html">first item muti attribute</a></li>
'''
ma_html = etree.HTML(muti_attribute_html)
# result_muti_attribute = ma_html.xpath('//li[@class="li"]/a/text()') 旧方法已经不可用
result_muti_attribute = ma_html.xpath('//li[contains(@class, "li")]/a/text()')
print(result_muti_attribute)

# 多属性匹配 使用多个属性确定一个一个节点 使用and进行连接
attribute_muti_html = '''
<li class="li li-first" name="item"><a href="link.html">first item muti attribute name item</a></li>
'''
am_html = etree.HTML(attribute_muti_html)
result_attribute_muti = am_html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print(result_attribute_muti)

# 按照顺序选择，比如在满足条件中的第二个节点进行获取
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-1]/a/text()')
print(result)

# 使用节点轴
result = html.xpath('//li[1]//ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
# result = html.xpath('//li[1]/child/::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
result = html.xpath('//li[1]/following-silbing::*')
print(result)


