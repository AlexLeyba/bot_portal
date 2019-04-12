from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Bot(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Название бота', max_length=100)
    technology = models.CharField('Технологии', max_length=300)
    body = models.TextField('Описание бота')
    picture = models.ImageField('Картинка', upload_to="images/", blank=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'


class Profile(models.Model):
    name = models.CharField('ФИО', max_length=300)
    phone = models.IntegerField('Телефон', default=0)
    address = models.CharField('Адрес', max_length=300)
    about = models.TextField('Биография')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, id=instance.id)


class Stars(models.Model):
    name = models.CharField('Название', max_length=300)
    body = models.TextField('Описание')
    picture = models.ImageField('Картинка', upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Зыезда'
        verbose_name_plural = 'Звезды'


class Mistake(models.Model):
    name = models.CharField('Тип ошибки', max_length=500)
    date = models.DateField(auto_now=True)
    time = models.DateTimeField(auto_now=True)
    picture = models.ImageField('Картинка', upload_to='images/')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Ошибка'
        verbose_name_plural = 'Ошибки'


class News(models.Model):
    types = models.CharField(max_length=1000)
    urls = models.CharField('Ссылки', max_length=1000)
    data = models.DateField('Дата')
    key = models.CharField(max_length=300)

    def __str__(self):
        return '{}'.format(self.data)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


# class News2(models.Model):
#     """Пока не рабочая реализация #2"""
#     positive = models.CharField(max_length=300, blank=True, null=True)
#     negative = models.CharField(max_length=300, blank=True, null=True)
#     neutral = models.CharField(max_length=300, blank=True, null=True)

class News2(models.Model):
    """Рбочая реализация #1"""
    positive = models.IntegerField('1 = позитвная', blank=True, null=True)
    negative = models.IntegerField('2 = негативная', blank=True, null=True)
    neutral = models.IntegerField('3 = нейтрпльная', blank=True, null=True)
