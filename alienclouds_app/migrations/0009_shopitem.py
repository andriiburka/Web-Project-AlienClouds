# Generated by Django 3.1.4 on 2020-12-17 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alienclouds_app', '0008_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(blank=True)),
            ],
        ),
    ]
