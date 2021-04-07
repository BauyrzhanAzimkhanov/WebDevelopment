from django.urls import path, re_path
from api.views import *

urlpatterns = [
    path('hello/', greetings),
    path('products/', get_products),
    path('products/<int:id>/', get_product),
    path('categories/', get_categories),
    path('categories/<int:id>/', get_category)
]