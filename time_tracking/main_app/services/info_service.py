from django.conf import settings
from ..tools import DAO_Factory


DBMS = settings.DBMS

class InfoService:
    @staticmethod
    def convert_time(time_spent: str):
        hours = time_spent.seconds // 3600
        minutes = time_spent.seconds // 60 % 60
        seconds = time_spent.seconds % 60
        return f'{hours}:{minutes}:{seconds}'

    @staticmethod
    def get_activities(login : str):
        dao_activity = DAO_Factory.get_dao(DBMS).get_dao_implementation('activity')
        dao_user = DAO_Factory.get_dao(DBMS).get_dao_implementation('user')
        dao_time = DAO_Factory.get_dao(DBMS).get_dao_implementation('time_tracking')
        user = dao_user.find_by_login(login)
        time_records = dao_time.find_by_user(user)
        activities = [dao_activity.find_by_id(record.activity_id) for record in time_records]
        time_values = [InfoService.convert_time(record.time_spent) for record in time_records]
        result_dict = {activity.name_activity: time_val for activity, time_val in zip(activities, time_values)}
        return result_dict