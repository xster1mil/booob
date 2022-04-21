from flask import Blueprint, redirect, render_template, request, send_from_directory,flash
from App.models import Job, db, User
import json
from form import LogIn
from flask_login import LoginManager, current_user, login_user, login_required
from flask import Flask, request, render_template, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from App.controllers import login_user

login_views = Blueprint('login_views', __name__, template_folder='../templates')

@login_views.route('/login')
def index():
  form = LogIn()
  return render_template('login.html', form =form)

def getusername(username):
  return Job.query.filter(User.username.like('%'+username+'%'))

@login_views.route('/login', methods=['POST'])
def loginAction():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']): # check credentials
        flash('Logged in successfully.') # send message to next page
        #login_user(user) # login the user
        return render_template('jobs.html', jobs = Job.query.all()) # redirect to main page if login successful
  flash('Invalid credentials')
  return render_template('login.html', form = form)
  
