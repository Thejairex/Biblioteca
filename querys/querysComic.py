import time
from main import mysql

class qComcic():

    @classmethod
    def fetchall_comic(self):
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM comic"
            cur.execute(query)
            data = cur.fetchall()
            return data
        except Exception as e:
            return f"No Recibido {e}"

    @classmethod
    def fetchone_comic(self, id):
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM comic WHERE id_comic= {}".format(id)
            cur.execute(query)
            data = cur.fetchone()
            return data
        except Exception as e:
            return f"No Recibido {e}"

    @classmethod
    def add_comic(self, nombre,capitulos,autor,tipo):
        try:
            cur = mysql.connection.cursor()
            query = "INSERT INTO comic VALUES(null,'{}',{},'{}','{}')".format(nombre,capitulos,autor,tipo)
            cur.execute(query)
            mysql.connection.commit()
            return True
        except Exception as e:
            error = (1062, "Duplicate entry '{}' for key 'nombre'".format(nombre))
            if str(error) == str(e):
                return False
            else: 
                print(str(e))
                
    @classmethod
    def delete_comic(self,id):
        try:
            cur = mysql.connection.cursor()
            query = "DELETE FROM comic WHERE id_comic = {}".format(id)
            cur.execute(query)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(str(e))
    
    @classmethod
    def edit_comic(self, id,nombre,cap,autor, tipo):
        try:
            cur = mysql.connection.cursor()
            query = "UPDATE comic SET nombre='{}', cantidad_cap={} , autor='{}', tipo='{}' WHERE id_comic = {}".format(nombre,cap,autor,tipo,id)
            cur.execute(query)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(str(e))