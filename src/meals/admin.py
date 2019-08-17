from django.contrib import admin
from .models import Meals, Category
from django_summernote.admin import SummernoteModelAdmin


class MealsAdmin(SummernoteModelAdmin, admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name', 'category', 'people', 'preperation_time']
    search_fields = ['name', 'desc']
    list_filter = ['category', 'people']

admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)
