# Generated by Django 3.0.4 on 2020-04-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_auto_20200405_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchrespondent',
            name='rr_bod',
            field=models.DateField(null=True),
        ),
    ]
