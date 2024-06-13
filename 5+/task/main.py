from flask import Flask, render_template, redirect
from data.jobs import Jobs
from data.departments import Departments
from forms.job import AddJobForm
from forms.department import AddDepartmentForm
from data import db_session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/')
def index():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template('main_page.html', title="Works log", jobs=jobs)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job_form():
    form = AddJobForm()
    if form.validate_on_submit():
        db_session.global_init("db/mars_explorer.db")
        db_sess = db_session.create_session()

        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=True if form.is_finished.data == "Да" else False
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/success')
    return render_template('add_job.html', title="Add job form", form=form)


@app.route('/add_department', methods=['GET', 'POST'])
def add_department_form():
    form = AddDepartmentForm()
    if form.validate_on_submit():
        db_session.global_init("db/mars_explorer.db")
        db_sess = db_session.create_session()

        if db_sess.query(Departments).filter(Departments.email == form.email.data).first():
            return render_template('add_department.html', title='Add department form',
                                   form=form,
                                   message="Такой департамент уже есть")

        department = Departments(
            title=form.title.data,
            chief=form.chief.data,
            members=form.members.data,
            email=form.email.data
        )
        db_sess.add(department)
        db_sess.commit()
        return redirect('/success')
    return render_template('add_department.html', title="Add department form", form=form)


@app.route('/success')
def success():
    return '''<h1 style="text-align: center; color: #d22e3a;">Успешно сохранено</h1>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
