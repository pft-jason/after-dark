from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from GALLERY.views import gallery_home as default 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallery/', include('GALLERY.urls')),
    path('auth/', include('AUTH.urls')),
    path('', default)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
