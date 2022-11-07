# Import libraries
from flask import Flask, render_template, redirect, request, url_for, make_response, jsonify
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_wtf.csrf import CSRFProtect
import hashlib

from querys.entities.User import User
# Import Modules
from querys.querysUser import qUser
# Import de blueprints
from blueprint.animes import animes
from blueprint.comics import comics
from blueprint.novelas import novelas
from blueprint.registers import registers


# Init App FLask
app = Flask(__name__)
mysql = MySQL(app)
csrf = CSRFProtect(app)

# Config Connection DDBB

# app.config['MYSQL_HOST'] = 'Thejairex2.mysql.pythonanywhere-services.com'
# app.config['MYSQL_USER'] = 'Thejairex2'
# app.config['MYSQL_PASSWORD'] = 'Aiwa2015'
# app.config['MYSQL_DB'] = 'Thejairex2$biblioteca'
app.secret_key = "OtakuTeca"


app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "biblioteca"

# Login

login_manager = LoginManager(app)
login_manager.login_view = "login"

# Load user
@login_manager.user_loader
def load_user(id):
	return qUser.getUserID(id)

# Api Logins
@app.route("/api/login", methods=["POST"])
def api_login():
	if request.method == "POST":
		username = request.form['username'] 
		password = request.form['password']
		password = hashlib.sha256(password.encode('utf-8')).hexdigest()

		user = User(0,username,password,None)

		logged_user = qUser.loginUser(user)

		if logged_user == None:
			return "El usuario no esta registrado"
		else:
			if logged_user.password:
				login_user(logged_user, remember=False)
				return redirect(url_for('index'))
			else:
				return "Contraseña incorrecta" 


# Route Login
@app.route("/login")
def login():
	return render_template("login.html", 
	titlePage = "Biblioteca",
	title = "Login")

# Route Logout
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('login'))

def cookies():
	theme = request.cookies.get('theme')
	if theme == None:
		res = make_response("")
		res.set_cookie('theme', 'css/bootstrap.min.neon.css')
	
		return res
	return theme

# Route Main
@app.route("/")
@login_required
def index():
	res = cookies()
	print(res)
	return render_template('index.html',titlePage="Biblioteca",
	res = res)
	
# Routes Errors
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html',
	titlePage = "Not Found"), 404
	
@app.errorhandler(500)
def page_error_internal(e):
	return render_template('500.html',
	titlePage = "Error Internal Server"), 500

# Register Blueprint
app.register_blueprint(animes)
app.register_blueprint(comics)
app.register_blueprint(novelas)
app.register_blueprint(registers)


if __name__ == '__main__':
	csrf.init_app(app)
	app.run(debug=True)