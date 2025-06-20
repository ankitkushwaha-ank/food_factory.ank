# Generated by Django 5.2 on 2025-04-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0018_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='item',
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(related_name='carts', to='service.service'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_oldprice',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_price',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
