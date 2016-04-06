# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyna_forms', '0002_auto_20160406_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assosiative',
            name='heading1',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
