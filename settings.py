from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
db.init_app(app)
app.config['SECRET_KEY'] = 'moew'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://septt@localhost:8000/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
