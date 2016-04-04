from django import forms
from django.contrib.auth.models import User
from user_accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):
    #username = forms.CharField(widgets=forms.TextArea(attrs={'class':'form-control'}))
    #email = forms.CharField(widgets=forms.TextArea(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')