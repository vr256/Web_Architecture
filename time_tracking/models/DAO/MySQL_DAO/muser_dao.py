import logging

from typing import List, Union
from sqlalchemy import select, update, delete, desc
from sqlalchemy.exc import SQLAlchemyError
from ....tools import singleton
from ...entities import User
from ..IDAO import IUser_DAO
from ....properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class MUser_DAO(IUser_DAO):
    def select_all(self, connection) -> List[User]:
        try:
            select_stmt = select(User)
            users = connection.scalars(select_stmt)
            return users if users else False
        except SQLAlchemyError:
            logging.exception('')

    def find_by_login(self, connection, login : str) -> Union[User, bool]:
        try:
            select_stmt = select(User).where(User.login == login)
            user = connection.scalars(select_stmt).one()
            return user if user else False
        except SQLAlchemyError:
            logging.exception('')
    
    def find_by_email(self, connection, email : str) -> Union[User, bool]:
        try:
            select_stmt = select(User).where(User.email == email)
            user = connection.scalars(select_stmt).one()
            return user if user else False
        except SQLAlchemyError:
            logging.exception('')

    def find_last(self, connection) -> Union[User, bool]:
        try:
            select_stmt = select(User).order_by(desc(User.user_id)).limit(1)
            user = connection.scalars(select_stmt).one()
            return user if user else False
        except SQLAlchemyError:
            logging.exception('')
    
    def insert(self, connection, users : List[User]):
        try:
            connection.add_all(users)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def update(self, connection, users : List[User]):
        try:
            for user in users:
                update_stmt = update(User).where(User.user_id == user.user_id).values(
                    login=user.login,
                    email=user.email,
                    password=user.password,
                    role_id=user.role_id)
                connection.execute(update_stmt)

            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def delete(self, connection, users : List[User]):
        try:
            for user in users:
                delete_stmt = delete(User).where(User.user_id == user.user_id)
                connection.execute(delete_stmt)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')