# Generated by Django 2.0.3 on 2018-08-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KIA_auth', '0006_profile_is_restricted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='balance',
            new_name='credit',
        ),
    ]
