from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors <pre>%s</pre>' % escape(html))
############ End of pdf gen logic ################
@login_required
def index(request):
    forms = Assosiative.objects.all()
    if len(forms) == 0:
        messages.add_message(request, messages.INFO, 'No forms are added currently, Contact Admin')
    return render(request, 'index.html', locals())

@login_required
def master_reports(request, pk):
    report = get_object_or_404(Master, pk=pk)
    return render(request, 'master_report.html', {'report':report})

######## pending for edits####################
def master_report_edit(request,slug):
    associate = get_object_or_404(Assosiative, slug=slug)
    MasterForm = get_form_class(associate)
    form = MasterForm(request.POST or None)
    form_name = associate.pk
    l_query = Label.objects.get(assosiative__pk=form_name)
    
    form = MasterForm(request.POST or None)
    if form.is_valid():
        associate = form.save(commit=False)
        associate.save()
        return redirect('dyna_forms.views.master_reports', slug=associate.slug)
    return render(request, 'master_report_edit.html', locals())
##################################################

@login_required
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


@login_required
def master(request,slug):
    fields = ['short_text1', 'short_text2', 'short_text3', 'short_text4',
              'short_text5', 'short_text6', 'short_text7', 'short_text8', 
              'short_text9', 'short_text10', 'short_text11', 'short_text12',
              'short_text13', 'short_text14', 'short_text15', 'short_text16',
              'short_text17', 'short_text18', 'short_text19', 'short_text20', 
              'short_text21', 'short_text22', 'short_text23', 'short_text24',
              'short_text25', 'short_text26', 'short_text27', 'short_text28',
              'short_text29', 'short_text30', 'short_text31', 'short_text32',
              'short_text33', 'short_text34', 'short_text35', 'short_text36',
              'short_text37', 'short_text38', 'short_text39', 'short_text40',
              'num_field1', 'num_field2', 'num_field3', 'num_field4', 'num_field5',
              'num_field6', 'num_field7', 'num_field8', 'num_field9', 'num_field10',
              'long_text1', 'long_text2', 'long_text3', 'long_text4', 'long_text5',
              'long_text6', 'long_text7', 'long_text8', 'long_text9', 'long_text10',
              'long_text11', 'long_text12', 'long_text13', 'long_text14', 'long_text15',
              'long_text16', 'long_text17', 'long_text18', 'long_text19', 'long_text20',
              'image_field1', 'image_field2', 'image_field3', 'image_field4', 'image_field5',
              'date_field1', 'date_field2', 'date_field3', 'date_field4', 'date_field5'
              ]

    #fields = ['short_text1', 'short_text2', 'short_text3', 'short_text4', 'num_field1', 'num_field2', 'long_text1',
    #          'long_text1','long_text2','long_text3','long_text4','long_text5','date_field1','date_field2','date_field3']
    associate = get_object_or_404(Assosiative, slug=slug)
    MasterForm = get_form_class(associate)
    #######Logic for rendering field labels#######
    form_name = associate.pk
    #l_query = Label.objects.get(assosiative__form_name=form_name).values('assosiative__form_name')
    l_query = Label.objects.get(assosiative__pk=form_name)
    form = MasterForm(request.POST, request.FILES or None)
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

@login_required
def master_report_pdf(request, pk):
    report = get_object_or_404(Master, pk=pk)
    return render_to_pdf('master_report_pdf.html',{
        'pagesize': 'A4',
        'report': report})
