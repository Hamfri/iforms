from django.conf.urls import include, url

urlpatterns = [
    url(r'^register/$', 'user_accounts.views.register', name='register'),
    url(r'^login/$', 'user_accounts.views.user_login', name='login'),
    url(r'^logout/$', 'user_accounts.views.user_logout', name='logout'),
]
