from ..models.dao.mysql_impl.mrole_dao import MRole_DAO
from ..models.dao.mysql_impl.muser_dao import MUser_DAO 


class MySQL_DAO_Factory:
    @staticmethod
    def get_dao_implementation(option : str):
        m_dao = {
            'user': MUser_DAO, 
            'role': MRole_DAO
                 }
        if option.lower() not in m_dao:
            return False
        return m_dao[option.lower()]()


class DAO_Factory:
    @staticmethod
    def get_dao(option : str):
        dbms_dao = {
            'mysql': MySQL_DAO_Factory
            }
        if option.lower() not in dbms_dao:
            return False
        return dbms_dao[option.lower()]