from django.urls import path
from .views import index_page, sign_in, sign_up,   \
                       sign_out,    \
                       handle_404, handle_500, home_page

urlpatterns = [
    path('', index_page, name='index'),
    path('signin/', sign_in, name='signin'),
    path('signup/', sign_up, name='signup'),
    path('home/', home_page, name='home')
]