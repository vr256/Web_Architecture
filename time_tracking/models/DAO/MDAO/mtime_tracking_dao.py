import logging
import mysql.connector

from typing import List
from ....tools import singleton
from ...entities import TimeTracking
from ..IDAO import ITimeTracking_DAO
from ....properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class MTimeTracking_DAO(ITimeTracking_DAO):
    def select_all(self, connection) -> List[TimeTracking]:
        cursor = connection.cnx.cursor()
        query = 'SELECT * FROM time_tracking;'
        cursor.execute(query)
        time_trackings = [TimeTracking(*i) for i in cursor.fetchall()]
        cursor.close()
        return time_trackings

    def find_by_user_id(self, connection, user_id : int) -> List[TimeTracking]:
        cursor = connection.cnx.cursor()
        query = f'SELECT * FROM time_tracking WHERE user_id={user_id};'
        cursor.execute(query)
        time_trackings = [TimeTracking(*i) for i in cursor.fetchall()]
        cursor.close()
        return time_trackings
    
    def find_by_activity_id(self, connection, activity_id : int) -> List[TimeTracking]:
        cursor = connection.cnx.cursor()
        query = f'SELECT * FROM time_tracking WHERE activity_id={activity_id};'
        cursor.execute(query)
        time_trackings = [TimeTracking(*i) for i in cursor.fetchall()]
        cursor.close()
        return time_trackings
    
    def find_by_action_id(self, connection, action_id : int) -> List[TimeTracking]:
        cursor = connection.cnx.cursor()
        query = f'SELECT * FROM time_tracking WHERE action_id={action_id};'
        cursor.execute(query)
        time_trackings = [TimeTracking(*i) for i in cursor.fetchall()]
        cursor.close()
        return time_trackings

    def insert(self, connection, time_trackings : List[TimeTracking]):
        try:
            cursor = connection.cnx.cursor()
            for time_track in time_trackings:
                query = 'INSERT INTO time_tracking (activity_id, user_id, action_id, time_spent)\n' + \
                        f'VALUES ({time_track.activity_id}, {time_track.user_id}, ' + \
                        f'{time_track.action_id}, "{time_track.time_spent}");'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def update(self, connection, time_trackings : List[TimeTracking]):
        try:
            cursor = connection.cnx.cursor()
            for time_track in time_trackings:
                query = 'UPDATE time_tracking\n' + \
                        f'SET activity_id={time_track.activity_id}, user_id={time_track.user_id}, ' + \
                        f'action_id={time_track.action_id}, time_spent="{time_track.time_spent}"\n' + \
                        f'WHERE activity_id={time_track.activity_id} AND user_id={time_track.user_id} ' + \
                        f'AND action_id={time_track.action_id};'
                cursor.execute(query)
            connection.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
            connection.cnx.rollback()
        finally:
            cursor.close()

    def delete(self, connection, time_trackings : List[TimeTracking]):
        cursor = connection.cnx.cursor()
        for time_track in time_trackings:
            query = 'DELETE FROM time_tracking\n' + \
                    f'WHERE activity_id={time_track.activity_id} ' + \
                    f'AND user_id={time_track.user_id} ' + \
                    f'AND action_id={time_track.action_id};'
            cursor.execute(query)
        connection.cnx.commit()
        cursor.close()