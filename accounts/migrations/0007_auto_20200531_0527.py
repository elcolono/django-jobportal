# Generated by Django 3.0.6 on 2020-05-31 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200531_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_employer',
            field=models.BooleanField(default=True),
        ),
    ]