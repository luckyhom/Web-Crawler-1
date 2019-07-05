import pymysql

from config import MYSQL_HOST
from config import MYSQL_USER
from config import MYSQL_PASSWORD
from config import MYSQL_PORT
from config import MYSQL_DATABASE


class MySQL():
    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 database=MYSQL_DATABASE):
        """
        MySQL 初始化
        :param host: 数据库地址
        :param username: 数据库用户名
        :param password: 数据库密码
        :param port: 数据库端口
        :param database: 数据库名称
        """
        try:
            self.db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
            self.cursor = self.db.cursor()
        except pymysql.MySQLError as e:
            print(e.args)

    def insert(self, table, data):
        """
        插入数据
        :param table:
        :param data:
        :return:
        """
        keys = ', '.join(data.keys)
        values = ', '.join(['%s'] * len(data))
        sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cursor.excute(sql_query, tuple(data, keys, values))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
