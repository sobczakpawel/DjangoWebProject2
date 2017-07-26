from django.contrib import admin
from app.models import Categories
from app.models import Products


# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    admin.ModelAdmin.list_display('name', 'description')
    
admin.site.register(Categories, CategoriesAdmin)