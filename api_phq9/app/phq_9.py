from flask import Blueprint, jsonify, request
from app import app, db
from .models import AnswersPHQ9, ResultPHQ9
import re

phq9_bp = Blueprint('phq9', __name__, url_prefix='/phq9')

@phq9_bp.route('/answers/<int:user_id>', methods=['GET'])
def get_answers(user_id:int)->jsonify:
    """Consulta las respuestas que ingresó el usuario en el formulario PHQ-9

    Args:
        user_id (int): id del usuario

    Returns:
        jsonify: archivo json con el valor de cada respuésta del usuario
    """
    def question_value(answers:object)->str:
        answers_dict = [answer.to_dict() for answer in answers]
        user_response = {}
        
        for answer_dict in answers_dict:
            for value in answer_dict:
                if re.match(r"^answer_\d+$", value) and answer_dict[value] == 0:
                    user_response[value] = 'Ningún día'
                elif re.match(r"^answer_\d+$", value) and answer_dict[value] == 1:
                    user_response[value] = 'Varios días'
                elif re.match(r"^answer_\d+$", value) and answer_dict[value] == 2:
                    user_response[value] = 'Más de la mitad de los días'
                elif re.match(r"^answer_\d+$", value) and answer_dict[value] == 3:
                    user_response[value] = 'Casi todos los días'

            
        return user_response
    
    
    answers = AnswersPHQ9.query.filter_by(user_id= user_id)
    
    user_responses = question_value(answers)
    return jsonify({'answers': user_responses,
                    'db_values': [answer.to_dict() for answer in answers]})



@phq9_bp.route('/register', methods=['POST'])
def register_phq9()->jsonify:
    """registra en la base de datos los valores de cada pregunta y calcula el total que sacó en la prueba

    Returns:
        jsonify: archivo json con el id de usuario, las respuestas del formulario, y el resultado de la escala
    """
    
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

