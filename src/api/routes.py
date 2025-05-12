"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint, select
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/register', methods=['POST'])
def register():
    try:
        # extraer datos del pedido
        data = request.json
        # verificar que tenemos todos los datos
        if not data['email'] or not data['password']:
            raise Exception("missing data")
        # verificar si el email ya esta registrado
        stm = select(User).where(User.email == data['email'])
        # scalar devuelve un objeto, sino se devolvería el query a la bd como tupla
        existing_user = db.session.execute(stm).scalar_one_or_none()
        if existing_user:
            return jsonify({"error": "email en uso, intenta logearte"}), 418
        new_user = User(
            email=data['email'],
            password=data['password'],
            is_active=True
        )
        # Aquí probablemente falta guardar el usuario y hacer commit en la base de datos
        # db.session.add(new_user)
        # db.session.commit()

    except Exception as e:
        print(e)
        return jsonify({"Error": 'algo paso'})
    

@api.route('/login', methods=['POST'])
def login():
    try:
        # Extraer datos del pedido
        data = request.json
        # Verificar que tenemos todos los datos
        if not data['email'] or not data['password']:
            raise Exception("missing data")
        # Verificar si el email ya está registrado
        stm = select(User).where(User.email == data['email'])
        user = db.session.execute(stm).scalar_one_or_none()
        if not user:
            return jsonify({"error": "el email no esta registrado"}), 418

        if user.password != data['password']:
            return jsonify({"error": "email/contraseña no valido"}), 418

        return jsonify(user.serialize())

    except Exception as e:
        print(e)
        return jsonify({"Error": 'algo paso'})
