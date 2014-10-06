# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='first_name',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='detail',
            old_name='last_name',
            new_name='last_Name',
        ),
        migrations.AddField(
            model_name='detail',
            name='confirm_Password',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='detail',
            name='password',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
    ]
