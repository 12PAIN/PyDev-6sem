from sqlalchemy.orm import Session

from models.tasks import Task
from schemas.tasks import CreateTaskSchema

from models.tasks import StatusEnum


def create_task(session: Session, task: CreateTaskSchema):
    db_task = Task(**task.dict())
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


def get_task_by_id(session: Session, id: int):
    return session.query(Task).filter(Task.id == id).one()


def change_status(session: Session, task: Task, status: StatusEnum):
    task.status = status
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def get_tasks_by_user(session: Session, user_id: int):
    return session.query(Task).filter(Task.creator_id == user_id).all()
