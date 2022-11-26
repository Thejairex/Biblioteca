import time
from main import mysql

class qAnime():

    @classmethod
    def fetchall_anime(self):
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM anime"
            cur.execute(query)
            data = cur.fetchall()
            return data
        except Exception as e:
            return f"No Recibido {e}"

    @classmethod
    def fetchone_anime(self, id):
        try:
            cur = mysql.connection.cursor()
            query = "SELECT * FROM anime WHERE id_anime= {}".format(id)
            cur.execute(query)
            data = cur.fetchone()
            return data
        except Exception as e:
            return f"No Recibido {e}"

    @classmethod
    def fetch10_anime(self, offset):
        cur = mysql.connection.cursor()
        query = "SELECT * FROM anime LIMIT 10 OFFSET {}".format(offset)
        cur.execute(query)
        data = cur.fetchall()
        return data

    def fetchall_anime_asc(self):
        try:
            pass
        except:
            pass

    @classmethod
    def add_anime(self, nombre,capitulos,temporadas,tipo):
        try:
            cur = mysql.connection.cursor()
            query = "INSERT INTO anime VALUES(null,'{}',{},{},'{}')".format(nombre,capitulos,temporadas,tipo)
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
    def delete_anime(self,id):
        try:
            cur = mysql.connection.cursor()
            query = "DELETE FROM anime WHERE id_anime = {}".format(id)
            cur.execute(query)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(str(e))