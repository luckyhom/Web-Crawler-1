import logging
import requests
logging.captureWarnings(True)
response = requests.get('http://www.12306.cn', verify=False)
print(response.status_code)
