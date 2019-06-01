import requests
import re


def get_one_page(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko)'
                      'Chrome/65.0.3325.162 Safari/537.36',
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        html = response.text
        pattern = re.compile(
            '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>'
            + '.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
            re.S
        )
        items = re.findall(pattern, html)
        print(items)

    return None


def main():
    url = 'https://maoyan.com/board/4'
    get_one_page(url)


main()