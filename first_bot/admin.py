from django.contrib import admin
from .models import *


class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'technology', 'slug')


class MistakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time')


admin.site.register(Bot, BotAdmin)
admin.site.register(Profile)
admin.site.register(Medal)
admin.site.register(Errors, MistakeAdmin)
admin.site.register(News)
admin.site.register(News2)
