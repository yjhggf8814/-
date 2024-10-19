from django.contrib import admin
from .models import Produkt
# Register your models here.
@admin.register(Produkt)
class ProductAdmin(admin.ModelAdmin):
    pass