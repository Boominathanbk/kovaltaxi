# Generated by Django 5.1.6 on 2025-03-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
