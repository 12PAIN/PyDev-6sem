import json
import shutil
import uuid
from typing import Tuple, Any

from fastapi import Depends
from flask import abort, redirect, make_response, jsonify
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session
from werkzeug.datastructures import FileStorage

from models import User
from schemas.users import CreateUserSchema
from services.db import users as users_db_service
import settings
from decorators.token_required import token_required
from forms.upload_task_form import TaskUploadForm
from schemas.tasks import CreateTaskSchema, TaskSchema
from settings import pages
from db_initializer import get_db
from schemas.tasks import TaskSchema
from services.tasksProcessingService.tasksProcessingService import TasksProcessingService
import services.db.tasks as task_db_services

app = Flask(__name__)

app.config['SECRET_KEY'] = settings.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


@app.route('/detect', methods=['GET', 'POST'])
@token_required
def detect_page(current_user):
    form = TaskUploadForm()

    params = {
        'title': "Определить на фото",
        'form': form
    }

    if form.validate_on_submit():
        f = form.photo.data
        filename = f.filename

        file = FileStorage(filename=filename, stream=f.read())

        create_task(file, current_user=current_user)
        return redirect("/")

    return render_template("task_upload_form.html", **params)


@app.post('/tasks')
@token_required
def create_task(current_user, session: Session = Depends(get_db)):
    file = request.files['file']

    to_return = None

    try:
        user_id = current_user.id
        file_path = settings.FILES_UPLOAD_PATH + f"user_{user_id}_{uuid.uuid4()}_" + file.filename

        task: CreateTaskSchema = CreateTaskSchema(creator_id=user_id, file_path=file_path)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.read(), buffer)

        to_return = task_db_services.create_task(session, task=task)
        taskProcessingService.process(to_return, session)
    finally:
        file.close()

    if to_return is not None:
        return jsonify(TaskSchema(**to_return.__dict__).json())
    else:
        abort(404)


@app.route('/')
@app.route('/index')
def index():
    params = {
        'pages': pages,
        'title': "Главная"
    }
    return render_template('index.html', **params)


@app.route('/login', methods=['POST'])
def login(session: Session = Depends(get_db)):
    # creates dictionary of form data
    auth = request.form

    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )

    user: User = users_db_service.get_user(session, email=auth.get('email'))

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
        )

    if user.validate_password(auth.get('password')):
        # generates the JWT Token
        token = user.generate_pure_token()

        return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
    # returns 403 if password is wrong
    return make_response(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
    )


# signup route
@app.route('/signup', methods=['POST'])
def signup(session: Session = Depends(get_db)):
    # creates a dictionary of the form data
    data = request.form

    # gets name, email and password
    name, email = data.get('name'), data.get('email')
    password = data.get('password')

    # checking for existing user
    user = users_db_service.get_user(session, email=email)
    if not user:
        # database ORM object

        userSchema = CreateUserSchema(full_name=name, email=email, hashed_password=User.hash_password(password))

        users_db_service.create_user(session, userSchema)

        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)


if __name__ == '__main__':
    with app.app_context():

        taskProcessingService = TasksProcessingService()



    app.run(port=8080, host='0.0.0.0')
