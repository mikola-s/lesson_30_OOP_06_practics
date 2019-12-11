import sqlite3


class DBData:
    def __init__(self):
        self.conn = sqlite3.connect('sqlite.db')
        self.cursor = self.conn.cursor()
        self.users_list = self.create_users()
        self.product_list = self.create_product()

    def create_users(self):
        pass

    def create_product(self):
        pass
