# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('ask', models.BigIntegerField(default=0)),
                ('identify', models.BigIntegerField(default=0)),
                ('diagnosis', models.BigIntegerField(default=0)),
                ('refer', models.BigIntegerField(default=0)),
                ('reinforce', models.BigIntegerField(default=0)),
                ('recommend', models.BigIntegerField(default=0)),
                ('reduce', models.BigIntegerField(default=0)),
                ('attune', models.BigIntegerField(default=0)),
                ('prescribe', models.BigIntegerField(default=0)),
                ('close', models.BigIntegerField(default=0)),
                ('burnout', models.BigIntegerField(default=0)),
            ],
        ),
    ]
