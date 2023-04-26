from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Category(Base):

    __tablename__ = 'category'

    category_id: Mapped[int] = mapped_column(primary_key=True)
    name_category: Mapped[str] = mapped_column(String(40))

    activities: Mapped[List['Activity']] = relationship(back_populates='category', cascade='all')

    def __repr__(self) -> str:
         return f'Category(category_id={self.category_id!r}, name_category={self.name_category!r})'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Category) and self.name_category == other.name_category

    def __hash__(self) -> int:
        return hash(self.name_category)