from __future__ import annotations
from __datetime__ import datetime,UTC

from  sqlalchemy import Column, Integer, String, ForeignKey, DateTime, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    image_filename: Mapped[str] = mapped_column(String, nullable=True)
    posts: Mapped[list[Post]] = relationship("Post", back_populates="author")

    @property
    def image_url(self) -> str:
        if self.image_filename:
            return f"/uploads/{self.image_filename}"
        return "/static/images/default.png"
    
class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now(UTC))