import re

class UserService:
    def __init__(self, name: str = None, lastname: str = None, email: str = None, password: str = None, password_confirm: str = None):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.password_confirm = password_confirm

    def validate_name(self):
        """Valida solo el nombre y lanza un error si no se cumple."""
        if not self.name or len(self.name.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")

    def validate_lastname(self):
        """Valida solo el apellido."""
        if not self.lastname or len(self.lastname.strip()) < 2:
            raise ValueError("El apellido debe tener al menos 2 caracteres.")

    def validate_email(self):
        """Valida solo el email."""
        if not self.email or len(self.email.strip()) < 5:
            raise ValueError("El email es obligatorio y debe tener al menos 5 caracteres.")

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, self.email):
            raise ValueError("El email no tiene un formato válido.")

    def validate_password(self):
        """Valida solo la contraseña."""
        if self.password != self.password_confirm:
            raise ValueError("Las contraseñas no coinciden.")

        if len(self.password) < 8:
            raise ValueError("La contraseña debe tener al menos 8 caracteres.")

    def validate_all(self):
        """Ejecuta todas las validaciones. Si alguna falla, lanza una excepción."""
        self.validate_name()
        self.validate_lastname()
        self.validate_email()
        self.validate_password()
