import re

content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content)  # sub()方法有三个参数，第一个参数用来匹配，第二个参数为替换成的字符，第三个参数是用于筛选的字符。
print(content)