import mysql.connector
from app.database.db_connection import Database
from config.config import db_config

class DLL:

    def __init__(self):
        """Constructor que ejecuta la configuración de la base de datos al instanciar la clase."""
        self.create_tables("app/database/schema.sql")

    def create_tables(self, sql_file_path):
        """Lee un archivo .sql y ejecuta las consultas para crear las tablas."""
        try:
            with open(sql_file_path, "r", encoding="utf-8") as file:
                sql_script = file.read()

            with Database() as db:
                for statement in sql_script.split(";"):
                    statement = statement.strip()
                    if statement:  # Evitar ejecutar líneas vacías
                        db.execute(statement)
                db.commit()
                print("✅ Tablas creadas correctamente.")
        except (mysql.connector.Error, FileNotFoundError) as e:
            print(f"❌ Error al crear las tablas: {e}")