# Generated by Django 3.0.5 on 2020-05-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0007_auto_20200501_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_likes',
            field=models.IntegerField(default=0),
        ),
    ]