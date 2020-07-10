from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    #Main urls, returns website
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('product/<int:pk>', views.product, name='product'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),

    #Test urls (csv, json), returns test websites
    path('upload', views.simple_upload, name='upload'),
    path('i_csv', views.import_csv, name='i_csv'),
    path('e_csv', views.export_csv, name='e_csv'),
    path('i_json', views.import_json, name='i_json'),
    path('e_json', views.export_json, name='e_json'),

    #Background urls, returns what it says
    path('api_register', views.api_register_view, name='api_register'),
    path('logout', views.logout_view, name='logout'),

]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
