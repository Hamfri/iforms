from django import forms
from django.shortcuts import get_object_or_404
from .models import Master, Label, Assosiative, Contact

                              
class MasterddeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MasterForm, self).__init__(*args, **kwargs)
        l = [0,1,1,0,1,1]
        if l[0] == 0:
            self.fields['short_text1'] = forms.CharField()
        if l[0] == 0:
            self.fields['short_text2'] = forms.CharField()
        if l[0] == 0:
            self.fields['short_text3'] = forms.CharField()
        if l[0] == 0:
            self.fields['short_text4'] = forms.CharField()
        if l[0] == 0:
            self.fields['num_field1'] = forms.CharField()
        
    class Meta:
        model = Master
        fields = []
           
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
            if associate.num_field1 == 1:
                fields.append('num_field1')
            if associate.num_field2 == 1:
                fields.append('num_field2')
            #['long_text1','long_text2','long_text3','long_text4','long_text5','date_field1','date_field2','date_field3']
            if associate.long_text1 ==1:
                fields.append('long_text1')
            if associate.long_text2 ==1:
                fields.append('long_text2')
            if associate.long_text3 ==1:
                fields.append('long_text3')
            if associate.long_text4 ==1:
                fields.append('long_text4')
            if associate.long_text5 ==1:
                fields.append('long_text5')
            if associate.date_field1 ==1:
                fields.append('date_field1')
            if associate.date_field2 ==1:
                fields.append('date_field2')
            if associate.date_field3 ==1:
                fields.append('date_field3')
                
            
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