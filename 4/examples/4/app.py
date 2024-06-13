from flask import Flask, url_for, render_template, json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Студент"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')