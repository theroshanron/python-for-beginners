from django.contrib import admin

from .models import Product, Discount

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'description','Discount')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product, ProductAdmin)
admin.site.register(Discount, DiscountAdmin)