# Generated by Django 3.0.6 on 2020-07-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200701_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_root',
            field=models.ImageField(default='img/product-3_dAtZf9b.jpg', upload_to='img/'),
        ),
    ]
