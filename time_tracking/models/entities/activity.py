from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Activity(Base):

    __tablename__ = 'activity'

    activity_id: Mapped[int] = mapped_column(primary_key=True)
    name_activity: Mapped[str] = mapped_column(String(100))
    category_id: Mapped[int] = mapped_column(ForeignKey('category.category_id'))

    category: Mapped['Category'] = relationship(back_populates='activities', cascade='all')
    time_trackings: Mapped['TimeTracking'] = relationship(back_populates='activity', cascade='all')

    def __repr__(self) -> str:
         return f'Activity(activity_id={self.activity_id!r}, name_activity={self.name_activity!r}, category_id={self.category_id!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, Activity) and self.name_activity == other.name_activity

    def __hash__(self) -> int:
        return hash(self.name_activity)
