import os

# Database url configuration
DATABASE_URL = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}".format(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    db_name=os.getenv("POSTGRES_DB"),
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
)

SECRET_KEY = os.getenv("SECRET_KEY")

FILES_UPLOAD_PATH = "./uploads/"

DETECTOR_MODEL_PATH = "./yolo/detector.pt"
CLASSIFICATOR_MODEL_PATH = "./yolo/classificator.pt"
DETECTION_CONF = 0.6
CLASSIFICATION_CONF = 0.5
CLASSIFICATOR_IMAGE_SIZE = (64, 64)

pages = [
        {
            'title': "Вход/регистрация",
            'route': '/signin'
        },
        {
            'title': "Определить на фото",
            'route': '/detect'
        },
        {
            'title': "История",
            'route': '/history'
        }
    ]

