from typing import List, Union
from django.db import transaction
from django.apps import apps
from ....tools import singleton
from ..interfaces import IRole_DAO


Role = apps.get_model('main_app', 'Role')

@singleton
class MRole_DAO(IRole_DAO):
    def select_all(self) -> List[Role]:
        roles = Role.objects.all()
        return roles if roles else False

    def find_by_id(self, id : int) -> Union[Role, bool]:
        role = Role.objects.get(role_id=id)
        return role if role else False

    def find_by_name(self, name : str) -> Union[Role, bool]:
        role = Role.objects.get(role_name=name)
        return role if role else False

    def insert(self, roles : List[Role]):
        with transaction.atomic():
            Role.objects.bulk_create(roles)

    def update(self, roles : List[Role]):
        with transaction.atomic():
            for role in roles:
                Role.objects.filter(role_id=role.role_id).update(
                    name_role=role.name_role
                )

    def delete(self, roles : List[Role]):
        with transaction.atomic():
            for role in roles:
                Role.objects.filter(role_id=role.role_id).delete()