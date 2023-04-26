from typing import Optional
from sqlalchemy import ForeignKey, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class TimeTracking(Base):

    __tablename__ = 'time_tracking'

    activity_id: Mapped[int] = mapped_column(ForeignKey('activity.activity_id'), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'), primary_key=True)
    action_id: Mapped[int] = mapped_column(ForeignKey('action.action_id'), primary_key=True)
    time_spent: Mapped[Optional[str]]

    activity: Mapped['Activity'] = relationship(back_populates='time_trackings', cascade='all')
    user: Mapped['User'] = relationship(back_populates='time_trackings', cascade='all')
    action: Mapped['Action'] = relationship(back_populates='time_trackings', cascade='all')
    
    def __repr__(self) -> str:
         return f'TimeTracking(activity_id={self.activity_id!r}, user_id={self.user_id!r}, action_id={self.action_id!r}, time_spent={self.time_spent!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, TimeTracking) and       \
               self.activity_id == other.activity_id and \
               self.user_id == other.user_id and         \
               self.action_id == other.action_id

    def __hash__(self) -> int:
        return hash((self.activity_id, self.user_id, self.action_id))