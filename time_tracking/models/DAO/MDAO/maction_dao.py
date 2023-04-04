import logging
import mysql.connector

from typing import List, Union
from ....tools import singleton
from ...entities import Action
from ..IDAO import IAction_DAO
from ....properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class MAction_DAO(IAction_DAO):
    def select_all(self, connection) -> List[Action]:
        try:
            cursor = connection.cnx.cursor()
            query = 'SELECT * FROM action;'
            cursor.execute(query)
            actions = [Action(*i) for i in cursor.fetchall()]
            return actions
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()
        

    def find_by_name(self, connection, name : str) -> Union[Action, bool]:
        try:
            cursor = connection.cnx.cursor()
            query = f'SELECT * FROM action WHERE name_action="{name}";'
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                return Action(*result[0])
            return False
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def insert(self, connection, actions : List[Action]):
        try:
            cursor = connection.cnx.cursor()
            for action in actions:
                query = 'INSERT INTO action (name_action)\n' + \
                        f'VALUES ("{action.name_action}");'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def update(self, connection, actions : List[Action]):
        try:
            cursor = connection.cnx.cursor()
            for action in actions:
                query = 'UPDATE action\n' + \
                        f'SET name_action="{action.name_action}"\n' + \
                        f'WHERE action_id={action.action_id};'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def delete(self, connection, actions : List[Action]):
        try:
            cursor = connection.cnx.cursor()
            for action in actions:
                query = 'DELETE FROM action\n' + \
                        f'WHERE name_action="{action.name_action}";'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()