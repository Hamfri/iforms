from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import login, logout, authenticate 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user_accounts.forms import UserProfileForm

def register(request):
    field_class = ('username', 'email', 'password')
    registered = False
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
        else:
            print user_form.errors
    else:
        user_form = UserProfileForm()
    for key in user_form.fields.keys():
        if key in field_class:
            field = user_form.fields[key]
            field.widget.attrs['class'] = 'form-control'
        
    return render(request, 'accounts/register.html', locals())


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.INFO, 'Your account is disabled')
        else:
            print "Invalid login details: {0}, {1}".format(username,password)
            messages.add_message(request, messages.INFO, 'Invalid login details')
            return redirect("user_accounts:login")
    else:
        return render(request, 'accounts/login.html', locals())
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')