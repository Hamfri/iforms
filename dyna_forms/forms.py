from django import forms
from django.shortcuts import get_object_or_404
from .models import Master, Label, Assosiative, Contact
           
def get_form_class(associate, *args, **kwargs):
    class MasterForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(MasterForm,self).__init__(*args, **kwargs)
        class Meta:
            model = Master
            fields = []
            fields.append('label')
            if associate.short_text1 == 1:
                fields.append('short_text1')
            if associate.short_text2 == 1:
                fields.append('short_text2')
            if associate.short_text3 == 1:
                fields.append('short_text3')
            if associate.short_text4 == 1:
                fields.append('short_text4')
            if associate.short_text5 == 1:
                fields.append('short_text5')
            if associate.short_text6 == 1:
                fields.append('short_text6')
            if associate.short_text7 == 1:
                fields.append('short_text7')
            if associate.short_text8 == 1:
                fields.append('short_text8')
            if associate.short_text9 == 1:
                fields.append('short_text9')
            if associate.short_text10 == 1:
                fields.append('short_text10')
            if associate.short_text11 == 1:
                fields.append('short_text11')
            if associate.short_text12 == 1:
                fields.append('short_text12')
            if associate.short_text13 == 1:
                fields.append('short_text13')
            if associate.short_text14 == 1:
                fields.append('short_text14')
            if associate.short_text15 == 1:
                fields.append('short_text15')
            if associate.short_text16 == 1:
                fields.append('short_text16')
            if associate.short_text17 == 1:
                fields.append('short_text17')
            if associate.short_text18 == 1:
                fields.append('short_text18')
            if associate.short_text19 == 1:
                fields.append('short_text19')
            if associate.short_text20 == 1:
                fields.append('short_text20')
            if associate.short_text21 == 1:
                fields.append('short_text21')
            if associate.short_text22 == 1:
                fields.append('short_text22')
            if associate.short_text23 == 1:
                fields.append('short_text23')
            if associate.short_text24 == 1:
                fields.append('short_text24')
            if associate.short_text25 == 1:
                fields.append('short_text25')
            if associate.short_text26 == 1:
                fields.append('short_text26')
            if associate.short_text27 == 1:
                fields.append('short_text27')
            if associate.short_text28 == 1:
                fields.append('short_text28')
            if associate.short_text29 == 1:
                fields.append('short_text29')
            if associate.short_text30 == 1:
                fields.append('short_text30')
            if associate.short_text31 == 1:
                fields.append('short_text31')
            if associate.short_text32 == 1:
                fields.append('short_text32')
            if associate.short_text33 == 1:
                fields.append('short_text33')
            if associate.short_text34 == 1:
                fields.append('short_text34')
            if associate.short_text35 == 1:
                fields.append('short_text35')
            if associate.short_text36 == 1:
                fields.append('short_text36')
            if associate.short_text37 == 1:
                fields.append('short_text37')
            if associate.short_text38 == 1:
                fields.append('short_text38')
            if associate.short_text39 == 1:
                fields.append('short_text39')
            if associate.short_text40 == 1:
                fields.append('short_text40')
            if associate.num_field1 == 1:
                fields.append('num_field1')
            if associate.num_field2 == 1:
                fields.append('num_field2')
            if associate.num_field3 == 1:
                fields.append('num_field3')
            if associate.num_field4 == 1:
                fields.append('num_field4')
            if associate.num_field5 == 1:
                fields.append('num_field5')
            if associate.num_field6 == 1:
                fields.append('num_field6')
            if associate.num_field7 == 1:
                fields.append('num_field7')
            if associate.num_field8 == 1:
                fields.append('num_field8')
            if associate.num_field9 == 1:
                fields.append('num_field9')
            if associate.num_field10 == 1:
                fields.append('num_field10')
            if associate.long_text1 == 1:
                fields.append('long_text1')
            if associate.long_text2 == 1:
                fields.append('long_text2')
            if associate.long_text3 == 1:
                fields.append('long_text3')
            if associate.long_text4 == 1:
                fields.append('long_text4')
            if associate.long_text5 == 1:
                fields.append('long_text5')
            if associate.long_text6 == 1:
                fields.append('long_text6')
            if associate.long_text7 == 1:
                fields.append('long_text7')
            if associate.long_text8 == 1:
                fields.append('long_text8')
            if associate.long_text9 == 1:
                fields.append('long_text9')
            if associate.long_text10 == 1:
                fields.append('long_text10')
            if associate.long_text11 == 1:
                fields.append('long_text11')
            if associate.long_text12 == 1:
                fields.append('long_text12')
            if associate.long_text13 == 1:
                fields.append('long_text13')
            if associate.long_text14 == 1:
                fields.append('long_text14')
            if associate.long_text15 == 1:
                fields.append('long_text15')
            if associate.long_text16 == 1:
                fields.append('long_text16')
            if associate.long_text17 == 1:
                fields.append('long_text17')
            if associate.long_text18 == 1:
                fields.append('long_text18')
            if associate.long_text19 == 1:
                fields.append('long_text19')
            if associate.long_text20 == 1:
                fields.append('long_text20')
            if associate.image_field1 == 1:
                fields.append('image_field1')
            if associate.image_field2 == 1:
                fields.append('image_field2')
            if associate.image_field3 == 1:
                fields.append('image_field3')
            if associate.image_field4 == 1:
                fields.append('image_field4')
            if associate.image_field5 == 1:
                fields.append('image_field5')
            if associate.date_field1 == 1:
                fields.append('date_field1')
            if associate.date_field2 == 1:
                fields.append('date_field2')
            if associate.date_field3 == 1:
                fields.append('date_field3')
            if associate.date_field4 == 1:
                fields.append('date_field4')
            if associate.date_field5 == 1:
                fields.append('date_field5')
                
    return MasterForm

def get_field_label(l_asso, *args, **kwargs):
    class LabelForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super(LabelForm,self).__init__(*args, **kwargs)
        class Meta:
            model = Label
            fields = []
            fields.append('assosiative')
            if l_asso.short_text1 == 1:
                fields.append('short_text1')
            if l_asso.short_text2 == 1:
                fields.append('short_text2')
            if l_asso.short_text3 == 1:
                fields.append('short_text3')
            if l_asso.short_text4 == 1:
                fields.append('short_text4')
            if l_asso.num_field1 == 1:
                fields.append('num_field1')
            if l_asso.num_field2 == 1:
                fields.append('num_field2')
            if l_asso.long_text1 ==1:
                fields.append('long_text1')
            if l_asso.long_text2 ==1:
                fields.append('long_text2')
            if l_asso.long_text3 ==1:
                fields.append('long_text3')
            if l_asso.long_text4 ==1:
                fields.append('long_text4')
            if l_asso.long_text5 ==1:
                fields.append('long_text5')
            if l_asso.date_field1 ==1:
                fields.append('date_field1')
            if l_asso.date_field2 ==1:
                fields.append('date_field2')
            if l_asso.date_field3 ==1:
                fields.append('date_field3')
            
    return LabelForm


class AssosiativeForm(forms.ModelForm):
    class Meta:
        model = Assosiative
        fields = ['short_text1', 'short_text2', 'short_text3', 'short_text4', 'num_field1', 'num_field2']
        
        
               
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']