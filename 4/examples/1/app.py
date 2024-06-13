from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Студент"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')