import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the quotes class.
  '''

  def setUp(self):
    '''
    Set up method that will run before every test.
    '''
    
    self.new_quote = Quote('snape', 'I have spied for you and lied for you, put myself in mortal danger for you. Everything was supposed to be to keep Lily Potter’s son safe. Now you tell me you have been raising him like a pig for slaughter —')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_quote))

if __name__ == '__main__':
  unittest.main()