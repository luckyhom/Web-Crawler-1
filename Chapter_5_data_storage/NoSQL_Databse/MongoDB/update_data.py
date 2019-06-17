import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students

student = {
    'id': '20171010',
    'name': 'Kevin',
    'age': 22,
    'gender': 'male',
}

collection.insert_one(student)

condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
# 还可以使用$set操作符对数据进行更新
# result = condition.update(condition, {'$set': student})
# 这样只更新student字典内存在的字段。如果之前还有其他字段，则不会更新，也不会删除，若不用$set，则会把之前的数据全部用student字典替换，
# 如果原本存在其他字段，则被删除
print(result)
# update()方法其实也是官方不推荐的方法。官方推荐的方法分为 update_one()和update_many()，他们的第二个参数需要使用$类型操作符作为字典的键名
# 示例如下
condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)

# 另一个例子
condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
