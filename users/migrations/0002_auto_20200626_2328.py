# Generated by Django 3.0.7 on 2020-06-26 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='wallet',
            field=models.IntegerField(default=10000),
        ),
    ]
