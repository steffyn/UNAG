# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_auto_20160303_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='modulo',
            field=models.CharField(default=9, max_length=b'80'),
            preserve_default=False,
        ),
    ]
