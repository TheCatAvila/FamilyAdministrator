from flask import Blueprint, request, session, redirect, render_template
from app.models.user import User
from app.models.expense_category import ExpenseCategory
from app.models.expense_subcategory import ExpenseSubcategory

# Blueprint llamado 'main'
budget = Blueprint('budget', __name__)

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
        category_name = request.form['category_name']
        subcategory_id = request.form['edit_subcategory_id']
        subcategory_name = request.form['edit_subcategory_name']
        subcategory_budget = request.form['edit_subcategory_budget']
        # Formatear datos recibidos
        budget = subcategory_budget.replace(".", "")

        ExpenseSubcategory(id=subcategory_id, name=subcategory_name, budget=budget).edit()
        
        return redirect(f'/finanzas/presupuesto/{category_name}')

@budget.route('/delete_subcategory', methods=['POST'])
def delete_subcategory():
    if request.method == 'POST':
        # Obtener los datos del formulario
        category_name = request.form['category_name']
        subcategory_id = request.form['subcategory_id']
        ExpenseSubcategory(id=subcategory_id).delete()
        
        return redirect(f'/finanzas/presupuesto/{category_name}')