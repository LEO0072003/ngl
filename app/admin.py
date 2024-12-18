import django
from django.contrib import admin
from app.models import App, Category, SubCategory
# Register your models here.

admin.site.register(App)
admin.site.register(Category)
admin.site.register(SubCategory)
