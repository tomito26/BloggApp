from . import db
class Quote:
    '''
    Quotes class to define class object
    '''
    def __init__(self, quote, author, id):
        self.quote = quote
        self.author = author
        self.id = id

class User(db.Model):
    __tablename__ = 'users'
    
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    role_id =db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure=db.Column(db.String(255))
    
    def __repr__(self):
        
        return f'User {self.username}'


class Role(db.Model):
    
    __tablename__='roles'
    
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref='role',lazy='dynamic')
    
    def __repr__(self):
        return f'User {self.name}'