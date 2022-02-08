from django.contrib import admin
from django.contrib import admin
from rango.models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'category']
    list_filter = ['category']
    list_editable = ['category']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
