from flask import Flask, render_template, request, redirect, url_for
import redis 
# import boto3

app = Flask(__name__) #setting up db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' #Name of path to DB, relative path

from models import db, linuxTable, pythonTable, dockerTable, awsTable

db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()

red = redis.Redis(host='redis', port=6379, db=0) #not sure about port and db = 0

@app.route("/")
def main():
    # records = DevResource.query.all()
    # print(records) #prints entire db records
    return render_template("base.html") #(, records=records)
    
@app.route("/addLinux", methods=["POST"])
def addLinux():
    url_link = request.form.get("url_link")

    new_record = linuxTable(url_link=url_link)
    db.session.add(new_record)
    db.session.commit()

    red.hset(id, "url_link", url_link)

    #record = linuxTable.query.filter_by(id=id).first() #filters by id #
    #print(record)

    print(red.hgetall(id))

    return render_template('base.html', saved=1, id=id, url_link=red.hget(id, "url_link"))

@app.route("/addPython", methods=["POST"])
def addPython():
    url_link = request.form.get("url_link")

    new_record = pythonTable(url_link=url_link)
    db.session.add(new_record)
    db.session.commit()

    red.hset(id, "url_link", url_link)

    #record = linuxTable.query.filter_by(id=id).first() #filters by id #
    #print(record)

    print(red.hgetall(id))

    return render_template('base.html', saved=1, id=id, url_link=red.hget(id, "url_link"))

@app.route("/addDocker", methods=["POST"])
def addDocker():
    url_link = request.form.get("url_link")

    new_record = dockerTable(url_link=url_link)
    db.session.add(new_record)
    db.session.commit()

    red.hset(id, "url_link", url_link)

    #record = linuxTable.query.filter_by(id=id).first() #filters by id #
    #print(record)

    print(red.hgetall(id))

    return render_template('base.html', saved=1, id=id, url_link=red.hget(id, "url_link"))

@app.route("/addAWS", methods=["POST"])
def addAWS():
    url_link = request.form.get("url_link")

    new_record = awsTable(url_link=url_link)
    db.session.add(new_record)
    db.session.commit()

    red.hset(id, "url_link", url_link)

    #record = linuxTable.query.filter_by(id=id).first() #filters by id #
    #print(record)

    print(red.hgetall(id))

    return render_template('base.html', saved=1, id=id, url_link=red.hget(id, "url_link"))

