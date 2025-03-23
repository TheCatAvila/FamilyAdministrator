from flask import Flask
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Importar y registrar Blueprints
    from app.routes.main import main
    from app.routes.auth import auth_routes
    app.register_blueprint(main)
    app.register_blueprint(auth_routes)

    return app
