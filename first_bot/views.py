from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from first_bot.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, FormView, DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from first_bot.forms import ProfileForm, NewsForm, News2Form


class General(View):
    @staticmethod
    def get(request):
        return render(request, 'first_bot/general.html')


class ProfileView(DetailView):
    template_name = 'first_bot/profile.html'
    context_object_name = 'profile'
    model = Profile

    def get_object(self, queryset=None):
        obj = get_object_or_404(Profile, user=self.request.user)
        if obj.user != self.request.user:
            raise Http404
        return obj


class NewsSave(CreateView):
    template_name = 'first_bot/newsform.html'
    model = News
    form_class = NewsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/news/')

    @staticmethod
    def success_url():
        return redirect('/news/')


class NewsSave2(CreateView):
    template_name = 'first_bot/newsform2.html'
    model = News2
    form_class = News2Form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/news/')

    @staticmethod
    def success_url():
        return redirect('/news/')


class EditProfile(UpdateView):
    model = Profile
    template_name = 'first_bot/editProfile.html'
    form_class = ProfileForm


# class EditProfile(UpdateView):
#     form_class = ProfileForm
#     model = Profile
#     template_name = 'first_bot/editprofile.html'
#
#     def get_object(self, queryset=None):
#         return self.request.user.profile
#
#     def form_valid(self, form):
#         messages.success(self.request, 'Profile has been updated!')
#         return super().form_valid(form)
#
#     @staticmethod
#     def success_url():
#         return redirect('/profile/')


# class NewsView(View):
#     """Пока не рабочий вариант"""
#     def get(self, request):
#         news = News.objects.all()
#         positive = News2.objects.values_list('positive').count()
#         negative = News2.objects.values_list('negative').count()
#         neutral = News2.objects.values_list('neutral').count()
#         context = {
#             'news': news,
#             'positive': positive,
#             'negative': negative,
#             'neutral': neutral,
#         }
#         return render(request, 'first_bot/news.html', context)
#

class NewsView(View):
    """Рабочая реализация №1"""

    @staticmethod
    def get(request):
        news = News.objects.all()
        positive = News2.objects.filter(positive=1).count()
        negative = News2.objects.filter(negative=2).count()
        neutral = News2.objects.filter(neutral=3).count()

        context = {
            'news': news,
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
        }
        return render(request, 'first_bot/news.html', context)
