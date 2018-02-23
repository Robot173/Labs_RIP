from django.contrib import admin
from .models import Horse

# Register your models here.
def sorted_case(obj):
    return("%s" % (sorted(obj.horse_name)))


class HorseAdmin(admin.ModelAdmin):
    list_display = (sorted_case,'horse_name', 'horse_owner', 'horse_picture')
    list_filter = ('horse_club',)
    list_display_links = ('horse_name',)
    search_fields = ['horse_name']

admin.site.register(Horse, HorseAdmin)

# Register your models here.
