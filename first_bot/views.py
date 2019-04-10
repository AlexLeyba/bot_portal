from django.http import HttpResponseRedirect
from first_bot.models import *
from django.shortcuts import render
from django.views.generic import View, ListView, FormView
from django.views.generic.edit import UpdateView, CreateView
from first_bot.forms import ProfileForm, NewsForm


class General(View):
    @staticmethod
    def get(request):
        return render(request, 'first_bot/general.html')


class Profile(ListView):
    template_name = 'first_bot/profile.html'

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class NewsSave(CreateView, FormView):
    template_name = 'first_bot/newsform.html'
    model = News
    form_class = NewsForm

    def form_valid(self, form):
        return HttpResponseRedirect('/')


class EditProfile(UpdateView):
    model = Profile
    template_name = 'first_bot/editprofile.html'
    form_class = ProfileForm
