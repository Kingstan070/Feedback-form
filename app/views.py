from . import app
from flask import render_template, url_for, request, session, redirect, flash
from .models import create_db, check_emailid

@app.route('/', methods=['GET','POST'])
def index():
    '''
    Login Page for Student

    '''
    
    if request.method == "POST":
        usr_mail = request.form["student-email"]
        session['usr-mail'] = usr_mail
        check = check_emailid(usr_mail)
        if check[0]:
            #checks whether the user have already answered the feedbacks
            session['usr-name'] = check[1] # setting user name to session for further use
            return redirect(url_for('questions'))
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
        return render_template('questions.html', usr=usr_name)
    else:
        return redirect(url_for('index'))
