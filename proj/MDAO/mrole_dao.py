import logging
import mysql.connector

from typing import List, Union
from ..utills import singleton
from ..IDAO.irole import IRole_DAO
from ..entity.role import Role

logging.basicConfig(level=logging.DEBUG, filename="logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

@singleton
class MRole_DAO(IRole_DAO):
    def __init__(self, connection):
        self.cnx = connection.cnx

    def select_all(self) -> List[Role]:
        cursor = self.cnx.cursor()
        query = 'SELECT * FROM role;'
        cursor.execute(query)
        roles = [Role(*i) for i in cursor.fetchall()]
        cursor.close()
        return roles

    def find_by_name(self, name : str) -> Union[Role, bool]:
        cursor = self.cnx.cursor()
        query = f'SELECT * FROM role WHERE name_role="{name}";'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if result:
            return Role(*result[0])
        return False

    def insert(self, roles : List[Role]):
        try:
            cursor = self.cnx.cursor()
            for role in roles:
                query = 'INSERT INTO role (name_role)\n' + \
                        f'VALUES ("{role.name_role}");'
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def update(self, roles : List[Role]):
        try:
            cursor = self.cnx.cursor()
            for role in roles:
                query = 'UPDATE role\n' + \
                        f'SET name_role="{role.name_role}"\n' + \
                        f'WHERE role_id={role.role_id};'
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def delete(self, roles : List[Role]):
        cursor = self.cnx.cursor()
        for role in roles:
            query = 'DELETE FROM role\n' + \
                    f'WHERE name_role="{role.name_role}";'
            cursor.execute(query)
        self.cnx.commit()
        cursor.close()