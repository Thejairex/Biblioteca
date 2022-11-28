# Library
from flask import  request, Blueprint, render_template, flash, redirect, abort
from flask_login import login_required, current_user

# Modules
from querys.querysComic import qComcic # Querys Comic
from blueprint.Funciones import Funciones # Filter System

# Init blueprint comics
comics = Blueprint('comics', __name__, template_folder='app/templates')

# All Comics
@comics.route("/comics")
@login_required
def comicsList():
    print(current_user.rol)
    data = qComcic.fetchall_comic()
    return render_template("series/series.html", 
		datas = data, 
		titlePage = "Comics - Biblioteca",
		title = "Lista de Comics",
		serie = "comic",
		th = "Autor",
		case = "Autor",
		addForm = 'Comic')


# Search Comics
@comics.route("/comic" , methods=['POST'])
@login_required
def comic():
	if request.method == 'POST':
		search = request.form['search']
		data = qComcic.fetchall_comic()
		dataFilter = Funciones.Filter(data, search) # Filter
		if len(dataFilter) != 1:
			return render_template("series/series.html", 
				datas = dataFilter, 
				titlePage = "Comics - Biblioteca",
				title = "{} Resultados".format(len(dataFilter)),
				serie = "comic",
				th = "Autor",
				case = "Autor",
				addForm = 'Comic')
			
		else:
			return render_template("series/search.html", 
				data=dataFilter[0],
				titlePage = "Comics - Biblioteca",
				title = "{} Resultado".format(len(dataFilter)),
				serie = "comic",
				th = "Autor",
				case = "Autor",
				addForm = 'Comic')

# Add comic
@comics.route("/api/addComic" , methods=['POST'])
@login_required
def add_anime():
    if current_user.rol == 'Administrador':
        if request.method == 'POST':
            nombre = request.form['nombre']
            capitulos = int(request.form['capitulos'])
            autor = request.form['Autor']
            tipoTemp = int(request.form.get('tipo'))
            tipo = ['Japones', 'Coreano', 'Chino']
            tipo = tipo[tipoTemp]
            
            data = qComcic.add_comic(nombre,capitulos,autor,tipo)
            if data == True:
                flash('Se ha agregado exitosamente...')
                return	redirect('/comics')
            elif data == False:
                flash('El comic ya existe...')
                return	redirect('/comics')
            else:
                abort(500)
   
# Api anime
@comics.route("/api/comic/<id>" , methods=['POST','GET'])
@login_required
def apiAnime(id):
    if current_user.rol == 'Administrador':
        if request.method == "GET":
            data = qComcic.delete_comic(id)
            if data:
                flash("Se ha eliminado exitosamente...")
                return redirect('/comics')
            else:
                print(data)
                return redirect('/comics')
        if request.method == "POST":
            nombre = request.form['nombre']
            capitulos = int(request.form['capitulos'])
            Autor = request.form['Autor']
            tipoTemp = int(request.form.get('tipo'))
            tipo = ['Japones', 'Coreano', 'Chino']
            tipo = tipo[tipoTemp]
            data = qComcic.edit_comic(id,nombre,capitulos,Autor,tipo)
            if data == True:
                flash('Se ha editado exitosamente...')
                return	redirect('/comics')
            else:
                abort(500)
    else:
        abort(401)