from flask import Blueprint, redirect, render_template, request, send_from_directory,flash
from App.models import Job, db, User
import json
from form import SignUp
from flask_login import LoginManager, current_user, login_user, login_required
from flask import Flask, request, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from App.controllers import create_user

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')

@signup_views.route('/signup')
def index():
  form = SignUp()
  return render_template('signup.html', form =form)

@signup_views.route('/signup', methods=['POST'])
def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    create_user( data['username'],data['password'])
    flash('Account Created!')# send message
    return render_template('login.html', form =form)# redirect to login page
  flash('Error invalid input!')
  return render_template('signup.html', form =form)