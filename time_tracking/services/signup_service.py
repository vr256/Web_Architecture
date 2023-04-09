import logging

from flask import current_app as app
from ..tools import encrypt, singleton, Connection_Factory, DAO_Factory
from ..properties import LOG_FORMAT, LOG_PATHES
from ..models import User

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

@singleton
class SignupService:
    pass