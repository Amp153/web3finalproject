from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from django.contrib import auth
#from django.template import loader
#from .models import User
from django.contrib.auth.models import User
#from .forms import SignUpForm, SignInForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request, 'forum/create_cat.html', {})
'''
def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.user_date = timezone.now()
            #post.user_level = 0
            post.save()
            #userName = form.cleaned_data['user_name']
    else:
        form = SignUpForm()
        #pending_user_name = 'user_name'
        #form = SignUpForm(initial={'user_name':pending_user_name,})

    return render(request, 'forum/signup.html', {'form': form})

def signin(request):
    #request.POST.get('user_name', None)
    
    form = SignInForm()
    return render(request, 'forum/signin.html', {'form': form})
    '''
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/forum')
    else:
        form = SignUpForm()
    return render(request, 'forum/signup.html', {'form': form})