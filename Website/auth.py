from flask import Blueprint, render_template,request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from Website import db
from flask_login import login_user, login_required,logout_user,current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data=request.form
    print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        #filter on the basis of email
        user = User.query.filter_by(email=email).first()
        if user :
            if check_password_hash(user.password,password):
                flash('logged in successfully!', category='success')
                #Make sure that user is remebered
                login_user(user, remember=True)
                return redirect((url_for('views.home')))
            else:
                flash('Incorrect Password, Try Again!', category='error')

        else:
            flash('Email does not exist', category = 'error')





    return render_template("login.html", boolean = "True")

@auth.route('/logout')
def logout():
    return "<p>Logout Sucessful </p>"

@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists!', category='error')

        elif len(email) < 4:
            flash('Email must be greater than 4 characters!', category='error')

        elif len(firstName) < 2:
            flash('First Name must be greater than 2 characters!', category='error')


        elif password1 != password2:
            flash('Passwords Provided Must Match!', category='error')


        elif len(password1) < 7:
            flash('Password must be greater than 6 characters!', category='error')


        else:
            new_user = User(email=email,first_name=firstName,password=generate_password_hash(password1, method = 'sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account Created', category='success')
            #redirects user to the home page
            return redirect(url_for('views.home'))



    return render_template("signup.html")
