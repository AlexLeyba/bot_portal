from django.http import HttpResponseRedirect
from first_bot.models import *
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic.edit import UpdateView, CreateView
from first_bot.forms import ProfileForm, NewsForm, News2Form
from django.core.paginator import Paginator


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
        if form.is_valid():
            news.positive += a
            news.negative += b
            news.neutral += c
            news.save()
            return HttpResponseRedirect('/news/')


class EditProfile(UpdateView):
    model = Profile
    template_name = 'first_bot/editprofile.html'
    form_class = ProfileForm


class NewsView(View):

    @staticmethod
    def get(request):
        news = News.objects.all()
        paginator = Paginator(news, 4)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        news2 = News2.objects.order_by('-id')[0:1]
        context = {
            'news': contacts,
            'news2': news2,
        }
        return render(request, 'first_bot/news.html', context)
