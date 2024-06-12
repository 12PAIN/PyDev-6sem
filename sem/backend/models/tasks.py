from sqlalchemy import (
    Column,
    String,
    PrimaryKeyConstraint,
    ForeignKey, ForeignKeyConstraint
)
from sqlalchemy.orm import relationship
from db_initializer import Base

import enum
from sqlalchemy import Integer
from sqlalchemy import Enum


class StatusEnum(str, enum.Enum):
    waiting = "WAITING"
    created = "CREATED"
    rejected = "REJECTED"
    at_work = "AT_WORK"
    finished = "FINISHED"


class Task(Base):
    """Models a detect tasks table"""
    __tablename__ = "tasks"
    id = Column(Integer, nullable=False, primary_key=True)
    creator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    file_path = Column(String, nullable=False)
    status = Column(Enum(StatusEnum), default=StatusEnum.created)

    PrimaryKeyConstraint("id", name="pk_task_id")
    ForeignKeyConstraint(["creator_id"], ["users.id"], name="fk_task_to_user")
    creator = relationship("User", backref="tasks", foreign_keys=[creator_id])

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<Task {id!r}>".format(id=self.id)
