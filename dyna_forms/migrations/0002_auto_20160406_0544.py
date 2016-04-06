# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyna_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assosiative',
            name='heading10',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='heading2',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='heading3',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='heading4',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='heading5',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='heading6',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='heading7',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='heading8',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='heading9',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='assosiative',
            name='instructions',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
