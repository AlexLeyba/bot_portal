# Generated by Django 2.2 on 2019-04-26 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_bot', '0026_auto_20190426_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='profile',
        ),
        migrations.AddField(
            model_name='bot',
            name='profile',
            field=models.ManyToManyField(blank=True, null=True, to='first_bot.Profile'),
        ),
    ]
