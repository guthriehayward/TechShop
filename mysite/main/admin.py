from django.contrib import admin
from .models import Product, ProductCategory, ProductManufacturer
from django.db import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name/date", {"fields":["productName", "uploadDate"]}),
        ("Manufacturer", {"fields":["product_manufacturer"]}),
        ("URL", {"fields":["product_slug"]}),
        ("Category", {"fields":["product_category"]}),
        ("Price", {"fields":["price"]}),
        ("Description", {"fields":["description"]})
    ]

admin.site.register(ProductManufacturer)
admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
