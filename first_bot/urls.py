from first_bot.views import *
from django.urls import path, include

urlpatterns = [
    path('', General.as_view()),
    path('profile/', Profile.as_view(), name='profile'),
    path('edit/', EditProfile.as_view(), name='edit'),
    path('newsform/', NewsSave.as_view(), name='sendnews')
]
