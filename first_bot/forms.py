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


class News2Form(forms.ModelForm):
    class Meta:
        model = News2
        fields = ('negative', 'positive', 'neutral')
        widgets = {
            'negative': forms.TextInput(attrs={'placeholder': 'Негативные'}),
            'positive': forms.TextInput(attrs={'placeholder': 'Позитивные'}),
            'neutral': forms.TextInput(attrs={'placeholder': 'Нейтральные'}),
        }
