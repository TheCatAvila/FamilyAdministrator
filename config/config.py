import os
from dotenv import load_dotenv
from datetime import timedelta

# Asegurar que el directorio de sesiones exista
if not os.path.exists('./flask_sessions'):
    os.makedirs('./flask_sessions')

# Carga las variables del archivo .env
load_dotenv()  

class Config:

    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    SECRET_KEY = os.getenv("SECRET_KEY")

    @staticmethod
    def get_db_config():
        return {
            'host': Config.DB_HOST,
            'user': Config.DB_USER,
            'password': Config.DB_PASSWORD,
            'database': Config.DB_NAME
        }
    
    @staticmethod
    def get_flask_config():
        return {
            'SECRET_KEY': Config.SECRET_KEY,
            'SESSION_TYPE': 'filesystem',
            'SESSION_FILE_DIR': './flask_sessions',
            'PERMANENT_SESSION_LIFETIME': timedelta(days=30)
        }

# Obtener la configuración de la base de datos
db_config = Config.get_db_config()
# Obtener la configuración de Flask
flask_config = Config.get_flask_config()
