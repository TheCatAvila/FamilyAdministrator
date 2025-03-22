from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_migrate import Migrate

# Inicializar SQLAlchemy
db = SQLAlchemy()

# Tabla intermedia para la relación muchos a muchos entre usuarios y familias
user_family = db.Table('user_family',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('family_id', db.Integer, db.ForeignKey('family.id'), primary_key=True),
    db.Column('role', db.String(50), nullable=False)  # 'admin' o 'user'
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    families = relationship('Family', secondary=user_family, back_populates='members')

class Family(db.Model):
    __tablename__ = 'family'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    members = relationship('User', secondary=user_family, back_populates='families')
    expenses = relationship('Egreso', back_populates='family')

class Egreso(db.Model):
    __tablename__ = 'egresos'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('egreso_category.id'), nullable=False)
    subcategory_id = db.Column(db.Integer, db.ForeignKey('egreso_subcategory.id'))
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'), nullable=False)
    family = relationship('Family', back_populates='expenses')
    category = relationship('EgresoCategory')
    subcategory = relationship('EgresoSubcategory')

class EgresoCategory(db.Model):
    __tablename__ = 'egreso_category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    subcategories = relationship('EgresoSubcategory', back_populates='category')

class EgresoSubcategory(db.Model):
    __tablename__ = 'egreso_subcategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('egreso_category.id'), nullable=False)
    category = relationship('EgresoCategory', back_populates='subcategories')
