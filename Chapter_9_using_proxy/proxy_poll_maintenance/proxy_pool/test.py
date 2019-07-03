from db import RedisClient

redisclient = RedisClient()
print(redisclient.count())