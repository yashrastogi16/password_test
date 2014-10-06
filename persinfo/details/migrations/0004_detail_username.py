# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_auto_20140923_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='username',
            field=models.CharField(max_length=120, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
