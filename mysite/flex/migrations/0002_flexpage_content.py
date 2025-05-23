# Generated by Django 5.2.1 on 2025-05-12 11:09

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='content',
            field=wagtail.fields.StreamField([('title_and_text', 2)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your title', 'required': True}), 1: ('wagtail.blocks.TextBlock', (), {'help_text': 'Add your text', 'required': True}), 2: ('wagtail.blocks.StructBlock', [[('title', 0), ('text', 1)]], {})}, null=True),
        ),
    ]
