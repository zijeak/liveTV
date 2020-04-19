# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
#        migrations.CreateModel(
#           name='Category',
#           fields=[
#                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
#               ('name', models.CharField(verbose_name='分类名称', max_length=200)),
#           ],
#       ),
#        migrations.CreateModel(
#            name='channel',
#            fields=[
#                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
#                ('name', models.CharField(verbose_name='频道名称', max_length=200)),
#                ('address', models.CharField(verbose_name='频道串流', max_length=1000)),
#                ('category', models.ForeignKey(to='tv.Category')),
#            ],
#        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='通知标题', max_length=200)),
                ('content', models.CharField(verbose_name='通知内容', max_length=200, null=True)),
            ],
        ),
    ]
