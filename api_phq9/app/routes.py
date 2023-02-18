# app/routes.py

from flask import jsonify, request
from app import app, db
from .models import User

@app.route('/')
def index():
    return jsonify({'message': 'API is running!'})

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})

@app.route('/users', methods=['POST'])
def create_user():
    name = request.json.get('name')
    email = request.json.get('email')

    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({
    "id_user": user.id_user,
    "name": user.name,
    "email": user.email
}), 201