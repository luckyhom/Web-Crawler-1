import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)  # 贪婪匹配尽可能匹配多的字符
result = re.match('^He.*?(\d+).*Demo', content)  # 非贪婪匹配尽可能匹配少的字符
print(result)
print(result.group())
print(result.group(1))
# 总结在匹配时，字符串中间尽量使用非贪婪匹配，也就是用 .*? 来代替 .* ，以免出现匹配结果确实的情况。但在结尾时使用 .*? 可能匹配不到任何内容。
