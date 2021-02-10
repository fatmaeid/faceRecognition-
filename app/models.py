from datetime import datetime
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(120),  nullable=False)
    year = db.Column (db.DateTime,  nullable=False , default= datetime.now())
    term = db.Column(db.Integer,   nullable=False)
    pic =  db.Column (db.String(20), nullable=False)

class Attendence (db.Model):  
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column (db.DateTime, nullable=False , default= datetime.now())
    term = db.Column(db.Integer,   nullable=False)
    doc_name = db.Column (db.String(120),  nullable=False)
    data = db.Column (db.DateTime,  nullable=False , default= datetime.now())
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    Full_name = db.Column(db.String(20), nullable=False)
    Password = db.Column(db.String(40), nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey('subject.id') ,nullable=False)

class Subject(db.Model):
    id = db.Column(db.Integer,primary_key=True )
    name =db.Column(db.String(20), nullable=False)
    doctor_id = db.Column(db.Integer,db.ForeignKey('doctor.id') ,nullable=False)

class Login (db.Model):
    id = db.Column(db.Integer, primary_key =True)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id') ,nullable=False)
    subject_id = db.Column(db.Integer,db.ForeignKey('subject.id') ,nullable=False)
    doctor_id = db.Column(db.Integer,db.ForeignKey('doctor.id') ,nullable=False)
    apply = db.Column(db.String(20),  nullable=False)


