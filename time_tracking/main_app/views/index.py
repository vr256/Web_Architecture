from django.shortcuts import redirect, render
from django.conf import settings
from ..services import AuthService, AdminService



LANG = settings.LANG

def index_page(request):
    #request.session.flush()
    context = {'current_language': LANG}
    if 'login' in request.session:
        role = AuthService.get_role(request.session['role_id'])
        context['role'] = role
        context['login'] = request.session.get('login')
    return render(request, 'index.html', context)