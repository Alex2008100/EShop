# Generated by Django 3.0.6 on 2020-06-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20200614_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_root',
            field=models.ImageField(upload_to='img/products'),
        ),
    ]
