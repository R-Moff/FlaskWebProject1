"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, request
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/football', methods=['post', 'get'])
def football():
    """Renders the football page."""
    link=request.form.get('search')
    return render_template(
        'football.html',
        title='Football',
        year=datetime.now().year,
        message='Football news.',
        
        link=request.form.get('search'),
        link2='https://www.bbc.co.uk/sport/football/teams/',
        link3=link2 + link
    )



