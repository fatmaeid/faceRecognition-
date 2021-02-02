@app.route('/')
def GetInformation():
   return render_template('GetInformation.html')

@app.route('/login')
def login():
   return render_template(login.html)

@app.route('/getreport')
def getreport():
   return render_template(getreport.html)


@app.route('/UpLoadImage')
def UpLoadImage():
   return render_template(UpLoadImage.html)    

@app.route('/reg')
def reg():
   return render_template(reg.html)

@app.route('/take_attendance')
def take_attendance():
   return render_template(take_attendance.html)