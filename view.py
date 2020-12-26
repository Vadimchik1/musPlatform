from application import appplicaton, db
from flask import render_template, redirect, url_for, flash, request, make_response
from forms import RegistrationForm, LoginForm, AddSongForm
from models import Author, Song
from flask_login import current_user, login_user, login_required, logout_user
from jinja2.ext import Extension
from jinja2 import Environment
import os

class MyExtension(Extension):
    pass


environment = Environment(extensions=[MyExtension])



def get_author_id():
    return Author.query.filter_by(nickname=str(current_user)[6:-1:1]).first().id


def get_author_name():
    return Author.query.filter_by(nickname=str(current_user)[6:-1:1]).first().nickname


@appplicaton.route('/')
def index():
    authors = Author.query.filter_by().all()
    return render_template('index.html', title='Vadimchikpunk', authors=authors)


@appplicaton.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Author.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильный логин или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        try:
            path = os.path.join(os.getcwd(), 'static/songs', get_author_name())
            os.mkdir(path)
        except FileExistsError:
            pass

        return redirect(url_for('index'))

    return render_template('login.html', title='Вход в свой аккаунт', form=form)


@appplicaton.route('/register', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        author = Author(nickname=form.nickname.data, email=form.email.data, age=form.age.data)
        author.set_password(form.password.data)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@appplicaton.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@appplicaton.route('/profile')
@login_required
def my_profile():
    if not current_user:
        return redirect(url_for('login'))
    user = Author.query.filter_by(id=get_author_id()).first()
    songs = Song.query.filter_by(author_id=get_author_id()).all()
    song_dict = {}
    for i in songs:
        song_dict[i.title] = str(url_for('static', filename=i.song_url))
        a = song_dict[i.title]
        b = a.replace('%5C', '/')
        song_dict[i.title] = b
    return render_template('my_profile.html', title='Моя страница', songs=song_dict, user=user )


@appplicaton.route('/profile/<alias>')
@login_required
def show_profile(alias):
    user = Author.query.filter_by(nickname=alias).first()
    songs = Song.query.filter_by(author_id=user.id).all()
    song_dict = {}
    for i in songs:
        song_dict[i.title] = str(url_for('static', filename=i.song_url))
        print(song_dict[i.title])
        # a = song_dict[i.title]
        # b = a.replace('%5C', '/')
        # song_dict[i.title] = b
    return render_template('profile.html', user=user, songs=song_dict)


@appplicaton.route('/my_profile/add_song', methods=['GET', 'POST'])
@login_required
def add_song():
    form = AddSongForm()
    if form.validate_on_submit():
        if request.files:
            song_file = request.files['song_file']
            song_url = os.path.join('songs', get_author_name(), song_file.filename)
            song_file.save(os.path.join(appplicaton.config['UPLOAD_FOLDER'], get_author_name(), song_file.filename))
            song = Song(title=form.title.data, genre=form.genre.data, author_id=get_author_id(), song_url=song_url)
            db.session.add(song)
            db.session.commit()
        return redirect(url_for('add_song'))
    return render_template('add_song.html', form=form)
