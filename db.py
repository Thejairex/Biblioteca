import sqlite3

class Db:
    def __init__(self) -> None:
        self.conn = sqlite3.Connection("db.db")
        self.cur = self.conn.cursor()
        self.create()
        
        
    def create(self):
        try:
            self.cur.execute("""
                             CREATE TABLE IF NOT EXISTS NOVELS(
                                 id_novel INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name VARCHAR(500) UNIQUE,
                                 type VARCHAR(100),
                                 status VARCHAR(100),
                                 my_status VARCHAR(100),
                                 score FLOAT,
                                 favorite INTEGER,
                                 link VARCHAR(1000))""")
                                 
                                 
            self.conn.commit()
        except Exception as e:
            print(str(e))
            
    def init_thread(self):
        conn = sqlite3.Connection("db.db")
        cur = conn.cursor()
        return conn, cur
    

        
    def table_info(self, table: str, cur):
        cur.execute(f"PRAGMA table_info({table})")
        columnas = cur.fetchall()
        columnas.pop(0)
        columnas_str = ', '.join([columna[1] for columna in columnas])
        print(columnas_str)
        placeholders = ', '.join(['?' for _ in columnas]) 
        print(placeholders)
        return columnas_str, placeholders
    
    def insert(self, table: str, values):
        try:
            conn, cur = self.init_thread()
            columnas, placeholders = self.table_info(table, cur)
            query = f"INSERT INTO {table} ({columnas}) VALUES ({placeholders})"
            cur.execute(query, values)
            conn.commit()
            conn.close()
            return True, None
        
        except Exception as e:
            print(str(f"Ocurrio este erorr: '{e}'"))
            if str(e) == "UNIQUE constraint failed: NOVELS.name":
                return False, "La Novela ya se ha agregado."
        
    def insert_many(self, table: str, values):
        columnas, placeholders = self.table_info(table)
        placeholders = ', '.join(['?' for _ in range(len(values[0]))])  # Crear los placeholders para los valores
        query = f"INSERT INTO {table} ({columnas}) VALUES (null,{placeholders})"
        self.cur.execute(query, values)
        self.conn.commit()
    
    def select_all(self, table):
        conn, cur = self.init_thread()
        query = f"SELECT * FROM {table}"
        cur.execute(query)
        datas = cur.fetchall()
        conn.close()
        return datas
    
if __name__ == "__main__":
    data = Db()
    columnas, holders = data.table_info("Items_Shop")
    print(columnas)