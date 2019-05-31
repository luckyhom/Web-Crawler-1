from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'germy',
}
headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11_4) AppleWebKit/573.36 (KHTML, like Gecko)'
                  'Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url=url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)