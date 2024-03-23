from app.app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    homes = db.relationship('Home', backref='user', lazy=True)

class Home(db.Model):
    home_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    home_name = db.Column(db.String(100), nullable=False)
    rooms = db.relationship('Room', backref='home', lazy=True)

class Room(db.Model):
    room_id = db.Column(db.Integer, primary_key=True)
    home_id = db.Column(db.Integer, db.ForeignKey('home.home_id'), nullable=False)
    room_name = db.Column(db.String(100), nullable=False)
    lights = db.relationship('Light', backref='room', lazy=True)

class Light(db.Model):
    light_id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.room_id'), nullable=False)
    light_name = db.Column(db.String(100), nullable=False)
    color_id = db.Column(db.String(10), db.ForeignKey('color.color_id'), nullable=False)
    brightness = db.Column(db.Integer)
    status = db.Column(db.Enum('on', 'off'), default='off')
    history = db.relationship('History', backref='light', lazy=True)

class History(db.Model):
    history_id = db.Column(db.Integer, primary_key=True)
    light_id = db.Column(db.Integer, db.ForeignKey('light.light_id'), nullable=False)
    status = db.Column(db.Enum('on', 'off'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

class Color(db.Model):
    color_id = db.Column(db.Integer, primary_key=True)
    color_name = db.Column(db.String(20), nullable=False)
    hex_code = db.Column(db.String(6), nullable=False)
    lights = db.relationship('Light', backref='color', lazy=True)
