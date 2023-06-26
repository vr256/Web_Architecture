from django.conf import settings
from django.shortcuts import render, redirect
from ..services import AuthService, InfoService


ERRORS = settings.ERRORS


def home_page(request):
    login = request.session.get('login')
    role = AuthService.get_role(request.session['role_id'])
    activities = InfoService.get_activities(login)
    context = {
        'login': login,
        'role': role,
        'activities': activities,
    }
    if not 'signout' in request.session:
        request.session['signout'] = True
        context['signout'] = None
        return render(request, 'home.html', context)
    else:
        request.session.pop('signout')
        if 'yes_button' in request.POST:
            sign_out(request)
            context['signout'] = True
        return render(request, 'home.html', context)


def sign_out(request):
    request.session.pop('login')
    request.session.pop('role_id')
    return redirect('/')
