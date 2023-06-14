from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('profile', views.profile, name='profile'),
    path('memories', views.memories, name='memories'),
    path('training', views.training, name='training'),
    path('profil', views.profile, name='character'),
    path('profil', views.profile, name='character'),
    path('profil', views.profile, name='character'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
]