from flask import request, session, render_template, redirect, url_for, current_app as app
from ..services import AuthService
from ..properties import ERRORS

def sign_in():
    with app.app_context():
        if request.method == 'POST':
            credentials = request.form.get('creds')
            password = request.form.get('password')
            if credentials is None:
                return render_template('sign_in.html')
            if not {'', None}.isdisjoint({credentials, password}):
                return render_template('sign_in.html', error='Empty field')
            
            user = AuthService.get_by_creds(credentials)
            if not user:
                return render_template('sign_in.html', error=ERRORS['AUTH_CRED'])

            if AuthService.check_password(password, user):
                return render_template('sign_in.html', error=ERRORS['AUTH_PASS'])
            
            session['login'] = user.login
            session['role_id'] = user.role_id
            return redirect(url_for('index_page'))
        
        return render_template('sign_in.html', error=None)
    

def sign_up():
    with app.app_context():
        if request.method == 'POST':
            login = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            if login is None:
                return render_template('sign_up.html')
            if not {'', None}.isdisjoint({login, email, password}):
                return render_template('sign_up.html', error='Empty field')
            
            validity = AuthService.check_data(login=login, email=email, password=password)
            if validity != True:
                 return render_template('sign_up.html', error=validity)

            accessibility = AuthService.check_accessibility(login, email)
            if accessibility:
                return render_template('sign_up.html', error=ERRORS[accessibility])

            user = AuthService.sign_up(login, email, password)
            
            session['login'] = login
            session['role_id'] = user.role_id
            return redirect(url_for('index_page'))
        
        return render_template('sign_up.html', error=None)


def back_to_login():
    return redirect(url_for('sign_in'))