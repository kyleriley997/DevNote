from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Linux(db.Model):
    id = db.Column(db.String, primary_key=True)
    url_link = db.Column(db.String) #should this be a list?

    def __init__(self, id, url_link):
        self.id=id
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.id}-{self.url_link}'

class Python(db.Model):
    id = db.Column(db.String, primary_key=True)
    url_link = db.Column(db.String) #should this be a list?

    def __init__(self, id, url_link):
        self.id=id
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.id}-{self.url_link}'

class Docker(db.Model):
    id = db.Column(db.String, primary_key=True)
    url_link = db.Column(db.String) #should this be a list?

    def __init__(self, id, url_link):
        self.id=id
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.id}-{self.url_link}'

class AWS(db.Model):
    id = db.Column(db.String, primary_key=True)
    url_link = db.Column(db.String) #should this be a list?

    def __init__(self, id, url_link):
        self.id=id
        self.url_link=url_link

    def __repr__(self): #prints out representation of object, 
        return f'<topic-description-url_link : {self.id}-{self.url_link}'


