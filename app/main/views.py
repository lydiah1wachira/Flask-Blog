from flask import render_template,request
from . import main
from ..requests import get_quote
from flask_login import login_required

@main.route('/')
def index():
  '''
  View root function that returns the index page and its data.
  '''
  title = "Blog App"

  return render_template('index.html', title = title)

@main.route('/blogs')
@login_required
def new_blog():
  quote = get_quote()
  title = 'Blogs'

  return render_template('blogs.html', title= title, quote = quote )
