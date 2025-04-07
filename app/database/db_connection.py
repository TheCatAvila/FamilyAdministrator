import mysql.connector
from config.config import db_config

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(**db_config)
            self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as err:
            raise Exception(f"Error al conectar con la base de datos: {err}")
        
    def __enter__(self):
        """Permite usar la clase con 'with' para manejar la conexión automáticamente."""
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Cierra la conexión y el cursor al salir del bloque 'with'."""
        self.cursor.close()
        self.conn.close()

    def execute(self, query, values=None):
        self.cursor.execute(query, values)

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def last_insert_id(self):
        return self.cursor.lastrowid

    def commit(self):
        self.conn.commit()