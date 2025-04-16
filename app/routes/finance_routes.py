from flask import Blueprint, session, redirect, render_template, request
from app.models.expenses import Expense
from app.models.user import User
from app.models.expense_category import ExpenseCategory
from app.models.expense_subcategory import ExpenseSubcategory

# Blueprint llamado 'main'
finance= Blueprint('finance', __name__)

@finance.route('/finanzas/presupuesto', methods=['GET'])
@finance.route('/finanzas/presupuesto/<string:category_name>', methods=['GET'])
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

@finance.route('/add_expense', methods=['POST'])
def add_expense():
    if request.method == 'POST':
        # Obtener los datos del formulario
        expense_date = request.form['expense_date']
        subcategory_id = int(request.form['subcategoria'])
        expense_amount = request.form['expense_amount']
        expense_description = request.form['expense_description']
        # Formatear datos recibidos
        format_amount = expense_amount.replace(".", "")
        # Obtener el ID del usuario de la sesión
        user_id = session.get("user_id")
        # Obtener la familia seleccionada del usuario
        user_response = User(id=user_id).get_family_selected_id()
        family_id = user_response["family_selected_id"]

        # Crear la instancia de Expense y guardar el gasto
        Expense(
            user_id=user_id,
            family_id=family_id,
            date=expense_date,
            subcategory_id=subcategory_id,
            amount=float(format_amount),
            description=expense_description
        ).create()
    
    return redirect('/finanzas')

@finance.route('/edit_expense', methods=['POST'])
def edit_expense():
    if request.method == 'POST':
        # Obtener los datos del formulario
        expense_id = request.form['edit_expense_id']
        expense_date = request.form['edit_expense_date']
        expense_subcategory = request.form['edit_subcategoria']
        expense_amount = request.form['edit_expense_amount']
        expense_description = request.form['edit_expense_description']
        # Formatear datos recibidos
        amount = expense_amount.replace(".", "")

        Expense(id=expense_id, date=expense_date, subcategory_id=expense_subcategory, 
                amount=amount, description=expense_description).edit()
        
        return redirect(f'/finanzas')

@finance.route('/delete_expense', methods=['POST'])
def delete_expense():
    if request.method == 'POST':
        # Obtener los datos del formulario
        expense_id = request.form['expense_id']

        Expense(id=expense_id).delete()
        
        return redirect(f'/finanzas')