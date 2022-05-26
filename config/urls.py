from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from core.nynet.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nynet/', include('core.nynet.urls')),
    path('', home_view, name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
