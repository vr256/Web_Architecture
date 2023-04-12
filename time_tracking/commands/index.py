from flask import render_template, redirect, url_for, session
from ..services import AuthService, AdminService

def index_page():
    if 'login' in session:
        role = AuthService.get_role(session['role_id']) 
        return render_template('index.html', login=session.get('login'), role=role)
    else:
        return render_template('index.html')


def show_users():
    users = AdminService.get_users()
    return render_template('index.html', login=session.get('login'), 
                            users=[user.login for user in users])