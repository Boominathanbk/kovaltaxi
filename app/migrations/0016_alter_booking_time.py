# Generated by Django 5.1.6 on 2025-03-04 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
