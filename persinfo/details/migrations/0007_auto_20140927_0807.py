# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_auto_20140926_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
