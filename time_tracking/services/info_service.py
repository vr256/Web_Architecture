import logging

from flask import current_app as app
from ..tools import Connection_Factory, DAO_Factory
from ..properties import LOG_FORMAT, LOG_PATHES, ROLES, ERRORS

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

class InfoService:
    @staticmethod
    def convert_time(time_spent: str):
        hours = time_spent.seconds // 3600
        minutes = time_spent.seconds // 60 % 60
        seconds = time_spent.seconds % 60
        return f'{hours}:{minutes}:{seconds}'

    @staticmethod
    def get_activities(login : str):
        try:
            with Connection_Factory.get_cnx(app.config['dbms'], app.config['db']) as cnx:
                dao_activity = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('activity')
                dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
                dao_time = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('time_tracking')
                user = dao_user.find_by_login(cnx, login)
                time_records = dao_time.find_by_user_id(cnx, user.user_id)
                activities = [dao_activity.find_by_id(cnx, record.activity_id) for record in time_records]
                time_values = [InfoService.convert_time(record.time_spent) for record in time_records]
                result_dict = {activity.name_activity: time_val for activity, time_val in zip(activities, time_values)}
                return result_dict
        except Exception:
            logging.exception('')