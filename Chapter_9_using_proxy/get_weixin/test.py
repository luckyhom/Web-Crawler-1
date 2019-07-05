import requests


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'SUV=00EE712F77F8F1285C9A141F36334105; ABTEST=0|1562225137|v1; IPLOC=CN4403; SUID=1C013C3A4A42910A000000005D1DA9F1; SUID=1C013C3A5218910A000000005D1DA9F2; weixinIndexVisited=1; sct=1; SNUID=43615C5A5F65ECB5BB7AE454600977ED; ppinf=5|1562234904|1563444504|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo3OnN0aWNrZXJ8Y3J0OjEwOjE1NjIyMzQ5MDR8cmVmbmljazo3OnN0aWNrZXJ8dXNlcmlkOjQ0Om85dDJsdU9oeDFXdktJNm1GLV9JSk1PZ241NHdAd2VpeGluLnNvaHUuY29tfA; pprdig=j3pXVh43ek0qmlyN738VY_0Lno7YTfzPO1-52g0fRZ3SW93xnLY_uCVNTjYNKkADx0ySyXYgvrWojM6Lb8vFNzELWfGt6IoZ-G7QiYNH83yeiXZ2j4y1fexHB--636SyKIU_My2i1UdrvvNOQnSWUC-iVWJd04vyVl0ZQCpbHpo; sgid=12-41039275-AV0d0BgzrgksahCjtjianUTM; ppmdig=1562306345000000b94d15df908fdedf755f385f9678951a; JSESSIONID=aaasgD9OOLOWpcz5edkRw',
    'DNT': '1',
    'Host': 'weixin.sougou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}
proxy = '117.87.178.88:9000'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
base_url = 'https://weixin.sogou.com/weixin?query=Python&type=2'
try:
    response = requests.get(base_url, headers=None, proxies=None)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('error:', e.args)


