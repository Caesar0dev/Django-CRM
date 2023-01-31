# Generated by Django 4.1.1 on 2022-10-31 09:01

import cms.blocks
from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_blogdetailpage_bloglistpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdetailpage',
            name='show_legend',
        ),
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.fields.StreamField([('content_title', cms.blocks.BlogContentTitleBlock()), ('code', cms.blocks.BlogCodeBlock()), ('rich_text', cms.blocks.BlogRichTextBlock()), ('image', cms.blocks.BlogImageBlock())], use_json_field=None),
        ),
    ]
