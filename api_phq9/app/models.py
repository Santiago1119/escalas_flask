from app import db

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    answers_phq9 = db.relationship('AnswersPHQ9', backref='user', lazy=True)
    results_phq9 = db.relationship('ResultPHQ9', backref='user', lazy=True)

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