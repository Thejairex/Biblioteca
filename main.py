from flask import Flask
from flask_mysqldb import MySQL
from flask_jwt_extended import  JWTManager
from flask_login import LoginManager

app = Flask(__name__)

mysql = MySQL(app)

jwt = JWTManager(app)
