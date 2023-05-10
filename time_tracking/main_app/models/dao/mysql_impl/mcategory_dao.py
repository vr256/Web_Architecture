from typing import List, Union
from django.db import transaction
from django.apps import apps
from ....tools import singleton
from ..interfaces import ICategory_DAO


Category = apps.get_model('main_app', 'Category')

@singleton
class MCategory_DAO(ICategory_DAO):
    def select_all(self) -> List[Category]:
        categories = Category.objects.all()
        return categories if categories else False      
            
    def find_by_name(self, name : str) -> Union[Category, bool]:
        category = Category.objects.get(name_category=name)
        return category if category else False      
            
    def insert(self, categories : List[Category]):
        with transaction.atomic():
            Category.objects.bulk_create(categories)
            
    def update(self, categories : List[Category]):
        with transaction.atomic():
            for category in categories:
                Category.objects.filter(category_id=category.category_id).update(
                    name_category=category.name_category
                )
            
    def delete(self, categories : List[Category]):
       with transaction.atomic():
            for category in categories:
                Category.objects.filter(category_id=category.category_id).delete()