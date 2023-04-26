import logging

from typing import List, Union
from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError
from ....tools import singleton
from ...entities import Role
from ..IDAO import IRole_DAO
from ....properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class MRole_DAO(IRole_DAO):
    def select_all(self, connection) -> List[Role]:
        try:
            select_stmt = select(Role)
            roles = connection.scalars(select_stmt)
            return roles if roles else False
        except SQLAlchemyError:
            logging.exception('')

    def find_by_id(self, connection, id : int) -> Union[Role, bool]:
        try:
            select_stmt = select(Role).where(Role.role_id == id)
            role = connection.scalars(select_stmt).one()
            return role if role else False
        except SQLAlchemyError:
            logging.exception('')

    def find_by_name(self, connection, name : str) -> Union[Role, bool]:
        try:
            select_stmt = select(Role).where(Role.name_role == name)
            role = connection.scalars(select_stmt).one()
            return role if role else False
        except SQLAlchemyError:
            logging.exception('')

    def insert(self, connection, roles : List[Role]):
        try:
            connection.add_all(roles)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def update(self, connection, roles : List[Role]):
        try:
            for role in roles:
                update_stmt = update(Role).where(Role.role_id == role.role_id).values(
                    name_role=role.name_role)
                connection.execute(update_stmt)

            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def delete(self, connection, roles : List[Role]):
        try:
            for role in roles:
                delete_stmt = delete(Role).where(Role.role_id == role.role_id)
                connection.execute(delete_stmt)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')