html = """
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
"""
from pyquery import PyQuery as pq  # 取一个别名pq

# 使用字符串初始化
doc = pq(html)
print(doc('li'))

# URL初始化
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

# 上面初始化过程和下面的方法一样
import requests
doc = pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))

# 文件初始化,除了传递URL意外，还可以传递本地的文件名，参数指定为filename即可
doc = pq(filename='demo.html')
print(doc('li'))

# 上面就是三种初始化方法，最常用的还是以字符串形式传递

# 基本CSS选择器
html = """
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html>fifth item</a></li>
</ul>
</div>
"""
doc = pq(html)
print(doc('#container .list li'))
print(type(doc('#container .list li')))

# 查找子节点，查找子节点时，需要用到find()方法
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

# find()的查找范围时节点的子孙节点，如果我们只想查找子节点，可以使用children()方法

html = """
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html>fifth item</a></li>
</ul>
</div>
"""
doc = pq(html)
items = doc('.list')
lis = items.children()
print(type(lis))
print(lis)

# 筛选出子节点中class为active的节点
html = """
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html>fifth item</a></li>
</ul>
</div>
"""
doc = pq(html)
items = doc('.list')
lis = items.children('.active')
print(lis)

# 使用parent()方法来获取某个节点的父节点
html = """
<div class="wrap">
<div class="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html>fifth item</a></li>
</ul>
</div>
</div>
"""
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

# parent()只会获得直接父节点，不会再去查找父节点的父节点（即祖先节点）。想要获得祖先节点，使用parents()方法
print('使用parents()')
parents = items.parents()
print(type(parents))
print(parents)

# 筛选祖先节点的话，可以向parents()方法传入CSS选择器
print('传入CSS选择器')
parent = items.parents('.wrap')
print(parent)

# 兄弟节点，获取兄弟节点使用siblings()方法
html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html>fifth item</a></li>
</ul>
</div>
</div>
"""
doc = pq(html)
li = doc('.list .item-0.active')
print('获取兄弟节点')
print(li)
print('使用siblings')
print(li.siblings())

# 筛选兄弟节点传入siblings()
li = doc('.list .item-0.active')
print('筛选兄弟节点')
print(li.siblings('.active'))

# pyquery的选择结果可能是多个节点，也可能是单个节点，类型都是PyQuery类型，没有返回列表。
# 对于单个节点可以直接打印输出，也可以直接转成字符串。
li = doc('.item-0.active')
print('直接输出：', li)
print('str输出：', str(li))
# 多个节点进行遍历获取，调用items()方法
doc = pq(html)
lis = doc('li').items()
print(lis)
print('进行遍历输出')
for li in lis:
    print(li, type(li))

# 获取信息之获取属性
html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html>fifth item</a></li>
</ul>
</div>
</div>
"""
doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))  # 调用attr()方法传入属性的名称来获取，该属性的值。
# 也可以通过调用attr属性来获取属性
print(a.attr.href)
# 如果返回节点是多个，想要获得多个节点的属性就要先遍历再获取属性
doc = pq(html)
lis = doc('li')
for li in lis.items():
    print(li.attr.class_)

# 获取属性之获取文本，通过调用text()来实现
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())  # text()会忽略节点内部包含的所有HTML，只返回纯文字内容
# 想要获取这个节点内部的HTML文本，就要使用html()方法
li = doc('.item-0.active')
print(li)
print(li.html())

# 如果我们选中的多个节点，html()方法返回的是第一个节点的内部HTML文本，而text()返回了所有选中节点的文本，用空格隔开，结果为一个字符串。
# 涉及到多个节点时HTML文本要遍历，text()无需遍历。

# 节点操作
# pyquery提供了一系列方法来对节点进行动态修改，添加class或移除某个节点。
# addClass和removeClass
html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html>fifth item</a></li>
</ul>
</div>
</div>
"""
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

# attr、text和html
# 可以通过attr()方法对属性进行操作，用text()方法和html()方法改变节点内部内容
html = """
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul> 
"""
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name', 'link')  # attr() 方法来修改属性，该方法第一个参数是属性名，第二个参数是属性值。attr()只传入一个参数时为获取属性值
# 传入两个参数时，用来修改属性。
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)
# text() 和 html() 方法如果不传参则是获取节点内纯文本和html文本，若有参数，则进行赋值。
# remove()方法就是移除
html = """
<div class="wrap">
    Hello, World
<p> This is a paragraph.</p>
</div>
"""
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
# 此时想要提取Hello，Wrold,不要<p>节点内部的字符串的话，单纯使用text()是无法实现的此时需要使用remove()方法,然后再进行提取即可。
wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">third item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
"""
doc = pq(html)
li = doc("li:first-child")  # 第一个li节点
print(li)
li = doc('li:last-child')  # 最后一个li节点
print(li)
li = doc('li:nth-child(2)')  # 第二个li节点
print(li)
li = doc('li:gt(2)')  # 第三个节点后的li节点
print(li)
li = doc('li:nth-child(2n)')  # 偶数位置的li节点
print(li)
li = doc('li:contains(second)')  # 包含second文本的li节点
print(li)
