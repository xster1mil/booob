from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.models import Job, db
import json

api_views = Blueprint('api_views', __name__, template_folder='../templates')

def searchJob(search):
  return Job.query.filter(Job.Name.like('%'+search+'%'))

@api_views.route('/')
def search():
  search = request.args.get('search')
  job=None
  if search:
    job=searchJob(search)
    return render_template('index.html', job=job)
  return render_template('index.html')
  
  
  


