from flask import Blueprint, jsonify, request
from app import app, db
from .models import AnswersPHQ9, ResultPHQ9
import re

motivation_treatment_bp = Blueprint('motivation_treatment', __name__, url_prefix='/motivation_treatment')

@motivation_treatment_bp.route('/')
def index():
    return 'funciona'