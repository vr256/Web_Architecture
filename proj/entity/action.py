class Action:
    def __init__(self, action_id : int, name_action : str):
        self._action_id = action_id
        self._name_action = name_action

    def __str__(self) -> str:
        return f'{self._action_id, self._name_action}'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Action) and self._name_action == other._name_action
    
    def __hash__(self) -> int:
        return hash(self._name_action)
    
    @property
    def action_id(self) -> int:
        return self._action_id
    
    @action_id.setter
    def action_id(self, val : int):
        self._action_id = val

    @property
    def name_action(self) -> str:
        return self._name_action
    
    @name_action.setter
    def name_action(self, val : str):
        self._name_action = val