from django.db import models
from django.template.defaultfilters import slugify

class Assosiative(models.Model):
    form_name = models.CharField(max_length=100, unique=True)
    form_description = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    instructions = models.TextField(max_length=500, blank=True, null=True)
    heading1 = models.TextField(max_length=500, blank=True, null=True)
    short_text1 = models.BooleanField(default=False)
    short_text2 = models.BooleanField(default=False)
    short_text3 = models.BooleanField(default=False)
    short_text4 = models.BooleanField(default=False)
    short_text5 = models.BooleanField(default=False)
    short_text6 = models.BooleanField(default=False)
    short_text7 = models.BooleanField(default=False)
    short_text8 = models.BooleanField(default=False)
    short_text9 = models.BooleanField(default=False)
    short_text10 = models.BooleanField(default=False)
    heading2 = models.TextField(max_length=500, blank=True, null=True)
    short_text11 = models.BooleanField(default=False)
    short_text12 = models.BooleanField(default=False)
    short_text13 = models.BooleanField(default=False)
    short_text14 = models.BooleanField(default=False)
    short_text15 = models.BooleanField(default=False)
    short_text16 = models.BooleanField(default=False)
    short_text17 = models.BooleanField(default=False)
    short_text18 = models.BooleanField(default=False)
    short_text19 = models.BooleanField(default=False)
    short_text20 = models.BooleanField(default=False)
    heading3 = models.TextField(max_length=500, blank=True, null=True)
    short_text21 = models.BooleanField(default=False)
    short_text22 = models.BooleanField(default=False)
    short_text23 = models.BooleanField(default=False)
    short_text24 = models.BooleanField(default=False)
    short_text25 = models.BooleanField(default=False)
    short_text26 = models.BooleanField(default=False)
    short_text27 = models.BooleanField(default=False)
    short_text28 = models.BooleanField(default=False)
    short_text29 = models.BooleanField(default=False)
    short_text30 = models.BooleanField(default=False)
    heading4 = models.TextField(max_length=500, blank=True, null=True)
    short_text31 = models.BooleanField(default=False)
    short_text32 = models.BooleanField(default=False)
    short_text33 = models.BooleanField(default=False)
    short_text34 = models.BooleanField(default=False)
    short_text35 = models.BooleanField(default=False)
    short_text36 = models.BooleanField(default=False)
    short_text37 = models.BooleanField(default=False)
    short_text38 = models.BooleanField(default=False)
    short_text39 = models.BooleanField(default=False)
    short_text40 = models.BooleanField(default=False)
    heading5 = models.TextField(max_length=500, blank=True, null=True)
    short_text41 = models.BooleanField(default=False)
    short_text42 = models.BooleanField(default=False)
    short_text43 = models.BooleanField(default=False)
    short_text44 = models.BooleanField(default=False)
    short_text45 = models.BooleanField(default=False)
    short_text46 = models.BooleanField(default=False)
    short_text47 = models.BooleanField(default=False)
    short_text48 = models.BooleanField(default=False)
    short_text49 = models.BooleanField(default=False)
    short_text50 = models.BooleanField(default=False)
    heading6 = models.TextField(max_length=500, blank=True, null=True)
    short_text51 = models.BooleanField(default=False)
    short_text52 = models.BooleanField(default=False)
    short_text53 = models.BooleanField(default=False)
    short_text54 = models.BooleanField(default=False)
    short_text55 = models.BooleanField(default=False)
    short_text56 = models.BooleanField(default=False)
    short_text57 = models.BooleanField(default=False)
    short_text58 = models.BooleanField(default=False)
    short_text59 = models.BooleanField(default=False)
    short_text60 = models.BooleanField(default=False)
    heading7 = models.TextField(max_length=500, blank=True, null=True)
    num_field1 = models.BooleanField(default=False)
    num_field2 = models.BooleanField(default=False)
    num_field3 = models.BooleanField(default=False)
    num_field4 = models.BooleanField(default=False)
    num_field5 = models.BooleanField(default=False)
    num_field6 = models.BooleanField(default=False)
    num_field7 = models.BooleanField(default=False)
    num_field8 = models.BooleanField(default=False)
    num_field9 = models.BooleanField(default=False)
    num_field10 = models.BooleanField(default=False)
    heading8 = models.TextField(max_length=500, blank=True, null=True)
    long_text1 = models.BooleanField(default=False)
    long_text2 = models.BooleanField(default=False)
    long_text3 = models.BooleanField(default=False)
    long_text4 = models.BooleanField(default=False)
    long_text5 = models.BooleanField(default=False)
    long_text6 = models.BooleanField(default=False)
    long_text7 = models.BooleanField(default=False)
    long_text8 = models.BooleanField(default=False)
    long_text9 = models.BooleanField(default=False)
    long_text10 = models.BooleanField(default=False)
    heading9 = models.TextField(max_length=500, blank=True, null=True)
    long_text11 = models.BooleanField(default=False)
    long_text12 = models.BooleanField(default=False)
    long_text13 = models.BooleanField(default=False)
    long_text14 = models.BooleanField(default=False)
    long_text15 = models.BooleanField(default=False)
    long_text16 = models.BooleanField(default=False)
    long_text17 = models.BooleanField(default=False)
    long_text18 = models.BooleanField(default=False)
    long_text19 = models.BooleanField(default=False)
    long_text20 = models.BooleanField(default=False)
    heading10 = models.TextField(max_length=500, blank=True, null=True)
    image_field1 = models.BooleanField(default=False)
    image_field2 = models.BooleanField(default=False)
    image_field3 = models.BooleanField(default=False)
    image_field4 = models.BooleanField(default=False)
    image_field5 = models.BooleanField(default=False)
    date_field1 = models.BooleanField(default=False)
    date_field2 = models.BooleanField(default=False)
    date_field3 = models.BooleanField(default=False)
    date_field4 = models.BooleanField(default=False)
    date_field5 = models.BooleanField(default=False)
    time_stamp = models.DateTimeField(auto_now=True)


    
    class Meta:
        verbose_name = ('Select Form Fields')
        verbose_name_plural =('Select Form Fields')
    
    def __unicode__(self):
        return self.form_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.form_name)
        super(Assosiative, self).save(*args, **kwargs)


