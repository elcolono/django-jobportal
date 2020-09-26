# Generated by Django 3.0.6 on 2020-06-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0016_remove_task_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobhardskill',
            name='relevanz',
        ),
        migrations.RemoveField(
            model_name='typehardskill',
            name='relevanz',
        ),
        migrations.AddField(
            model_name='jobhardskill',
            name='priority',
            field=models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='typehardskill',
            name='priority',
            field=models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], max_length=10, null=True),
        ),
    ]