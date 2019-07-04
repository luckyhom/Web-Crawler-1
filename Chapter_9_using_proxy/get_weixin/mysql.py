import pymysql

from .config import *


class MySQL():
    def __init__(self, host=MYSQL_HOST, useranme=MYSQL_USER,
                 password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 databse=MYSQL_DATABASE):
        """
        MySQL 初始化
        :param host:
        :param useranme:
        :param password:
        :param port:
        :param databse:
        """
        try:
            self.db = pymysql.connect(host, useranme, password, databse, charset='utf8', port=port)
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
