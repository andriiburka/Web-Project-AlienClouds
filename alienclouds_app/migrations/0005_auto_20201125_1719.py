# Generated by Django 3.1.3 on 2020-11-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alienclouds_app', '0004_delete_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_title',
            field=models.CharField(max_length=50),
        ),
    ]
