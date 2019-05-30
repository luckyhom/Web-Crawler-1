import requests

cookies = '_zap=92a13a24-6eb2-4402-b4d6-1acffac37717;' \
          '_xsrf=LG89ZxUHrY4TGfrauikQBH00wXhsr1t4;' \
          'd_c0="ANBg6u-7FA-PTvcNdZG1snIACZULL1pwaNw=|1551869481";' \
          '__utmv=51854390.100-1|2=registration_date=20181207=1^3=entry_date=20181207=1;' \
          'q_c1=f698710b5fbe49d69fab6b8f87b89ecf|1557211541000|1551869512000;' \
          'l_cap_id="NTNkNDU0YjQ4YWQ0NGViZWJjMzJhNWU3OGNmZjc1ODY=|1557730185|fd92c4d004953be4fc2a9727b9e74e936a94f09a";' \
          'r_cap_id="ZTM1NTZhYjY1NWYxNGJhNjkzMjc5NmQ2MjczYjZhZjM=|1557730185|f64e44f650688f960e98ac92f26397a25da173b7";' \
          'cap_id="NWVlMzRiODg1NmYzNDY2YWE2ZWIzYjI5YzIwNGM5M2Q=|1557730185|8f1ed0a0071f9718f1fa95b73150de614508dfca";' \
          'capsion_ticket="2|1:0|10:1557730189|14:capsion_ticket|44:NzdhZGQwNjUzOWZkNDZjMWFhYTYwMTc2NDgyZGYyMjQ=|7cc7e620bf50f2b482186809278f0cbdb125daa19f50c2b809da89f1f7db8d59";' \
          'z_c0="2|1:0|10:1557730198|4:z_c0|92:Mi4xNTk1dERRQUFBQUFBMEdEcTc3c1VEeVlBQUFCZ0FsVk5sbUhHWFFEMEh1X2U0dHFyRDZ2c1hwa01Ucmk4V3o3YVVn|2a58a037d74705b6fbb9dcaec20a2e83b3095b29133600a31e7486a1630e9cb5";' \
          'utma=51854390.1896794676.1555256057.1557843346.1558347703.12;' \
          '__utmz=51854390.1558347703.12.12.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/;' \
          'tst=r; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c'
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host': 'www.zhihu.com',
    'User-agent': 'Mozilla/5.0 (Maintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/53.0.2785.116 Safari/537.36'
}
for cookie in cookies.split(';'):
    key, value = cookies.split('=', 1)
    jar.set(key, value)
r = requests.get('https://www.zhihu.com', cookies=jar, headers=headers)
print(r.text)
