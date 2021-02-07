from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class student(db.Model):
    id = db.column(db.Integer, primary_key = True)
    name = db.column (db.string(120), unique= True, nullable=False)
    year = db.column (db.DataTime, unique= True, nullable=False , default= DataTime.now)
    term = db.column(db.Integer,  unique= True, nullable=False)
    pic =  db.column (db.string(20), nullable=False)

class attendence (db.Model):  
     id = db.column(db.Integer, primary_key = True)
     year = db.column (db.DataTime, unique= True, nullable=False , default= DataTime.now)
     term = db.column(db.Integer,  unique= True, nullable=False)
     doc_name = db.column (db.string(120), unique= True, nullable=False)
     data = db.column (db.DataTime, unique= True, nullable=False , default= DataTime.now)
     student_id = db.column(db.Integer, db.foreignKey('stubent.id'))
     doc_id = db.column(db.Integer, db.foreignKey('doctor.id'))
class Doctor(db.Model):
    id = db.column(db.Integer, primary_Key =True)
    Full_name = db.column(db.String(20), unique=True , nullable=False)
    Password = db.column(db.String(40), nullable=False)
   subject_id = db.column(db.Integer,db.Foreignkey('subject_id') ,nullable=False)

class subject(db.Model):
    id = db.column(db.Integer,primary_Key=True )
    name =db.column(db.String(20), unique=True , nullable=False)
    doctor_id = db.column(db.Integer,db.Foreignkey('doctor_id ') ,nullable=False)

class Login (db.Model):
     id = db.column(db.Integer, primary_Key =True)
     student_id = db.column(db.Integer,db.Foreignkey('student_id') ,nullable=False)
     subject_id = db.column(db.Integer,db.Foreignkey('subject_id') ,nullable=False)
     doctor_id = db.column(db.Integer,db.Foreignkey('doctor_id') ,nullable=False)
     apply = db.column(db.String(20), unique=True , nullable=False


