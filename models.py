from application import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Author(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer)
    password_hash = db.Column(db.String(300))
    about_me = db.Column(db.String(800))

    songs = db.relationship('Song', backref='author', lazy=True)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.nickname}>'


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    genre = db.Column(db.String(50))
    date_add = db.Column(db.DateTime, default=datetime.utcnow())
    song_url = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

@login.user_loader
def load_user(id):
    return Author.query.get(int(id))
