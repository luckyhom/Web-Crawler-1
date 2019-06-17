html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elise--></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the buttom of a well.</P>
<p class="story">...</p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)

# 选择元素
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

# 提取信息
print(soup.title.name)

# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])

# 获取内容
print(soup.p.string)

# 嵌套选择
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

# 关联选择
html = """
<html>
<head>
<title>The Dormouse's Story</title>
</head>
<body>
<p class="story">
    Once upon a time there wre three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
    <span>Elsie</span>
    </a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    and they lived at the bottom of a well.
</p>
<p class="story'>...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents)

print(soup.p.children)
for i, child in enumerate(soup.p.children):
    print(i, child)

# 得到所有的子孙节点，使用descendants
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# 父节点和祖先节点
html ="""
<html>
<head>
<title>The Dormouse's stroy</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id = "link1">
    <span>Elsie</span>
    </a>
    </p>
    <p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)  # soup.a.parent a的直接父节点，想要再向外寻找父节点的祖先节点，使用下面的parents

print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

# 获得兄弟节点（即同级节点）
html = """
<html>
<body>
<p class="story">
            Once upon a time there wre there little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
            Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
</P>
"""
soup = BeautifulSoup(html, 'lxml')
print('**********************************')
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print(type(soup.a.previous_sibling))
print(type(soup.a.next_sibling))
print(type(enumerate(soup.a.next_sibling)))
print(type(enumerate(soup.a.previous_sibling)))
print(enumerate(soup.a.next_sibling))
print(enumerate(soup.a.previous_sibling))
print('Next Sibling', list(enumerate(soup.a.next_sibling)))
print('Prev Sibling', list(enumerate(soup.a.previous_sibling)))

# 提取信息
html = """
<html>
<body>
<p class="story">
     Once upon a time there were three little sisters; and their names were
     <a href="http://example.com/elsia" class="sister" id="link1">Bob</a>
     <a href="http://example.com/lacie" class="lacie" id="link2">Lacie</a>
</p>
"""
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parents:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])

# 方法选择器
# find_all() : 查询所有符合条件的元素。
# API： find_all(name, attrs, recursive, text, **kwargs)
# name: 可以根据节点名来查询元素
html = """
<div class="panel">
<div class="panel-heading">
<h4>HELLO</h4>
</div>
<div class="panel-body" name="elements">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

# attrs
# 除了根据节点名查询，我们也可以传入一些属性来查询
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

# 常用的属性比如id和class也可以直接传入
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))

# text
# text参数可用来匹配节点的文本，传入的形式可以是字符串可以是正则表达式
import re
html = """
<div class="panel">
<div class="panel-body">
<a>Hello, this is a link</a>
<a>Hello, this is a link, too</a>
</div>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.find_all(text=re.compile('link')))

# find() 返回第一个而匹配的元素
html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-smaill" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

# 其他一些常见方法
# find_parents() 和 find_parent(): 前者返回所有祖先节点，后者返回直接父节点
# find_next_siblings() 和 find_next_sibling(): 前者返回后面所有的兄弟节点，后者返回后米娜第一个兄弟节点。
# find_previous_siblings() 和 find_previous_sibling(): 前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点
# find_all_next() 和 find_next(): 前者返回节点后所有符合条件的节点，后面返回第一个符合条件的节点。
# find_all_previous() 和 find_previous(): 前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。

# CSS选择器
# 使用 CSS选择器时，只需要调用select()方法,传入响应的CSS选择器即可
html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

# select() 同样支持嵌套选择。例如先选择所有ul节点，再遍历每个ul节点，选择其li节点，样例如下。
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul.select('li'))

# 获取属性
soup = BeautifulSoup(html, 'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取文本 可以使用string和get_text()
soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print('String:', li.string)

# BeautifulSoup注意事项
# 推荐使用lxml及解析库，必要时使用html.parser。
# 节点选择筛选功能弱但是速度快
# 建议使用find()或者find_all()查询匹配单个结果或者多个结果
# 如果对CSS选择器熟悉的话，可以使用select()方法选择
