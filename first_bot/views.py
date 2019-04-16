from first_bot.models import *
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import UpdateView, CreateView
from first_bot.forms import ProfileForm, NewsForm, News2Form


class General(View):
    @staticmethod
    def get(request):
        return render(request, 'first_bot/general.html')


class ProfileView(View):
    @staticmethod
    def get(request):
        profile = Profile.objects.get(user=request.user)
        context = {
            'profile': profile,
        }
        return render(request, "first_bot/profile.html", context)


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
    template_name = 'first_bot/editprofile.html'
    form_class = ProfileForm


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

