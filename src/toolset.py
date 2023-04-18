import mysql.connector

from options import Options


class Tool:
    def __init__(self, options: Options, connector=mysql.connector):
        self.mysql_connector = connector
        self.options = options

    def connect(self):
        self.conn = self.mysql_connector.connect(
            user=self.options.username,
            password=self.options.password,
            host=self.options.host,
            port=self.options.port,
            database=self.options.database,
        )

    def query(self, query, param):
        cur = self.conn.cursor()
        cur.execute(query, param)
        return cur
