from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from flask_login import current_user

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    '''
    Form class for the comments on blogs.
    '''
    
    comment = TextAreaField('Add a comment', validators = [DataRequired()])

    submit = SubmitField('submit')

class AddBlog(FlaskForm):
    title = StringField('Title', validators =[DataRequired()])
    content = TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField('Post Blog')