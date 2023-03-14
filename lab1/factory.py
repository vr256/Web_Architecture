from lab1.MDAO import mactivity_dao, mcategory_dao, mrole_dao, mtime_tracking_dao, muser_dao, maction_dao
from lab1.connector import *

class MySQL_DAO_Factory:
    @staticmethod
    def get_dao_implementation(connection : IConnection, option : str):
        m_dao = {
            'user': muser_dao.MUser_DAO, 
            'role': mrole_dao.MRole_DAO,
            'category': mcategory_dao.MCategory_DAO,
            'activity': mactivity_dao.MActivity_DAO,
            'action': maction_dao.MAction_DAO,
            'time_tracking': mtime_tracking_dao.MTimeTracking_DAO
                 }
        if option.lower() not in m_dao:
            return False
        return m_dao[option.lower()](connection)


class DAO_Factory:
    @staticmethod
    def get_dao(option : str):
        dbms_dao = {
            'mysql': MySQL_DAO_Factory
            }
        if option.lower() not in dbms_dao:
            return False
        return dbms_dao[option.lower()]


class DB_Factory:
    @staticmethod
    def get_db(option : str):
        dbms = {
            'mysql': MySQL_DB
            }
        if option.lower() not in dbms:
            return False
        return dbms[option.lower()]()
    

class Connection_Factory:
    @staticmethod
    def get_cnx(option, db : str):
        dbms = {
            'mysql': MySQL_CNX
            }
        if option.lower() not in dbms:
            return False
        return dbms[option.lower()](db)