import json

str = '''
[{
    "name": "BOb",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)  # 使用loads() 方法把字符串转换为json对象
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))

