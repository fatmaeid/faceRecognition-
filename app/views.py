from flask import render_template ,request, redirect, flash, session
from app import app, db
from app import models
from app import face_recognition


@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['full_name']
        password = request.form['password']
        
        doctor = models.Doctor.query.filter(models.Doctor.full_name == name).first()
        if doctor == None or password != doctor.password:
            flash("Wrong name or password")
            return redirect("/")
        
        session["user"] = name
        return redirect("/getInformation")
        
    else:
        return render_template('login.html')

@app.route('/getInformation', methods=['GET','POST'])
def getInformation():
    if "user" not in session:
        return redirect("/")
        
    students = models.Student.query.all()
    return render_template('GetInformation.html', students=students) 
    
      

@app.route('/getreport' ,methods=['GET','POST'])
def getreport():
    if request.method == 'POST':
        pass
    else:
        return render_template('getreport.html')


@app.route('/upLoadImage', methods=['GET','POST'])
def upLoadImage():
    if request.method == 'POST':
        subject_id = request.form['subject']
        lecNum = request.form['lecNum']
        
        file = request.files['file']
        image = face_recognition.file2RGB(file)
        student = face_recognition.getStudentFromImage(image)
        if student == None:
            return redirect("/upLoadImage")
        
        attendance = models.Attend(lecture_number=lecNum, student_id=student.id, subject_id=subject_id)
        db.session.add(attendance)
        db.session.commit()
        
        print(student.name, " has attended")
        return redirect("/")
        
    else:
        subjects = models.Subject.query.all()
        return render_template('UploadImage.html', subjects=subjects)    

@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        
        full_name = first_name + " " + last_name
        doctor = models.Doctor(full_name=full_name, password=password)
        db.session.add(doctor)
        db.session.commit()
        
        return redirect("/")
        
    else:
        return render_template('reg.html')

@app.route('/subjectRegisteration', methods=['GET','POST'])
def subjectRegisteration():
    if request.method == 'POST':
        pass
    else:
        return render_template('subjectRegisteration.html')

@app.route('/studentRegisteration', methods=['GET', 'POST'])
def studentRegistration():
    if request.method == 'POST':
        name = request.form['name']
        year = request.form['year']
        term = request.form['term']
        file = request.files['file']
        
        image = face_recognition.file2RGB(file)
        face_encoding = face_recognition.getEncoding(image)
        face_encoding = str(face_encoding.tolist())
        
        student = models.Student(name=name, year=year, term=term, face_encoding=face_encoding)
        db.session.add(student)
        db.session.commit()
        
        return redirect("/getInformation")
    else:
        return render_template('studentRegistration.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')
