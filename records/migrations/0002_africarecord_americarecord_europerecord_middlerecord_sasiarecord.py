# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfricaRecord',
            fields=[
                ('record_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='records.Record')),
            ],
            bases=('records.record',),
        ),
        migrations.CreateModel(
            name='AmericaRecord',
            fields=[
                ('record_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='records.Record')),
            ],
            bases=('records.record',),
        ),
        migrations.CreateModel(
            name='EuropeRecord',
            fields=[
                ('record_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='records.Record')),
            ],
            bases=('records.record',),
        ),
        migrations.CreateModel(
            name='MiddleRecord',
            fields=[
                ('record_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='records.Record')),
            ],
            bases=('records.record',),
        ),
        migrations.CreateModel(
            name='SAsiaRecord',
            fields=[
                ('record_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='records.Record')),
            ],
            bases=('records.record',),
        ),
    ]
