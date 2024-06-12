import os
import time
import uuid
import fastapi
from fastapi import Body, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from typing import Dict, List
from starlette import status
from starlette.responses import JSONResponse
import base64
from auth.jwthandler import OAuth2PasswordBearerCookie
from settings import pages
from fastapi.responses import RedirectResponse
from schemas.results import Part as schemaPart
from services.tasksProcessingService.tasksProcessingService import TasksProcessingService
from settings import FILES_UPLOAD_PATH
from db_initializer import get_db
from models import users as user_model, Result
from schemas.users import CreateUserSchema, UserSchema
from schemas.tasks import CreateTaskSchema, TaskSchema
from services.db import users as user_db_services
from services.db import results as result_db_services
from services.db import tasks as task_db_services
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import shutil
from fastapi.staticfiles import StaticFiles
from fastapi import File, UploadFile
from multiprocessing import Queue
from schemas.results import ResultSchema
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware  # NEW

# setup authentication scheme
oauth2_scheme = OAuth2PasswordBearerCookie(token_url="/login")
app = fastapi.FastAPI()

task_processing_service = TasksProcessingService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_tasks_processing_service():
    return task_processing_service


@app.get("/")
def home():
    return "Hello, World!"


@app.post('/signup', response_model=UserSchema)
def signup(
        payload: CreateUserSchema = Body(),
        session: Session = Depends(get_db)
):
    """Processes request to register user account."""
    try:

        payload.hashed_password = user_model.User.hash_password(payload.hashed_password)
        return user_db_services.create_user(session, user=payload)
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Account cannot be created.")


@app.get("/results/{task_id}", response_model=ResultSchema)
def get_result_by_task(
        task_id: int,
        token: str = Depends(oauth2_scheme),
        session: Session = Depends(get_db)
):
    result: Result = result_db_services.get_result_by_task_id(session=session, task_id=task_id)

    parts = [schemaPart(name=partRel.part.name, pcs=partRel.pcs) for partRel in result.parts]

    inp_file_code = None
    out_file_code = None
    if result.input_file is not None:
        with open(result.input_file, "rb") as input_image_file:
            encoded_input_string = base64.b64encode(input_image_file.read()).decode('utf-8')

        inp_file_code = f"data:image/{result.input_file.split('.')[2]};base64," + encoded_input_string

    if result.output_file is not None:
        with open(result.output_file, "rb") as output_image_file:
            encoded_output_string = base64.b64encode(output_image_file.read()).decode('utf-8')

        out_file_code = f"data:image/{result.output_file.split('.')[2]};base64," + encoded_output_string

    to_return = ResultSchema(task_id=task_id, parts=parts, input_img_code=inp_file_code, output_img_code=out_file_code)

    return to_return


@app.post('/tasks', response_model=TaskSchema)
def create_task(
        file: UploadFile = File(),
        # queue: TasksQueue = Depends(get_queue),
        taskProcessingService: TasksProcessingService = Depends(get_tasks_processing_service),
        token: str = Depends(oauth2_scheme),
        session: Session = Depends(get_db)
):
    """Creates a new task."""

    to_return = None

    try:

        user_id = user_model.User.get_user_info_by_token(token)['id']

        file_path = FILES_UPLOAD_PATH + f"user_{user_id}_{uuid.uuid4()}_" + file.filename

        task: CreateTaskSchema = CreateTaskSchema(creator_id=user_id, file_path=file_path)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        to_return = task_db_services.create_task(session, task=task)

        taskProcessingService.process(to_return, session)

    finally:
        file.file.close()

    if to_return is not None:
        return to_return
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task could not be created."
        )


@app.get("/tasks/{id}", response_model=TaskSchema)
def get_task(
        id: int,
        token: str = Depends(oauth2_scheme),
        session: Session = Depends(get_db)
):
    return task_db_services.get_task_by_id(session=session, id=id)


@app.get("/tasks", response_model=List[TaskSchema])
def get_task(
        token: str = Depends(oauth2_scheme),
        session: Session = Depends(get_db)
):
    user_id = user_model.User.get_user_info_by_token(token)['id']
    return task_db_services.get_tasks_by_user(session=session, user_id=user_id)


@app.get("/users/me", response_model=UserSchema)
def profile(
        token: str = Depends(oauth2_scheme),
        session: Session = Depends(get_db)
):
    """
    Processes request to retrieve the requesting user profile
    """

    return user_db_services.get_user_by_id(session, user_model.User.get_user_info_by_token(token)['id'])


@app.post('/login')
def login(
        payload: OAuth2PasswordRequestForm = Depends(),
        session: Session = Depends(get_db)
):
    """Processes user's authentication and returns a token
    on successful authentication.

    request body:

    - username: Unique identifier for a user e.g email,
                phone number, name

    - password:
    """
    try:
        user: user_model.User = user_db_services.get_user(
            session=session, email=payload.username
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    is_validated: bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials"
        )

    content = user.generate_token()
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {content['access_token']}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response
