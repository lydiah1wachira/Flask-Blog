import unittest
from app.models import Blog

class BLogModelTest(unittest.TestCase):
  '''
  Test case to check behaviour of blog model.
  '''
  def setUp(self):
    '''
    Set up method that will run before every test.
    '''
    
    self.new_blog = Blog(21,'snape requiem', 'I have spied for you and lied for you, put myself in mortal danger for you. Everything was supposed to be to keep Lily Potter’s son safe. Now you tell me you have been raising him like a pig for slaughter —')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_blog))
