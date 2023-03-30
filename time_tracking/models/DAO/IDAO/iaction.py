from abc import ABCMeta, abstractmethod
from typing import List, Union
from ...entities import Action

class IAction_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self, connection) -> List[Action]:
        '''
        Should return list of actions
        '''

    @abstractmethod
    def find_by_name(self, connection, name : str) -> Union[Action, bool]:
        '''
        Should return action with given name 
        or False if no such action found
        '''

    @abstractmethod
    def insert(self, connection, actions : List[Action]):
        '''
        Should insert given list of actions
        '''

    @abstractmethod
    def update(self, connection, actions : List[Action]):
        '''
        Should update given list of actions
        '''

    @abstractmethod
    def delete(self, connection, actions : List[Action]):
        '''
        Should delete given list of actions 
        '''