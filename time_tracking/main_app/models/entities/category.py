from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=40)

    class Meta:
        db_table = 'category'

    def __repr__(self) -> str:
        return f'Category(category_id={self.category_id!r}, name_category={self.name_category!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, Category) and self.name_category == other.name_category

    def __hash__(self) -> int:
        return hash(self.name_category)