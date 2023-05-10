from abc import ABCMeta, abstractmethod


class IUser_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self):
        '''
        Should return list of users
        '''

    @abstractmethod
    def find_by_login(self, login):
        '''
        Should return user with given login 
        or False if no such user found
        '''

    @abstractmethod
    def find_by_email(self, email):
        '''
        Should return user with given email 
        or False if no such user found
        '''

    @abstractmethod
    def find_last(self):
        '''
        Should return the last user
        or False if there's no users 
        '''


    @abstractmethod
    def insert(self, users):
        '''
        Should insert given list of users
        '''

    @abstractmethod
    def update(self, users):
        '''
        Should update given list of users
        '''

    @abstractmethod
    def delete(self, users):
        '''
        Should delete given list of users and 
        '''