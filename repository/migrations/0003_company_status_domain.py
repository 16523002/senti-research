# Generated by Django 3.0.4 on 2020-04-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0002_auto_20200405_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='status_domain',
            field=models.BooleanField(default=False),
        ),
    ]
