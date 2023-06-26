from django.conf import settings
from django.http import HttpResponse
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


def sign_up(request):
    if request.method == 'POST':
        login = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if login is None:
            return render(request, 'sign_up.html')
        if not {'', None}.isdisjoint({login, email, password}):
            context = {'error': 'Empty field'}
            return render(request, 'sign_up.html', context)

        validity = AuthService.check_data(login=login, email=email,
                                          password=password)
        if validity != True:
            context = {'error': validity}
            return render(request, 'sign_up.html', context)

        accessibility = AuthService.check_accessibility(login, email)
        if accessibility:
            context = {'error': ERRORS[accessibility]}
            return render(request, 'sign_up.html', context)

        user = AuthService.sign_up(login, email, password)

        request.session['login'] = login
        request.session['role_id'] = user.role_id
        return redirect('/')

    context = {'error': None}
    return render(request, 'sign_up.html', context)
