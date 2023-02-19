from flask import Blueprint, jsonify, request
from app import app, db
from .models import AnswersPHQ9, ResultPHQ9

phq9_bp = Blueprint('phq9', __name__, url_prefix='/phq9')

@phq9_bp.route('/answers/<int:user_id>', methods=['GET'])
def get_answers(user_id):
    answers = AnswersPHQ9.query.filter_by(user_id= user_id)
    return jsonify({'answers': [answer.to_dict() for answer in answers]})

@phq9_bp.route('/register', methods=['POST'])
def register_phq9():
    user_id = request.json.get('user_id')
    answer_1 = request.json.get('answer_1')
    answer_2 = request.json.get('answer_2')
    answer_3 = request.json.get('answer_3')
    answer_4 = request.json.get('answer_4')
    answer_5 = request.json.get('answer_5')
    answer_6 = request.json.get('answer_6')
    answer_7 = request.json.get('answer_7')
    answer_8 = request.json.get('answer_8')
    answer_9 = request.json.get('answer_9')
    answers = [answer_1, answer_2, answer_3, answer_4, answer_5, answer_6, answer_7, answer_8, answer_9]
    total_score = sum(answers)
    
    try:
        result = ResultPHQ9(result=total_score, user_id=user_id)
        answers = AnswersPHQ9(answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4, answer_5=answer_5, answer_6=answer_6, answer_7=answer_7, answer_8=answer_8, answer_9=answer_9, user_id=user_id)
        db.session.add_all([answers, result])
        db.session.commit()
        return jsonify({
            "id_user": user_id,
            "answer_1": answers.answer_1,
            "answer_2": answers.answer_2,
            "answer_3": answers.answer_3,
            "answer_4": answers.answer_4,
            "answer_5": answers.answer_5,
            "answer_6": answers.answer_6,
            "answer_7": answers.answer_7,
            "answer_8": answers.answer_8,
            "answer_9": answers.answer_9,
            "result_test": total_score
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error en la sentencia SQL: {str(e)}'}), 500

