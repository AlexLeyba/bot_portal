# Generated by Django 2.2 on 2019-05-07 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_bot', '0003_buttons_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buttons',
            old_name='number',
            new_name='num',
        ),
    ]