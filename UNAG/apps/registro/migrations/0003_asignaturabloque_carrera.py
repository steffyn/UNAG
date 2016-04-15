# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_auto_20160330_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignaturabloque',
            name='carrera',
            field=models.ForeignKey(default=9, to='registro.Carrera'),
            preserve_default=False,
        ),
    ]
