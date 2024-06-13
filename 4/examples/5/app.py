from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Студент"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/var')
def var():
    return render_template('var.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')