from data.jobs import Jobs
from data.users import User
from data.departments import Departments
from data import db_session
from sqlalchemy import func

db_session.global_init("db/mars_explorer.db")

db_sess = db_session.create_session()


query = db_sess.query(User.surname, User.name).join(Jobs).join(Departments).filter(Departments.id == 1).group_by(User.id)\
    .having(func.sum(Jobs.work_size) > 25).all()

for worker in query:
    print(f"{worker.surname} {worker.name}")

db_sess.close()
