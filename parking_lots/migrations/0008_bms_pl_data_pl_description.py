# Generated by Django 3.2.7 on 2021-11-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_lots', '0007_alter_bms_pl_data_pl_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bms_pl_data',
            name='pl_description',
            field=models.CharField(blank=True, max_length=2500, null=True),
        ),
    ]
