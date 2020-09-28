from flask import render_template,redirect,flash,url_for
from ..request import get_quotes
from .forms import  BlogForm, CommentsForm
from . import main
from .. import db,photos
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
@main.route('/')
def index():
    '''
    Functin that returns index page and its data
    '''
    title = 'BlogApp-Welcome to blogapp your trusted site for creativity'
    
    quote_item = get_quotes()
    blog_item = Blog.get_all_blogs()
    print(quote_item)
    return render_template('index.html',title = title , quote_item=quote_item,blog_item=blog_item) 

@main.route('/post/<int:post_id>',metods=['GET','POST'])
def post(post_id):
    '''
    Function that retuns the blog page and its data
    '''
    post = Blog.query.filter_by(id=post_id).one()
    post_comments = Comment.get_comments(post_id)
    
    return render_template('post.html',post=post,post_comments=post_comments)

@main.route('/createblog',methods=['GET','POST'])
@login_required
def createblog():
    '''
    View root page that returns the createblog post page and its data
    '''
    form = BlogForm()
    if form.validate_on_submit():
        title=form.title.data
        content=form.content.data
        
        new_post = Blog(title=title,content=content, user=current_user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('addblog.html',form=form)

@main.route('/post/comments/newblog/<int:id>')
@login_required
def new_comment(id):
    form = CommentsForm()
    
    if form.validate_on_submit():
        new_comment = Comment(blog_id=id,comment=form.comment.data)
        new_comment.save_comments()
        return redirect(url_for('main.post',post_id=id))
    return render_template('new_comment.html',comment_form=form)

@main.route('/user/uname>/update/pic',methods =['Post'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if'photo' in request.files
    
 