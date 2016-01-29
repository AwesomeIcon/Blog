# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-timestamp',)},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
