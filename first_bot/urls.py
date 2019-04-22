from first_bot.views import *
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', General.as_view()),
    path('profile/', ProfileView.as_view(), name='profiles'),
    path('edit/<int:pk>/', EditProfile.as_view(), name='edit'),
    path('newsform/', NewsSave.as_view(), name='sendnews'),
    path('newsform2/', NewsSave2.as_view(), name='sendnews2'),
    path('news/', NewsView.as_view(), name='news')
]
