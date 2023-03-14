from abc import ABCMeta, abstractmethod
from typing import List, Union
from lab1.entity.action import Action

class IAction_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self) -> List[Action]:
        '''
        Should return list of actions
        '''

    @abstractmethod
    def find_by_name(self, name : str) -> Union[Action, bool]:
        '''
        Should return action with given name 
        or False if no such action found
        '''

    @abstractmethod
    def insert(self, actions : List[Action]):
        '''
        Should insert given list of actions
        '''

    @abstractmethod
    def update(self, actions : List[Action]):
        '''
        Should update given list of actions
        '''

    @abstractmethod
    def delete(self, actions : List[Action]):
        '''
        Should delete given list of actions 
        '''