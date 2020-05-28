# Generated by Django 3.0.6 on 2020-05-28 12:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200527_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardskill',
            name='dependency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Hardskill'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hardskill',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]