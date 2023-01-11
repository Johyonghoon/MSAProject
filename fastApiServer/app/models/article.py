from pydantic import BaseConfig
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy_utils import UUIDType

from app.models.mixins import TimestampMixin


class Article(Base, TimestampMixin):

    __tablename__ = 'articles'

    art_seq = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(String(1000))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'), nullable=True)

    user = relationship('User', back_populates='articles')


    class Config:
        arbitrary_types_allowed = True
