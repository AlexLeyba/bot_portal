from first_bot.views import *
from django.urls import path, include

urlpatterns = [
    path('', General.as_view())
]
