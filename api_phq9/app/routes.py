# app/routes.py

from flask import jsonify, request
from app import app, db
from .models import User

@app.route('/')
def index():
    return jsonify({'message': 'API is running!'})
