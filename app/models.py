from . import db 

class Quote:
  '''
  Blueprint class to display random quotes from the API
  '''
  
  def __init__(self, author, quote):
    self.author = author
    self.quote = quote

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255))

  def __repr__(self):
    return f'User {self.username}'

