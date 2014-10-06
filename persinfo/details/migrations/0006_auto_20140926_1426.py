# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0005_auto_20140926_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='password1',
            new_name='password',
        ),
    ]
