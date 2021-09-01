from flask import Flask, render_template, request, redirect
import redis 
# import boto3

app = Flask(__name__) #setting up db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #Name of path to DB, relative path

from models import db, DevResource

red = redis.Redis(host='redis', port=6379, db=0) #not sure about port and db = 0

app.route("/")
def main():
    # records = DevResource.query.all()
    # print(records) #prints entire db records
    return render_template("base.html") #(, records=records)
    
app.route("/add", methods=["POST"])
def add():
    topic = request.form("topic")
    description = request.form("description")
    url_link = request.form("url_link")

    new_record= DevResource(topic=topic, description=description, url_link=url_link)
    db.session.add(new_record)
    db.session.commit()

    red.hset(topic, "description", description)
    red.hset(topic, "url_link", url_link)

    record = DevResource.query.filter_by(topic=topic).first() #filters by topic
    print(record)

    print(red.hgetall(topic))

    return render_template('index.html', saved=1, topic=topic, description=red.hget(topic, "description"), url_link=red.hget(topic, "url_link"))