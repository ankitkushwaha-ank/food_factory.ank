# Generated by Django 5.2 on 2025-04-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_alter_cart_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item_price',
            field=models.CharField(default=None, null=True),
        ),
    ]
