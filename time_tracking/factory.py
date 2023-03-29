from .models import MUser_DAO, MRole_DAO, MCategory_DAO, MActivity_DAO, MAction_DAO, MTimeTracking_DAO
from .connector import IDatabase, IConnection, MySQL_DB, MySQL_CNX

class MySQL_DAO_Factory:
    @staticmethod
    def get_dao_implementation(connection : IConnection, option : str):
        m_dao = {
            'user': MUser_DAO, 
            'role': MRole_DAO,
            'category': MCategory_DAO,
            'activity': MActivity_DAO,
            'action': MAction_DAO,
            'time_tracking': MTimeTracking_DAO
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