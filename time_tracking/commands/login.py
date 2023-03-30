import logging

from flask import request, session, render_template, redirect, url_for
from flask import current_app as app
from ..utills import encrypt
from ..factory import Connection_Factory, DAO_Factory
from ..config import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

def general_login():
    with app.app_context():
        try:
            if request.method == 'POST':
                credentials = request.form.get('creds')
                if credentials is None:
                    return render_template('login.html')
                if credentials =='':
                    return render_template('login.html', error='Empty login field')
                
                cnx = Connection_Factory.get_cnx(app.config['dbms'], app.config['db'])
                dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
                user_by_login = dao_user.find_by_login(cnx, credentials)
                user_by_email = dao_user.find_by_email(cnx, credentials)

                if not user_by_login and not user_by_email:
                    return redirect(url_for('auth_error', code='AUTH_CRED'))

                user = list(filter(lambda x: x, [user_by_login, user_by_email]))[0]
                password = request.form.get('password')

                if encrypt(password, user.login) != user.password:
                    return redirect(url_for('auth_error', code='AUTH_PASS'))
                
                session['login'] = user.login
                session['role_id'] = user.role_id
                return redirect(url_for('general_index'))
            
            return render_template('login.html', error=None)
            
        except Exception:
            logging.exception('')