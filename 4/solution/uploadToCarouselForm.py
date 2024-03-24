from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, SubmitField


class UploadPhotoToCarouserlForm(FlaskForm):
    photo = FileField('Добавить фото', validators=[FileRequired("Фотография обязательна!"),
                                               FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField('Добавить')