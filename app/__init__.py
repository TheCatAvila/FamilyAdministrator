from flask import Flask, session
from flask_session import Session
from config.config import flask_config
from app.database.db_dll import DLL

def create_app():
    app = Flask(__name__)
    app.secret_key = flask_config['SECRET_KEY']
    app.config.update(flask_config)

    # Inicializar Flask-Session
    Session(app)

    # Crear la base de datos y tablas si no existen
    DLL()

    @app.before_request
    def make_session_permanent():
        session.permanent = True

    # Importar y registrar Blueprints
    from app.routes.main_routes import main
    from app.routes.auth_routes import auth
    from app.routes.finance_routes import finance
    from app.routes.budget_routes import budget
    from app.routes.families_routes import families
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(finance)
    app.register_blueprint(budget)
    app.register_blueprint(families)

    return app
