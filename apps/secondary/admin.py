from django.contrib import admin
from apps.secondary import models
# Register your models here.

class StyleInfoInline(admin.TabularInline):
    model = models.StyleInfo
    extra = 1

class StyleFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [StyleInfoInline]

class GlanceInfoInline(admin.TabularInline):
    model = models.GlanceInfo
    extra = 1

class GlanceFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
    inlines = [GlanceInfoInline]


class DiscountFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'descriptions')
    search_fields = ('name', 'descriptions')
    
class CollectionInfoInline(admin.TabularInline):
    model = models.CollectionInline
    extra = 1

class CollectionFilterAdmin(admin.ModelAdmin):
    inlines = [CollectionInfoInline]


class TestimonialsInfoInline(admin.TabularInline):
    model = models.TestimonialsInline
    extra = 1

class TestimonialsFilterAdmin(admin.ModelAdmin):
    list_filter = ('mini_descriptions', )
    list_display = ('mini_descriptions', )
    search_fields = ('mini_descriptions', )
    inlines = [TestimonialsInfoInline]

admin.site.register(models.Art)
admin.site.register(models.Partner)
admin.site.register(models.Trends)
admin.site.register(models.Testimonials, TestimonialsFilterAdmin)
admin.site.register(models.Collection, CollectionFilterAdmin)
admin.site.register(models.Discount, DiscountFilterAdmin)
admin.site.register(models.Glance, GlanceFilterAdmin )
admin.site.register(models.Style, StyleFilterAdmin)


