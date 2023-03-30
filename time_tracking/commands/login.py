from flask import request, session, render_template, redirect, url_for
from flask import current_app as app
from ..services import AuthService

def general_login():
    with app.app_context():
        if request.method == 'POST':
            credentials = request.form.get('creds')
            if credentials is None:
                return render_template('login.html')
            if credentials =='':
                return render_template('login.html', error='Empty login field')
            
            user = AuthService().get_by_creds(credentials)
            if not user:
                return redirect(url_for('auth_error', code='AUTH_CRED'))

            password = request.form.get('password')
            if AuthService().check_password(password, user):
                return redirect(url_for('auth_error', code='AUTH_PASS'))
            
            session['login'] = user.login
            session['role_id'] = user.role_id
            return redirect(url_for('general_index'))
        
        return render_template('login.html', error=None)