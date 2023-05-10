import re

from django.conf import settings
from ..tools import encrypt, DAO_Factory
from ..models import User


DBMS = settings.DBMS
ROLES = settings.ROLES
VALIDATORS = settings.VALIDATORS
ERRORS = settings.ERRORS

class AuthService:
    @staticmethod
    def get_role(role_id : int):
        dao_role = DAO_Factory.get_dao(DBMS).get_dao_implementation('role')
        role = dao_role.find_by_id(role_id)
        return role.name_role

    @staticmethod
    def get_by_creds(credentials : str):
        dao_user = DAO_Factory.get_dao(DBMS).get_dao_implementation('user')
        user_by_login = dao_user.find_by_login(credentials)
        user_by_email = dao_user.find_by_email(credentials)
        if user_by_login:
            return user_by_login
        return user_by_email

    @staticmethod
    def get_last():
        dao_user = DAO_Factory.get_dao(DBMS).get_dao_implementation('user')
        return dao_user.find_last()

    @staticmethod
    def check_password(password : str, user : User):
        return encrypt(password, user.login) != user.password
    
    @staticmethod
    def check_accessibility(login : str, email : str):
        dao_user = DAO_Factory.get_dao(DBMS).get_dao_implementation('user')
        user_by_login = dao_user.find_by_login(login)
        user_by_email = dao_user.find_by_email(email)
        if user_by_login:
            return 'REG_NAME'
        if user_by_email:
            return 'REG_EMAIL'

    @staticmethod
    def sign_up(login : str, email : str, password: str):
        dao_user = DAO_Factory.get_dao(DBMS).get_dao_implementation('user')
        current_id = AuthService.get_last().user_id
        user = User(user_id=current_id + 1, login=login, email=email, \
                    password=encrypt(password, login), role_id=ROLES['user'])
        dao_user.insert([user])
        return user

    @staticmethod
    def validate_data(data : str, dtype : str):
        is_valid = re.fullmatch(VALIDATORS[f'{dtype}'], data)
        return True if is_valid else ERRORS[f'INVALID_{dtype.upper()}']
    
    @staticmethod
    def check_data(login : str, email : str, password: str):
        login_validity = AuthService.validate_data(login, 'login')
        if login_validity != True:
            return login_validity
        
        email_validity = AuthService.validate_data(email, 'email')
        if email_validity != True:
            return email_validity
        
        password_validity = AuthService.validate_data(password, 'password')
        if password_validity != True:
            return password_validity
        
        return True
