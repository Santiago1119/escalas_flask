from app import db

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    results_phq9 = db.relationship('ResultPHQ9', backref='user', lazy=True)
    answers_phq9 = db.relationship('AnswersPHQ9', backref='user', lazy=True)
    results_motivation_treatment = db.relationship('ResultMotivationTreatment', backref='user', lazy=True)
    answers_motivation_treatment = db.relationship('AnswersMotivationTreatment', backref='user', lazy=True)
    
    def to_dict(self):
        return {
            'id_user': self.id_user,
            'name': self.name,
            'email': self.email
        }
        
class ResultPHQ9(db.Model):
    id_result = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    
    def to_dict(self):
        return {
            'id_result': self.id_result,
            'result': self.result,
            'user_id': self.user_id
        }

class AnswersPHQ9(db.Model):
    id_answers = db.Column(db.Integer, primary_key=True)
    answer_1 = db.Column(db.Integer, nullable=False)
    answer_2 = db.Column(db.Integer, nullable=False)
    answer_3 = db.Column(db.Integer, nullable=False)
    answer_4 = db.Column(db.Integer, nullable=False)
    answer_5 = db.Column(db.Integer, nullable=False)
    answer_6 = db.Column(db.Integer, nullable=False)
    answer_7 = db.Column(db.Integer, nullable=False)
    answer_8 = db.Column(db.Integer, nullable=False)
    answer_9 = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)

    def to_dict(self):
        return {
            'id_answers': self.id_answers,
            'answer_1': self.answer_1,
            'answer_2': self.answer_2,
            'answer_3': self.answer_3,
            'answer_4': self.answer_4,
            'answer_5': self.answer_5,
            'answer_6': self.answer_6,
            'answer_7': self.answer_7,
            'answer_8': self.answer_8,
            'answer_9': self.answer_9,
            'user_id': self.user_id
        }

class ResultMotivationTreatment(db.Model):
    id_result = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    
    def to_dict(self):
        return {
            'id_result': self.id_result,
            'result': self.result,
            'user_id': self.user_id
        }

class AnswersMotivationTreatment(db.Model):
    id_result = db.Column(db.Integer, primary_key=True)
    answer_1 = db.Column(db.Integer, nullable=False)
    answer_2 = db.Column(db.Integer, nullable=False)
    answer_3 = db.Column(db.Integer, nullable=False)
    answer_4 = db.Column(db.Integer, nullable=False)
    answer_5 = db.Column(db.Integer, nullable=False)
    answer_6 = db.Column(db.Integer, nullable=False)
    answer_7 = db.Column(db.Integer, nullable=False)
    answer_8 = db.Column(db.Integer, nullable=False)
    answer_9 = db.Column(db.Integer, nullable=False)
    answer_10 = db.Column(db.Integer, nullable=False)
    answer_11 = db.Column(db.Integer, nullable=False)
    answer_12 = db.Column(db.Integer, nullable=False)
    answer_13 = db.Column(db.Integer, nullable=False)
    answer_14 = db.Column(db.Integer, nullable=False)
    answer_15 = db.Column(db.Integer, nullable=False)
    answer_16 = db.Column(db.Integer, nullable=False)
    answer_17 = db.Column(db.Integer, nullable=False)
    answer_18 = db.Column(db.Integer, nullable=False)
    answer_19 = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False)
    
    def to_dict(self):
        return {
            'id_answers': self.id_answers,
            'answer_1': self.answer_1,
            'answer_2': self.answer_2,
            'answer_3': self.answer_3,
            'answer_4': self.answer_4,
            'answer_5': self.answer_5,
            'answer_6': self.answer_6,
            'answer_7': self.answer_7,
            'answer_8': self.answer_8,
            'answer_9': self.answer_9,
            'answer_10': self.answer_10,
            'answer_11': self.answer_11,
            'answer_12': self.answer_12,
            'answer_13': self.answer_13,
            'answer_14': self.answer_14,
            'answer_15': self.answer_15,
            'answer_16': self.answer_16,
            'answer_17': self.answer_17,
            'answer_18': self.answer_18,
            'answer_19': self.answer_19,
            'user_id': self.user_id
        }