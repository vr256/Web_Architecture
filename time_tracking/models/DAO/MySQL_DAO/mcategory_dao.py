import logging

from typing import List, Union
from sqlalchemy import select, update, delete
from sqlalchemy.exc import SQLAlchemyError
from ....tools import singleton
from ...entities import Category
from ..IDAO import ICategory_DAO
from ....properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class MCategory_DAO(ICategory_DAO):
    def select_all(self, connection) -> List[Category]:
        try:
            select_stmt = select(Category)
            categories = connection.execute(select_stmt).fetchall()
            return categories if categories else False
        except SQLAlchemyError:
            logging.exception('')

    def find_by_name(self, connection, name : str) -> Union[Category, bool]:
        try:
            select_stmt = select(Category).where(Category.name_category == name)
            category = connection.execute(select_stmt).fetchone()
            return category if category else False
        except SQLAlchemyError:
            logging.exception('')

    def insert(self, connection, categories : List[Category]):
        try:
            connection.add_all(categories)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def update(self, connection, categories : List[Category]):
        try:
            for category in categories:
                update_stmt = update(Category).where(Category.category_id == category.category_id).values(
                    name_category=category.name_category)
                connection.execute(update_stmt)

            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')

    def delete(self, connection, categories : List[Category]):
        try:
            for category in categories:
                delete_stmt = delete(Category).where(Category.category_id == category.category_id)
                connection.execute(delete_stmt)
            connection.commit()
        except SQLAlchemyError:
            connection.rollback()
            logging.exception('')