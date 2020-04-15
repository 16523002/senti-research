# Generated by Django 3.0.4 on 2020-04-12 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_researchrespondent_rr_bod'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchproject',
            name='rp_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='researchrespondent',
            name='rr_registered_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='registered at'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researchrespondent',
            name='rr_updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='researchproject',
            name='rp_created_at',
            field=models.DateField(auto_now_add=True, verbose_name='created at'),
        ),
    ]
