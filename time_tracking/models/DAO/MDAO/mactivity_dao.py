import logging
import mysql.connector

from typing import List, Union
from ....tools import singleton
from ...entities import Activity
from ..IDAO import IActivity_DAO
from ....properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class MActivity_DAO(IActivity_DAO):
    def select_all(self, connection) -> List[Activity]:
        cursor = connection.cnx.cursor()
        query = 'SELECT * FROM activity;'
        cursor.execute(query)
        roles = [Activity(*i) for i in cursor.fetchall()]
        cursor.close()
        return roles

    def find_by_name(self, connection, name : str) -> Union[Activity, bool]:
        cursor = connection.cnx.cursor()
        query = f'SELECT * FROM activity WHERE name_activity="{name}";'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if result:
            return Activity(*result[0])
        return False

    def insert(self, connection, activities : List[Activity]):
        try:
            cursor = connection.cnx.cursor()
            for activity in activities:
                query = 'INSERT INTO activity (name_activity, category_id)\n' + \
                        f'VALUES ("{activity.name_activity}", {activity.category_id});'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def update(self, connection, activities : List[Activity]):
        try:
            cursor = connection.cnx.cursor()
            for activity in activities:
                query = 'UPDATE activity\n' + \
                        f'SET name_activity="{activity.name_activity}", category_id={activity.category_id}\n' + \
                        f'WHERE activity_id={activity.activity_id};'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def delete(self, connection, activities : List[Activity]):
        cursor = connection.cnx.cursor()
        for activity in activities:
            query = 'DELETE FROM activity\n' + \
                    f'WHERE name_activity="{activity.name_activity}";'
            cursor.execute(query)
        connection.cnx.commit()
        cursor.close()