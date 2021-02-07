
from datetime import datetime
from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(120), unique= True, nullable=False)
    year = db.Column (db.DataTime, unique= True, nullable=False , default= datetime.now())
    term = db.Column(db.Integer,  unique= True, nullable=False)
    pic =  db.Column (db.String(20), nullable=False)

class Attendence (db.Model):  
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column (db.DataTime, unique= True, nullable=False , default= datetime.now())
    term = db.Column(db.Integer,  unique= True, nullable=False)
    doc_name = db.Column (db.String(120), unique= True, nullable=False)
    data = db.Column (db.DataTime, unique= True, nullable=False , default= datetime.now())
    student_id = db.Column(db.Integer, db.ForeignKey('stubent.id'))
    doc_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_Key =True)
    Full_name = db.Column(db.String(20), unique=True , nullable=False)
    Password = db.Column(db.String(40), nullable=False)
    subject_id = db.Column(db.Integer,db.Foreignkey('subject_id') ,nullable=False)

class Subject(db.Model):
    id = db.Column(db.Integer,primary_Key=True )
    name =db.Column(db.String(20), unique=True , nullable=False)
    doctor_id = db.Column(db.Integer,db.Foreignkey('doctor_id ') ,nullable=False)

class Login (db.Model):
    id = db.Column(db.Integer, primary_Key =True)
    student_id = db.Column(db.Integer,db.Foreignkey('student_id') ,nullable=False)
    subject_id = db.Column(db.Integer,db.Foreignkey('subject_id') ,nullable=False)
    doctor_id = db.Column(db.Integer,db.Foreignkey('doctor_id') ,nullable=False)
    apply = db.Column(db.String(20), unique=True , nullable=False)


