# Generated by Django 2.0.7 on 2018-07-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_project_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
