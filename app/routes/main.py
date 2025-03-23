from flask import Blueprint, render_template

# Blueprint llamado 'main'
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/finanzas')
def finanzas():
    return render_template('finanzas.html')