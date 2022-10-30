from flask import  request, Blueprint, render_template

from querys.querysComic import qComcic
from blueprint.Funciones import Filter

comics = Blueprint('comics', __name__, template_folder='app/templates')

@comics.route("/comics")
def comicsList():
	data = qComcic.fetchall_comic()
	return render_template("comics.html", datas=data, titlePage="Comics - Biblioteca")

@comics.route("/comic" , methods=['POST'])
def comic():
	if request.method == 'POST':
		search = request.form['search']
		data = qComcic.fetchall_comic()
		dataFilter = Filter.Filter(data, search)
		if len(dataFilter) != 1:
			return render_template("comics.html", datas=dataFilter, titlePage="Animes - Biblioteca")
			
		else:
			return render_template("comic.html", datas=dataFilter[0], serie="comic", titulo="Comic", titlePage="Comic - Biblioteca")
