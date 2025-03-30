from flask import Blueprint, session, redirect, render_template
from app.models.user import User

# Blueprint llamado 'main'
main = Blueprint('main', __name__)

@main.route('/')
def index():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return render_template("index.html")
    
    # Si el usuario está logueado, obtenemos sus datos
    user_name = user_login_data["name"]

    return render_template('index.html', user_name=user_name)

@main.route('/finanzas')
def finanzas():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return redirect("/ingresar")
    
    # Si el usuario está logueado, obtenemos sus datos
    user_name = user_login_data["name"]

    return render_template('finanzas.html', user_name=user_name)

@main.route('/finanzas/presupuesto')
def presupuesto():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return redirect("/ingresar")
    
    # Si el usuario está logueado, obtenemos sus datos
    user_name = user_login_data["name"]

    return render_template('presupuesto.html', user_name=user_name)