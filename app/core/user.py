from flask_bcrypt import Bcrypt
from app.models import db, User
from sqlalchemy.exc import IntegrityError

bcrypt = Bcrypt()  # Se debe inicializar en la app Flask

class User:
    def __init__(self, username: str = None, email: str = None, password: str = None):
        """
        Constructor que permite crear una instancia con los datos del usuario.
        """
        self.username = username
        self.email = email
        self.password = password
        self.user = None  # Aquí almacenaremos el objeto User si existe en la BD

    def register(self):
        """
        Registra al usuario usando los atributos de la instancia.
        """
        hashed_password = bcrypt.generate_password_hash(self.password).decode('utf-8')
        new_user = User(username=self.username, email=self.email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            self.user = new_user  # Guardamos el usuario en la instancia
            return {"message": "Usuario registrado exitosamente"}
        except IntegrityError:
            db.session.rollback()
            return {"error": "El usuario o email ya están en uso"}

    def authenticate(self):
        """
        Intenta autenticar al usuario con el email y la contraseña.
        """
        self.user = User.query.filter_by(email=self.email).first()
        if self.user and bcrypt.check_password_hash(self.user.password, self.password):
            return {"message": "Autenticación exitosa", "user": self.user}
        return {"error": "Credenciales incorrectas"}
