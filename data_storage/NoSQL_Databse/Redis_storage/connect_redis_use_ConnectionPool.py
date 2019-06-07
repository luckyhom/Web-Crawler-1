from redis import StrictRedis, ConnectionPool

pool = ConnectionPool()
redis = StrictRedis(connection_pool=pool)
print(redis.get('name'))
print(redis.dbsize())
print(redis.ttl('name'))

