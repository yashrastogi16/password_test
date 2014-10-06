# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20140923_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='confirm_Password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detail',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
