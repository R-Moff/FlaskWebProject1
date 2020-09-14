"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, request
from FlaskWebProject1 import app
import pypyodbc
import pymssql
#pypyodbc
connection = pymssql.connect('Driver={SQL Server};Server=LAPTOP-3TH991FS;Database=TutorialDB;uid=LAPTOP-3TH991FS\ryant;')
mycursor = connection.cursor()


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

        #mycursor.execute = ("select * from Customers")  
    )



