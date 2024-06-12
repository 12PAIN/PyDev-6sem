from sqlalchemy import (
    Column,
    String,
    PrimaryKeyConstraint,
    Integer
)

from db_initializer import Base


class Part(Base):
    """Model a parts table"""
    __tablename__ = "parts"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

    PrimaryKeyConstraint("id", name="pk_part_id")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<Part {name} {id!r}>".format(name=self.name, id=self.id)
