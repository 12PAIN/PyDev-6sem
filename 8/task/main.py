from flask import Flask, render_template
from data.jobs import Jobs
from data import db_session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/')
def index():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template('main_page.html', title="Works log", jobs=jobs)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
