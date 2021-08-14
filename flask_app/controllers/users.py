from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/register' , methods = ['POST'])
def register_user():


    data = {
        'first_name': request.form['first_name'],
        'last_name':request.form['last_name'],
        'email_address':request.form['email_address'],
        'password':request.form['password'],
        'confirm_password':request.form['password']
    }

    valid = User.validate_registration(data)

    if valid:
        User.create_user(data)
        flash('account created congratulations, please log in !')

    return redirect('/')

@app.route('/users/login',methods = ['POST'])
def login_user():

    data = {
        'email_address':request.form['email_address']
    }

    user = User.user_email(data)

    if user == None:
        flash('Email is invalid')
        return redirect('/')

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Password is incorrect!')
        return redirect ('/')

    session['user_id'] = user.id
    session['email'] = user.email

    return redirect('/recipes')
        

# @app.route('/users/success')
# def congrats():

#     if 'user_id' not in session:
#         return redirect('/')

#     return render_template('congrats.html')


@app.route('/users/logout')
def logout():

    session.clear()

    return redirect('/')
