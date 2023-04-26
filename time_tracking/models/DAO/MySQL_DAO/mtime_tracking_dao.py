import logging

from typing import List
from sqlalchemy import select, update, delete, and_
from sqlalchemy.exc import SQLAlchemyError
from ....tools import singleton
from ...entities import TimeTracking
from ..IDAO import ITimeTracking_DAO
from ....properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class MTimeTracking_DAO(ITimeTracking_DAO):
    def select_all(self, connection) -> List[TimeTracking]:
        try:
            select_stmt = select(TimeTracking)
            time_trackings = connection.scalars(select_stmt)
            return time_trackings if time_trackings else False
        except SQLAlchemyError:
            logging.exception('')

    def find_by_user_id(self, connection, user_id : int) -> List[TimeTracking]:
        try:
            select_stmt = select(TimeTracking).where(TimeTracking.user_id == user_id)
            time_tracking = connection.scalars(select_stmt)
            return time_tracking if time_tracking else False
        except SQLAlchemyError:
            logging.exception('')
    
    def find_by_activity_id(self, connection, activity_id : int) -> List[TimeTracking]:
        try:
            select_stmt = select(TimeTracking).where(TimeTracking.activity_id == activity_id)
            time_tracking = connection.scalars(select_stmt)
            return time_tracking if time_tracking else False
        except SQLAlchemyError:
            logging.exception('')
    
    def find_by_action_id(self, connection, action_id : int) -> List[TimeTracking]:
        try:
            select_stmt = select(TimeTracking).where(TimeTracking.action_id == action_id)
            time_tracking = connection.scalars(select_stmt)
            return time_tracking if time_tracking else False
        except SQLAlchemyError:
            logging.exception('')
            connection.rollback()

    def insert(self, connection, time_trackings : List[TimeTracking]):
        try:
            connection.add_all(time_trackings)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def update(self, connection, time_trackings : List[TimeTracking]):
        try:
            for time_tracking in time_trackings:
                update_stmt = update(TimeTracking).where(and_(
                TimeTracking.action_id == time_tracking.action_id,
                TimeTracking.user_id == time_tracking.user_id,
                TimeTracking.activity_id == time_tracking.activity_id
                )).values(
                action_id=time_tracking.action_id,
                user_id=time_tracking.user_id,
                activity_id=time_tracking.activity_id,
                time_spent=time_tracking.time_spent
                )
                connection.execute(update_stmt)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def delete(self, connection, time_trackings : List[TimeTracking]):
        try:
            for time_tracking in time_trackings:
                delete_stmt = delete(TimeTracking).where(and_(
                TimeTracking.action_id == time_tracking.action_id,
                TimeTracking.user_id == time_tracking.user_id,
                TimeTracking.activity_id == time_tracking.activity_id
                ))                
                connection.execute(delete_stmt)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')