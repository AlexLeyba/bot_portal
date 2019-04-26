from django import forms
from .models import Profile, News, News2, Mistake, Bot


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
        labels = {'types': '', 'urls': '', 'data': '',}
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
        model = Mistake
        fields = ('name', 'picture',)
        labels = {'name': '', 'picture':''}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Тип ошибки'}),
        }
