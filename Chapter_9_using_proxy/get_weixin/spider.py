import requests

from pyquery import PyQuery as pq
from requests import Session
from requests import ReadTimeout
from requests import ConnectionError
from urllib.parse import urlencode

from config import PROXY_POOL_URL
from config import MAX_FAILED_TIME
from config import VALID_STATUSES
from mysql import MySQL
from redisqueue import RedisQueue
from weixinrequest import WeixinRequest


class Spider():
    base_url = 'https://weixin.sogou.com/weixin'
    keyword = 'Python'
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
    session = Session()
    queue = RedisQueue()
    mysql = MySQL()

    def get_proxy(self):
        """
        从代理池中获取代理
        :return:
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('Get Proxy', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None

    def start(self):
        """
        初始化工作
        :return:
        """
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'query': self.keyword, 'type': 2})
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.queue.add(weixin_request)

    def parse_index(self, response):
        """
        解析索引页
        :param response: 响应
        :return: 新的响应
        """
        doc = pq(response)
        items = doc('.new-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = item.attr('href')
            weixin_request = WeixinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.base_url + str(next)
            weixin_request = WeixinRequest(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request

    def parse_detail(self, response):
        """
        解析详情页
        :param response: 响应
        :return: 公众号文章
        """
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text(),
            'data': doc('#post-data').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        yield data

    def request(self, weixin_request):
        """
        执行请求
        :param weixin_request: 请求
        :return: 响应
        """
        try:
            if weixin_request.need_proxy:
                propxy = self.get_proxy()
                if propxy:
                    proxies = {
                        'http': 'http://' + propxy,
                        'https': 'https://' + propxy,
                    }
                    return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout,
                                             allow_redirects=False, proxies=proxies)
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timout, allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            return False

    def error(self, weixin_request):
        """
        错误处理
        :param weixin_request: 请求
        :return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('Request fail', weixin_request.fail_time, 'Times', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            callback = weixin_request.callback
            print('Schedule', weixin_request.url)
            response = self.request(weixin_request)
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print('New Result', result)
                        if isinstance(result, WeixinRequest):
                            self.queue.add(result)
                        if isinstance(result, dict):
                            self.mysql.insert('articles', result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def run(self):
        """
        入口
        :return:
        """
        self.start()
        self.schedule()


if __name__ == '__main__':
    spider = Spider()
    spider.run()