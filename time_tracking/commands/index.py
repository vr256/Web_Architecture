import logging

from flask import render_template, redirect, url_for, session
from flask import current_app as app
from ..factory import Connection_Factory, DAO_Factory
from ..config import LOG_FORMAT, LOG_PATHES

logging.basicConfig(level=logging.DEBUG, filename=LOG_PATHES[__name__], 
                    filemode="a+", format=LOG_FORMAT)

def general_index():
    if 'login' in session:
        try:
            cnx = Connection_Factory.get_cnx(app.config['dbms'], app.config['db'])
            dao_role = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('role')
            role = dao_role.find_by_id(cnx, session['role_id'])
            return render_template('index.html', login=session.get('login'), role=role.name_role)
        except Exception:
            logging.exception('')
    else:
        return render_template('index.html')
    

def show_users():
    try:
        cnx = Connection_Factory.get_cnx(app.config['dbms'], app.config['db'])
        dao_user = DAO_Factory.get_dao(app.config['dbms']).get_dao_implementation('user')
        users = dao_user.select_all(cnx)
        return render_template('index.html', login=session.get('login'), role_id=session.get('role_id'), 
                               users=[user.login for user in users])
    except Exception:
        logging.exception('')


def logout():
  session.pop('login', None)
  return redirect(url_for('general_index'))

