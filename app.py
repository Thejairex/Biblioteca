# Import libraries
from flask import Flask, render_template, redirect, request, url_for, make_response
from flask_mysqldb import MySQL
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, verify_jwt_in_request
import hashlib

# Import Modules
from blueprint.Funciones import Funciones

# Import de blueprints
from blueprint.animes import animes
from blueprint.comics import comics
from blueprint.novelas import novelas

# Init App FLask
app = Flask(__name__)

# Config Connection DDBB
mysql = MySQL(app)
# app.config['MYSQL_HOST'] = 'Thejairex2.mysql.pythonanywhere-services.com'
# app.config['MYSQL_USER'] = 'Thejairex2'
# app.config['MYSQL_PASSWORD'] = 'Aiwa2015'
# app.config['MYSQL_DB'] = 'Thejairex2$biblioteca'
app.secret_key = "OtakuTeca"


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "biblioteca"

# Json Web Token
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = "oTAKUtECA"


# Api Login
@app.route("/api/login", methods=["POST"])
def api_login():
	if request.method == "POST":
		username = request.form['username'] 
		password = request.form['lastname']
		password = hashlib.sha256(password.encode('utf-8')).hexdigest()
		data = (username,password)
		return render_template("logeado.html",
				data = data)

# Route Login
@app.route("/login")
def login():
	return render_template("login.html", 
	titlePage = "Biblioteca",
	title = "Login")

# Route Main
@app.route("/")
def index():
	try:
		verifiqued = Funciones.verificarToken()
		print(verifiqued)
		return render_template("index.html")
	except:
		return redirect(url_for('login'))
	

	# print(status)
	# if status == None:
	# 	resp = make_response(redirect(url_for('login')))
	# 	status = "False"
	# 	resp.set_cookie('status', status)
	# 	return resp
	# else:
	

# Register Blueprint
app.register_blueprint(animes)
app.register_blueprint(comics)
app.register_blueprint(novelas)

if __name__ == '__main__':
	app.run(debug=True, port=3000)