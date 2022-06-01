from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.nynet.views import home_view
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nynet/', include('core.nynet.urls')),
    path('', home_view, name='home'),
    path('login/', include('core.login.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
