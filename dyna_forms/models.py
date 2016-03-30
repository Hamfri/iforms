from django.db import models
from django.template.defaultfilters import slugify

class Assosiative(models.Model):
    form_name = models.CharField(max_length=100, unique=True)
    form_description = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_text1 = models.BooleanField(default=False)
    short_text2 = models.BooleanField(default=False)
    short_text3 = models.BooleanField(default=False)
    short_text4 = models.BooleanField(default=False)
    num_field1 = models.BooleanField(default=False)
    num_field2 = models.BooleanField(default=False)
    long_text1 = models.BooleanField(default=False)
    long_text2 = models.BooleanField(default=False)
    long_text3 = models.BooleanField(default=False)
    long_text4 = models.BooleanField(default=False)
    long_text5 = models.BooleanField(default=False)
    date_field1 = models.BooleanField(default=False)
    date_field2 = models.BooleanField(default=False)
    date_field3 = models.BooleanField(default=False)
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
    num_field1 = models.CharField(max_length=150, blank=True, null=True)
    num_field2 = models.CharField(max_length=150, blank=True, null=True)
    long_text1 = models.CharField(max_length=150, blank=True, null=True)
    long_text2 = models.CharField(max_length=150, blank=True, null=True)
    long_text3 = models.CharField(max_length=150, blank=True, null=True)
    long_text4 = models.CharField(max_length=150, blank=True, null=True)
    long_text5 = models.CharField(max_length=150, blank=True, null=True)
    date_field1 = models.CharField(max_length=150, blank=True, null=True)
    date_field2 = models.CharField(max_length=150, blank=True, null=True)
    date_field3 = models.CharField(max_length=150, blank=True, null=True)
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
    short_text1 = models.CharField(max_length=100, blank=True, null=True)
    short_text2 = models.CharField(max_length=100, blank=True, null=True)
    short_text3 = models.CharField(max_length=100, blank=True, null=True)
    short_text4 = models.CharField(max_length=100, blank=True, null=True)
    num_field1 = models.IntegerField(blank=True, null=True)
    num_field2 = models.IntegerField(blank=True, null=True)
    long_text1 = models.TextField(max_length=500, blank=True, null=True)
    long_text2 = models.TextField(max_length=500, blank=True, null=True)
    long_text3 = models.TextField(max_length=500, blank=True, null=True)
    long_text4 = models.TextField(max_length=500, blank=True, null=True)
    long_text5 = models.TextField(max_length=500, blank=True, null=True)
    date_field1 = models.DateTimeField(blank=True, null=True)
    date_field2 = models.DateTimeField(blank=True, null=True)
    date_field3 = models.DateTimeField(blank=True, null=True)
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
    