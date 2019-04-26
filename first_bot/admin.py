from django.contrib import admin
from .models import *


class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'technology', 'slug')


admin.site.register(Bot, BotAdmin)
admin.site.register(Profile)
admin.site.register(Medal)
admin.site.register(Mistake)
admin.site.register(News)
admin.site.register(News2)
