# Generated by Django 3.0.4 on 2020-04-16 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0012_auto_20200416_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='activate_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='request',
            name='request_role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='repository.Role'),
        ),
    ]
