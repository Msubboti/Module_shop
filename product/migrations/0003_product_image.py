# Generated by Django 3.0.7 on 2020-06-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200630_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/media/images/product/'),
        ),
    ]
