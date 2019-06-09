import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

result = collection.remove({'name': 'Kevin'})
print(result)

# 两个推荐的方法 delete_one() delete_many()
result = collection.delete_one({'name': 'Kevin'})  # 删除第一条符合
print(result)
print(result.deleted_count)

result = collection.delete_many({'age': {'$lt': 25}})  # 删除所有符合数据
print(result.deleted_count)