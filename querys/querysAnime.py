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