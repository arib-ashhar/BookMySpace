# Generated by Django 3.2.7 on 2021-10-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_signup',
            name='user_type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
