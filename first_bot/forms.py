from django import forms
from .models import Profile, News, News2


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('types', 'urls', 'data', 'key')
        labels = {'types': '', 'urls': '', 'data': '', 'key': ''}
        widgets = {
            'types': forms.TextInput(attrs={'placeholder': 'Тип статьи'}),
            'urls': forms.TextInput(attrs={'placeholder': 'url'}),
            'data': forms.TextInput(attrs={'placeholder': 'дата'}),
            'key': forms.TextInput(attrs={'placeholder': 'key'}),
        }


class News2Form(forms.ModelForm):
    class Meta:
        model = News2
        fields = ('negative', 'positive', 'neutral')
