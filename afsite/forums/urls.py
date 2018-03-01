from django.urls import path
from django.conf.urls import url
from . import views as forums_views
from . import views
#from django.contrib.auth import views as auth_views

app_name = 'forums'
urlpatterns = [
	# ex: /forums/
	# path('',views.index,name='index'),
	path('', views.IndexView.as_view(), name='index'),
    # ex: /forums/5/
	#path('<int:question_id>/', views.detail, name='detail'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	# ex: /forums/5/results
	#path('<int:question_id>/results/', views.results, name='results'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	# Allow the user to change the password: use this in templates
	# <a href="{% url 'password_change' %}">{% trans "Change password" %}</a>
	# original code:
	# url(r'^accounts/', include('django.contrib.auth.urls')),
	# path(r'^accounts/', include('django.contrib.auth.urls')),
	url(r'^signup/$', forums_views.signup, name='signup'),
]