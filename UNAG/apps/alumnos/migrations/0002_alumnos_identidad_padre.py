# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='identidad_padre',
            field=models.CharField(default=1, max_length=18, verbose_name='Identidad Padre'),
            preserve_default=False,
        ),
    ]
