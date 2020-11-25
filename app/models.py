from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """Model for user accounts."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String,
                         nullable=False,
                         unique=True)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    active = db.Column(db.Boolean,
                       default = True)
    registered_on = db.Column(db.DateTime, 
                              default = datetime.utcnow() )
    links = db.relationship('Urls', 
                            backref='author')

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User {}>'.format(self.username)



class Urls(db.Model):
    """ model for real urls """
    __tablename__ = 'urls'
    id = db.Column(db.Integer, 
                    primary_key = True)
    name = db.Column(db.String(30), 
                     nullable = False)
    url_address = db.Column(db.String(250),
                            nullable = False)
    visits = db.Column(db.Integer, 
                       default = 0)
    short_url = db.relationship('ShortUrl', 
                                backref = "url", 
                                uselist = False)
    author_id = db.Column(db.Integer, 
                          db.ForeignKey('users.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self.short_url)
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Url {}>'.format(self.name)



class ShortUrl(db.Model):
    """ Model for short url """
    __tablename__ = 'shorts'
    id = db.Column(db.Integer, 
                   primary_key= True)
    value = db.Column(db.String(10), 
                      nullable = False)
    created_on = db.Column(db.DateTime, 
                           default = datetime.utcnow())
    last_visited = db.Column(db.DateTime)
    url_id = db.Column(db.Integer, 
                       db.ForeignKey('urls.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Short {}>'.format(self.url.name)
