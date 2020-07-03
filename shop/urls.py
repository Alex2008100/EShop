from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('product/<int:pk>', views.product, name='product'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),

    path('write', views.write_view),
    path('icsv', views.import_csv),
    path('ecsv', views.export_csv),
    path('ijs', views.import_json),
    path('ejs', views.export_json),

    path('api_register', views.api_register_view, name='api_register'),
    path('logout', views.logout_view, name='logout'),
    path('upload', views.simple_upload),
]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
