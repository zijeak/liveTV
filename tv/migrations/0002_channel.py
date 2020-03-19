# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='频道名称', max_length=200)),
                ('address', models.CharField(verbose_name='频道串流', max_length=200)),
                ('category', models.ForeignKey(to='tv.Category')),
            ],
        ),
    ]
