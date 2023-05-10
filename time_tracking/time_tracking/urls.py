from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
]

handler404 = 'main_app.views.error.handle_404'
handler500 = 'main_app.views.error.handle_500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)