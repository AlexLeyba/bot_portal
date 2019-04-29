from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    name = models.CharField('ФИО', max_length=300)
    photo = models.ImageField('Фото профиля', upload_to="images/", null=True, blank=True)
    phone = models.CharField('Телефон', max_length=100)
    address = models.CharField('Адрес', max_length=100)
    about = models.CharField('О себе', max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('profiles')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Medal(models.Model):
    name = models.CharField('Название', max_length=300)
    body = models.TextField('Описание')
    picture = models.ImageField('Картинка', upload_to='images/', null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    profile = models.ManyToManyField(Profile, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Зыезда'
        verbose_name_plural = 'Звезды'


class Bot(models.Model):
    name = models.CharField('Название бота', max_length=100)
    technology = models.CharField('Технологии', max_length=300)
    body = models.TextField('Описание бота')
    picture = models.ImageField('Картинка', upload_to="images/", null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    profile = models.ManyToManyField(Profile, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('news')


    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'


class Errors(models.Model):
    name = models.CharField('Номер ошибки', max_length=100, null=True, blank=True)
    types = models.CharField('Тип ошибки', max_length=300, null=True, blank=True)
    date = models.CharField('Дата', max_length=10, null=True, blank=True)
    time = models.CharField('Время', max_length=10, null=True, blank=True)
    picture = models.ImageField('Картинка', upload_to='images/', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Ошибка'
        verbose_name_plural = 'Ошибки'


class News(models.Model):
    types = models.CharField(max_length=1000)
    urls = models.CharField('Ссылки', max_length=1000)
    data = models.DateField('Дата')

    def __str__(self):
        return '{}'.format(self.data)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class News2(models.Model):
    """Рбочая реализация #1"""
    positive = models.IntegerField('позитвная', blank=True, null=True, default=0)
    negative = models.IntegerField('негативная', blank=True, null=True, default=0)
    neutral = models.IntegerField('нейтральная', blank=True, null=True, default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, id=instance.id)
