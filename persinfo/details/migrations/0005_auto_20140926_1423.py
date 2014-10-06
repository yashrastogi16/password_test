# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_detail_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='password',
            new_name='password1',
        ),
    ]
