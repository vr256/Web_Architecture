from abc import ABCMeta, abstractmethod
from typing import List, Union
from ...entities import User

class IUser_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self, connection) -> List[User]:
        '''
        Should return list of users
        '''

    @abstractmethod
    def find_by_login(self, connection, login : str) -> Union[User, bool]:
        '''
        Should return user with given login 
        or False if no such user found
        '''

    @abstractmethod
    def find_by_email(self, connection, email : str) -> Union[User, bool]:
        '''
        Should return user with given email 
        or False if no such user found
        '''

    @abstractmethod
    def insert(self, connection, users : List[User]):
        '''
        Should insert given list of users
        '''

    @abstractmethod
    def update(self, connection, users : List[User]):
        '''
        Should update given list of users
        '''

    @abstractmethod
    def delete(self, connection, users : List[User]):
        '''
        Should delete given list of users and 
        '''