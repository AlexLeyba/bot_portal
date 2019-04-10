from django.shortcuts import render
from django.views.generic import View


class General(View):
    """Вывод главной страницы"""
    def get(self, request):
        return render(request, 'first_bot/general.html')
