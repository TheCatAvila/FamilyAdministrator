from flask import Blueprint, session, redirect, render_template
from app.models.user import User

# Blueprint llamado 'main'
main = Blueprint('main', __name__)

@main.route('/')
def index():

    # Verificar si el usuario está logueado
    user_id = session.get("user_id")
    if not user_id:
        return render_template('index.html')
        
    # Obtener los datos del usuario logueado
    user_login_data = User(id=user_id).get_login_data()
    user_name = user_login_data["name"]

    return render_template('index.html', user_name=user_name)

@main.route('/finanzas')
def finanzas():

    # Verificar si el usuario está logueado
    user_id = session.get("user_id")
    if not user_id:
        return redirect("/ingresar")

    # Obtener los datos del usuario logueado
    user_login_data = User(id=user_id).get_login_data()
    user_name = user_login_data["name"]

    return render_template('finanzas.html', user_name=user_name)