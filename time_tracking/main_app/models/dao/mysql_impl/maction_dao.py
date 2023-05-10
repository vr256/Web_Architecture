from typing import List, Union
from django.db import transaction
from django.apps import apps
from ....tools import singleton
from ..interfaces import IAction_DAO


Action = apps.get_model('main_app', 'Action')

@singleton
class MAction_DAO(IAction_DAO):
    def select_all(self) -> List[Action]:
        actions = Action.objects.all()
        return actions if actions else False          

    def find_by_name(self, name : str) -> Union[Action, bool]:
        action = Action.objects.filter(name_action=name).first()
        return action if action else False
        
    def insert(self, actions : List[Action]):
        with transaction.atomic():
            Action.objects.bulk_create(actions)
            
    def update(self, actions : List[Action]):
        with transaction.atomic():
            for action in actions:
                Action.objects.filter(action_id=action.action_id).update(
                    name_action=action.name_action
                    )
            
    def delete(self, actions : List[Action]):
        with transaction.atomic():
            for action in actions:
                Action.objects.filter(action_id=action.action_id).delete()