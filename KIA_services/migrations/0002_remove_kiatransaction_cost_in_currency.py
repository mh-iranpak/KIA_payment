# Generated by Django 2.0.7 on 2018-08-26 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KIA_services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kiatransaction',
            name='cost_in_currency',
        ),
    ]
