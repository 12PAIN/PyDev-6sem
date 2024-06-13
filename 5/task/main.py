import datetime

from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.departments import Departments

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


def add_user(surname, name, age, position, speciality, address, email):
    user = User()

    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def add_job(team_leader, user_job, work_size, collaborators, start_date, is_finished):
    jobs = Jobs()

    jobs.team_leader = team_leader
    jobs.job = user_job
    jobs.work_size = work_size
    jobs.collaborators = collaborators
    jobs.start_date = start_date
    jobs.is_finished = is_finished

    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()


def add_department(title, chief, members, email):
    departments = Departments()
    departments.title = title
    departments.chief = chief
    departments.members = members
    departments.email = email

    db_sess = db_session.create_session()
    db_sess.add(departments)
    db_sess.commit()


def main():
    db_session.global_init("db/mars_explorer.db")

    add_user("Scott", "Ridley", 21, "captain", "research engineer", "module_1", "scott_chief@mars.org")

    add_user("Ivanov", "Ivan", 30, "manager", "Driving a rover", "module_2", "ivanov@mars.org")
    add_user("Petrov", "Alexey", 35, "engineer", "astronomer", "module_2", "petrov@mars.org")
    add_user("Sidorova", "Elena", 28, "middle scientist", "geolog", "module_1", "sidorova@mars.org")
    add_user("Kozlov", "Dmitry", 32, "technician", "electronics engineer", "module_1", "kozlov@mars.org")
    add_user("Morozova", "Anna", 16, "assistant", "biologist", "module_1", "morozova@mars.org")

    db_sess = db_session.create_session()
    for user in db_sess.query(User).all():
        print(user.name)

    add_job(1, "deployment of residential modules 1 and 2", 15, "2, 3", datetime.datetime.now(), False)
    add_job(3, "Engineer", 25, "2, 3, 4", datetime.datetime.now(), False)
    add_job(2, "Astromer", 30, "4, 2", datetime.datetime.now(), False)
    add_job(4, "Cook", 15, "2, 3", datetime.datetime.now(), True)

    add_department("department_1", 2, "2, 3", "email@mail.ru")

    app.run()


if __name__ == '__main__':
    main()
