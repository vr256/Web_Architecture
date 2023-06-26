from django.db import models


class TimeTracking(models.Model):
    time_tracking_id = models.AutoField(primary_key=True)
    activity = models.ForeignKey('Activity', related_name='time_trackings',
                                 on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='time_trackings',
                             on_delete=models.CASCADE)
    action = models.ForeignKey('Action', related_name='time_trackings',
                               on_delete=models.CASCADE)
    time_spent = models.DateTimeField(null=True)

    class Meta:
        db_table = 'time_tracking'
        unique_together = ('activity', 'user', 'action')

    def __repr__(self) -> str:
        return f'TimeTracking(activity_id={self.activity_id!r}, user_id={self.user_id!r}, action_id={self.action_id!r}), time_spent={self.time_spent!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, TimeTracking) and       \
            self.activity_id == other.activity_id and    \
            self.user_id == other.user_id and            \
            self.action_id == other.action_id

    def __hash__(self) -> int:
        return hash((self.activity_id, self.user_id, self.action_id))
