# Generated by Django 3.0.6 on 2020-07-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0040_auto_20200708_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='experience',
            field=models.ManyToManyField(related_name='type_experience', through='jobs.TypeExperience', to='jobs.Type'),
        ),
    ]