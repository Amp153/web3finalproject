from django.urls import path
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('accounts/login/$', login),
    path('accounts/logout/$', logout),
]