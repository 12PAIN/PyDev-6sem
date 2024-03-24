from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, EmailField, SelectField, TextAreaField, FileField, \
    RadioField
from wtforms.validators import DataRequired, email, regexp
from flask_wtf.file import FileAllowed, FileRequired


class AstronautForm(FlaskForm):
    lastName = StringField('Фамилия', validators=[DataRequired("Поле обязательно к заполнению")])

    firstName = StringField('Имя', validators=[DataRequired("Поле обязательно к заполнению")])

    email = EmailField('Электронная почта', validators=[
        DataRequired("Поле обязательно к заполнению"), email("Введена неправильная почта!!!")
    ])

    education = SelectField('Образование',
                            choices=['Высшее', 'Среднее', 'Среднее специальное'],
                            validators=[DataRequired("Поле обязательно к заполнению")]
                            )

    mainProfession = SelectField('Основная профессия', validators=[DataRequired("Поле обязательно к заполнению")],
                                 choices=[
                                     'инженер-исследователь', 'пилот', 'строитель',
                                     'экзобиолог', 'врач', 'инженер по терраформированию', 'климатолог',
                                     'специалист по радиационной защите',
                                     'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
                                     'оператор марсохода', 'киберинженер',
                                     'штурман', 'пилот дронов'
                                 ]
                                 )

    sex = SelectField('Пол', validators=[DataRequired("Поле обязательно к заполнению")],
                     choices=[
                         'Мужской', 'Женский'
                     ]
                     )

    motivation = TextAreaField('Мотивация', description='Коротко о вашей мотивации',
                               validators=[DataRequired("Поле обязательно к заполнению")])

    agreeToStay = BooleanField('Согласны остаться на Марсе?')

    photo = FileField('Ваше фото', validators=[FileRequired("Фотография обязательна!"),
                                               FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])

    submit = SubmitField('Отправить')
