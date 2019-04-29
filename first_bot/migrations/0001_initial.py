# Generated by Django 2.2 on 2019-04-29 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Errors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер ошибки')),
                ('types', models.CharField(blank=True, max_length=300, null=True, verbose_name='Тип ошибки')),
                ('date', models.CharField(blank=True, max_length=10, null=True, verbose_name='Дата')),
                ('time', models.CharField(blank=True, max_length=10, null=True, verbose_name='Время')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Ошибка',
                'verbose_name_plural': 'Ошибки',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=1000)),
                ('urls', models.CharField(max_length=1000, verbose_name='Ссылки')),
                ('data', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='News2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positive', models.IntegerField(blank=True, default=0, null=True, verbose_name='позитвная')),
                ('negative', models.IntegerField(blank=True, default=0, null=True, verbose_name='негативная')),
                ('neutral', models.IntegerField(blank=True, default=0, null=True, verbose_name='нейтральная')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото профиля')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('about', models.CharField(max_length=100, verbose_name='о себе')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название')),
                ('body', models.TextField(verbose_name='Описание')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('profile', models.ManyToManyField(blank=True, null=True, to='first_bot.Profile')),
            ],
            options={
                'verbose_name': 'Зыезда',
                'verbose_name_plural': 'Звезды',
            },
        ),
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название бота')),
                ('technology', models.CharField(max_length=300, verbose_name='Технологии')),
                ('body', models.TextField(verbose_name='Описание бота')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('profile', models.ManyToManyField(blank=True, null=True, to='first_bot.Profile')),
            ],
            options={
                'verbose_name': 'Бот',
                'verbose_name_plural': 'Боты',
            },
        ),
    ]
