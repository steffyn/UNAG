# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_auto_20160727_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
