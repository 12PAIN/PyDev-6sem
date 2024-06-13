from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader = IntegerField('id руководителя, целое число', validators=[DataRequired()])
    job = StringField('Описание работы', validators=[DataRequired()])
    work_size = IntegerField('Объем работы в часах', validators=[DataRequired()])
    collaborators = StringField('список id участников (если несколько, перечислить через запятую)', validators=[DataRequired()])
    is_finished = RadioField('Завершено?', choices=["Да", "Нет"])
    submit = SubmitField('Сохранить')
