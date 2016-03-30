from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'dyna_forms.views.index', name='index'),
    url(r'^master/(?P<slug>[-\w]+)/$', 'dyna_forms.views.master', name='master'),
    #url(r'^query/(?P<pk>[0-9]+)/$', 'dyna_forms.views.master', name='query'),
    url(r'^master_reports/(?P<pk>[0-9]+)/$', 'dyna_forms.views.master_reports', name='master_reports'),
    url(r'^master_report_pdf/(?P<pk>[0-9]+)/$', 'dyna_forms.views.master_report_pdf', name='master_report_pdf'),
    url(r'^label/(?P<slug>[-\w]+)/$', 'dyna_forms.views.label', name='label'),
    url(r'^associative/$', 'dyna_forms.views.associative', name='associative'),
    url(r'^contact/$', 'dyna_forms.views.contact', name='contact'),
]