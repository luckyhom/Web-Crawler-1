import requests

# requests.get('http://httpbin.org/cookies/set/number/1234567')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
# 上述放方法无法获取cookies

s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)