# Generated by Django 5.2 on 2025-05-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orderedfood', '0002_alter_order_payment_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='food',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
