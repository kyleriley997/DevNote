from flask import Flask, render_template, request, redirect, url_for
import redis 
# import boto3

app = Flask(__name__) #setting up db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #Name of path to DB, relative path

from models import db, DevResource

db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()

red = redis.Redis(host='redis', port=6379, db=0)

@app.route("/update/<int:topic_id>", methods = ["POST", "GET"])
def update(topic_id):

    if url_for("linux"):
    if url_for("python"):
    if url_for("github"):
    if url_for("aws"):
    if url_for("boto3"):
    updateTopic = 
