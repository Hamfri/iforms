from django import forms
from accounts.models import User

class RegistrationForm(forms.ModelForm):
    """
    Form for registerin a new account
    """
    email = forms.EmailField(widget=forms.widget.TextInput, label="Email")
    password1 = forms.CharField(widget=forms.widget.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.widget.PasswordInput, label="Password (Again)")
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        
    def clean(self):
        """
        verifies that values entered into the password fields match
        NB: Errors here will appear in ``non_field_errors()`` because it applies to more than on e field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    