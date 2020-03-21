# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0003_category_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='url',
        ),
    ]
