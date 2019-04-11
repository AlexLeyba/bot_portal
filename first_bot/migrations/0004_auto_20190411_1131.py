# Generated by Django 2.2 on 2019-04-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_bot', '0003_profile_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='News2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.CharField(max_length=1000)),
                ('negative', models.CharField(max_length=1000)),
                ('neutral', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(choices=[('1', 'положительная'), ('2', 'отрицательная'), ('3', 'нейтаральная')], default='1', max_length=1),
        ),
    ]
