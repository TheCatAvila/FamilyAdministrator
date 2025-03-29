from flask import Flask, session
from flask_session import Session
from config.config import flask_config

def create_app():
    app = Flask(__name__)
    app.secret_key = flask_config['SECRET_KEY']
    app.config.update(flask_config)

    # Inicializar Flask-Session
    Session(app)

    @app.before_request
    def make_session_permanent():
        session.permanent = True

    # Importar y registrar Blueprints
    from app.routes.main import main
    from app.routes.auth import auth_routes
    app.register_blueprint(main)
    app.register_blueprint(auth_routes)

    return app
