from django import forms
from .models import Profile, News, News2, Bot, Errors


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'phone', 'address', 'about', 'photo')
        # labels = {'name': '', 'phone': '', 'address': '', 'about': '', }
        # widgets = {
        #     'photo' : forms.I
        #     'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
        #     'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
        #     'address': forms.TextInput(attrs={'placeholder': 'Адресс'}),
        #     'about': forms.TextInput(attrs={'placeholder': 'О себе'}),
        # }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('types', 'urls', 'data')
        labels = {'types': '', 'urls': '', 'data': '', }
        widgets = {
            'types': forms.TextInput(attrs={'placeholder': 'Тип статьи'}),
            'urls': forms.TextInput(attrs={'placeholder': 'url'}),
            'data': forms.TextInput(attrs={'placeholder': 'дата'}),
        }


class News2Form(forms.ModelForm):
    class Meta:
        model = News2
        fields = ('negative', 'positive', 'neutral')


class AddmistakeForm(forms.ModelForm):
    class Meta:
        model = Errors
        fields = ('name', 'types', 'date', 'time', 'picture')
        labels = {'name': '', 'picture': '', 'date': '', 'time': '', 'types': ''}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Номер ошибки'}),
            'types': forms.TextInput(attrs={'placeholder': 'Тип ошибки'}),
            'time': forms.TextInput(attrs={'placeholder': 'Время'}),
            'date': forms.TextInput(attrs={'placeholder': 'Дата'}),
        }

class AddBotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ('name', 'technology', 'body', 'slug', 'picture')
        labels = {'name': '', 'technology': '', 'body': '', 'slug': '', 'picture': ''}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Название бота'}),
            'technology': forms.TextInput(attrs={'placeholder': 'Используемые технологии'}),
            'body': forms.TextInput(attrs={'placeholder': 'Описание'}),
            'slug': forms.TextInput(attrs={'placeholder': 'То что будет в урле'}), #сделать авто генерацию слаг
        }


