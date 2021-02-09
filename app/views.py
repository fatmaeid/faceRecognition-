from flask import render_template , request
from app import app

@app.route('/', methods=['GET','POST'])
def login():
   if request.method == 'POST':
      pass
   else:
      return render_template('login.html')

@app.route('/getInformation', methods=['GET','POST'])

def getInformation():
   if request.method == 'POST':
      pass
   else:
      return render_template('GetInformation.html')   

@app.route('/getreport' ,methods=['GET','POST'])
def getreport():
   if request.method == 'POST':
      pass
   else:
      return render_template('getreport.html')


@app.route('/upLoadImage' ,methods=['GET','POST'])
def upLoadImage():
   if request.method == 'POST':
      pass
   else:
      return render_template('UploadImage.html')    

@app.route('/reg' ,methods=['GET','POST'])
def reg():
   if request.method == 'POST':
      pass 
   else:
      return render_template('reg.html')

@app.route('/take_attendance' ,methods=['GET','POST'])
def take_attendance():
   if request.method == 'POST':
      pass
   else:
      return render_template('take_attendance.html')