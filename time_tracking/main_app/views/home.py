from django.shortcuts import render
#from ..services import AuthService, InfoService


def home_page(request):
    return
    # login = session.get('login')
    # role = AuthService.get_role(session['role_id'])
    # activities = InfoService.get_activities(login)
    # if not 'signout' in session:
    #     session['signout'] = True
    #     return render_template('home.html', login=login, role=role, \
    #                            activities=activities, signout=None)
    # else:
    #     session.pop('signout')
    #     if 'yes_button' in request.form:
    #         sign_out()
    #     return render_template('home.html', login=login, role=role, \
    #                            activities=activities, signout=True)


def sign_out():
    return
    # session.pop('login')
    # session.pop('role_id')
    # return redirect(url_for('index_page'))