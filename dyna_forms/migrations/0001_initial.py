# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assosiative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('form_name', models.CharField(unique=True, max_length=100)),
                ('form_description', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('short_text1', models.BooleanField(default=False)),
                ('short_text2', models.BooleanField(default=False)),
                ('short_text3', models.BooleanField(default=False)),
                ('short_text4', models.BooleanField(default=False)),
                ('num_field1', models.BooleanField(default=False)),
                ('num_field2', models.BooleanField(default=False)),
                ('long_text1', models.BooleanField(default=False)),
                ('long_text2', models.BooleanField(default=False)),
                ('long_text3', models.BooleanField(default=False)),
                ('long_text4', models.BooleanField(default=False)),
                ('long_text5', models.BooleanField(default=False)),
                ('date_field1', models.BooleanField(default=False)),
                ('date_field2', models.BooleanField(default=False)),
                ('date_field3', models.BooleanField(default=False)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Select Form Fields',
                'verbose_name_plural': 'Select Form Fields',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Messages',
            },
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('short_text1', models.CharField(max_length=150, null=True, blank=True)),
                ('short_text2', models.CharField(max_length=150, null=True, blank=True)),
                ('short_text3', models.CharField(max_length=150, null=True, blank=True)),
                ('short_text4', models.CharField(max_length=150, null=True, blank=True)),
                ('num_field1', models.CharField(max_length=150, null=True, blank=True)),
                ('num_field2', models.CharField(max_length=150, null=True, blank=True)),
                ('long_text1', models.CharField(max_length=150, null=True, blank=True)),
                ('long_text2', models.CharField(max_length=150, null=True, blank=True)),
                ('long_text3', models.CharField(max_length=150, null=True, blank=True)),
                ('long_text4', models.CharField(max_length=150, null=True, blank=True)),
                ('long_text5', models.CharField(max_length=150, null=True, blank=True)),
                ('date_field1', models.CharField(max_length=150, null=True, blank=True)),
                ('date_field2', models.CharField(max_length=150, null=True, blank=True)),
                ('date_field3', models.CharField(max_length=150, null=True, blank=True)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('assosiative', models.OneToOneField(to='dyna_forms.Assosiative')),
            ],
            options={
                'verbose_name': 'Input Field Labels',
                'verbose_name_plural': 'Input Field Labels',
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_text1', models.CharField(max_length=100, null=True, blank=True)),
                ('short_text2', models.CharField(max_length=100, null=True, blank=True)),
                ('short_text3', models.CharField(max_length=100, null=True, blank=True)),
                ('short_text4', models.CharField(max_length=100, null=True, blank=True)),
                ('num_field1', models.IntegerField(null=True, blank=True)),
                ('num_field2', models.IntegerField(null=True, blank=True)),
                ('long_text1', models.TextField(max_length=500, null=True, blank=True)),
                ('long_text2', models.TextField(max_length=500, null=True, blank=True)),
                ('long_text3', models.TextField(max_length=500, null=True, blank=True)),
                ('long_text4', models.TextField(max_length=500, null=True, blank=True)),
                ('long_text5', models.TextField(max_length=500, null=True, blank=True)),
                ('date_field1', models.DateTimeField(null=True, blank=True)),
                ('date_field2', models.DateTimeField(null=True, blank=True)),
                ('date_field3', models.DateTimeField(null=True, blank=True)),
                ('time_stamp', models.DateTimeField(auto_now=True)),
                ('label', models.ForeignKey(to='dyna_forms.Label')),
            ],
            options={
                'verbose_name': 'Saved Data for individual Forms',
                'verbose_name_plural': 'Saved Data for individual Forms',
            },
        ),
    ]
