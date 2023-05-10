from django.conf import settings
from django.shortcuts import render, redirect
from ..services import AuthService


ERRORS = settings.ERRORS

def sign_in(request):
    if request.method == 'POST':
        credentials = request.POST.get('creds')
        password = request.POST.get('password')
        if credentials is None:
            return render(request, 'sign_in.html')
        if not {'', None}.isdisjoint({credentials, password}):
                context = {'error': 'Empty field'}
                return render(request, 'sign_in.html', context)
        user = AuthService.get_by_creds(credentials)
        if not user:
             context = {'error': ERRORS['AUTH_CRED']}
             return render(request, 'sign_in.html', context)
        if AuthService.check_password(password, user):
            context = {'error': ERRORS['AUTH_PASS']}
            return render(request, 'sign_in.html', context)
        
        request.session['login'] = user.login
        request.session['role_id'] = user.role_id
        print('redir')
        return redirect('/')
    else:
        context = {'error': None}
        return render(request, 'sign_in.html', context)

    # with app.app_context():
    #     if request.method == 'POST':
    #         credentials = request.form.get('creds')
    #         password = request.form.get('password')
    #         if credentials is None:
    #             return render_template('sign_in.html')
    #         if not {'', None}.isdisjoint({credentials, password}):
    #             return render_template('sign_in.html', error='Empty field')
            
    #         user = AuthService.get_by_creds(credentials)
    #         if not user:
    #             return render_template('sign_in.html', error=ERRORS['AUTH_CRED'])

    #         if AuthService.check_password(password, user):
    #             return render_template('sign_in.html', error=ERRORS['AUTH_PASS'])
            
    #         session['login'] = user.login
    #         session['role_id'] = user.role_id
    #         return redirect(url_for('index_page'))
        
    #     return render_template('sign_in.html', error=None)
    

def sign_up(request):
    return
    # with app.app_context():
    #     if request.method == 'POST':
    #         login = request.form.get('username')
    #         email = request.form.get('email')
    #         password = request.form.get('password')
    #         if login is None:
    #             return render_template('sign_up.html')
    #         if not {'', None}.isdisjoint({login, email, password}):
    #             return render_template('sign_up.html', error='Empty field')
            
    #         validity = AuthService.check_data(login=login, email=email, password=password)
    #         if validity != True:
    #              return render_template('sign_up.html', error=validity)

    #         accessibility = AuthService.check_accessibility(login, email)
    #         if accessibility:
    #             return render_template('sign_up.html', error=ERRORS[accessibility])

    #         user = AuthService.sign_up(login, email, password)
            
    #         session['login'] = login
    #         session['role_id'] = user.role_id
    #         return redirect(url_for('index_page'))
        
    #     return render_template('sign_up.html', error=None)