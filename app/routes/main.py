from flask import Blueprint, session, redirect, render_template, request
from app.models.family import Family
from app.models.user import User
from app.models.expense_category import ExpenseCategory

# Blueprint llamado 'main'
main = Blueprint('main', __name__)

@main.route('/')
def index():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return render_template("index.html")

    # Obtener grupo familiar
    family_response = Family(id=user_id).get()
    families = family_response["families"] if family_response["success"] else []
    if not family_response["success"]:
        return render_template('error.html', error=family_response["error"])

    return render_template('index.html', user_login_data=user_login_data, families=families)

@main.route('/create_family', methods=['POST'])
def add_category():
    if request.method == 'POST':
        # Obtener los datos del formulario
        family_name = request.form['family_name']

        user_id = session.get("user_id")

        family = Family(name=family_name)
        created_family = family.create()
        print("Familia creada: ", created_family)
        if created_family["success"]:
            family.id = created_family["family_id"]
            #family.associate_with_user(user_id=user_id)
            print("Familia asociada al usuario: ", family.associate_with_user(user_id=user_id))
        else:
            return render_template('error.html', error=created_family["error"])
        
        return redirect('/')

@main.route('/finanzas')
def finanzas():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return redirect("/ingresar")

    # Obtener las categorías de egresos
    all_categories_response = ExpenseCategory().get_select_data()
    if not all_categories_response["success"]:
        return render_template('error.html', error=all_categories_response["error"])
    categories = all_categories_response["categories"]

    return render_template('finanzas.html', user_login_data=user_login_data, categories=categories)