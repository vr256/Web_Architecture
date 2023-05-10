from abc import ABCMeta, abstractmethod


class IActivity_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self):
        '''
        Should return list of activities
        '''

    @abstractmethod
    def find_by_name(self, name):
        '''
        Should return activity with given name 
        or False if no such activity found
        '''

    @abstractmethod
    def insert(self, activities):
        '''
        Should insert given list of activities
        '''

    @abstractmethod
    def update(self, activities):
        '''
        Should update given list of activities
        '''

    @abstractmethod
    def delete(self, activities):
        '''
        Should delete given list of activities 
        '''