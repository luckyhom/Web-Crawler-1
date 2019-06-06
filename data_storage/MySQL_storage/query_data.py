import pymysql

db = pymysql.connect(host='localhost', user='root', password='Xiaoai@0013', port=3306, db='spiders')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:',one)
    results = cursor.fetchall()
    print('Results:',results)
    print('Results type:', type(results))
    for row in results:
        print(row)
except:
    print('Error')

# 当数据量不大时可以是fetchaall()获取全部数据，当数据量很大时使用fetch()开销就会很大
# 此时推荐使用如下方法
sql = 'SELECT * FROM students WHERE age >=20'
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')

db.close()
