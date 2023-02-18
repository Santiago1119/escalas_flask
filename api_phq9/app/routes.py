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
    print(users)
    return jsonify({'users': [user.to_dict() for user in users]})

@app.route('/users', methods=['POST'])
def create_user():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')

    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({
    "id": user.id,
    "name": user.name,
    "email": user.email
}), 201