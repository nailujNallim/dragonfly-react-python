from pydantic import BaseModel
from typing import Union
from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)

class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: Union[str, None] = None
    completed: Union[bool, None] = None


class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True
