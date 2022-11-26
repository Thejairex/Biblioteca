# Librarys
from flask import  request, Blueprint, render_template, redirect, flash, abort
from flask_login import login_required

# Modules
from querys.querysNovelas import qNovela # Querys Novelas
from blueprint.Funciones import Funciones # Filter System


# Init blueprint novelas
novelas = Blueprint('novelas', __name__, template_folder='app/templates')

# All novelas
@novelas.route("/novelas")
@login_required
def novelasList():
	
	data = qNovela.fetchall_novela()
	return render_template("series/series.html", 
		datas = data, 
		titlePage = "Novelas - Biblioteca",
		title = "Lista de Novelas",
		serie = "novela",
		th = "autor",
		case = "Autor",
		addForm = "Novela")

# Search novelas
@novelas.route("/novela" , methods=['POST'])
@login_required
def novela():
	if request.method == 'POST':
		search = request.form['search']
		data = qNovela.fetchall_novela()

		dataFilter = Funciones.Filter(data, search) # Filter

		if len(dataFilter) != 1:
			return render_template("series/series.html", 
				datas = dataFilter, 
				titlePage = "Comics - Biblioteca",
				title = "{} Resultados".format(len(dataFilter)),
				serie = "comic",
				th = "autor",
				case = "Autor",
				addForm = "Novela")
		else:
			return render_template("series/search.html", 
				datas=dataFilter[0],
				titlePage = "Novelas - Biblioteca",
				title = "{} Resultado".format(len(dataFilter)),
				serie = "novela",
				th = "autor",
				case = "Autor",
				addForm = "Novela")

# Add novela
@novelas.route("/api/addNovela" , methods=['POST'])
@login_required
def add_anime():
	if request.method == 'POST':
		nombre = request.form['nombre']
		capitulos = int(request.form['capitulos'])
		autor = request.form['Autor']
		tipoTemp = int(request.form.get('tipo'))
		tipo = ['Japones', 'Coreano', 'Chino']
		tipo = tipo[tipoTemp]
		
		data = qNovela.add_novela(nombre,capitulos,autor,tipo)
		if data == True:
			flash('Se ha agregado exitosamente...')
			return	redirect('/novelas')
		elif data == False:
			flash('La novela ya existe...')
			return	redirect('/novelas')
		else:
			abort(500)
   
# Api novela
@novelas.route("/api/novela/<id>" , methods=['POST','GET'])
@login_required
def apiAnime(id):
    if request.method == "GET":
        data = qNovela.delete_novela(id)
        if data:
            flash("Se ha eliminado exitosamente...")
            return redirect('/novelas')
        else:
            print(data)
            return redirect('/novelas')
        
    if request.method == "POST":
        nombre = request.form['nombre']
        capitulos = int(request.form['capitulos'])
        Autor = request.form['Autor']
        tipoTemp = int(request.form.get('tipo'))
        tipo = ['Japones', 'Coreano', 'Chino']
        tipo = tipo[tipoTemp]
        
        data = qNovela.edit_novela(id,nombre,capitulos,Autor,tipo)
        
        if data == True:
            flash('Se ha editado exitosamente...')
            return	redirect('/novelas')
        else:
            abort(500)