class TimeTracking:
    def __init__(self, activity_id, user_id, action_id : int, time_spent : str):
        self._activity_id = activity_id
        self._user_id = user_id
        self._action_id = action_id
        self._time_spent = time_spent 

    def __str__(self) -> str:
        return f'{self._activity_id, self._user_id, self._time_spent}'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, TimeTracking) and \
               self._activity_id == other._activity_id and \
               self._user_id == other._user_id and \
               self._action_id == other._action_id

    def __hash__(self) -> int:
        return hash((self._activity_id, self._user_id, self._action_id))

    @property
    def activity_id(self) -> int:
        return self._activity_id
    
    @activity_id.setter
    def activity_id(self, val : int):
        self._activity_id = val

    @property
    def user_id(self) -> int:
        return self._user_id
    
    @user_id.setter
    def user_id(self, val : int):
        self._user_id = val

    @property
    def action_id(self) -> int:
        return self._action_id
    
    @action_id.setter
    def action_id(self, val : int):
        self._action_id = val

    @property
    def time_spent(self) -> str:
        return self._time_spent
    
    @time_spent.setter
    def time_spent(self, val : str):
        self._time_spent = val