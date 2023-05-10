from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from ..services import AdminService

from django.apps import apps


User = apps.get_model('main_app', 'User')

#from ..services import AuthService, AdminService

# def index(request, **kwargs):
#     if kwargs and kwargs['arg2'] > 10:
#         if kwargs['arg2'] > 100:
#             raise Http404
#         else: # Returns HttpResponseRedirect - 30x; permanent=True for 301 and False for 302
#             return redirect('main', permanent=True)

#     return HttpResponse('Main page' + ' '.join([str(i) for i in kwargs.values()]))

# def not_found(request, exception):
#     return HttpResponseNotFound('Page not found (customized)')


def index_page(request):
    users = AdminService.get_users()
    print(users)
    return render(request, 'index.html')
    # if 'login' in session:
    #     role = AuthService.get_role(session['role_id']) 
    #     return render_template('index.html', login=session.get('login'), role=role, current_language='en')
    # else:
    #     return render_template('index.html', current_language='en')


def show_users():
    return
    # users = AdminService.get_users()
    # return render_template('index.html', login=session.get('login'), 
    #                         users=[user.login for user in users],
    #                         current_language='en')