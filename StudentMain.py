from serviceImpl.StudServiceImplInfo import StudentImpl
from model.StudentInfo import myapp,Student,mydb
from flask import request,render_template, redirect

simpl = StudentImpl()

dummy = Student(id=0, fname='',lname='',age=0,email='',address='')

@myapp.route('/index/',methods=['GET'])
def appStandingPage():
    return render_template('Students.html',student = dummy,students=simpl.getAllStudents())

@myapp.route('/student/',methods=['POST', 'GET'])
def addOrUpdateStudent():
    print('request : ', request.method)
    print(request.form['id'], request.form['fname'], request.form['lname'], request.form['age'], request.form['email'], request.form['address'])
    print(request.method)

    emsg = "";

    if request.method=="POST":
        sid = int(request.form['id'])
        print('sid : ', sid)

        if sid == 0:
            print("inside add method")
            st = Student(fname=request.form['fname'], lname=request.form['lname'], age=request.form['age'],
                         email=request.form['email'], address=request.form['address'])
            simpl.addStudent(st)
            emsg = 'Student Added Successfully...!'

        else:
            st = Student(fname=request.form['fname'], lname=request.form['lname'], age=request.form['age'],
                         email=request.form['email'], address=request.form['address'], id=sid)
            simpl.updateStudent(st)
            emsg = "Student updated successfully..!"

    return redirect("/index")


@myapp.route('/edit/<id>',methods=['GET'])
def edit(id):
    stud = simpl.getStudent(id)
    return render_template('Students.html', student=stud, students=simpl.getAllStudents())

@myapp.route('/delete/<id>', methods=['GET'])
def deleteStudent(id):
    simpl.deleteStudent(id)
    return render_template('Students.html',student = dummy, students=simpl.getAllStudents(), msg='Student Deleted Successfully...!')

if __name__ == '__main__':

    mydb.create_all()
    myapp.run(debug=True)