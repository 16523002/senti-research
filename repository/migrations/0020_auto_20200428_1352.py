# Generated by Django 3.0.4 on 2020-04-28 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0019_auto_20200427_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='researchrespondent',
            old_name='rr_bod',
            new_name='rr_birth',
        ),
    ]
