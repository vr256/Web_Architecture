from django.db import models


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    name_activity = models.CharField(max_length=100)
    category = models.ForeignKey('Category', related_name='activities', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'activity'

    def __repr__(self) -> str:
         return f'Activity(activity_id={self.activity_id!r}, name_activity={self.name_activity!r}, category_id={self.category_id!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, Activity) and self.name_activity == other.name_activity

    def __hash__(self) -> int:
        return hash(self.name_activity)