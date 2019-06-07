from redis import StrictRedis

redis = StrictRedis()
redis.set('name', 'Bob')
print(redis.get('name'))