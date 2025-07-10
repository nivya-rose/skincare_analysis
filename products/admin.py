from django.contrib import admin
from .models import Product, Ingredient, Review

admin.site.register(Product)
admin.site.register(Ingredient)
admin.site.register(Review)
