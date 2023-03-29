import logging
import mysql.connector

from typing import List, Union
from ...utills import singleton
from .. import *

logging.basicConfig(level=logging.DEBUG, filename="../logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

@singleton
class MRole_DAO(IRole_DAO):
    def select_all(self, connection) -> List[Role]:
        cursor = connection.cnx.cursor()
        query = 'SELECT * FROM role;'
        cursor.execute(query)
        roles = [Role(*i) for i in cursor.fetchall()]
        cursor.close()
        return roles

    def find_by_name(self, connection, name : str) -> Union[Role, bool]:
        cursor = connection.cnx.cursor()
        query = f'SELECT * FROM role WHERE name_role="{name}";'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if result:
            return Role(*result[0])
        return False

    def insert(self, connection, roles : List[Role]):
        try:
            cursor = connection.cnx.cursor()
            for role in roles:
                query = 'INSERT INTO role (name_role)\n' + \
                        f'VALUES ("{role.name_role}");'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def update(self, connection, roles : List[Role]):
        try:
            cursor = connection.cnx.cursor()
            for role in roles:
                query = 'UPDATE role\n' + \
                        f'SET name_role="{role.name_role}"\n' + \
                        f'WHERE role_id={role.role_id};'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def delete(self, connection, roles : List[Role]):
        cursor = connection.cnx.cursor()
        for role in roles:
            query = 'DELETE FROM role\n' + \
                    f'WHERE name_role="{role.name_role}";'
            cursor.execute(query)
        connection.cnx.commit()
        cursor.close()