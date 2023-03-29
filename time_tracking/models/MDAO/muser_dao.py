import logging
import mysql.connector

from typing import List, Union
from ...utills import singleton
from .. import *

logging.basicConfig(level=logging.DEBUG, filename="../logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

@singleton
class MUser_DAO(IUser_DAO):
    def select_all(self, connection) -> List[User]:
        cursor = connection.cnx.cursor()
        query = 'SELECT * FROM user;'
        cursor.execute(query)
        users = [User(*i) for i in cursor.fetchall()]
        cursor.close()
        return users

    def find_by_login(self, connection, login : str) -> Union[User, bool]:
        cursor = connection.cnx.cursor()
        query = f'SELECT * FROM user WHERE login="{login}";'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if result:
            return User(*result[0])
        return False
    
    def find_by_email(self, connection, email : str) -> Union[User, bool]:
        cursor = connection.cnx.cursor()
        query = f'SELECT * FROM user WHERE email="{email}";'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if result:
            return User(*result[0])
        return False
    
    def insert(self, connection, users : List[User]):
        try:
            cursor = connection.cnx.cursor()
            for user in users:
                query = 'INSERT INTO user (login, password, email, role_id)\n' + \
                        f'VALUES ("{user.login}", "{user.password}", "{user.email}", {user.role_id});'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def update(self, connection, users : List[User]):
        try:
            cursor = connection.cnx.cursor()
            for user in users:
                query = 'UPDATE user\n' + \
                        f'SET login="{user.login}", password="{user.password}", ' + \
                        f'email="{user.email}", role_id={user.role_id}\n' + \
                        f'WHERE user_id={user.user_id};'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def delete(self, connection, users : List[User]):
        cursor = connection.cnx.cursor()
        for user in users:
            query = 'DELETE FROM user\n' + \
                    f'WHERE login="{user.login}";'
            cursor.execute(query)
        connection.cnx.commit()
        cursor.close()