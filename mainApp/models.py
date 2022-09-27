from mainApp import db
from datetime import date,datetime,timedelta

class QuestionTypeOne(db.Model):
    __tablename__ = "questiontypeone"
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer_option_1 = db.Column(db.Text, nullable=False)
    answer_option_2 = db.Column(db.Text, nullable=False)
    answer_option_3 = db.Column(db.Text, nullable=False)
    correct_answer = db.Column(db.String, nullable=False)
    marks_available = db.Column(db.Integer, nullable=False)
    correct_answer_feedback = db.Column(db.Text, nullable=False)
    incorrect_answer_feedback = db.Column(db.Text, nullable=False)
    feedforward_comments = db.Column(db.Text, nullable=False)
    question_tag_1 = db.Column(db.Text, nullable=False)
    question_tag_2 = db.Column(db.Text, nullable=False)
    question_tag_3 = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.question}"


class QuestionType2(db.Model):
    __tablename__ = "questiontype2"
    id = db.Column(db.Integer, primary_key=True)
    questionType = db.Column(db.Integer, nullable= False)
    name = db.Column(db.Text, nullable=False)
    shortDescription = db.Column(db.Text, nullable=False)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    correctFeedback = db.Column(db.Text, nullable=False)
    incorrectFeedback = db.Column(db.Text, nullable=False)
    marksAwarded = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"{self.question}"



# Assessment

class Asessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assessment_title = db.Column(db.Integer,nullable=False)
    assessment_difficulty = db.Column(db.Integer,nullable=False) 
    assessment_type = db.Column(db.Integer,nullable=False)
    date_created_on = db.Column(db.DateTime,default=datetime.now)
    questions = db.relationship('questions',backref='asessment')


class questions(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    question = db.Column(db.Text,nullable=False)
    option_one = db.Column(db.Text,nullable=True)
    option_two = db.Column(db.Text,nullable=True)
    option_three = db.Column(db.Text,nullable=True)
    assessment_id = db.Column(db.Integer,db.ForeignKey('asessment.id'))




    def __repr__(self):
        return self.question
