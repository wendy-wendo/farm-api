from django.contrib import admin

from .models import UserDetail, Product, Order

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Product)
admin.site.register(Order)