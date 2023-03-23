class Category:
    def __init__(self, category_id : int, name_category : str):
        self._category_id = category_id
        self._name_category = name_category

    def __str__(self) -> str:
        return f'{self._category_id, self._name_category}'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Category) and self._name_category == other._name_category

    def __hash__(self) -> int:
        return hash(self._name_category)

    @property
    def category_id(self) -> int:
        return self._category_id
    
    @category_id.setter
    def category_id(self, val : int):
        self._category_id = val

    @property
    def name_category(self) -> str:
        return self._name_category
    
    @name_category.setter
    def name_category(self, val : str):
        self._name_category = val