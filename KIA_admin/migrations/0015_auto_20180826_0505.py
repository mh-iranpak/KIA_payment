# Generated by Django 2.0.7 on 2018-08-26 05:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('KIA_admin', '0014_auto_20180826_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyofadminactivities',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='systemtransactions',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]