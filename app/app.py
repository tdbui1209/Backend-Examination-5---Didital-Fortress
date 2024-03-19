from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///light_db.db'
db = SQLAlchemy(app)


# Registering the routes
from app.routes import *

if __name__ == '__main__':
    app.run(debug=True)
