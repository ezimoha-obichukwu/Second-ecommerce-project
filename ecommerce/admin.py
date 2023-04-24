from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "description"]
    list_editable = ["price"]
    list_filter = ["category"]

admin.site.register(Product, ProductAdmin)