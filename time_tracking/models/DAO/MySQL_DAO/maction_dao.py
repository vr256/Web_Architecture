import logging

from typing import List, Union
from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError
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
            select_stmt = select(Action)
            actions = connection.execute(select_stmt).fetchall()
            return actions if actions else False
        except SQLAlchemyError:
            logging.exception('')
        

    def find_by_name(self, connection, name : str) -> Union[Action, bool]:
        try:
            select_stmt = select(Action).where(Action.name_action == name)
            action = connection.execute(select_stmt).fetchone()
            return action if action else False
        except SQLAlchemyError:
            logging.exception('')

    def insert(self, connection, actions : List[Action]):
        try:
            connection.add_all(actions)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def update(self, connection, actions : List[Action]):
        try:
            for action in actions:
                update_stmt = update(Action).where(Action.action_id == action.action_id).values(
                    name_action=action.name_action)
                connection.execute(update_stmt)

            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def delete(self, connection, actions : List[Action]):
        try:
            for action in actions:
                delete_stmt = delete(Action).where(Action.action_id == action.action_id)
                connection.execute(delete_stmt)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')