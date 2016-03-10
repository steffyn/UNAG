# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodo',
            name='clase',
            field=models.IntegerField(default=2014),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='periodo',
            name='fecha_final',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 15, 38, 40, 438000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='periodo',
            name='fecha_inicio',
            field=models.DateField(default=datetime.datetime(2016, 2, 29, 15, 38, 50, 198000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
