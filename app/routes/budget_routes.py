from flask import Blueprint, request, session, redirect, render_template
from app.models.user import User
from app.models.expense_category import ExpenseCategory
from app.models.expense_subcategory import ExpenseSubcategory

# Blueprint llamado 'main'
budget = Blueprint('budget', __name__)

@budget.route('/finanzas/presupuesto', methods=['GET'])
@budget.route('/finanzas/presupuesto/<string:category_name>', methods=['GET'])
def presupuesto(category_name=None):
    # Verificar si el usuario está logueado y obtener sus datos de sesión
    user_id = session.get("user_id")
    user_login_data = User(id=user_id).get_login_data()
    if not user_login_data:
        return redirect("/ingresar")
    
    # Obtener la familia seleccionada del usuario
    user_response = User(id=user_id).get_family_selected_id()
    family_id = user_response["family_selected_id"]

    # Obtener las categorías de egresos
    all_categories_response = ExpenseCategory(family_id=family_id).get_all_of_family()
    if not all_categories_response["success"]:
        return render_template('error.html', error=categories["error"])
    categories = all_categories_response["categories"]
    # Obtener el presupuesto total de la familia
    total_budget_response = ExpenseSubcategory().get_total_budget_by_family(family_id=family_id)
    if not total_budget_response["success"]:
        return render_template('error.html', error=total_budget_response["error"])
    total_budget = total_budget_response["total_budget"]

    subcategories = []
    selected_category = None
    if category_name:
        expense_category = ExpenseCategory(name=category_name)
        category_id_response = expense_category.get_id_by_name()
        if not category_id_response["success"]:
            return render_template('error.html', error=category_id_response["error"])
        selected_category = category_name
        category_id = category_id_response["id"]
    
        subcategories_response = ExpenseSubcategory(category_id=category_id).get_by_category_id()
        if not subcategories_response["success"]:
            return render_template('error.html', error=subcategories_response["error"])
        subcategories = subcategories_response["subcategories"]

    return render_template('presupuesto.html', user_login_data=user_login_data, categories=categories, subcategories=subcategories, selected_category=selected_category,
                           total_budget=total_budget)

# CATEGORÍAS
# ----------------------------------------------------------------------
@budget.route('/add_category', methods=['POST'])
def add_category():
    if request.method == 'POST':
        # Obtener los datos del formulario
        category_name = request.form['category_name']

        user_id = session.get("user_id")
        user_response = User(id=user_id).get_family_selected_id()
        family_id = user_response["family_selected_id"]

        ExpenseCategory(name=category_name, family_id=family_id).create()
        
        return redirect('/finanzas/presupuesto')

@budget.route('/get_subcategorias/<int:categoria_id>')
def get_subcategorias(categoria_id):
    # Suponiendo que tienes una función que obtiene subcategorías desde la base de datos
    subcategories_result = ExpenseSubcategory(category_id=categoria_id).get_by_category_id()
    if not subcategories_result["success"]:
        return render_template('error.html', error=subcategories_result["error"])
    subcategories = subcategories_result["subcategories"]
    return subcategories


# SUB CATEGORÍAS
# ----------------------------------------------------------------------
@budget.route('/add_subcategory', methods=['POST'])
def add_subcategory():
    if request.method == 'POST':
        # Obtener los datos del formulario
        category_name = request.form['category_name']
        subcategory_name = request.form['subcategory_name']
        subcategory_budget = request.form['subcategory_budget']

        # Formatear datos recibidos
        budget = subcategory_budget.replace(".", "")

        category_id_response = ExpenseCategory(name=category_name).get_id_by_name()
        if not category_id_response["success"]:
            return render_template('error.html', error=category_id_response["error"])
        category_id = category_id_response["id"]

        ExpenseSubcategory(name=subcategory_name, budget=budget ,category_id=category_id).create()
        
        return redirect(f'/finanzas/presupuesto/{category_name}')

@budget.route('/edit_subcategory', methods=['POST'])
def edit_subcategory():
    if request.method == 'POST':
        # Obtener los datos del formulario
        subcategory_id = request.form['subcategory_id']
        #ExpenseSubcategory(name=category_name, category_id=1).create_subcategory()
        
        return redirect('/finanzas/presupuesto')

@budget.route('/delete_subcategory', methods=['POST'])
def delete_subcategory():
    if request.method == 'POST':
        # Obtener los datos del formulario
        subcategory_id = request.form['subcategory_id']
        ExpenseSubcategory(id=subcategory_id).delete()
        
        return redirect('/finanzas/presupuesto')