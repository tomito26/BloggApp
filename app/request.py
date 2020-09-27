import requests
from .models import Quote



# Getting the Quote base url
base_url = None


def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_API_URL']

def get_quotes():
    '''
    Function that gest the json response to our url
    '''
    get_quote_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    print(get_quote_response)
    
    return get_quote_response