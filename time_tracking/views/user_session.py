from flask import request, render_template, redirect, url_for

from flask import current_app as app
from ..models import User
from ..utills import encode
from ..factory import Connection_Factory, DAO_Factory


@app.route('/login/')
def login():
    with app.app_context():
        try:
            cnx1 = Connection_Factory.get_cnx(app.config['dbms'], app.config['db'])
            dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
            users = dao_user.select_all(cnx1)
        except Exception as err:
            return str(err.args)
        return '\n\n'.join([str(user) for user in users])
        #return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html')