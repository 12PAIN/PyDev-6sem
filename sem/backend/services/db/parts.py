from sqlalchemy.orm import Session

from models.parts import Part


def get_part_by_name(session: Session, name: str):
    return session.query(Part).filter(Part.name == name).first()


def create_part(session: Session, name: str):
    if session.query(Part).filter(Part.name == name).first() is None:

        db_part = Part(name=name)
        session.add(db_part)
        session.commit()
        session.refresh(db_part)
        return db_part

    else:
        return session.query(Part).filter(Part.name == name).first()
