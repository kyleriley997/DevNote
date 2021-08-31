from app.app.models import DevResource
from flask import Flask, render_template, request, redirect
import redis 
# import boto3

app = Flask(__name__) #setting up db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #Name of path to DB, relative path

from models import db DevResource
