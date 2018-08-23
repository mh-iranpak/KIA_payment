# Generated by Django 2.0.3 on 2018-08-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kia_services', '0003_auto_20180811_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='kiaservicefield',
            name='optional',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='kiaservicefield',
            name='type',
            field=models.IntegerField(choices=[(1, 'BooleanField'), (2, 'CharField'), (3, 'CharField'), (5, 'DateField'), (6, 'DateTimeField'), (7, 'DecimalField'), (9, 'EmailField'), (10, 'FileField'), (13, 'IntegerField'), (14, 'MultipleChoiceField')]),
        ),
    ]
