from flask import request, redirect, render_template
from flask import Blueprint, render_template
from app.models.user import User
from app.services.user_service import UserService

# Blueprint llamado 'main'
auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/ingresar')
def login():
    return render_template('auth/login.html')

@auth_routes.route('/registrar')
def register():
    return render_template('auth/register.html')

@auth_routes.route("/register_user", methods=["POST"])
def register_user():
    if request.method == "POST":
        # Obtener los datos del formulario
        name = request.form["name"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        password_confirm = request.form["password_confirm"]

        # Validar los datos del formulario
        user_service = UserService(name, lastname, email, password, password_confirm)
        user_service.validate_all()

        # Registrar al usuario
        User(name, lastname, email, password).register()
        
        return redirect("/ingresar")  # Redirige al login después de registrar
    
    return render_template("register.html")  # Muestra el formulario si es GET