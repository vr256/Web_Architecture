from typing import List
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Role(Base):

    __tablename__ = 'role'

    role_id: Mapped[int] = mapped_column(primary_key=True)
    name_role: Mapped[str] = mapped_column(String(25))

    users: Mapped[List['User']] = relationship(back_populates='role', cascade='all')

    def __repr__(self) -> str:
         return f'Role(role_id={self.role_id!r}, name_role={self.name_role!r})'
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Role) and self.name_role == other.name_role
    
    def __hash__(self) -> int:
        return hash(self.name_role)