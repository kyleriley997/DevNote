from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class DevResource(db.Model):
    topic = db.Column(db.String, primary_key=True)
    description = db.Column(db.String)
    url_link = db.Column(db.String)

    def __init__(self, topic, description, url_link):
        self.topic=topic
        self.description=description
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.topic}-{self.description}-{self.url_link}'