# Generated by Django 3.0.4 on 2020-04-22 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0015_auto_20200417_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to='repository/assets/images/'),
        ),
    ]
