from django import forms
from .models import Profile, News


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('name', 'urls', 'data', 'key')



