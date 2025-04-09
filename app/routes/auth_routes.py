from flask import request, session, redirect, render_template
from flask import Blueprint, render_template
from flask import jsonify
from app.models.user import User
from app.services.user_service import UserService

# Blueprint llamado 'main'
auth = Blueprint('auth_routes', __name__)

@auth.route('/ingresar')
def login():
    return render_template('auth/login.html')

@auth.route('/registrar')
def register():
    return render_template('auth/register.html')

@auth.route("/login_user", methods=["POST"])
def login_user():
    if request.method == "POST":
        # Obtener los datos del formulario
        email = request.form["email"]
        password = request.form["password"]

        # Validar los datos del formulario
        user_service = UserService(email=email)
        user_service.validate_email()

        # Logear al usuario
        if User(email=email, password=password).login():
            # Si el login es exitoso
            return jsonify({"success": True, "message": "Inicio de sesión exitoso."})
        else:
            # Si el login falla
            return jsonify({"success": False, "message": "Contraseña o email incorrectos."})

@auth.route("/register_user", methods=["POST"])
def register_user():
    if request.method == "POST":
        # Obtener los datos del formulario
        name = request.form["name"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        password = request.form["password"]
        password_confirm = request.form["password_confirm"]

        # Validar los datos del formulario
        user_service = UserService(name=name, 
                                   lastname=lastname, 
                                   email=email, 
                                   password=password, 
                                   password_confirm=password_confirm)
        user_service.validate_all()

        # Registrar al usuario
        User(name=name, lastname=lastname, email=email, password=password).register()
        
        return redirect("/ingresar")  # Redirige al login después de registrar
    
    return render_template("register.html")  # Muestra el formulario si es GET

@auth.route("/logout", methods=["POST"])
def logout():
    """Cierra la sesión del usuario."""
    session.pop("user_id", None)
    return redirect("/ingresar")