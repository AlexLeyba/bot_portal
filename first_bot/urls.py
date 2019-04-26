from django.conf import settings
from django.conf.urls.static import static
from first_bot.views import *
from django.urls import path, include

urlpatterns = [
                  path('accounts/', include('allauth.urls')),
                  path('', General.as_view()),
                  path('profile/', ProfileView.as_view(), name='profiles'),
                  path('edit/<int:pk>/', EditProfile.as_view(), name='edit'),
                  path('newsform/', NewsSave.as_view(), name='sendnews'),
                  path('newsform2/', NewsSave2.as_view(), name='sendnews2'),
                  path('news/', NewsView.as_view(), name='news'),
                  path('addmistake/', AddMistake.as_view(), name='addmistake')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
