from flask_bcrypt import Bcrypt
from app.database.db_connection import Database
from app.utils.security import hash_password

bcrypt = Bcrypt()

class User:
    def __init__(self, name: str = None, lastname: str = None, email: str = None, password: str = None):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def verify_login(self):
        pass
    
    def login(self):
        """Logea al usuario usando los atributos de la instancia."""
        try:
            query = "INSERT INTO users (name, lastname, email, password, register_date) VALUES (%s, %s)"
            values = (self.name, self.lastname, self.email)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Usuario registrado exitosamente."}
        
        except mysql.connector.Error as err:
            return {"success": False, "error": f"Error en la base de datos: {err}"}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}

    def register(self):
        """Registra al usuario usando los atributos de la instancia."""
        try:
            hashed_password = hash_password(self.password)
            query = "INSERT INTO users (name, lastname, email, password, register_date) VALUES (%s, %s, %s, %s, NOW())"
            values = (self.name, self.lastname, self.email, hashed_password)

            with Database() as db:
                db.execute(query, values)
                db.commit()

            return {"success": True, "message": "Usuario registrado exitosamente."}
        
        except mysql.connector.Error as err:
            return {"success": False, "error": f"Error en la base de datos: {err}"}
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
