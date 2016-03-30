from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django import forms

from .models import Master, Label, Assosiative
from .forms import AssosiativeForm, ContactForm, get_field_label, get_form_class

################Backup###########################
#def master(request,pk):
#    associate = get_object_or_404(Assosiative, pk=pk)
#    MasterForm = get_form_class(associate)
#    form = MasterForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#    else:
#        print form.errors
#    return render(request, 'master.html', locals())



############ pdf Generation logic ################
"""
PDF GENERATION LOGIC
"""
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from cgi import escape

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html = template.render(context)
    result = StringIO.StringIO()
    
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors <pre>%s</pre>' % escape(html))
############ End of pdf gen logic ################
def index(request):
    forms = Assosiative.objects.all()
    if len(forms) == 0:
        messages.add_message(request, messages.INFO, 'No forms are added currently, Contact Admin')
    return render(request, 'index.html', locals())

def master_reports(request, pk):
    report = get_object_or_404(Master, pk=pk)
    return render(request, 'master_report.html', {'report':report})

def query_master(request,pk):
    query = get_object_or_404(Master, pk=pk)
    return render(request, 'query_master.html', locals())

def contact(request):
    fields = ['name', 'email', 'message']
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(request, messages.INFO, 'Your message has been sent Successfully'
                                 )
            return HttpResponseRedirect('/')
        else:
            print form.errors
    else:
        form = ContactForm()
    for key in form.fields.keys():
        if key in fields:
            field = form.fields[key]
            field.widget.attrs['class'] = 'form-control'
        
    return render(request, 'contact.html', locals())


def master(request,slug):
    fields = ['short_text1', 'short_text2', 'short_text3', 'short_text4', 'num_field1', 'num_field2', 'long_text1',
              'long_text1','long_text2','long_text3','long_text4','long_text5','date_field1','date_field2','date_field3']
    associate = get_object_or_404(Assosiative, slug=slug)
    MasterForm = get_form_class(associate)
    #######Logic for rendering field labels#######
    form_name = associate.pk
    #l_query = Label.objects.get(assosiative__form_name=form_name).values('assosiative__form_name')
    l_query = Label.objects.get(assosiative__pk=form_name)
    form = MasterForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.add_message(request, messages.INFO, 'Your Form has been posted successfully'
                                )
        return redirect('dyna_forms.views.master_reports', pk=post.pk)
        #return redirect('form_gen.views.query_doc', pk=post.pk)
    else:
        print form.errors
    for key in form.fields.keys():
        if key in fields:
            field = form.fields[key]
            field.widget.attrs['class'] = 'form-control'
    
    return render(request, 'master.html', locals())


def label(request,slug):
    l_asso = get_object_or_404(Assosiative, slug=slug)
    LabelForm = get_field_label(l_asso)
    form_name = l_asso.pk
    #l_query = Label.objects.get(assosiative__form_name=form_name).values('assosiative__form_name')
    l_query = Label.objects.get(assosiative__pk=form_name)
    ####Debug zone for labels#######
    short_text1 = l_query.short_text1
    print short_text1
    print l_query,"Associative"
    print form_name,"Label"
    #######End of debug zone######
    form = LabelForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'label.html', locals())

def associative(request):
    if request.method == 'POST':
        form = AssosiativeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print form.errors
    else:
        form = AssosiativeForm()
    return render(request, 'associative.html', locals())


def master_report_pdf(request, pk):
    report = get_object_or_404(Master, pk=pk)
    return render_to_pdf('master_report_pdf.html',{
        'pagesize': 'A4',
        'report': report})
