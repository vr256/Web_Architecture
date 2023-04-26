from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Action(Base):

    __tablename__ = 'action'

    action_id: Mapped[int] = mapped_column(primary_key=True)
    name_action: Mapped[str] = mapped_column(String(55))

    time_trackings: Mapped['TimeTracking'] = relationship(back_populates='action', cascade='all')

    def __repr__(self) -> str:
         return f'Action(action_id={self.action_id!r}, name_action={self.name_action!r})'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Action) and self.name_action == other.name_action
    
    def __hash__(self) -> int:
        return hash(self.name_action)