from flask import request, render_template, redirect, url_for

from flask import current_app as app
from ..models import User
from ..utills import encode
from ..factory import DB_Factory, Connection_Factory, DAO_Factory


@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')