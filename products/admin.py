from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_filter = ("category", "stock", "creation_date", "available",)
    list_display = ("name_product", "category", "stock", "available",)
    search_fields = ("name_product", "category",)


admin.site.register(Product, ProductAdmin)