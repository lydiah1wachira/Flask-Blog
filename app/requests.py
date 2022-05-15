from .models import Quote
import requests

url = "http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
  '''
  Function to consumme http request and return a Quote object
  '''

  response = requests.get(url).json()
  
  random_quote = Quote(response.get("author"), response.get("quote"))

  return random_quote