# Generated by Django 5.1.4 on 2024-12-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='points',
            field=models.IntegerField(default=100),
        ),
    ]
