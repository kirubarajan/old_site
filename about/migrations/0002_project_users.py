# Generated by Django 2.0.7 on 2018-07-03 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.CharField(default='Deprecated', max_length=50),
            preserve_default=False,
        ),
    ]
