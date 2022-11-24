# Import libraries
from flask import Flask, render_template, redirect, request, url_for, make_response, jsonify, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_wtf.csrf import CSRFProtect

import hashlib
from querys.entities.User import User
# Import Modules
from blueprint.Funciones import Funciones
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

app.config['MYSQL_HOST'] = 'Thejairex2.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'Thejairex2'
app.config['MYSQL_PASSWORD'] = 'Aiwa2015'
app.config['MYSQL_DB'] = 'Thejairex2$biblioteca'
app.secret_key = "OtakuTeca"


# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = ""
# app.config['MYSQL_DB'] = "biblioteca"

# Login

login_manager = LoginManager(app)
login_manager.login_view = "login"


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
        next = request.form['next']
        print(next)
        user = User(0,username,password,None)
        
        logged_user = qUser.loginUser(user)
        
        if logged_user == None:
            flash("El usuario no esta registrado")
            return redirect(url_for('login', next=next))
        else:
            if logged_user.password:
                login_user(logged_user)
                return redirect(next)
            else:
                flash("Contraseña incorrecta")
                return redirect(url_for('login', next=next))


# Route Login
@app.route("/login")
def login():
    print(len(request.args))
    if len(request.args) != 0 and request.args.get('next'):
        next = request.args.get('next')
        
        return render_template("login.html", 
		titlePage = "Biblioteca",
		title = "Iniciar Sesion",
		next = next), 200
    else:
        return render_template("login.html", 
		titlePage = "Biblioteca",
		title = "Iniciar Sesion",
        next = "/")
    
    # colum = []
    # data = []
    
    # for x in request.args:
    #     colum.append(x)
    #     data.append(request.args.get(x))

# Route Logout
@app.route('/logout')
def logout():
	logout_user()
	flash('Se ha cerrado sesion correctamente.')
	return redirect(url_for('login')) ,200


# Route Main
@app.route("/")
@login_required
def index():
	print(current_user.username)
	return render_template('index.html',titlePage="Biblioteca"), 200
	

	
	

# Register Blueprint
app.register_blueprint(animes)
app.register_blueprint(comics)
app.register_blueprint(novelas)
app.register_blueprint(registers)


if __name__ == '__main__':
	csrf.init_app(app)
	app.run(debug=True)