class Label(models.Model):
    assosiative = models.OneToOneField(Assosiative, unique=True)
    slug = models.SlugField(unique=True)
    short_text1 = models.CharField(max_length=150, blank=True, null=True)
    short_text2 = models.CharField(max_length=150, blank=True, null=True)
    short_text3 = models.CharField(max_length=150, blank=True, null=True)
    short_text4 = models.CharField(max_length=150, blank=True, null=True)
    short_text5 = models.CharField(max_length=150, blank=True, null=True)
    short_text6 = models.CharField(max_length=150, blank=True, null=True)
    short_text7 = models.CharField(max_length=150, blank=True, null=True)
    short_text8 = models.CharField(max_length=150, blank=True, null=True)
    short_text9 = models.CharField(max_length=150, blank=True, null=True)
    short_text10 = models.CharField(max_length=150, blank=True, null=True)
    short_text11 = models.CharField(max_length=150, blank=True, null=True)
    short_text12 = models.CharField(max_length=150, blank=True, null=True)
    short_text13 = models.CharField(max_length=150, blank=True, null=True)
    short_text14 = models.CharField(max_length=150, blank=True, null=True)
    short_text15 = models.CharField(max_length=150, blank=True, null=True)
    short_text16 = models.CharField(max_length=150, blank=True, null=True)
    short_text17 = models.CharField(max_length=150, blank=True, null=True)
    short_text18 = models.CharField(max_length=150, blank=True, null=True)
    short_text19 = models.CharField(max_length=150, blank=True, null=True)
    short_text20 = models.CharField(max_length=150, blank=True, null=True)
    short_text21 = models.CharField(max_length=150, blank=True, null=True)
    short_text22 = models.CharField(max_length=150, blank=True, null=True)
    short_text23 = models.CharField(max_length=150, blank=True, null=True)
    short_text24 = models.CharField(max_length=150, blank=True, null=True)
    short_text25 = models.CharField(max_length=150, blank=True, null=True)
    short_text26 = models.CharField(max_length=150, blank=True, null=True)
    short_text27 = models.CharField(max_length=150, blank=True, null=True)
    short_text28 = models.CharField(max_length=150, blank=True, null=True)
    short_text29 = models.CharField(max_length=150, blank=True, null=True)
    short_text30 = models.CharField(max_length=150, blank=True, null=True)
    short_text31 = models.CharField(max_length=150, blank=True, null=True)
    short_text32 = models.CharField(max_length=150, blank=True, null=True)
    short_text33 = models.CharField(max_length=150, blank=True, null=True)
    short_text34 = models.CharField(max_length=150, blank=True, null=True)
    short_text35 = models.CharField(max_length=150, blank=True, null=True)
    short_text36 = models.CharField(max_length=150, blank=True, null=True)
    short_text37 = models.CharField(max_length=150, blank=True, null=True)
    short_text38 = models.CharField(max_length=150, blank=True, null=True)
    short_text39 = models.CharField(max_length=150, blank=True, null=True)
    short_text40 = models.CharField(max_length=150, blank=True, null=True)
    short_text41 = models.CharField(max_length=150, blank=True, null=True)
    short_text42 = models.CharField(max_length=150, blank=True, null=True)
    short_text43 = models.CharField(max_length=150, blank=True, null=True)
    short_text44 = models.CharField(max_length=150, blank=True, null=True)
    short_text45 = models.CharField(max_length=150, blank=True, null=True)
    short_text46 = models.CharField(max_length=150, blank=True, null=True)
    short_text47 = models.CharField(max_length=150, blank=True, null=True)
    short_text48 = models.CharField(max_length=150, blank=True, null=True)
    short_text49 = models.CharField(max_length=150, blank=True, null=True)
    short_text50 = models.CharField(max_length=150, blank=True, null=True)
    short_text51 = models.CharField(max_length=150, blank=True, null=True)
    short_text52 = models.CharField(max_length=150, blank=True, null=True)
    short_text53 = models.CharField(max_length=150, blank=True, null=True)
    short_text54 = models.CharField(max_length=150, blank=True, null=True)
    short_text55 = models.CharField(max_length=150, blank=True, null=True)
    short_text56 = models.CharField(max_length=150, blank=True, null=True)
    short_text57 = models.CharField(max_length=150, blank=True, null=True)
    short_text58 = models.CharField(max_length=150, blank=True, null=True)
    short_text59 = models.CharField(max_length=150, blank=True, null=True)
    short_text60 = models.CharField(max_length=150, blank=True, null=True)
    num_field1 = models.CharField(max_length=150, blank=True, null=True)
    num_field2 = models.CharField(max_length=150, blank=True, null=True)
    num_field3 = models.CharField(max_length=150, blank=True, null=True)
    num_field4 = models.CharField(max_length=150, blank=True, null=True)
    num_field5 = models.CharField(max_length=150, blank=True, null=True)
    num_field6 = models.CharField(max_length=150, blank=True, null=True)
    num_field7 = models.CharField(max_length=150, blank=True, null=True)
    num_field8 = models.CharField(max_length=150, blank=True, null=True)
    num_field9 = models.CharField(max_length=150, blank=True, null=True)
    num_field10 = models.CharField(max_length=150, blank=True, null=True)
    long_text1 = models.CharField(max_length=150, blank=True, null=True)
    long_text2 = models.CharField(max_length=150, blank=True, null=True)
    long_text3 = models.CharField(max_length=150, blank=True, null=True)
    long_text4 = models.CharField(max_length=150, blank=True, null=True)
    long_text5 = models.CharField(max_length=150, blank=True, null=True)
    long_text6 = models.CharField(max_length=150, blank=True, null=True)
    long_text7 = models.CharField(max_length=150, blank=True, null=True)
    long_text8 = models.CharField(max_length=150, blank=True, null=True)
    long_text9 = models.CharField(max_length=150, blank=True, null=True)
    long_text10 = models.CharField(max_length=150, blank=True, null=True)
    long_text11 = models.CharField(max_length=150, blank=True, null=True)
    long_text12 = models.CharField(max_length=150, blank=True, null=True)
    long_text13 = models.CharField(max_length=150, blank=True, null=True)
    long_text14 = models.CharField(max_length=150, blank=True, null=True)
    long_text15 = models.CharField(max_length=150, blank=True, null=True)
    long_text16 = models.CharField(max_length=150, blank=True, null=True)
    long_text17 = models.CharField(max_length=150, blank=True, null=True)
    long_text18 = models.CharField(max_length=150, blank=True, null=True)
    long_text19 = models.CharField(max_length=150, blank=True, null=True)
    long_text20 = models.CharField(max_length=150, blank=True, null=True)
    image_field1 = models.CharField(max_length=150, blank=True, null=True)
    image_field2 = models.CharField(max_length=150, blank=True, null=True)
    image_field3 = models.CharField(max_length=150, blank=True, null=True)
    image_field4 = models.CharField(max_length=150, blank=True, null=True)
    image_field5 = models.CharField(max_length=150, blank=True, null=True)
    date_field1 = models.CharField(max_length=150, blank=True, null=True)
    date_field2 = models.CharField(max_length=150, blank=True, null=True)
    date_field3 = models.CharField(max_length=150, blank=True, null=True)
    date_field4 = models.CharField(max_length=150, blank=True, null=True)
    date_field5 = models.CharField(max_length=150, blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ('Input Field Labels')
        verbose_name_plural =('Input Field Labels')
    
    def __unicode__(self):
        return "{0}".format(self.assosiative)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.assosiative)
        super(Label, self).save(*args, **kwargs)

