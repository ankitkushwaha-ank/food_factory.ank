# Generated by Django 5.2 on 2025-04-24 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_remove_service_service_name_service_service_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_price',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
