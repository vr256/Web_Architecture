from abc import ABCMeta, abstractmethod


class IAction_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self):
        '''
        Should return list of actions
        '''

    @abstractmethod
    def find_by_name(self, name):
        '''
        Should return action with given name 
        or False if no such action found
        '''

    @abstractmethod
    def insert(self, actions):
        '''
        Should insert given list of actions
        '''

    @abstractmethod
    def update(self, actions):
        '''
        Should update given list of actions
        '''

    @abstractmethod
    def delete(self, actions):
        '''
        Should delete given list of actions
        '''
