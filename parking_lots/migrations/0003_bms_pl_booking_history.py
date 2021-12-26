# Generated by Django 3.2.7 on 2021-10-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lots', '0002_auto_20211015_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='bms_pl_booking_history',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('pl_id', models.IntegerField()),
                ('booking_date', models.DateTimeField()),
                ('booking_code', models.IntegerField()),
            ],
        ),
    ]
