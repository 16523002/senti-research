# Generated by Django 3.0.4 on 2020-04-05 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_company_status_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='google_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
