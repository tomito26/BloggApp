import unittest
from app.models import quotes
Quote = quotes.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote=Quote('Never give up')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))
        

