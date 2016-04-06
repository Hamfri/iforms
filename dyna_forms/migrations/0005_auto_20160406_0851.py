# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyna_forms', '0004_auto_20160406_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='company',
        ),
        migrations.RemoveField(
            model_name='project',
            name='company',
        ),
    ]
