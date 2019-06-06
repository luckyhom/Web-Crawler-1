import pymysql

id = '20120001'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='Xiaoai@0013', port=3306, db='spiders')
cursor = db.cursor()
sql = "INSERT INTO students(id, user, age) values(%s, %s, %S)"
try:
    cursor.execute(sql)
    db.commit()  # 数据插入、更新、删除操作，都需要调用该方法才能生效
except:
    db.rollback()
db.close()