# Generated by Django 5.2 on 2025-05-11 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SysAdmin', '0003_alter_webusers_email_alter_webusers_mob_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webusers',
            name='email',
            field=models.EmailField(max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='webusers',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
