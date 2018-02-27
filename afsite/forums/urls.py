from django.urls import path
from . import views

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
]