from abc import ABCMeta, abstractmethod


class IRole_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self):
        '''
        Should return list of roles
        '''

    @abstractmethod
    def find_by_id(self, id):
        '''
        Should return role with given name 
        or False if no such role found
        '''

    @abstractmethod
    def find_by_name(self, name):
        '''
        Should return role with given name 
        or False if no such role found
        '''

    @abstractmethod
    def insert(self, roles):
        '''
        Should insert given list of roles
        '''

    @abstractmethod
    def update(self, roles):
        '''
        Should update given list of roles
        '''

    @abstractmethod
    def delete(self, roles):
        '''
        Should delete given list of roles 
        '''