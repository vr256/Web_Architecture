from django.db import models


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name_role = models.CharField(max_length=25)

    class Meta:
        db_table = 'role'

    def __repr__(self) -> str:
        return f'Role(role_id={self.role_id!r}, name_role={self.name_role!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, Role) and self.name_role == other.name_role
    
    def __hash__(self) -> int:
        return hash(self.name_role)