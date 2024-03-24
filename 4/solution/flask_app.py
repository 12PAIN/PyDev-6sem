import json
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from werkzeug.utils import secure_filename

from astronautForm import AstronautForm
from uploadToCarouselForm import UploadPhotoToCarouserlForm

from flask import Flask, url_for, render_template, Blueprint, redirect

app = Flask(__name__)
# app.config['SERVER_NAME'] = '127.0.0.1'
app.config['SECRET_KEY'] = 'my_secret_key'


@app.route('/')
@app.route('/index')
def index():
    params = {
        'pages': pages,
        'title': "Главная"
    }
    return render_template('index.html', **params)



@app.route('/list_prof/<list>')
def list_prof(list):


    professions = set()

    for profs in [member['professions'] for member in members]:
        for prof in profs:
            professions.add(prof)


    params = {
        'profs': professions,
        'list': list,
        'title': 'Профессии'
    }
    return render_template('list_prof.html', **params)

@app.route('/distribution')
def distribution():
    params = {
        'members': members,
        'title': 'Размещение'
    }
    return render_template('distribution.html', **params)

@app.route('/member/<int:number>')
@app.route('/member/random')
def memberInfo(number: int | None = None):

    params = {
        'members': members,
        'title': 'Член экипажа' if number is None else f'Член экипажа №{number}',
        'number': number
    }

    return render_template('member.html', **params)

@app.route("/room/<sex>/<int:age>")
def roomDesign(sex, age: int):

    params = {
        'title': "Оформление каюты",
        'sex': sex,
        'age': age
    }

    return render_template("roomDesign.html", **params)

@app.route('/astronaut_selection', methods=['GET', 'POST'])
def austronaut_selection():

    form = AstronautForm()

    params = {
        'title': "Запись добровольцем",
        'form': form
    }

    if form.validate_on_submit():
        sendEmail(form)

        return redirect("/")

    return render_template("astronaut_selection_form.html", **params)

@app.route('/galery', methods=['GET', 'POST'])
def galery():

    form = UploadPhotoToCarouserlForm()

    photoFileNames = os.listdir(carousel_photos_folder_path)

    params = {
        'title': 'Галерея',
        'form': form,
        'photoNames': photoFileNames
    }

    if form.validate_on_submit():

        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(carousel_photos_folder_path, filename))

        return redirect("/galery")

    return render_template("galery.html", **params)

def sendEmail(form):


    email = gl_email

    from_email = email
    to_email = "tvelvepain@yandex.ru"
    subject = "Заявки добровольцев на колонизацию Марса!"

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to_email

    html = f"""
    <html>
        <head></head>
            <body>
                <h2>Заявка от {form.firstName.data} {form.lastName.data}, email: {form.email.data}</h2
                <p>Образование:{form.education.data}</p>
                <p>Профессия:{form.mainProfession.data}</p>
                <p>Пол:{form.sex.data}</p>
                <p>Мотивация:{form.motivation.data}</p>
                <p>Готов остаться на марсе:{"Да" if form.agreeToStay.data == True else "Нет"}</p>
                <img src="cid:image1" alt="Не удалось загрузить изображение" style="max-width: 500px;"><br>
    
            </body>
    </html>
    """
    # Record the MIME types of text/html.
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part2)

    # This example assumes the image is in the current directory
    fp = form.photo.data
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    # Send the message via local SMTP server.
    mailsrv.sendmail(from_email, to_email, msg.as_string())
    mailsrv.quit()




if __name__ == '__main__':

    global gl_email
    global gl_password
    global mailsrv

    gl_email = input("Insert mail.ru email for smtp service:")
    gl_password = input("Insert password:")

    mailsrv = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    mailsrv.login(gl_email, gl_password)

    global carousel_photos_folder_path
    carousel_photos_folder_path = f'{app.root_path}/static/img/carousel'

    with app.app_context():
        blueprint = Blueprint('members', __name__, static_url_path='/static/members', static_folder=f'{app.root_path}/members')
        app.register_blueprint(blueprint)

        blueprint1 = Blueprint('roomsEmblems', __name__, static_url_path='/static/rooms/emblems',
                              static_folder=f'{app.root_path}/roomsDesign')
        app.register_blueprint(blueprint1)

        blueprint2 = Blueprint('galery', __name__, static_url_path='/static/galery',
                               static_folder=f'{app.root_path}/static/img/carousel')
        app.register_blueprint(blueprint2)

        global members
        with open(f'{app.root_path}/members/persons.json', 'r', encoding="utf8") as f:
            members = json.load(f)

        global pages
        pages = [
            {
                'title': "Список профессий",
                'route': '/list_prof/ol'
            },
            {
                'title': "Размещение",
                'route': '/distribution'
            },
            {
                'title': "Случайный член экипажа",
                'route': '/member/random'
            },
            {
                'title': "Оформление мужской каюты, возраст меньше 21",
                'route': '/room/male/20'
            },
            {
                'title': 'Подать заявку в качестве добровольца',
                'route': '/astronaut_selection'
            },
            {
                'title': 'Галерея',
                'route': '/galery'
            }
        ]

    app.run(port=8080, host='127.0.0.1')


