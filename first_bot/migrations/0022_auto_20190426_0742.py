# Generated by Django 2.2 on 2019-04-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_bot', '0021_auto_20190425_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mistake',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='mistake',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Тип ошибки'),
        ),
        migrations.AlterField(
            model_name='mistake',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/images', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='mistake',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
