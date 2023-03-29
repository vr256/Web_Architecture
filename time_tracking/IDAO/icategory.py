from abc import ABCMeta, abstractmethod
from typing import List, Union
from ..models.category import Category


class ICategory_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self) -> List[Category]:
        '''
        Should return list of categories
        '''

    @abstractmethod
    def find_by_name(self, name : str) -> Union[Category, bool]:
        '''
        Should return category with given name 
        or False if no such category found
        '''

    @abstractmethod
    def insert(self, categories : List[Category]):
        '''
        Should insert given list of categories
        '''

    @abstractmethod
    def update(self, categories : List[Category]):
        '''
        Should update given list of categories
        '''

    @abstractmethod
    def delete(self, categories : List[Category]):
        '''
        Should delete given list of categories 
        '''