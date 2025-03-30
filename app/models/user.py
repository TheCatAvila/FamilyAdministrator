from flask_bcrypt import Bcrypt
from flask import session
from app.database.db_connection import Database
from app.utils.security_utils import hash_password, check_password

bcrypt = Bcrypt()

class User:
    def __init__(self, id: int = None, name: str = None, lastname: str = None, email: str = None, password: str = None):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def verify_login(self):
        pass
    
    def login(self):
        """Logea al usuario usando los atributos de la instancia."""
        query = "SELECT id, password FROM users WHERE email = %s"
        values = (self.email,)
        
        with Database() as db:
                db.execute(query, values)
                user_result = db.fetchone()
                if user_result and check_password(user_result['password'], self.password):
                    session["user_id"] = user_result["id"]
                    return True
                else:
                    return False

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
        
        except Exception as e:
            return {"success": False, "error": f"Error inesperado: {e}"}
        
    def get_login_data(self):
        """Obtiene los datos del usuario logueado."""
        query = "SELECT name FROM users WHERE id = %s"
        values = (self.id,)
        
        with Database() as db:
            db.execute(query, values)
            login_data = db.fetchone()
            return login_data
