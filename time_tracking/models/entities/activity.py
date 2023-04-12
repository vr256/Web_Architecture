class Activity:
    def __init__(self, activity_id: int, name_activity: str, category_id: int):
        self._activity_id = activity_id
        self._name_activity = name_activity
        self._category_id = category_id

    def __str__(self) -> str:
        return f'{self._activity_id, self._category_id, self._name_activity}'

    def __eq__(self, other) -> bool:
        return isinstance(other, Activity) and self._name_activity == other._name_activity

    def __hash__(self) -> int:
        return hash(self._name_activity)

    @property
    def activity_id(self) -> int:
        return self._activity_id

    @activity_id.setter
    def activity_id(self, val: int):
        self._activity_id = val

    @property
    def category_id(self) -> int:
        return self._category_id

    @category_id.setter
    def category_id(self, val: int):
        self._category_id = val

    @property
    def name_activity(self) -> str:
        return self._name_activity

    @name_activity.setter
    def name_activity_id(self, val: str):
        self._name_activity = val
