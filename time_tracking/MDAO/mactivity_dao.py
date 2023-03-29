import logging
import mysql.connector

from typing import List, Union
from ..utills import singleton
from ..IDAO.iactivity import IActivity_DAO
from ..models.activity import Activity

logging.basicConfig(level=logging.DEBUG, filename="../logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

@singleton
class MActivity_DAO(IActivity_DAO):
    def __init__(self, connection):
        self.cnx = connection.cnx

    def select_all(self) -> List[Activity]:
        cursor = self.cnx.cursor()
        query = 'SELECT * FROM activity;'
        cursor.execute(query)
        roles = [Activity(*i) for i in cursor.fetchall()]
        cursor.close()
        return roles

    def find_by_name(self, name : str) -> Union[Activity, bool]:
        cursor = self.cnx.cursor()
        query = f'SELECT * FROM activity WHERE name_activity="{name}";'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        if result:
            return Activity(*result[0])
        return False

    def insert(self, activities : List[Activity]):
        try:
            cursor = self.cnx.cursor()
            for activity in activities:
                query = 'INSERT INTO activity (name_activity, category_id)\n' + \
                        f'VALUES ("{activity.name_activity}", {activity.category_id});'
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def update(self, activities : List[Activity]):
        try:
            cursor = self.cnx.cursor()
            for activity in activities:
                query = 'UPDATE activity\n' + \
                        f'SET name_activity="{activity.name_activity}", category_id={activity.category_id}\n' + \
                        f'WHERE activity_id={activity.activity_id};'
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def delete(self, activities : List[Activity]):
        cursor = self.cnx.cursor()
        for activity in activities:
            query = 'DELETE FROM activity\n' + \
                    f'WHERE name_activity="{activity.name_activity}";'
            cursor.execute(query)
        self.cnx.commit()
        cursor.close()