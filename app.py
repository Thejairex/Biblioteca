# Import libraries
from flask import Flask, render_template, redirect, request, url_for, make_response
from flask_mysqldb import MySQL

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

# Api Login
@app.route("/api/login", methods=["POST"])
def api_login():
	if request.method == "POST":
		data = request.form['username'], request.form['lastname']
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
	status = request.cookies.get('status')

	print(status)
	if status == None:
		resp = make_response(redirect(url_for('login')))
		status = "False"
		resp.set_cookie('status', status)
		return resp
	else:
		return render_template("index.html")

# Register Blueprint
app.register_blueprint(animes)
app.register_blueprint(comics)
app.register_blueprint(novelas)

if __name__ == '__main__':
	app.run(debug=True, port=3000)