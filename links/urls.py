from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'links'
urlpatterns = [
    path('hash', views.hash_url , name='hashing'),
    path('<slug:short_url>', views.lookup_url_and_redirect, name='lookup_redirect'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]