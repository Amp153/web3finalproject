from django import forms
from .models import User

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