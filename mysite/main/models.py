from django.db import models

class ProductCategory(models.Model):
    product_category = models.CharField(max_length = 255)
    category_summary = models.CharField(max_length = 255)
    category_slug = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.product_category

class Product(models.Model):
    productName = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    description = models.TextField(default="")
    product_category = models.ForeignKey(ProductCategory, default=1, verbose_name = "Category", on_delete=models.SET_DEFAULT)
    product_slug = models.CharField(max_length=255, default=1)

    def __str__(self):
        return self.productName
