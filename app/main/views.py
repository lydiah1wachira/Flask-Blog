from flask import render_template,request
from . import main
from ..requests import get_quote

@main.route('/')
def index():
  '''
  View root function that returns the index page and its data.
  '''
  title = "Blog App"

  return render_template('index.html', title = title)

