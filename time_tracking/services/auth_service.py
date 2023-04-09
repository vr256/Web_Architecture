import logging

from flask import current_app as app
from ..tools import encrypt, singleton, Connection_Factory, DAO_Factory
from ..properties import LOG_FORMAT, LOG_PATHES
from ..models import User

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class AuthService:
    def get_role(sefl, role_id : int):
        try:
            with Connection_Factory.get_cnx(app.config['dbms'], app.config['db']) as cnx:
                dao_role = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('role')
                role = dao_role.find_by_id(cnx, role_id)
                return role.name_role
        except Exception:
            logging.exception('')

    def get_by_creds(self, credentials : str):
        try:
            with Connection_Factory.get_cnx(app.config['dbms'], app.config['db']) as cnx:
                dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
                user_by_login = dao_user.find_by_login(cnx, credentials)
                user_by_email = dao_user.find_by_email(cnx, credentials)
                if user_by_login:
                    return user_by_login
                return user_by_email
        except Exception:
            logging.exception('')

    def check_password(self, password : str, user : User):
        return encrypt(password, user.login) != user.password
