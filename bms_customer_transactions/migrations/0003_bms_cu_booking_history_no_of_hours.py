# Generated by Django 3.2.7 on 2021-11-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms_customer_transactions', '0002_auto_20211101_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='bms_cu_booking_history',
            name='no_of_hours',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
