# Generated by Django 3.2 on 2021-09-22 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0015_auto_20210913_1918"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lead",
            old_name="company",
            new_name="org",
        ),
    ]
