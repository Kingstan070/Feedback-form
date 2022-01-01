from .import app
from flask import render_template, url_for, request, session, redirect
import copy, random



@app.route('/', methods=['GET','POST'])
def index():
    '''Login Page for Student'''
    if request.method == "POST":
        usr_mail = request.form["student-email"]
        session['usr-mail'] = usr_mail
        return redirect(url_for('questions'))
    else:
        return render_template('index.html')

@app.route('/login')
def teacher_login():
    '''Login Page for Teachers'''
    return render_template('login.html')

@app.route('/questions')
def questions():
    '''Page with the question for the students to answer'''
    if session["usr-mail"]:
        usr_mail = session["usr-mail"]
        return render_template('questions.html', usr=usr_mail)
    else:
        return redirect(url_for('index'))
