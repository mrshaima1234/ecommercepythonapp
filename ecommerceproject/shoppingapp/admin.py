from django.contrib import admin
from .models import Category, Product


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'slug']
    prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','stock','available','created_at','updated_at'] #for displaying data in admin panel
    list_editable = ['price','stock','available']  #editable fields
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)
