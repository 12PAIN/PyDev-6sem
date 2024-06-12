from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    ForeignKey, ForeignKeyConstraint
)
from sqlalchemy.orm import relationship
from db_initializer import Base

from sqlalchemy import Integer


class ResultsPartsRel(Base):
    """Models a detect tasks table"""
    __tablename__ = "results_parts_rel"
    id = Column(Integer, nullable=False, primary_key=True)
    result_id = Column(Integer, ForeignKey('results.id'), nullable=False)
    part_id = Column(Integer, ForeignKey('parts.id'), nullable=False)
    pcs = Column(Integer, nullable=False)

    PrimaryKeyConstraint("id", name="pk_result_part_rel_id")
    ForeignKeyConstraint(["result_id"], ["results.id"], name="fk_result_part_rel_to_results")
    ForeignKeyConstraint(["part_id"], ["parts.id"], name="fk_result_part_rel_to_parts")

    # result = relationship("Result", backref="parts", foreign_keys=[result_id])
    part = relationship("Part", foreign_keys=[part_id])

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<ResultsPartsRel {id!r}>".format(id=self.id)
