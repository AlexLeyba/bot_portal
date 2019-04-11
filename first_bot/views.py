from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from first_bot.models import *
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, FormView, DetailView, ListView
from django.views.generic.edit import UpdateView, CreateView
from first_bot.forms import ProfileForm, NewsForm


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


class NewsSave(CreateView, FormView):
    template_name = 'first_bot/newsform.html'
    model = News
    form_class = NewsForm

    def form_valid(self, form):
        return HttpResponseRedirect('/')


class EditProfile(UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'first_bot/editprofile.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Profile has been updated!')
        return super().form_valid(form)


# class NewsView(View):
#     def get(self, request, ):
#         news = News.objects.all()
#         news2 = News2.objects.all()
#         b = news2.negative
#         c = news2.neutral
#
#         context = {
#             'news': news,
#             'news2': news2,
#             'positive': a,
#             'negative': b,
#             'neutral': c,
#         }
#         return render(request, 'first_bot/news.html', context)
