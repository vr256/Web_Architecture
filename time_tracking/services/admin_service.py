import logging

from flask import current_app as app
from ..tools import singleton, Connection_Factory, DAO_Factory
from ..properties import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class AdminService:
    def get_users(self):
        try:
            cnx = Connection_Factory.get_cnx(app.config['dbms'], app.config['db'])
            dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
            users = dao_user.select_all(cnx)
            return users
        except Exception:
            logging.exception('')
        finally:
            del cnx
