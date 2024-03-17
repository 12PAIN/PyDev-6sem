from flask import Flask, url_for, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    adverts = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ]
    return "</br>".join(adverts)


@app.route('/image_mars')
def img_mars():
    return f"""
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>Привет, Марс!</title>
            </head>
            <body>
                <h1>Жди нас, Марс!</h1>
                <img src="{url_for('static', filename='img/mars.png')}" 
                 alt="Картинки не будет, увы!">
                 <h2>На Марсе классно - красные пески, крутые горы и кратеры</h2>
            </body>
        </html>
    """


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astro_select():
    if request.method == 'GET':
        return f'''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
            crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Хочешь попасть на марс?</title>
          </head>
          <body>
            <h1>Заполните небольшую анкету астронавта</h1>
            <div>
                <form class="login_form" method="post">
                    <input type="text" class="form-control" id="last_name" placeholder="Фамилия" name="last_name">
                    <input type="text" class="form-control" id="first_name"  placeholder="Имя" name="first_name">
                    <input type="email" class="form-control" id="email" placeholder="Электронная почта" name="email">

                    <div class="form-group">
                        <label for="education">Образование</label>
                        <select class="form-control" id="education" name="edu">
                          <option>Высшее</option>
                          <option>Среднее специальное</option>
                          <option>Среднее</option>
                          <option>Начальное</option>
                        </select>
                     </div>

                    <div class="form-group">
                        <label for="classSelect">Основная профессия</label>
                        <select class="form-control" id="profession" name="prof">
                          <option>Инженер-исследователь</option>
                          <option>Пилот</option>
                          <option>Строитель</option>
                          <option>Экзобиолог</option>
                          <option>Врач</option>
                          <option>Инженер по терраформированию</option>
                          <option>Климатолог</option>
                          <option>Специалист по радиационной защите</option>
                          <option>Астрогеолог</option>
                          <option>Гляциолог</option>
                          <option>Инженер жизнеобеспечения</option>
                          <option>Метеоролог</option>
                          <option>Оператор марсохода</option>
                          <option>Киберинженер</option>
                          <option>Штурман</option>
                          <option>Пилот дронов</option>
                        </select>
                     </div>

                    <div class="form-group">
                        <label for="form-check">Пол</label>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                          <label class="form-check-label" for="male">
                            Мужской
                          </label>
                        </div>
                        <div class="form-check">
                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                          <label class="form-check-label" for="female">
                            Женский
                          </label>
                        </div>
                    </div>

                     <div class="form-group">
                        <label for="about">Мотивация</label>
                        <textarea class="form-control" id="about" rows="3" name="motivation"></textarea>
                    </div>

                    <div class="form-group form-check">
                        <input type="checkbox" class="form-check-input" id="acceptRules" name="ready">
                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                    </div>
                    <button type="submit" class="btn btn-primary" style="background-color: #ff6600; border: 0px;">Отправить</button>
                </form>
            </div>
          </body>
        </html>
    '''
    elif request.method == 'POST':
        print(request.form['last_name'])
        print(request.form['first_name'])
        print(request.form['email'])
        print(request.form['edu'])
        print(request.form['prof'])
        print(request.form['sex'])
        print(request.form['motivation'])
        print(request.form['ready'])
        return f"""<h1 style="text-align: center; color: #d22e3a;">Форма отправлена</h1>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f'''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet"
       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
       crossorigin="anonymous">
        <title>Результаты</title>
      </head>
      <body>
        <h2>Астронавт {nickname} прошел испытаение на {level} этапе отбора с рейтингом {rating}</h2>
      </body>
    </html>
    '''


@app.route('/photo/<nickname>', methods=['POST', 'GET'])
def photo(nickname):
    if request.method == 'GET':
        return f'''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
             <link rel="stylesheet"
             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
             crossorigin="anonymous">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
            <title>Загрузите фото</title>
          </head>
          <body>
            <h2>Выберите фотографию</h2>
            <form method="post" enctype="multipart/form-data">
               <div class="form-group">
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
          </body>
    </html>
    '''
    elif request.method == 'POST':
        f = request.files['file']
        f.save(f'static/img/{secure_filename(f.filename)}')
        print(f.read())
        return f"""<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <title>Фото</title>
                                  </head>
                                  <body>
                                  <h2>Астронавт {nickname}</h2>
                                    <img src="{url_for('static', filename=f'img/{secure_filename(f.filename)}')}"
                                     alt="Картинки не будет, увы!">
                                  </body>
                                </html>"""


@app.route('/carousel')
def carousel():
    return f"""<!DOCTYPE html>
            <html>
            <head>
              <title>Добро пожаловать на Марс!</title>
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
            </head>
            <body>
              <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                <ol class="carousel-indicators">
                  <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                  <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                  <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                  <!-- Add more indicators if needed -->
                </ol>
                <div class="carousel-inner">
                  <div class="carousel-item active">
                    <img class="d-block w-100" src="{url_for('static', filename='img/mars.png')}" alt="First slide">
                  </div>
                  <div class="carousel-item">
                    <img class="d-block w-100" src="{url_for('static', filename='img/mars1.png')}" alt="Second slide">
                  </div>
                  <div class="carousel-item">
                    <img class="d-block w-100" src="{url_for('static', filename='img/mars2.png')}" alt="Third slide">
                  </div>
                </div>
                <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                  <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                  <span class="sr-only">Previous</span>
                </a>
                <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                  <span class="carousel-control-next-icon" aria-hidden="true"></span>
                  <span class="sr-only">Next</span>
                </a>
              </div>

              <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
              <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
              <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
            </body>
            </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
