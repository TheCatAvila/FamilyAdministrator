from flask import Blueprint, request, session, redirect, render_template
from app.models.family import Family
from app.models.user import User

# Blueprint llamado 'main'
families = Blueprint('families', __name__)

@families.route('/create_family', methods=['POST'])
def create_family():
    if request.method == 'POST':
        # Obtener los datos del formulario
        family_name = request.form['family_name']

        user_id = session.get("user_id")

        family = Family(name=family_name)
        created_family = family.create()
        if created_family["success"]:
            family.id = created_family["family_id"]
            family.associate_with_user(user_id=user_id, role_id=1)
        else:
            return render_template('error.html', error=created_family["error"])
        
        return redirect('/familias')

@families.route('/select_family', methods=['POST'])
def select_family():
    if request.method == 'POST':
        # Obtener los datos del formulario
        family_id = request.form['family_id']
        user_id = session.get("user_id")

        Family(id=family_id).select(user_id=user_id)
    
        return redirect('/familias')

@families.route('/add_member', methods=['POST'])
def add_member():
    if request.method == 'POST':
        # Obtener los datos del formulario
        family_id = request.form['new_member_family_id']
        member_email = request.form['new_member_email']
        member_rol = request.form['new_member_rol']
        # Obtener el ID del usuario a agregar
        user_response = User(email=member_email).get_id_by_email()
        if not user_response["success"]:
            return render_template('error.html', error=user_response["error"])
        new_member_id = user_response["user_id"]

        Family(id=family_id).associate_with_user(new_member_id, member_rol)


        return redirect('/familias')

@families.route('/remove_member', methods=['POST'])
def remove_member():
    if request.method == 'POST':
        # Obtener los datos del formulario
        family_id = request.form['remove_member_family_id']
        member_id = request.form['remove_member_id']

        Family(id=family_id).disassociate_with_user(member_id)

        return redirect('/familias')