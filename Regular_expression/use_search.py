import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
#result = re.match('Hello.*?(\d+).*?Demo', content)
# content 字符串以Extra 开头，正则表达式以Hello 开头故result 为 None
# match()方法在使用时需要考虑到开头的内容，因此match不适合做匹配，更适合做检测。
# 将上面的match修改为search方法
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))