# Generated by Django 3.0.4 on 2020-05-09 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0022_auto_20200508_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchanswer',
            name='research_project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='repository.ResearchProject'),
            preserve_default=False,
        ),
    ]