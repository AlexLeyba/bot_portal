from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class NewsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'urls', 'data', 'key')



