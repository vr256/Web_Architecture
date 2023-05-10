from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='users')

    class Meta:
        db_table = 'user'

    def __repr__(self) -> str:
        return f'User(user_id={self.user_id!r}, login={self.login!r}, email={self.email!r}, role_id={self.role_id!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, User) and self.login == other.login and self.email == other.email

    def __hash__(self) -> int:
        return hash((self.login, self.email))