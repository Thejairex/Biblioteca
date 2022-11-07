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
    def fetchall_anime_asc(self):
        try:
            pass
        except:
            pass