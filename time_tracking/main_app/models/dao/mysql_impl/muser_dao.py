from typing import List, Union
from django.db import transaction
from django.apps import apps
from ....tools import singleton
from ..interfaces import IUser_DAO


User = apps.get_model('main_app', 'User')

@singleton
class MUser_DAO(IUser_DAO):
    def select_all(self) -> List[User]:
        users = User.objects.all()
        return users if users else False

    def find_by_login(self, login : str) -> Union[User, bool]:
        user = User.objects.filter(login=login).first()
        return user if user else False
    
    def find_by_email(self, email : str) -> Union[User, bool]:
        user = User.objects.filter(email=email).first()
        return user if user else False

    def find_last(self) -> Union[User, bool]:
        user = User.objects.latest('user_id')
        return user if user else False
    
    def insert(self, users : List[User]):
        with transaction.atomic():
            User.objects.bulk_create(users)

    def update(self, users : List[User]):
        with transaction.atomic():
            for user in users:
                User.objects.filter(user_id=user.user_id).update(
                    login=user.login,
                    email=user.email,
                    password=user.password,
                    role_id=user.role.role_id
                )

    def delete(self, users : List[User]):
        with transaction.atomic():
            for user in users:
                User.objects.filter(user_id=user.user_id).delete()