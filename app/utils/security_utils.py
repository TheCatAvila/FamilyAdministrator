from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def hash_password(password: str) -> str:
    """Hashea una contraseña usando bcrypt."""
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(hashed_password: str, password: str) -> bool:
    """Verifica si una contraseña coincide con su hash."""
    return bcrypt.check_password_hash(hashed_password, password)