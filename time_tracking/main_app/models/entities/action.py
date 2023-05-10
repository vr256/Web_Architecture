from django.db import models


class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    name_action = models.CharField(max_length=55)

    class Meta:
        db_table = 'action'

    def __repr__(self) -> str:
         return f'Action(action_id={self.action_id!r}, name_action={self.name_action!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, Action) and self.name_action == other.name_action
    
    def __hash__(self) -> int:
        return hash(self.name_action)