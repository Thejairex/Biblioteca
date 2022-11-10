import time
from main import mysql

class qNovela():

    @classmethod
    def fetchall_novela(self):
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM novela"
            cur.execute(query)
            data = cur.fetchall()
            return data
        except Exception as e:
            return f"No Recibido {e}"

    @classmethod
    def fetchone_novela(self, id):
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM novela WHERE id_novela= {}".format(id)
            cur.execute(query)
            data = cur.fetchone()
            return data
        except Exception as e:
            return f"No Recibido {e}"

    @classmethod
    def add_comic(self, nombre,capitulos,autor,tipo):
        try:
            cur = mysql.connection.cursor()
            query = "INSERT INTO novela VALUES(null,'{}',{},'{}','{}')".format(nombre,capitulos,autor,tipo)
            cur.execute(query)
            mysql.connection.commit()
            return True
        except Exception as e:
            error = (1062, "Duplicate entry '{}' for key 'nombre'".format(nombre))
            if str(error) == str(e):
                return False
            else: 
                print(str(e))