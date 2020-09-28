from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required



class BlogForm(FlaskForm):
    
    title = StringField('Blog title',validators=[Required()])
    content = TextAreaField('Make a blog',validators=[Required()])
    submit = SubmitField('submit blog')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comments',validators=[Required()])
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio=TextAreaField('create your bio.',validators=[Required()])
    submit=SubmitField('submit')
    

    

