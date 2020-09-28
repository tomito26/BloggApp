from flask import render_template
from ..request import get_quotes
from . import main
from flask_login import login_required

@main.route('/')
def index():
    '''
    Functin that returns index page and its data
    '''
    title = 'BlogApp-Welcome to blogapp your trusted site for creativity'
    quote_item = get_quotes()
    print(quote_item)
    return render_template('index.html',title = title , quote_item=quote_item) 