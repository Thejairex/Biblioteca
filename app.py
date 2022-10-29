from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from querys.querysAnime import qAnime
from querys.querysComic import qComcic
from querys.querysNovelas import qNovela

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
	
	return render_template("index.html")

@app.route("/animes")
def animes():
	data = qAnime.fetchall_anime()
	return render_template("animes.html", datas=data)

@app.route("/comics")
def comics():
	data = qComcic.fetchall_comic()
	return render_template("comics.html", datas=data)

@app.route("/novelas")
def Novelas():
	data = qNovela.fetchall_novela()
	return render_template("novelas.html", datas=data)

@app.route("/comic" , methods=['POST'])
def comic():
	if request.method == 'POST':
		id = request.form['id']
		data = qComcic.fetchone_comic(id)
		return render_template("comic.html", datas=data, serie="comic", titulo="Comic")

@app.route("/anime" , methods=['POST'])
def anime():
	if request.method == 'POST':
		id = request.form['id']
		data = qAnime.fetchone_anime(id)
		return render_template("anime.html", datas=data)

@app.route("/novela" , methods=['POST'])
def novela():
	if request.method == 'POST':
		id = request.form['id']
		data = qNovela.fetchone_novela(id)
		return render_template("comic.html", datas=data,  serie="novela", titulo="Novela")


if __name__ == '__main__':
	app.run(debug=True)