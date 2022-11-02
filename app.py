from flask import Flask, render_template
from flask_mysqldb import MySQL

from blueprint.animes import animes
from blueprint.comics import comics
from blueprint.novelas import novelas


app = Flask(__name__)

mysql = MySQL(app)
app.config['MYSQL_HOST'] = 'Thejairex2.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'Thejairex2'
app.config['MYSQL_PASSWORD'] = 'Aiwa2015'
app.config['MYSQL_DB'] = 'Thejairex2$biblioteca'
app.secret_key = "OtakuTeca"

# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = ""
# app.config['MYSQL_DB'] = "biblioteca"

@app.route("/")
def index():
	return render_template("index.html" , titlePage="Biblioteca")

app.register_blueprint(animes)
app.register_blueprint(comics)
app.register_blueprint(novelas)

if __name__ == '__main__':
	app.run(debug=True)