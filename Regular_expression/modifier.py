import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
# result = re.match('^He.*?Demo$', content)  # 使用这个表达式无法匹配content 中的换行符，会产生AttributeError
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)  # 增加一个修饰符 re.S 即可解决上面那行代码的问题，这个修饰符的作用就是是 .
# 匹配包括换行符在内的所有字符
print(result.group(1))
