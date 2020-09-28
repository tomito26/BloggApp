from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin,current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


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
    email = db.Column(db.String(255),unique=True, index = True)
    password_hash=db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path= db.Column(db.String)
    blog = db.relationship('Blog',backref='user',lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
    def __repr__(self):

        return f'User {self.username}'


class Role(db.Model):

    __tablename__='roles'

    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref='role',lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'

class Blog(db.Model):
    __tablename__ = 'blog'

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    content=db.Column(db.String)
    date=db.Column(db.DateTime, default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    comments=db.relationship('Comment',backref = 'blog',lazy='dynamic')

    def save_blog(self):
        '''
        Function that saves the blogs
        '''
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        '''
        Function that deletes the blogs
        '''
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all_blogs(cls):
        '''
        Functions that queries the database
        '''
        return Blog.query.all()

class Comment(db.Model):
    
    __tablename__ =  'comments'
    
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String)
    blog_id=db.Column(db.Integer,db.ForeignKey('blog.id'))
    posted_date=db.Column(db.DateTime,default=datetime.utcnow)

    
    def save_comments(self):
        db.session.add(self)
        db.session.commit()
        
    
    @classmethod
    def get_comments(cls,id):
        comments=Comment.query.filter_by(blog_id=id).all()
        return comments

    @classmethod
    def clear_commwnts(cls):
        Comment.all_comments.clear
        

class Subscribe(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50))