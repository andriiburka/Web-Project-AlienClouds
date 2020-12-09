# Generated by Django 3.1.4 on 2020-12-09 08:39

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
                ('project_title', models.CharField(max_length=50)),
                ('project_main_image', models.ImageField(upload_to='media')),
                ('project_description', models.TextField()),
            ],
        ),
    ]
