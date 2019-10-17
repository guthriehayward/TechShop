from django.contrib import admin
from .models import Product, ProductCategory
from django.db import models
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Name", {"fields":["productName"]}),
        ("URL", {"fields":["product_slug"]}),
        ("Category", {"fields":["product_category"]}),
        ("Price", {"fields":["price"]}),
        ("Description", {"fields":["description"]})
    ]

admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
