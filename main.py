from flask import Flask
from flask_mysqldb import MySQL
from flask_jwt_extended import  JWTManager

app = Flask(__name__)

mysql = MySQL(app)

jwt = JWTManager(app)