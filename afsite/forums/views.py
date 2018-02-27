#from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect#, HttpResponse
from django.urls import reverse
from django.views import generic
#from django.template import loader
from django.utils import timezone

from .models import Post, Title
# Create your views here.

class IndexView(generic.ListView):
	template_name = 'forums/index.html'
	context_object_name = 'latest_title_list'

	def get_queryset(self):
		"""
    	Return the last five published posts (not including those set to be
    	published in the future).
    	"""
		return Title.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Title
    template_name = 'forums/detail.html'
    def get_queryset(self):
    	"""
    	Excludes any posts that aren't published yet.
    	"""
    	return Title.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Title
    template_name = 'forums/results.html'