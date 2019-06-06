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