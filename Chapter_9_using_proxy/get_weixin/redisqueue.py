import redis
import requests
from pickle import dumps, loads
from .weixinrequest import WeixinRequest


PROXY_POOL_URL = 'http://127.0.0.1:5555/random'


class RedisQueue():
    def __init__(self):
        """
        初始化Redis
        """
        self.db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self, request, fail_time):
        """
        向队列添加序列化后的Request
        :param request: 请求对象
        :param fail_time: 失败次数
        :return: 添加结果
        """
        if isinstance(request, WeixinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))

    def pop(self):
        """
        取出下一个Request并反序列化
        :return: Reuqest or None
        """
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0
