from abc import ABCMeta, abstractmethod
from typing import List, Union
from ..models.role import Role

class IRole_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self) -> List[Role]:
        '''
        Should return list of roles
        '''

    @abstractmethod
    def find_by_name(self, name : str) -> Union[Role, bool]:
        '''
        Should return role with given name 
        or False if no such role found
        '''

    @abstractmethod
    def insert(self, roles : List[Role]):
        '''
        Should insert given list of roles
        '''

    @abstractmethod
    def update(self, roles : List[Role]):
        '''
        Should update given list of roles
        '''

    @abstractmethod
    def delete(self, roles : List[Role]):
        '''
        Should delete given list of roles 
        '''