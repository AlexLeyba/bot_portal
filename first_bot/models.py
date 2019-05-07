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
    positive = models.IntegerField('позитвная', blank=True, null=True, default=0)
    negative = models.IntegerField('негативная', blank=True, null=True, default=0)
    neutral = models.IntegerField('нейтральная', blank=True, null=True, default=0)
    notapplicable = models.IntegerField('не относится', blank=True, null=True, default=0)


class Buttons(models.Model):
    botton1 = models.CharField("Значение кнопки", default='Копка 1', max_length=100)
    botton2 = models.CharField("Значение кнопки", default='Копка 2', max_length=100)
    botton3 = models.CharField("Значение кнопки", default='Копка 3', max_length=100)
    botton4 = models.CharField("Значение кнопки", default='Копка 4', max_length=100)
    botton5 = models.CharField("Значение кнопки", default='Копка 5', max_length=100)
    botton6 = models.CharField("Значение кнопки", default='Копка 6', max_length=100)
    botton7 = models.CharField("Значение кнопки", default='Копка 7', max_length=100)
    botton8 = models.CharField("Значение кнопки", default='Копка 8', max_length=100)
    botton9 = models.CharField("Значение кнопки", default='Копка 9', max_length=100)
    botton10 = models.CharField("Значение кнопки", default='Копка 10', max_length=100)
    botton11 = models.CharField("Значение кнопки", default='Копка 11', max_length=100)
    botton12 = models.CharField("Значение кнопки", default='Копка 12', max_length=100)
    botton13 = models.CharField("Значение кнопки", default='Копка 13', max_length=100)
    botton14 = models.CharField("Значение кнопки", default='Копка 14', max_length=100)
    botton15 = models.CharField("Значение кнопки", default='Копка 15', max_length=100)
    botton16 = models.CharField("Значение кнопки", default='Копка 16', max_length=100)
    botton17 = models.CharField("Значение кнопки", default='Копка 17', max_length=100)
    botton18 = models.CharField("Значение кнопки", default='Копка 18', max_length=100)
    botton19 = models.CharField("Значение кнопки", default='Копка 19', max_length=100)
    botton20 = models.CharField("Значение кнопки", default='Копка 20', max_length=100)


class Number(models.Model):
    namber = models.IntegerField(default=0)
    button = models.OneToOneField(Buttons, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, id=instance.id)
