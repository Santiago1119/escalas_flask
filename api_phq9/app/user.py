from flask import Blueprint, jsonify, request
from app import app, db
from .models import User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})

@user_bp.route('/users', methods=['POST'])
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