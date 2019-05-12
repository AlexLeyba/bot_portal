from django.conf import settings
from django.conf.urls.static import static
from first_bot.views import *
from django.urls import path, include

urlpatterns = [
                  path('accounts/', include('allauth.urls')),
                  path('', General.as_view()),
                  path('profile/<int:pk>/', ProfileView.as_view(), name='profiles'),
                  path('edit/<int:pk>/', EditProfile.as_view(), name='edit'),
                  path('newsform/', NewsSave.as_view(), name='sendnews'),
                  path('newsform2/', NewsSave2.as_view(), name='sendnews2'),
                  path('news/', NewsView.as_view(), name='news'),
                  path('addmistake/', AddMistake.as_view(), name='addmistake'),
                  path('mistake/', Mistake.as_view(), name='mistake'),
                  path('bot/<slug:slug>/', BotView.as_view(), name='bot'),
                  path('addbot/', AddBotView.as_view(), name='addbot'),
                  path('buttons/', ButtonsView.as_view(), name='buttons'),
                  path('numbers/', NumbersView.as_view(), name='numbers'),
                  path('num/<int:pk>/', GetNumber.as_view(), name='num')
                  # path('getnum/<int:pk>/', GetNumber.as_view(), name='getnum')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
