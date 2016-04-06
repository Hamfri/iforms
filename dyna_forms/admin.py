from django.contrib import admin
from .models import Master, Label, Assosiative, Contact, Project
from .forms import get_field_label

class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = Contact
        
admin.site.register(Contact, ContactAdmin)

class MasterAdmin(admin.ModelAdmin):
    class Meta:
        model = Master
        
admin.site.register(Master, MasterAdmin)

class LabelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['assosiative']}
    class Meta:
        #fields = []
        model = Label
        #fieldsets = None
        #LabelForm = get_field_label
        #form = LabelForm

admin.site.register(Label, LabelAdmin)

class AssociativeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['form_name']}
    class Meta:
        model = Assosiative
admin.site.register(Assosiative, AssociativeAdmin)

class ProjectAdmin(admin.ModelAdmin):
    class Meta:
        model = Project
admin.site.register(Project, ProjectAdmin)

admin.site.site_header = 'i-Form admin'
