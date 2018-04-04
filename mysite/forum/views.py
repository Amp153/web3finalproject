from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from django.contrib import auth
#from django.template import loader
from .models import User
from .forms import SignUpForm, SignInForm

# Create your views here.
def index(request):
    return render(request, 'forum/create_cat.html', {})

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_date = timezone.now()
            post.user_level = 0
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



def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/account/loggedout/")