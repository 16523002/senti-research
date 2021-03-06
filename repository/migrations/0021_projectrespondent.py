# Generated by Django 3.0.4 on 2020-05-04 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0020_auto_20200428_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectRespondent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.ResearchProject')),
                ('respondent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.ResearchRespondent')),
            ],
        ),
    ]
