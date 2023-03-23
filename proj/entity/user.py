class User:
    def __init__(self, user_id : int, login, password, email : str, role_id : int):
        self._user_id = user_id
        self._login = login
        self._password = password
        self._email = email
        self._role_id = role_id

    def __str__(self) -> str:
        return f'{self._user_id, self._login, self._password, self._email, self._role_id}'

    def __eq__(self, other) -> bool:
        return isinstance(other, User) and self._login == other._login
    
    def __hash__(self) -> int:
        return hash(self._login)

    @property
    def user_id(self) -> int:
        return self._user_id
    
    @user_id.setter
    def user_id(self, val : int):
        self.user_id = val

    @property
    def login(self) -> str:
        return self._login
    
    @login.setter
    def login(self, val : str):
        self._login = val

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, val : str):
        self._password = val

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, val : str):
        self._email = val

    @property
    def role_id(self) -> int:
        return self._role_id
    
    @role_id.setter
    def role_id(self, val : int):
        self._role_id = val