from django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

class SignUpForm(forms.ModelForm):
    '''
    user_name = forms.CharField()

    def clean_user_name(self):
        data = self.cleaned_data['user_name']
        return data
    '''
    class Meta:
        model = User
        fields = ('user_name','user_pass','user_email',)

class SignInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_name','user_pass',)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("forum/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/login.html", {
        'form': form,
    })