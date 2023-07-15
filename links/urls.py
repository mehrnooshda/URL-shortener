from django.urls import path

from . import views

app_name = 'links'
urlpatterns = [
    path('hash', views.hash_url , name='hashing'),
    path('<slug:short_url>', views.lookup_url_and_redirect, name='lookup_redirect')
]