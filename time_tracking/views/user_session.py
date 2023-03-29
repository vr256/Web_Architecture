import logging
import os

from flask import request, render_template, redirect, url_for, session

from flask import current_app as app
from ..models import User
from ..utills import encrypt
from ..factory import Connection_Factory, DAO_Factory
from ..properties import ERRORS

logging.basicConfig(level=logging.DEBUG, filename="../logfile.txt", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")

app.config['SECRET_KEY'] = os.urandom(20).hex()

@app.route('/login/', methods=['GET', 'POST'])
def login():
    with app.app_context():
        try:
            if request.method == 'POST':
                credentials = request.form['creds']
                if credentials == '':
                    return render_template('login.html', error='Empty login field')
                
                cnx = Connection_Factory.get_cnx(app.config['dbms'], app.config['db'])
                dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
                user_by_login = dao_user.find_by_login(cnx, credentials)
                user_by_email = dao_user.find_by_email(cnx, credentials)

                if not user_by_login and not user_by_email:
                    return redirect(url_for('auth_error', code='AUTH_CRED'))

                user = list(filter(lambda x: x, [user_by_login, user_by_email]))[0]
                password = request.form['password']

                if encrypt(password, user.login) != user.password:
                    return redirect(url_for('auth_error', code='AUTH_PASS'))
                
                session['login'] = user.login
                return redirect(url_for('index'))
            
            return render_template('login.html', error=None)
            
        except Exception:
            logging.exception('')


@app.route('/error/')
def auth_error():
    code = request.args['code']
    return render_template('error.html', error=ERRORS[code])


@app.route('/login', methods=['POST'])
def back_to_login():
  return redirect(url_for('login'))


@app.route('/logout', methods=['POST'])
def logout():
  session.pop('login', None)
  return redirect(url_for('index'))


@app.route('/')
def index():
    if 'login' in session:
        try:
            login = session['login']
            cnx = Connection_Factory.get_cnx(app.config['dbms'], app.config['db'])
            dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
            user = dao_user.find_by_login(cnx, login)
            return render_template('index.html', login=user.login)
        except Exception:
            logging.exception()
    else:
        return render_template('index.html', login=None)