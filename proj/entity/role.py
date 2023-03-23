class Role:
    def __init__(self, role_id : int, name_role : str):
        self._role_id = role_id
        self._name_role = name_role

    def __str__(self) -> str:
        return f'{self._role_id, self._name_role}'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Role) and self._name_role == other._name_role
    
    def __hash__(self) -> int:
        return hash(self._name_role)

    @property
    def role_id(self) -> int:
        return self._role_id
    
    @role_id.setter
    def role_id(self, val : int):
        self._role_id = val

    @property
    def name_role(self) -> str:
        return self._name_role
    
    @name_role.setter
    def name_role(self, val : str):
        self._name_role = val