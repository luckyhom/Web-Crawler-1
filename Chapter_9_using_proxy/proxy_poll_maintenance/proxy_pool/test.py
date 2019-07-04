from db import RedisClient
from crawler import Crawler


if __name__ == "__main__":
    redisclient = RedisClient()
    print(redisclient.count())
    crawler = Crawler()
    results = crawler.crawl_dail66()
    for result in results:
        print(result)
