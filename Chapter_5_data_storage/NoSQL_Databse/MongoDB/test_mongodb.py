import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
# 使用下面方式可以与上面等同
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test
# db = client['test']

collection = db.students
# collection = db['students']

# 插入数据
student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male',
}

result = collection.insert_one(student)
print(result)

student1 = {
    'id': '20170102',
    'name': 'Bob',
    'age': 20,
    'gender': 'male',
}

student2 = {
    'id': '20170103',
    'name': 'Tom',
    'age': 20,
    'gender': 'male',
}
result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
