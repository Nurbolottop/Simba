from django.contrib import admin
from apps.base import models
# Register your models here.

# class SettingsFilterAdmin(admin.ModelAdmin):
#     list_filter = ('title', )
#     list_display = ('title', 'descriptions')
#     search_fields = ('title', 'descriptions')

class SlideFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')

admin.site.register(models.Slide, SlideFilterAdmin)
