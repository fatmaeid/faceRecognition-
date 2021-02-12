from datetime import datetime
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(120))
    year = db.Column (db.Integer)
    term = db.Column(db.Integer)
    face_encoding =  db.Column(db.String(2000))

class SubjectRegistraton(db.Model):  
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column (db.Integer)
    term = db.Column(db.Integer)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))
    
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    full_name = db.Column(db.String(200))
    password = db.Column(db.String(40))

class Subject(db.Model):
    id = db.Column(db.Integer,primary_key=True )
    name =db.Column(db.String(200))
    doctor_id = db.Column(db.Integer,db.ForeignKey('doctor.id'))

class Attend(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    lecture_number = db.Column(db.Integer)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))
    subject_id = db.Column(db.Integer,db.ForeignKey('subject.id'))
    date = db.Column (db.DateTime, default= datetime.now()) 
