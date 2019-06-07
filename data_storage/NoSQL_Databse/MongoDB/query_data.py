import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

result = collection.find_one({'name': 'Jordan'})
print(type(result))
print(result)

results = collection.find({'age': 20})
print(type(results))
print(results)
for result in results:
    print(result)

# 计数
count = collection.find().count()
print(type(count))
print(count)

# 排序
results = collection.find().sort('name', pymongo.ASCENDING)
# pymongo.ASENDING 升序，pymongo.DESENDING 降序
print([result['name'] for result in results])

# 偏移，使用skip()方法
results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

# limit()方法指定要区的结果个数
results = collection.find().sort('name', pymongo.ASCENDING).limit(2)
print([result['name'] for result in results])

# 在数据库数量非常庞大的时候不要使用大的偏移量来查询，这样可能导致内存溢出。此时可以使用下面的操作
from bson.objectid import ObjectId
results = collection.find({'_id': {'$gt': ObjectId('5cf9f690785d4f381da11929')}})  # 此时需要记住上次查询的id
print([result['name'] for result in results])




