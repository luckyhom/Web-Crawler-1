import pymysql

db = pymysql.connect(host='localhost', user='root', password='Xiaoai@0013', port=3306, db='spiders')
cursor = db.cursor()
sql = "UPDATE students SET age = %S WHERE name = %S"
try:
    cursor.execute(sql, (25, 'Bob'))
    db.commit()
except:
    db.rollback()
db.close()

# 字典传参和去重之后的更新
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}

db = pymysql.connect(host='localhost', user='root', password='Xiaoai@0013', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
