from flask import Flask, url_for, render_template, redirect
from loginform import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_secret_key'

@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Студент"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login2.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')