from abc import ABCMeta, abstractmethod
from typing import List, Union
from ...entities import Role

class IRole_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self, connection) -> List[Role]:
        '''
        Should return list of roles
        '''

    @abstractmethod
    def find_by_id(self, connection, id : int) -> Union[Role, bool]:
        '''
        Should return role with given name 
        or False if no such role found
        '''

    @abstractmethod
    def find_by_name(self, connection, name : str) -> Union[Role, bool]:
        '''
        Should return role with given name 
        or False if no such role found
        '''

    @abstractmethod
    def insert(self, connection, roles : List[Role]):
        '''
        Should insert given list of roles
        '''

    @abstractmethod
    def update(self, connection, roles : List[Role]):
        '''
        Should update given list of roles
        '''

    @abstractmethod
    def delete(self, connection, roles : List[Role]):
        '''
        Should delete given list of roles 
        '''