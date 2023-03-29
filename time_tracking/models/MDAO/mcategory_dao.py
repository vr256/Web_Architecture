import logging
import mysql.connector

from typing import List, Union
from ...utills import singleton
from .. import *

logging.basicConfig(level=logging.DEBUG, filename="../logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

@singleton
class MCategory_DAO(ICategory_DAO):
    def select_all(self, connection) -> List[Category]:
        cursor = connection.cnx.cursor()
        query = 'SELECT * FROM category;'
        cursor.execute(query)
        categories = [Category(*i) for i in cursor.fetchall()]
        cursor.close()
        return categories

    def find_by_name(self, connection, name : str) -> Union[Category, bool]:
        cursor = connection.cnx.cursor()
        query = f'SELECT * FROM category WHERE name_category="{name}";'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if result:
            return Category(*result[0])
        return False

    def insert(self, connection, categories : List[Category]):
        try:
            cursor = connection.cnx.cursor()
            for category in categories:
                query = 'INSERT INTO category (name_category)\n' + \
                        f'VALUES ("{category.name_category}");'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def update(self, connection, categories : List[Category]):
        try:
            cursor = connection.cnx.cursor()
            for category in categories:
                query = 'UPDATE category\n' + \
                        f'SET name_category="{category.name_category}"\n' + \
                        f'WHERE category_id={category.category_id};'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def delete(self, connection, categories : List[Category]):
        cursor = connection.cnx.cursor()
        for category in categories:
            query = 'DELETE FROM category\n' + \
                    f'WHERE name_category="{category.name_category}";'
            cursor.execute(query)
        connection.cnx.commit()
        cursor.close()