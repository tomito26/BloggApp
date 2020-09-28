from flask import render_template,redirect,flash,url_for,abort,request
from ..request import get_quotes
from .forms import  BlogForm, CommentsForm,UpdateProfile
from . import main
from .. import db,photos
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Subscribe
from ..email import mail_message
import markdown2

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

@main.route('/post/<int:post_id>',methods=['GET','POST'])
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

@main.route('/user/<uname>/update/pic',methods =['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path= f'photo/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>') 
def profile(uname):
    
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)
    
    return render_template("profile/profile.html",user=user)
 
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)

@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Blog.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    form = BlogForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.content = form.content.data
        
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('main.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.subtitle = post.subtitle
        form.content.data = post.content
    return render_template('add.html', title='Update Post', form=form)

@main.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Blog.query.get_or_404(post_id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.index'))



#sSubscribe
@main.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    '''
    Function to send email upon subscription
    '''
    if request.method == 'POST':
        email = request.form['email']
        new_email = Subscribe(email=email)
        db.session.add(new_email)
        db.session.commit()
        # mail_message("Welcome to Blogging site","email/welcome_subscriber", new_email.email,new_email=new_email)
        flash('Thank you for your subscribing')
        return redirect(url_for('main.index'))
        