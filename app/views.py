from . import app
from flask import render_template, url_for, request, session, redirect, flash
from .models import create_db, check_emailid, get_student_values
from .utils import get_question

@app.route('/', methods=['GET','POST'])
def index():
    '''
    Login Page for Student

    '''
    
    if request.method == "POST":
        usr_mail = request.form["student-email"]
        session['usr-mail'] = usr_mail
        if check_emailid(usr_mail):
            #checks whether the user have already answered the feedbacks
            session['usr-name'] = get_student_values(usr_mail)[1] # setting user name to session for further use
            if get_student_values(usr_mail)[3] == 0:
                #If the student have not submited any feedBack
                return redirect(url_for('questions'))
            else:
                return render_template('exitpage.html', usr=session['usr-name'])
        else:
            #Flashing message
            flash('Email ID not found !','error')
            return render_template('index.html')
    else:
        return render_template('index.html')

@app.route('/login')
def teacher_login():
    '''
    Login Page for Teachers
    
    '''
    return render_template('login.html')

@app.route('/questions')
def questions():
    '''
    Page with the question for the students to answer
    
    '''
    if session["usr-name"]:
        usr_name = session["usr-name"]
        return render_template('questions.html', usr=usr_name, questions=get_question() )
    else:
        return redirect(url_for('index'))

@app.route('/question/submin', methods=['POST'])
def question_submit():
    if request.method == "POST":
        return render_template('exitpage.html', usr=session['usr-name'])