from sqlalchemy import (
    Column,
    String,
    PrimaryKeyConstraint,
    ForeignKey, ForeignKeyConstraint
)
from sqlalchemy.orm import relationship
from db_initializer import Base
from sqlalchemy import Integer


class Result(Base):
    """Models a detect tasks table"""
    __tablename__ = "results"
    id = Column(Integer, nullable=False, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'), nullable=False)

    PrimaryKeyConstraint("id", name="pk_result_id")
    ForeignKeyConstraint(["task_id"], ["tasks.id"], name="fk_results_to_tasks")
    task = relationship("Task", backref="result", foreign_keys=[task_id])
    input_file = Column(String)
    output_file = Column(String)
    # parts = relationship("Part", secondary="results_parts_rel")

    parts = relationship("ResultsPartsRel")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<Result {id!r}>".format(id=self.id)
