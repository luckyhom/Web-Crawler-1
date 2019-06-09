import pymysql

db = pymysql.connect(host='localhost', user='root', port=3306, password='Xiaoai@0013', db='spiders')
cursor = db.cursor()
sql = "CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL , name VARCHAR(255) NOT NULL," \
      "age INT NOT NULL, PRIMARY KEY (id))"
cursor.execute(sql)
db.close()
