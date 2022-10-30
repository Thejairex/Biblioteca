from flask import  request, Blueprint, render_template

from querys.querysAnime import qAnime
from blueprint.Funciones import Filter


animes = Blueprint('animes', __name__, template_folder='app/templates')

@animes.route("/animes")
def animesList():
	data = qAnime.fetchall_anime()
	return render_template("animes.html", datas=data, titlePage="Animes - Biblioteca")

@animes.route("/anime" , methods=['POST'])
def anime():
	if request.method == 'POST':
		search = request.form['search']
		data = qAnime.fetchall_anime()
		dataFilter = Filter.Filter(data, search)

		if len(dataFilter) != 1:
			return render_template("animes.html", datas=dataFilter, titlePage="Animes - Biblioteca")

		else:
			return render_template("anime.html", datas=dataFilter[0], titlePage="Anime - Biblioteca")
