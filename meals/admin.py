from django.contrib import admin
#from django_summernote.admin import SummernoteModelAdmin
from .models import Meal , Category




admin.site.register(Meal)
admin.site.register(Category)
