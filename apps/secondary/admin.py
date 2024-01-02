from django.contrib import admin
from apps.secondary.models import About, Faqs
# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']

@admin.register(Faqs)
class FaqsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'question', 'answer']