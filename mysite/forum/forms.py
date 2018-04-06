from django import forms
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
'''
class SignUpForm(forms.ModelForm):

    user_name = forms.CharField()

    def clean_user_name(self):
        data = self.cleaned_data['user_name']
        return data
    
    class Meta:
        model = User
        fields = ('user_name','user_pass','user_email',)

class SignInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('user_name','user_pass',)
        '''

class SignUpForm(UserCreationForm):
    #first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    #last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )