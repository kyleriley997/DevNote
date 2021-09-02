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

red = redis.Redis(host='redis', port=6379, db=0) #redis port

@app.route("/")
def main():
    # records = DevResource.query.all()
    # print(records) #prints entire db records
    return render_template("base.html") #(, records=records)
    
@app.route("/addLinux", methods=["POST"])
def addLinux():
    url_link = request.form("url_link")

    new_record = linuxTable(url_link=url_link)
    db.session.add(new_record)
    db.session.commit()

    red.hset(id, "url_link", url_link)

    #record = linuxTable.query.filter_by(id=id).first() #filters by id #
    #print(record)

    print(red.hgetall(id))

    return render_template('linux.html', saved=1, id=id, url_link=red.hget(id, "url_link"))

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

    return render_template('python.html', saved=1, id=id, url_link=red.hget(id, "url_link"))

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

    return render_template('docker.html', saved=1, id=id, url_link=red.hget(id, "url_link"))

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

    return render_template('aws_page.html', saved=1, id=id, url_link=red.hget(id, "url_link"))


# create different delete routes for each url page. No if and else. 
@app.route('/deleteLinux/<int:topic_id>', methods=['POST']) 
def deleteLinux(topic_id):
    topic = linuxTable.query.filter_by(id=topic_id).first()
    db.session.delete(topic)
    db.session.commit()
    return redirect(url_for('linux.html'))

   
@app.route('/deletePython/<int:topic_id>', methods=['POST']) 
def deletePython(topic_id):
    topic = pythonTable.query.filter_by(id=topic_id).first()
    db.session.delete(topic)
    db.session.commit()
    return redirect(url_for('python.html'))

@app.route('/deleteDocker/<int:topic_id>', methods=['POST']) 
def deleteDocker(topic_id):
    topic = dockerTable.query.filter_by(id=topic_id).first()
    db.session.delete(topic)
    db.session.commit()
    return redirect(url_for('docker.html'))


@app.route('/deleteAWS/<int:topic_id>', methods=['POST']) 
def deleteAWS(topic_id):
    topic = awsTable.query.filter_by(id=topic_id).first()
    db.session.delete(topic)
    db.session.commit()
    return redirect(url_for('aws_page.html'))


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)

