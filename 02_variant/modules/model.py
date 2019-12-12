import sqlite3
import controller


class DBData:
    """ реализовать singltone"""
    """получает данные из БД"""

    def __init__(self):
        self.conn = sqlite3.connect("sqlite.db")
        self.cursor = self.conn.cursor()
        self.buyers_list = self.read_buyers()
        print(*self.buyers_list, sep='\n')
        self.product_list = self.read_product()
        print(*self.product_list, sep='\n')

    def read_buyers(self):
        """ берет данные о покупателях из БД
        и делает список из объектов buyers на их основании """
        buyers_list = []
        query = "SELECT * FROM buyers WHERE status = 'Buyer'"
        for row in self.cursor.execute(query):
            buyers_list.append()
        return self.cursor.fetchall()

    def read_product(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()


if __name__ == "__main__":
    a = DBData()
