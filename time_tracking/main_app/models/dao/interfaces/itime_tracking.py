from abc import ABCMeta, abstractmethod


class ITimeTracking_DAO(metaclass=ABCMeta):
    @abstractmethod
    def select_all(self):
        '''
        Should return list of users,
        activities and time spent on them
        '''

    @abstractmethod
    def find_by_user_id(self, user_id):
        '''
        Should return list of activities 
        and time spent on them by given user
        '''

    @abstractmethod
    def find_by_activity_id(self, activity_id):
        '''
        Should return list of users and 
        time spent by them on given activity
        '''

    @abstractmethod
    def find_by_action_id(self, action_id):
        '''
        Should return list of users and 
        activities with given action
        '''

    @abstractmethod
    def insert(self, time_trackings):
        '''
        Should insert given list of users,
        activities and time spent on them
        '''

    @abstractmethod
    def update(self, time_trackings):
        '''
        Should update given list of users,
        activities and time spent on them
        '''

    @abstractmethod
    def delete(self, time_trackings):
        '''
        Should delete given list of users,
        activities and time spent on them
        '''