from first_bot.views import *
from django.urls import path

urlpatterns = [
    path('', General.as_view()),
    path('profile/', ProfileView.as_view(), name='profiles'),
    path('edit/', EditProfile.as_view(), name='edit'),
    path('newsform/', NewsSave.as_view(), name='sendnews'),
    # path('news/', NewsView.as_view(), name='news')
]
