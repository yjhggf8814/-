from django.urls import path
from shop.views import katalog

urlpatterns = [
    path('', katalog),
]