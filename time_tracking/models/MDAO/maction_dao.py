import logging
import mysql.connector

from typing import List, Union
from ...utills import singleton
from .. import *

logging.basicConfig(level=logging.DEBUG, filename="../logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

@singleton
class MAction_DAO(IAction_DAO):
    def __init__(self, connection):
        self.cnx = connection.cnx

    def select_all(self) -> List[Action]:
        cursor = self.cnx.cursor()
        query = 'SELECT * FROM action;'
        cursor.execute(query)
        actions = [Action(*i) for i in cursor.fetchall()]
        cursor.close()
        return actions

    def find_by_name(self, name : str) -> Union[Action, bool]:
        cursor = self.cnx.cursor()
        query = f'SELECT * FROM action WHERE name_action="{name}";'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if result:
            return Action(*result[0])
        return False

    def insert(self, actions : List[Action]):
        try:
            cursor = self.cnx.cursor()
            for action in actions:
                query = 'INSERT INTO action (name_action)\n' + \
                        f'VALUES ("{action.name_action}");'
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def update(self, actions : List[Action]):
        try:
            cursor = self.cnx.cursor()
            for action in actions:
                query = 'UPDATE action\n' + \
                        f'SET name_action="{action.name_action}"\n' + \
                        f'WHERE action_id={action.action_id};'
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def delete(self, actions : List[Action]):
        cursor = self.cnx.cursor()
        for action in actions:
            query = 'DELETE FROM action\n' + \
                    f'WHERE name_action="{action.name_action}";'
            cursor.execute(query)
        self.cnx.commit()
        cursor.close()