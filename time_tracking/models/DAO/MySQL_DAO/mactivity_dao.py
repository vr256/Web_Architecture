import logging

from typing import List, Union
from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError
from ....tools import singleton
from ...entities import Activity
from ..IDAO import IActivity_DAO
from ....properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class MActivity_DAO(IActivity_DAO):
    def select_all(self, connection) -> List[Activity]:
        try:
            select_stmt = select(Activity)
            activities = connection.scalars(select_stmt)
            return activities if activities else False
        except SQLAlchemyError:
            logging.exception('')

    def find_by_id(self, connection, id : int) -> Union[Activity, bool]:
        try:
            select_stmt = select(Activity).where(Activity.activity_id == id)
            activity = connection.scalars(select_stmt).one()
            return activity if activity else False
        except SQLAlchemyError:
            logging.exception('')

    def find_by_name(self, connection, name : str) -> Union[Activity, bool]:
        try:
            select_stmt = select(Activity).where(Activity.name_activity == name)
            activity = connection.scalars(select_stmt).one()
            return activity if activity else False
        except SQLAlchemyError:
            logging.exception('')

    def insert(self, connection, activities : List[Activity]):
        try:
            connection.add_all(activities)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def update(self, connection, activities : List[Activity]):
        try:
            for activity in activities:
                update_stmt = update(Activity).where(Activity.activity_id == activity.activity_id).values(
                    name_activity=activity.name_activity,
                    category_id=activity.category_id)
                connection.execute(update_stmt)

            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def delete(self, connection, activities : List[Activity]):
        try:
            for activity in activities:
                delete_stmt = delete(Activity).where(Activity.activity_id == activity.activity_id)
                connection.execute(delete_stmt)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')