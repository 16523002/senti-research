# Generated by Django 3.0.4 on 2020-04-16 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0013_auto_20200416_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchproject',
            name='rp_pic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='PIC', to='repository.User'),
        ),
    ]