# Generated by Django 3.2.13 on 2022-11-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product_image',
            field=models.URLField(max_length=255),
        ),
    ]