from sqlalchemy import (
    Column,
    PrimaryKeyConstraint,
    ForeignKey, ForeignKeyConstraint
)
from sqlalchemy.orm import relationship
from db_initializer import Base

from sqlalchemy import Integer


class UserPartsRel(Base):
    """Models a detect tasks table"""
    __tablename__ = "user_parts_rel"
    id = Column(Integer, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    part_id = Column(Integer, ForeignKey('parts.id'), nullable=False)
    pcs = Column(Integer, nullable=False)

    PrimaryKeyConstraint("id", name="pk_user_parts_rel_id")
    ForeignKeyConstraint(["user_id"],  ["users.id"], name="fk_user_parts_rel_to_users")
    ForeignKeyConstraint(["part_id"], ["parts.id"], name="fk_user_parts_rel_to_parts")

    user = relationship("User", backref="parts", foreign_keys=[user_id])
    part = relationship("Part", backref="usersParts", foreign_keys=[part_id])

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<UserPartsRel {id!r}>".format(id=self.id)
