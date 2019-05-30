import requests

proxies = {
    'http': 'http://user:password@10.10.1.10:3128/',
}
requests.get('http://www.taobao.com', proxies=proxies)