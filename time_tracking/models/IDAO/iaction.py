from abc import ABCMeta, abstractmethod
from typing import List, Union
from .. import *
from ...connector import IConnection

class IAction_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self, connection : IConnection) -> List[Action]:
        '''
        Should return list of actions
        '''

    @abstractmethod
    def find_by_name(self, connection : IConnection, name : str) -> Union[Action, bool]:
        '''
        Should return action with given name 
        or False if no such action found
        '''

    @abstractmethod
    def insert(self, connection : IConnection, actions : List[Action]):
        '''
        Should insert given list of actions
        '''

    @abstractmethod
    def update(self, connection : IConnection, actions : List[Action]):
        '''
        Should update given list of actions
        '''

    @abstractmethod
    def delete(self, connection : IConnection, actions : List[Action]):
        '''
        Should delete given list of actions 
        '''