class Master(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    posted_by = models.CharField(max_length=50, blank=True, null=True)
    project_name = models.CharField(max_length=100)
    #company = models.CharField(max_length=100)
    short_text1 = models.CharField(max_length=100, blank=True, null=True)
    short_text2 = models.CharField(max_length=100, blank=True, null=True)
    short_text3 = models.CharField(max_length=100, blank=True, null=True)
    short_text4 = models.CharField(max_length=100, blank=True, null=True)
    short_text5 = models.CharField(max_length=100, blank=True, null=True)
    short_text6 = models.CharField(max_length=100, blank=True, null=True)
    short_text7 = models.CharField(max_length=100, blank=True, null=True)
    short_text8 = models.CharField(max_length=100, blank=True, null=True)
    short_text9 = models.CharField(max_length=100, blank=True, null=True)
    short_text10 = models.CharField(max_length=100, blank=True, null=True)
    short_text11 = models.CharField(max_length=100, blank=True, null=True)
    short_text12 = models.CharField(max_length=100, blank=True, null=True)
    short_text13 = models.CharField(max_length=100, blank=True, null=True)
    short_text14 = models.CharField(max_length=100, blank=True, null=True)
    short_text15 = models.CharField(max_length=100, blank=True, null=True)
    short_text16 = models.CharField(max_length=100, blank=True, null=True)
    short_text17 = models.CharField(max_length=100, blank=True, null=True)
    short_text18 = models.CharField(max_length=100, blank=True, null=True)
    short_text19 = models.CharField(max_length=100, blank=True, null=True)
    short_text20 = models.CharField(max_length=100, blank=True, null=True)
    short_text21 = models.CharField(max_length=100, blank=True, null=True)
    short_text22 = models.CharField(max_length=100, blank=True, null=True)
    short_text23 = models.CharField(max_length=100, blank=True, null=True)
    short_text24 = models.CharField(max_length=100, blank=True, null=True)
    short_text25 = models.CharField(max_length=100, blank=True, null=True)
    short_text26 = models.CharField(max_length=100, blank=True, null=True)
    short_text27 = models.CharField(max_length=100, blank=True, null=True)
    short_text28 = models.CharField(max_length=100, blank=True, null=True)
    short_text29 = models.CharField(max_length=100, blank=True, null=True)
    short_text30 = models.CharField(max_length=100, blank=True, null=True)
    short_text31 = models.CharField(max_length=100, blank=True, null=True)
    short_text32 = models.CharField(max_length=100, blank=True, null=True)
    short_text33 = models.CharField(max_length=100, blank=True, null=True)
    short_text34 = models.CharField(max_length=100, blank=True, null=True)
    short_text35 = models.CharField(max_length=100, blank=True, null=True)
    short_text36 = models.CharField(max_length=100, blank=True, null=True)
    short_text37 = models.CharField(max_length=100, blank=True, null=True)
    short_text38 = models.CharField(max_length=100, blank=True, null=True)
    short_text39 = models.CharField(max_length=100, blank=True, null=True)
    short_text40 = models.CharField(max_length=100, blank=True, null=True)
    short_text41 = models.CharField(max_length=100, blank=True, null=True)
    short_text42 = models.CharField(max_length=100, blank=True, null=True)
    short_text43 = models.CharField(max_length=100, blank=True, null=True)
    short_text44 = models.CharField(max_length=100, blank=True, null=True)
    short_text45 = models.CharField(max_length=100, blank=True, null=True)
    short_text46 = models.CharField(max_length=100, blank=True, null=True)
    short_text47 = models.CharField(max_length=100, blank=True, null=True)
    short_text48 = models.CharField(max_length=100, blank=True, null=True)
    short_text49 = models.CharField(max_length=100, blank=True, null=True)
    short_text50 = models.CharField(max_length=100, blank=True, null=True)
    short_text51 = models.CharField(max_length=100, blank=True, null=True)
    short_text52 = models.CharField(max_length=100, blank=True, null=True)
    short_text53 = models.CharField(max_length=100, blank=True, null=True)
    short_text54 = models.CharField(max_length=100, blank=True, null=True)
    short_text55 = models.CharField(max_length=100, blank=True, null=True)
    short_text56 = models.CharField(max_length=100, blank=True, null=True)
    short_text57 = models.CharField(max_length=100, blank=True, null=True)
    short_text58 = models.CharField(max_length=100, blank=True, null=True)
    short_text59 = models.CharField(max_length=100, blank=True, null=True)
    short_text60 = models.CharField(max_length=100, blank=True, null=True)
    num_field1 = models.IntegerField(blank=True, null=True)
    num_field2 = models.IntegerField(blank=True, null=True)
    num_field3 = models.IntegerField(blank=True, null=True)
    num_field4 = models.IntegerField(blank=True, null=True)
    num_field5 = models.IntegerField(blank=True, null=True)
    num_field6 = models.IntegerField(blank=True, null=True)
    num_field7 = models.IntegerField(blank=True, null=True)
    num_field8 = models.IntegerField(blank=True, null=True)
    num_field9 = models.IntegerField(blank=True, null=True)
    num_field10 = models.IntegerField(blank=True, null=True)
    long_text1 = models.TextField(max_length=500, blank=True, null=True)
    long_text2 = models.TextField(max_length=500, blank=True, null=True)
    long_text3 = models.TextField(max_length=500, blank=True, null=True)
    long_text4 = models.TextField(max_length=500, blank=True, null=True)
    long_text5 = models.TextField(max_length=500, blank=True, null=True)
    long_text6 = models.TextField(max_length=500, blank=True, null=True)
    long_text7 = models.TextField(max_length=500, blank=True, null=True)
    long_text8 = models.TextField(max_length=500, blank=True, null=True)
    long_text9 = models.TextField(max_length=500, blank=True, null=True)
    long_text10 = models.TextField(max_length=500, blank=True, null=True)
    long_text11 = models.TextField(max_length=500, blank=True, null=True)
    long_text12 = models.TextField(max_length=500, blank=True, null=True)
    long_text13 = models.TextField(max_length=500, blank=True, null=True)
    long_text14 = models.TextField(max_length=500, blank=True, null=True)
    long_text15 = models.TextField(max_length=500, blank=True, null=True)
    long_text16 = models.TextField(max_length=500, blank=True, null=True)
    long_text17 = models.TextField(max_length=500, blank=True, null=True)
    long_text18 = models.TextField(max_length=500, blank=True, null=True)
    long_text19 = models.TextField(max_length=500, blank=True, null=True)
    long_text20 = models.TextField(max_length=500, blank=True, null=True)
    image_field1 = models.ImageField(upload_to = 'imgs', blank=True, null=True)
    image_field2 = models.ImageField(upload_to = 'imgs', blank=True, null=True)
    image_field3 = models.ImageField(upload_to = 'imgs', blank=True, null=True)
    image_field4 = models.ImageField(upload_to = 'imgs', blank=True, null=True)
    image_field5 = models.ImageField(upload_to = 'imgs', blank=True, null=True)
    date_field1 = models.DateField(blank=True, null=True)
    date_field2 = models.DateField(blank=True, null=True)
    date_field3 = models.DateField(blank=True, null=True)
    date_field4 = models.DateField(blank=True, null=True)
    date_field5 = models.DateField(blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ('Saved Data for individual Forms')
        verbose_name_plural = ('Saved Data for individual Forms')

    def __unicode__(self):
        return "{0}".format(self.time_stamp)
    


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Contact Messages"
        
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    #company = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.project_name