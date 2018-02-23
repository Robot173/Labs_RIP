from django.contrib import admin
from .models import Horse

# Register your models here.


class HorseAdmin(admin.ModelAdmin):
    list_display = ('horse_name', 'horse_owner', 'horse_picture')

admin.site.register(Horse, HorseAdmin)
