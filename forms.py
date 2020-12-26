from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange

genres = ['Rap', 'RnB', 'Pop', 'Rock', 'jazz', 'Pauzern-rap']


class RegistrationForm(FlaskForm):
    nickname = StringField('Псевдоним', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    age = StringField('Возраст')
    # age = StringField('Возраст', validators=[NumberRange(14, 100, 'Ваш возраст должен быть от 14 до 100')])
    submit = SubmitField('Регистрация')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class AddSongForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    genre = SelectField('Жанры', choices=genres)
    song_file = FileField('Аудифайл')
    submit = SubmitField('Добавить')
