import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)  # result 是一个SRE_Match对象有两个方法group() 和 span()
print(result)
print(result.group())  # group() 方法可以输出匹配到的内容
print(result.span())  # span() 方法可以输出匹配的范围，即匹配到的结果字符串在原字符串中的位置范围
