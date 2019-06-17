import pymysql

db = pymysql.connect(host='localhost', user='root', password='Xiaoai@0013', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition ='age > 20'

sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
try:
    cursor.execute(sql)
    db.commit()
    print('Successful')
except:
    db.rollback()

db.close()
