from django.conf import settings
from ..tools import DAO_Factory


DBMS = settings.DBMS

class AdminService:
    @staticmethod
    def get_users():
        dao_user = DAO_Factory.get_dao(DBMS).get_dao_implementation('user')
        users = dao_user.select_all()
        return users
