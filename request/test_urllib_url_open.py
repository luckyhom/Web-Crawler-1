import urllib.request

response = urllib.request.urlopen('https://www.python.org')
blog_response = urllib.request.urlopen('http://211.159.153.80')
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
print(blog_response.read().decode('utf-8'))
