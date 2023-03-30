from abc import ABCMeta, abstractmethod
from typing import List, Union
from ...entities import Category

class ICategory_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self, connection) -> List[Category]:
        '''
        Should return list of categories
        '''

    @abstractmethod
    def find_by_name(self, connection, name : str) -> Union[Category, bool]:
        '''
        Should return category with given name 
        or False if no such category found
        '''

    @abstractmethod
    def insert(self, connection, categories : List[Category]):
        '''
        Should insert given list of categories
        '''

    @abstractmethod
    def update(self, connection, categories : List[Category]):
        '''
        Should update given list of categories
        '''

    @abstractmethod
    def delete(self, connection, categories : List[Category]):
        '''
        Should delete given list of categories 
        '''