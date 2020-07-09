from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    #Redirect
    path('', include('shop.urls')),
    
    #Other tools
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
