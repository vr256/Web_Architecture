from abc import ABCMeta, abstractmethod


class ICategory_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self):
        '''
        Should return list of categories
        '''

    @abstractmethod
    def find_by_name(self, name):
        '''
        Should return category with given name 
        or False if no such category found
        '''

    @abstractmethod
    def insert(self, categories):
        '''
        Should insert given list of categories
        '''

    @abstractmethod
    def update(self, categories):
        '''
        Should update given list of categories
        '''

    @abstractmethod
    def delete(self, categories):
        '''
        Should delete given list of categories 
        '''