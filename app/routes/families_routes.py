from flask import Blueprint, request, session, redirect, render_template
from app.models.family import Family

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
            family.associate_with_user(user_id=user_id)
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