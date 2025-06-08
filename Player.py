from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    __tablename__ = "Player"
    UserID = db.Column(db.String(10), primary_key=True)
    UserName = db.Column(db.String(50), nullable=False)
    UserFullName = db.Column(db.String(50), nullable=False)
    UserPhone = db.Column(db.String(50), nullable=False)
    UserEmail = db.Column(db.String(50), nullable=False)
    UserElo = db.Column(db.Integer, nullable=False)
    UserUserName = db.Column(db.String(50), nullable=False)
    UserPassWord = db.Column(db.String(50), nullable=False)
    UserStatus = db.Column(db.String(10), nullable=False)
