from flask import Blueprint, session, redirect, render_template, request
from app.models.family import Family
from app.models.user import User
from app.models.expense_category import ExpenseCategory
from app.models.expense_subcategory import ExpenseSubcategory

# Blueprint llamado 'main'
main = Blueprint('main', __name__)

@main.route('/')
def index():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return render_template("index.html")

    return render_template('index.html', user_login_data=user_login_data)

@main.route('/familias')
def familias():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return redirect("/ingresar")
    
    # Obtener grupo familiar
    family_response = Family(id=user_id).get()
    families = family_response["families"] if family_response["success"] else []
    if not family_response["success"]:
        return render_template('error.html', error=family_response["error"])
    
    # Obtener la familia seleccionada por el usuario
    user_response = User(id=user_id).get_family_selected_id()
    family_selected_id = user_response["family_selected_id"]

    return render_template('familias.html', user_login_data=user_login_data, families=families, family_selected_id=family_selected_id)

@main.route('/finanzas')
def finanzas():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return redirect("/ingresar")
    
    # Obtener la familia seleccionada del usuario
    user_response = User(id=user_id).get_family_selected_id()
    family_id = user_response["family_selected_id"]

    # Obtener las categorías de egresos
    all_categories_response = ExpenseCategory().get_select_data()
    if not all_categories_response["success"]:
        return render_template('error.html', error=all_categories_response["error"])
    categories = all_categories_response["categories"]

    # Obtener el presupuesto total de la familia
    total_budget_response = ExpenseSubcategory().get_total_budget_by_family(family_id=family_id)
    if not total_budget_response["success"]:
        return render_template('error.html', error=total_budget_response["error"])
    total_budget = total_budget_response["total_budget"]

    return render_template('finanzas.html', user_login_data=user_login_data, categories=categories, total_budget=total_budget)

@main.route('/prestamos')
def prestamos():

    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return redirect("/ingresar")

    return render_template('prestamos.html', user_login_data=user_login_data)