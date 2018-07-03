# Generated by Django 2.0.7 on 2018-07-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('github', models.URLField()),
                ('link', models.URLField()),
            ],
            options={
                'db_table': 'Project',
            },
        ),
    ]
