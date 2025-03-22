from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from config.config import config

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_name="development"):
    app = Flask(__name__)

    if config_name not in config:
        raise ValueError(f"Configuración '{config_name}' no es válida. Usa 'development' o 'production'.")

    app.config.from_object(config[config_name])

    db.init_app(app)

    # Importar y registrar Blueprints
    from app.routes.main import main
    app.register_blueprint(main)

    # Crear la base de datos si estamos en desarrollo
    if config_name == "development":
        with app.app_context():
            db.create_all()

    return app
