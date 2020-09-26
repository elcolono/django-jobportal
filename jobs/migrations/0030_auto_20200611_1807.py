# Generated by Django 3.0.6 on 2020-06-11 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0029_auto_20200611_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='education',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='types', to='jobs.Education'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='TypeExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Experience')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Type')),
            ],
        ),
        migrations.AddField(
            model_name='type',
            name='experience',
            field=models.ManyToManyField(through='jobs.TypeExperience', to='jobs.Experience'),
        ),
    ]