# Generated by Django 5.1.6 on 2025-03-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_booking_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
