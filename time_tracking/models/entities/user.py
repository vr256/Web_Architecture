from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class User(Base):

    __tablename__ = 'user'

    user_id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(String(50))
    password: Mapped[str]
    email: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey('role.role_id'))

    role: Mapped['Role'] = relationship(back_populates='users', cascade='all')
    time_trackings: Mapped['TimeTracking'] = relationship(back_populates='user', cascade='all')

    def __repr__(self) -> str:
         return f'User(user_id={self.user_id!r}, login={self.login!r}, password={self.password!r}), email={self.email!r}, role_id={self.role_id!r})'

    def __eq__(self, other) -> bool:
        return isinstance(other, User) and self.login == other.login
    
    def __hash__(self) -> int:
        return hash(self.login)