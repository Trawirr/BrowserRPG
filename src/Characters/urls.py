from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('profil', views.index, name='character'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
]