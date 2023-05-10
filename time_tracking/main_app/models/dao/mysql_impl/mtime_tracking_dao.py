from typing import List
from django.db import transaction
from django.apps import apps
from ....tools import singleton
from ..interfaces import ITimeTracking_DAO


TimeTracking = apps.get_model('main_app', 'TimeTracking')

@singleton
class MTimeTracking_DAO(ITimeTracking_DAO):
    def select_all(self) -> List[TimeTracking]:
        time_trackings = TimeTracking.objects.all()
        return time_trackings if time_trackings else False       
            
    def find_by_user(self, user) -> List[TimeTracking]:
        time_trackings = TimeTracking.objects.filter(user=user)
        return list(time_trackings)

    def find_by_activity(self, activity) -> List[TimeTracking]:
        time_trackings = TimeTracking.objects.filter(activity=activity)
        return list(time_trackings)

    def find_by_action(self, action) -> List[TimeTracking]:
        time_trackings = TimeTracking.objects.filter(action=action)
        return list(time_trackings)

    def insert(self, time_trackings : List[TimeTracking]):
        with transaction.atomic():
            TimeTracking.objects.bulk_create(time_trackings)
            
    def update(self, time_trackings : List[TimeTracking]):
        with transaction.atomic():
            for time_tracking in time_trackings:
                TimeTracking.objects.filter(
                    user_id=time_tracking.user_id,
                    activity_id=time_tracking.activity_id).update(
                    action_id=time_tracking.action.action_id,
                    time_spent=time_tracking.time_spent
                )
            
    def delete(self, time_trackings : List[TimeTracking]):
        with transaction.atomic():
            for time_tracking in time_trackings:
                TimeTracking.objects.filter(
                    user_id=time_tracking.user_id,
                    activity_id=time_tracking.activity_id).delete()