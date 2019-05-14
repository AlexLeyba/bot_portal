from django.http import HttpResponseRedirect
from first_bot.models import *
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from first_bot.forms import ProfileForm, NewsForm, News2Form, AddmistakeForm, AddBotForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


class General(View):
    @staticmethod
    def get(request):
        return render(request, 'first_bot/general.html')


class ProfileView(View):
    @staticmethod
    def get(request, pk):
        profile = Profile.objects.get(pk=request.user.id)
        bot = Bot.objects.filter(profile__user__id=request.user.id)
        medal = Medal.objects.filter(profile__user__id=request.user.id)
        context = {
            'profile': profile,
            'bot': bot,
            'medal': medal,
        }
        return render(request, "first_bot/profile.html", context)


class NewsSave(CreateView):
    template_name = 'first_bot/newsform.html'
    model = News
    form_class = NewsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/newsform/')

    @staticmethod
    def success_url():
        return redirect('/news/')


class NewsSave2(View):
    @staticmethod
    def get(request):
        form = News2Form
        context = {
            'form': form
        }
        return render(request, 'first_bot/newsform2.html', context)

    @staticmethod
    def post(request):
        form = News2Form(request.POST)
        news = News2()
        a = int(request.POST.get('positive'))
        b = int(request.POST.get('negative'))
        c = int(request.POST.get('neutral'))
        d = int(request.POST.get('notapplicable'))
        if form.is_valid():
            news.positive += a
            news.negative += b
            news.neutral += c
            news.notapplicable += d
            news.save()
            return HttpResponseRedirect('/newsform2/')


class EditProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'first_bot/editprofile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/')
        # return redirect('/profile/{}'.format(request.user.id))

    @staticmethod
    def success_url():
        return redirect('/profile/')


class NewsView(View):

    @staticmethod
    def get(request):
        news = News.objects.all()
        news2 = News2.objects.order_by('-id')[0:1]
        context = {
            'news': news,
            'news2': news2,
        }
        return render(request, 'first_bot/news.html', context)


class Mistake(ListView):
    template_name = 'first_bot/mistake.html'
    model = Errors
    queryset = Errors.objects.all()


class AddMistake(CreateView):
    model = Errors
    template_name = 'first_bot/addmistake.html'
    form_class = AddmistakeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/profile/')

    @staticmethod
    def success_url():
        return redirect('/news/')


class BotView(View):
    def get(self, request, slug):
        bot = Bot.objects.filter(slug=slug)
        context = {
            'bot': bot
        }
        return render(request, 'first_bot/bots.html', context)


class AddBotView(CreateView):
    template_name = 'first_bot/addbot.html'
    model = Bot
    form_class = AddBotForm


class ButtonsView(View):
    def get(self, request):
        btn = Buttons.objects.all()
        return render(request, 'first_bot/buttons.html', {"buttons": btn})


class GetNumber(View):
    def get(self, request, pk):
        but = Buttons.objects.get(id=pk)
        if but.number == 0:
            but.number += 1
        elif but.number == 1:
            but.number -= 1
        but.save()
        return redirect("numbers")


class NumbersView(View):
    def get(self, request):
        num = Buttons.objects.all()
        context = {
            'nums': num
        }
        return render(request, 'first_bot/numbers.html', context)
