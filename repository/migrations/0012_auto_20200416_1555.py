# Generated by Django 3.0.4 on 2020-04-16 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0011_auto_20200416_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_domain',
            new_name='company_code',
        ),
    ]
