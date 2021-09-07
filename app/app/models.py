from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class linuxTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_link = db.Column(db.String)

    def __init__(self, url_link):
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.id}-{self.url_link}'

class pythonTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_link = db.Column(db.String)

    def __init__(self, url_link):
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.id}-{self.url_link}'

class dockerTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_link = db.Column(db.String)

    def __init__(self, url_link):
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.id}-{self.url_link}'

class awsTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_link = db.Column(db.String)

    def __init__(self, url_link):
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.id}-{self.url_link}'


