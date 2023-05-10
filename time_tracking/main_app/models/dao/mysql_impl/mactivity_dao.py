from typing import List, Union
from django.db import transaction
from django.apps import apps
from ....tools import singleton
from ..interfaces import IActivity_DAO


Activity = apps.get_model('main_app', 'Activity')

@singleton
class MActivity_DAO(IActivity_DAO):
    def select_all(self) -> List[Activity]:
        activities = Activity.objects.all()
        return activities if activities else False        
            
    def find_by_id(self, id : int) -> Union[Activity, bool]:
        activity = Activity.objects.filter(activity_id=id).first()
        return activity if activity else False
    
    def find_by_name(self, name : str) -> Union[Activity, bool]:
        activity = Activity.objects.filter(name_activity=name).first()
        return activity if activity else False   
        
    def insert(self, activities : List[Activity]):
        with transaction.atomic():
            Activity.objects.bulk_create(activities)
            
    def update(self, activities : List[Activity]):
        with transaction.atomic():
            for activity in activities:
                Activity.objects.filter(activity_id=activity.activity_id).update(
                    name_activity=activity.name_activity,
                    category_id=activity.category.category_id,
                )
            
    def delete(self, activities : List[Activity]):
        with transaction.atomic():
            for activity in activities:
                Activity.objects.filter(activity_id=activity.activity_id).delete()