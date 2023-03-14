import logging
import mysql.connector

from typing import List
from lab1.utills import singleton
from lab1.IDAO.itime_tracking import ITimeTracking_DAO
from lab1.entity.time_tracking import TimeTracking

logging.basicConfig(level=logging.DEBUG, filename="logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

@singleton
class MTimeTracking_DAO(ITimeTracking_DAO):
    def __init__(self, connection):
        self.cnx = connection.cnx

    def select_all(self) -> List[TimeTracking]:
        cursor = self.cnx.cursor()
        query = 'SELECT * FROM time_tracking;'
        cursor.execute(query)
        time_trackings = [TimeTracking(*i) for i in cursor.fetchall()]
        cursor.close()
        return time_trackings

    def find_by_user_id(self, user_id : int) -> List[TimeTracking]:
        cursor = self.cnx.cursor()
        query = f'SELECT * FROM time_tracking WHERE user_id={user_id};'
        cursor.execute(query)
        time_trackings = [TimeTracking(*i) for i in cursor.fetchall()]
        cursor.close()
        return time_trackings
    
    def find_by_activity_id(self, activity_id : int) -> List[TimeTracking]:
        cursor = self.cnx.cursor()
        query = f'SELECT * FROM time_tracking WHERE activity_id={activity_id};'
        cursor.execute(query)
        time_trackings = [TimeTracking(*i) for i in cursor.fetchall()]
        cursor.close()
        return time_trackings
    
    def find_by_action_id(self, action_id : int) -> List[TimeTracking]:
        cursor = self.cnx.cursor()
        query = f'SELECT * FROM time_tracking WHERE action_id={action_id};'
        cursor.execute(query)
        time_trackings = [TimeTracking(*i) for i in cursor.fetchall()]
        cursor.close()
        return time_trackings

    def insert(self, time_trackings : List[TimeTracking]):
        try:
            cursor = self.cnx.cursor()
            for time_track in time_trackings:
                query = 'INSERT INTO time_tracking (activity_id, user_id, action_id, time_spent)\n' + \
                        f'VALUES ({time_track.activity_id}, {time_track.user_id}, ' + \
                        f'{time_track.action_id}, "{time_track.time_spent}");'
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def update(self, time_trackings : List[TimeTracking]):
        try:
            cursor = self.cnx.cursor()
            for time_track in time_trackings:
                query = 'UPDATE time_tracking\n' + \
                        f'SET activity_id={time_track.activity_id}, user_id={time_track.user_id}, ' + \
                        f'action_id={time_track.action_id}, time_spent="{time_track.time_spent}"\n' + \
                        f'WHERE activity_id={time_track.activity_id} AND user_id={time_track.user_id} ' + \
                        f'AND action_id={time_track.action_id};'
                cursor.execute(query)
            self.cnx.commit()
        except mysql.connector.Error:
            logging.exception('')
        finally:
            cursor.close()

    def delete(self, time_trackings : List[TimeTracking]):
        cursor = self.cnx.cursor()
        for time_track in time_trackings:
            query = 'DELETE FROM time_tracking\n' + \
                    f'WHERE activity_id={time_track.activity_id} ' + \
                    f'AND user_id={time_track.user_id} ' + \
                    f'AND action_id={time_track.action_id};'
            cursor.execute(query)
        self.cnx.commit()
        cursor.close()