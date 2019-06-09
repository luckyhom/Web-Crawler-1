import re

content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)  # 当遇到用于正则匹配模式的特殊字符是，在前面加反斜线转义一下即可
print(result)
print(result.group())
print(result.span())
